import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { GitBranch, RotateCcw, Trash2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { api, errMsg } from "@/lib/api";
import { usePlaythrough } from "@/pages/Play";
import { LAST_PLAY_KEY } from "@/components/AppShell";

const KIND_STYLE = { auto: "text-mana border-mana/40", checkpoint: "text-gold border-gold/40", manual: "text-ash border-line" };

export default function Saves() {
  const { pid } = useParams();
  const navigate = useNavigate();
  const qc = useQueryClient();
  const { data: pt } = usePlaythrough(pid);
  const { data: saves = [] } = useQuery({ queryKey: ["saves", pid], queryFn: () => api.get(`/playthroughs/${pid}/saves`).then((r) => r.data) });
  const [label, setLabel] = useState("");

  const run = async (fn, msg) => {
    try { await fn(); toast.success(msg); } catch (e) { toast.error(errMsg(e)); }
  };
  const refresh = () => { qc.invalidateQueries({ queryKey: ["saves", pid] }); qc.invalidateQueries({ queryKey: ["playthrough", pid] }); qc.invalidateQueries({ queryKey: ["playthroughs"] }); };

  const create = () => run(async () => { await api.post(`/playthroughs/${pid}/saves`, { kind: "checkpoint", label: label || undefined }); setLabel(""); refresh(); }, "Checkpoint sealed");
  const load = (s) => run(async () => { await api.post(`/saves/${s.save_id}/load`); refresh(); navigate(`/play/${pid}`); }, `Restored “${s.label}”`);
  const branch = (s) => run(async () => {
    const { data } = await api.post(`/saves/${s.save_id}/branch`, {});
    localStorage.setItem(LAST_PLAY_KEY, data.playthrough_id);
    refresh();
    navigate(`/play/${data.playthrough_id}`);
  }, "A new timeline branches away");
  const remove = (s) => run(async () => { await api.delete(`/saves/${s.save_id}`); refresh(); }, "Save removed");
  const archive = () => run(async () => { await api.post(`/playthroughs/${pid}/${pt.status === "archived" ? "restore" : "archive"}`); refresh(); }, pt?.status === "archived" ? "Restored" : "Archived");

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-8 py-12 space-y-10">
      <div>
        <p className="tactical-label mb-3">Saves, checkpoints & branches</p>
        <h1 className="font-heading text-4xl sm:text-5xl text-parchment">{pt?.title || "…"}</h1>
        {pt?.branched_from && <p className="text-sm text-arcane mt-3 flex items-center gap-2"><GitBranch size={14} /> Branched at turn {pt.branched_from.clock}</p>}
      </div>
      <div className="flex flex-wrap gap-3">
        <Input value={label} onChange={(e) => setLabel(e.target.value)} placeholder="Name this checkpoint" className="bg-tome border-line w-full sm:w-72" data-testid="saves-label-input" />
        <Button onClick={create} data-testid="saves-create-new-button">Create checkpoint</Button>
        {pt && (
          <Button variant="outline" className="border-line ml-auto" onClick={archive} data-testid="saves-archive-toggle-button">
            {pt.status === "archived" ? "Restore playthrough" : "Archive playthrough"}
          </Button>
        )}
      </div>
      <ul className="space-y-3" data-testid="saves-checkpoint-list">
        {saves.map((s) => (
          <li key={s.save_id} className="bg-tome border border-line hover:border-gold/40 transition-colors p-5 flex flex-wrap items-center gap-4" data-testid={`saves-item-${s.save_id}`}>
            <span className={`text-[10px] font-mono uppercase tracking-widest border px-2 py-0.5 ${KIND_STYLE[s.kind]}`}>{s.kind}</span>
            <div className="flex-1 min-w-[180px]">
              <p className="text-parchment">{s.label}</p>
              <p className="text-xs font-mono text-dust">Turn {s.clock} · {s.campaign_time?.date} {s.campaign_time?.time} · {new Date(s.created_at).toLocaleString()}</p>
            </div>
            <Button size="sm" variant="outline" className="border-line" onClick={() => load(s)} data-testid={`saves-restore-button-${s.save_id}`}><RotateCcw size={13} className="mr-1" /> Load</Button>
            <Button size="sm" variant="outline" className="border-arcane/40 text-arcane" onClick={() => branch(s)} data-testid={`saves-branch-button-${s.save_id}`}><GitBranch size={13} className="mr-1" /> Branch</Button>
            {s.kind !== "auto" && (
              <Button size="sm" variant="ghost" onClick={() => remove(s)} data-testid={`saves-delete-button-${s.save_id}`}><Trash2 size={13} className="text-dust" /></Button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
