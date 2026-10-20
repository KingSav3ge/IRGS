import { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { api, errMsg } from "@/lib/api";
import { LAST_PLAY_KEY } from "@/components/AppShell";
import { NarrativeEntry } from "@/components/play/NarrativeEntry";
import { StatusPanel } from "@/components/play/StatusPanel";
import { ControlPanel } from "@/components/play/ControlPanel";
import { ActionComposer } from "@/components/play/ActionComposer";
import { useNarrator } from "@/hooks/useNarrator";
import { Type } from "lucide-react";

const SIZES = { s: "0.9", m: "1", l: "1.18" };
const PAPER = { "--c-parchment": "#2B382F", "--c-ash": "#536451", "--c-dust": "#6E7A68", "--c-line": "#D6CDB8", backgroundColor: "#F3EEDF" };

const ReadingSettings = ({ reading, setReading }) => (
  <div className="flex items-center gap-1" data-testid="gameplay-reading-settings">
    <Type size={13} className="text-dust mr-1" />
    {Object.keys(SIZES).map((k) => (
      <button key={k} onClick={() => setReading({ ...reading, size: k })} data-testid={`gameplay-reading-size-${k}`}
        className={`px-1.5 text-xs font-mono uppercase ${reading.size === k ? "text-gold" : "text-dust hover:text-ash"}`}>{k}</button>
    ))}
    <button onClick={() => setReading({ ...reading, paper: !reading.paper })} data-testid="gameplay-reading-paper-toggle"
      className={`ml-2 px-2 py-0.5 text-[10px] font-mono uppercase border ${reading.paper ? "border-gold text-gold" : "border-line text-dust hover:text-ash"}`}>paper</button>
  </div>
);

export const usePlaythrough = (pid) => useQuery({
  queryKey: ["playthrough", pid],
  queryFn: () => api.get(`/playthroughs/${pid}`).then((r) => r.data),
  refetchInterval: (q) => (q.state.data?.view.npc_pending ? 3000 : q.state.data?.chronicle.some((e) => e.image_status === "painting") ? 5000 : false),
});

export const usePaint = (pid) => {
  const qc = useQueryClient();
  return async (eventId) => {
    try {
      await api.post(`/playthroughs/${pid}/events/${eventId}/paint`);
      toast("The illuminator takes up the brush…");
      qc.invalidateQueries({ queryKey: ["playthrough", pid] });
    } catch (e) { toast.error(errMsg(e)); }
  };
};

export default function Play() {
  const { pid } = useParams();
  const qc = useQueryClient();
  const { data: pt, isError } = usePlaythrough(pid);
  const [busy, setBusy] = useState(false);
  const [reading, setReadingState] = useState(() => JSON.parse(localStorage.getItem("irgs_reading") || '{"size":"m","paper":false}'));
  const setReading = (r) => { setReadingState(r); localStorage.setItem("irgs_reading", JSON.stringify(r)); };
  const narrator = useNarrator();
  const paint = usePaint(pid);
  const feedRef = useRef(null);
  const count = pt?.chronicle.length;
  const { data: voices } = useQuery({ queryKey: ["voices"], queryFn: () => api.get("/voice/options").then((r) => r.data) });

  useEffect(() => { localStorage.setItem(LAST_PLAY_KEY, pid); }, [pid]);
  useEffect(() => { feedRef.current?.scrollTo({ top: feedRef.current.scrollHeight, behavior: "smooth" }); }, [count, busy]);

  if (isError) return <p className="p-12 text-crimson" data-testid="gameplay-error">This playthrough could not be found.</p>;
  if (!pt) return <p className="p-12 tactical-label">Unrolling the scene…</p>;

  const act = async (declaration) => {
    setBusy(true);
    const request_id = crypto.randomUUID();
    const send = () => api.post(`/playthroughs/${pid}/act`, { declaration, request_id }, { timeout: 120000 });
    try {
      // retry once on a dropped connection; the request id makes the retry safe (never double-commits)
      const { data } = await send().catch((e) => (e.response ? Promise.reject(e) : send()));
      if (data.replayed) toast("Your action was already recorded, so it was not repeated.");
      qc.setQueryData(["playthrough", pid], data.playthrough);
      return true;
    } catch (e) {
      toast.error(errMsg(e, "The action could not be committed"));
      return false;
    } finally { setBusy(false); }
  };

  const passTime = async (span) => {
    setBusy(true);
    try {
      const request_id = crypto.randomUUID();
      const send = () => api.post(`/playthroughs/${pid}/pass-time`, { span, request_id });
      const { data } = await send().catch((e) => (e.response ? Promise.reject(e) : send()));
      qc.setQueryData(["playthrough", pid], data.playthrough);
    } catch (e) {
      toast.error(errMsg(e, "Time could not pass"));
    } finally { setBusy(false); }
  };

  const onSettings = async (body) => {
    try {
      const { data } = await api.patch(`/playthroughs/${pid}/settings`, body);
      qc.setQueryData(["playthrough", pid], data);
    } catch (e) { toast.error(errMsg(e)); }
  };

  const voiceOpts = { engine: pt.voice_engine, voice: pt.narrator_voice, calendar: pt.view.campaign_time.calendar,
    castPid: voices?.premium_active && pt.voice_engine === "elevenlabs" ? pid : null };

  return (
    <div data-theme={pt.theme} className="themed" data-testid="gameplay-theme-scope">
    <div className="relative z-10 mx-auto max-w-[1600px] px-4 sm:px-6 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6 lg:h-[calc(100vh-4rem)]">
      <div className="lg:col-span-3 lg:h-full lg:overflow-hidden order-2 lg:order-none"><StatusPanel pt={pt} /></div>
      <section className="order-1 lg:order-none lg:col-span-6 flex flex-col bg-tome gold-frame lg:h-full min-h-[70vh] lg:overflow-hidden">
        <div className="px-6 sm:px-10 pt-6 pb-3 border-b border-line flex items-center justify-between">
          <h1 className="font-heading text-lg text-parchment truncate" data-testid="gameplay-title">{pt.title}</h1>
          {pt.status === "archived" && <span className="tactical-label !text-crimson">Archived</span>}
          <ReadingSettings reading={reading} setReading={setReading} />
        </div>
        <div ref={feedRef} className="flex-1 overflow-y-auto scroll-thin px-6 sm:px-10 py-8 space-y-8" data-testid="gameplay-narrative-feed-container"
          style={{ zoom: SIZES[reading.size], ...(reading.paper ? PAPER : {}) }}>
          {pt.chronicle.map((e, i) => (
            <NarrativeEntry key={e.id} entry={e} index={i} narrator={narrator} voiceOpts={voiceOpts} onPaint={paint} />
          ))}
          {busy && <p className="tactical-label !text-mana animate-pulse" data-testid="gameplay-resolving-indicator">The engine resolves · the narrator composes…</p>}
          {!busy && pt.view.npc_pending && <p className="tactical-label !text-ash animate-pulse" data-testid="gameplay-npc-pending-indicator">The world stirs · others weigh their next move…</p>}
        </div>
        <ActionComposer onSubmit={act} onPass={passTime} busy={busy} disabled={pt.status === "archived"} />
      </section>
      <div className="lg:col-span-3 lg:h-full lg:overflow-hidden order-3 lg:order-none"><ControlPanel pt={pt} onSettings={onSettings} /></div>
    </div>
    </div>
  );
}
