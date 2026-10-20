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
    try {
      const { data } = await api.post(`/playthroughs/${pid}/act`, { declaration }, { timeout: 120000 });
      qc.setQueryData(["playthrough", pid], data.playthrough);
      return true;
    } catch (e) {
      toast.error(errMsg(e, "The action could not be committed"));
      return false;
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
        </div>
        <div ref={feedRef} className="flex-1 overflow-y-auto scroll-thin px-6 sm:px-10 py-8 space-y-8" data-testid="gameplay-narrative-feed-container">
          {pt.chronicle.map((e, i) => (
            <NarrativeEntry key={e.id} entry={e} index={i} narrator={narrator} voiceOpts={voiceOpts} onPaint={paint} />
          ))}
          {busy && <p className="tactical-label !text-mana animate-pulse" data-testid="gameplay-resolving-indicator">The engine resolves · the narrator composes…</p>}
          {!busy && pt.view.npc_pending && <p className="tactical-label !text-ash animate-pulse" data-testid="gameplay-npc-pending-indicator">The world stirs · others weigh their next move…</p>}
        </div>
        <ActionComposer onSubmit={act} busy={busy} disabled={pt.status === "archived"} />
      </section>
      <div className="lg:col-span-3 lg:h-full lg:overflow-hidden order-3 lg:order-none"><ControlPanel pt={pt} onSettings={onSettings} /></div>
    </div>
    </div>
  );
}
