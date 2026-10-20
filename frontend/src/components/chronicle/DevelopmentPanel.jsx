import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Check, RotateCcw, Target, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { api, errMsg, fmtDate } from "@/lib/api";

const COLORS = { health: "var(--c-crimson)", stamina: "var(--c-emerald)", morale: "var(--c-gold)" };

const Chart = ({ points }) => {
  if (points.length < 2) return <p className="text-sm text-dust">Play a few turns to see how your character holds up.</p>;
  const w = 600, h = 140, min = Math.min(...points.map((p) => p.at)), span = Math.max(...points.map((p) => p.at)) - min || 1;
  const line = (k) => points.map((p) => `${((p.at - min) / span) * w},${h - (p[k] / 100) * h}`).join(" ");
  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="w-full h-40 border border-line bg-void/40" data-testid="development-chart">
      {Object.entries(COLORS).map(([k, c]) => <polyline key={k} points={line(k)} fill="none" stroke={c} strokeWidth="2" />)}
    </svg>
  );
};

export const DevelopmentPanel = ({ pid }) => {
  const qc = useQueryClient();
  const [title, setTitle] = useState("");
  const { data } = useQuery({ queryKey: ["development", pid], queryFn: () => api.get(`/playthroughs/${pid}/development`).then((r) => r.data) });
  const refresh = () => ["development", "playthrough"].forEach((k) => qc.invalidateQueries({ queryKey: k === "playthrough" ? [k, pid] : [k, pid] }));

  const add = async () => {
    try { await api.post(`/playthroughs/${pid}/goals`, { title }); setTitle(""); refresh(); toast.success("Goal set"); } catch (e) { toast.error(errMsg(e)); }
  };
  const setStatus = async (gid, status) => {
    try { await api.patch(`/playthroughs/${pid}/goals/${gid}`, { status }); refresh(); } catch (e) { toast.error(errMsg(e)); }
  };
  if (!data) return <p className="tactical-label">Reading the record…</p>;

  return (
    <div className="grid lg:grid-cols-2 gap-10" data-testid="development-panel">
      <section className="space-y-4">
        <p className="tactical-label">Condition over time</p>
        <Chart points={data.points} />
        <div className="flex gap-4 text-xs">{Object.entries(COLORS).map(([k, c]) => <span key={k} className="capitalize font-semibold" style={{ color: c, filter: "brightness(1.25)" }}>— {k}</span>)}</div>
        <p className="tactical-label pt-4">How you've acted</p>
        <div className="flex flex-wrap gap-2" data-testid="development-intents">
          {Object.entries(data.intents).map(([k, n]) => <span key={k} className="text-xs font-mono border border-line px-2 py-1 text-ash">{k} × {n}</span>)}
        </div>
        {Object.keys(data.testimony || {}).length > 0 && (
          <div className="space-y-1 pt-4"><p className="tactical-label">Your own account</p>
            {Object.entries(data.testimony).map(([k, v]) => <p key={k} className="text-sm text-ash"><span className="capitalize text-parchment">{k}:</span> {v}</p>)}</div>
        )}
        <p className="tactical-label pt-4">Turning points</p>
        <ul className="space-y-2 text-sm" data-testid="development-milestones">
          {data.milestones.map((m) => <li key={m.id} className="text-ash"><span className="font-mono text-dust text-xs">#{m.at} {fmtDate(m.date)}</span>{" · "}{m.title}</li>)}
        </ul>
      </section>
      <section className="space-y-4">
        <p className="tactical-label flex items-center gap-2"><Target size={12} /> Personal goals (optional)</p>
        <p className="text-xs text-dust">Goals are your own aims. The narrator knows about them but never completes them for you; you decide when one is achieved.</p>
        <div className="flex gap-2">
          <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="e.g. Earn a place in a lord's household" className="bg-tome border-line" data-testid="goal-title-input" />
          <Button onClick={add} disabled={!title.trim()} data-testid="goal-add-button">Add</Button>
        </div>
        <ul className="space-y-2" data-testid="goals-list">
          {data.goals.length === 0 && <li className="text-sm text-dust">No goals set.</li>}
          {data.goals.map((g) => (
            <li key={g.id} className="flex items-center gap-3 border border-line px-4 py-3" data-testid={`goal-${g.id}`}>
              <span className={`flex-1 text-sm ${g.status === "active" ? "text-parchment" : "text-dust line-through"}`}>{g.title}</span>
              <span className={`text-[10px] font-mono uppercase ${g.status === "achieved" ? "text-emerald" : "text-dust"}`} data-testid={`goal-status-${g.id}`}>{g.status}</span>
              {g.status === "active" ? (
                <>
                  <button onClick={() => setStatus(g.id, "achieved")} title="Mark achieved" data-testid={`goal-achieve-${g.id}`}><Check size={14} className="text-emerald" /></button>
                  <button onClick={() => setStatus(g.id, "abandoned")} title="Set aside" data-testid={`goal-abandon-${g.id}`}><X size={14} className="text-crimson" /></button>
                </>
              ) : (
                <button onClick={() => setStatus(g.id, "active")} title="Take up again" data-testid={`goal-reactivate-${g.id}`}><RotateCcw size={13} className="text-ash" /></button>
              )}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};
