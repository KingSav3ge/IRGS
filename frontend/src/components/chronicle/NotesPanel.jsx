import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { FileText, StickyNote, Trash2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { api, errMsg, fmtDate } from "@/lib/api";

export const NotesPanel = ({ pid, entities = [] }) => {
  const qc = useQueryClient();
  const { data: notes = [] } = useQuery({ queryKey: ["notes", pid], queryFn: () => api.get(`/playthroughs/${pid}/notes`).then((r) => r.data) });
  const [form, setForm] = useState({ kind: "note", title: "", body: "", entity_ids: [] });

  const save = async () => {
    try {
      await api.post(`/playthroughs/${pid}/notes`, form);
      setForm({ kind: form.kind, title: "", body: "", entity_ids: [] });
      qc.invalidateQueries({ queryKey: ["notes", pid] });
      qc.invalidateQueries({ queryKey: ["entity", pid] });
      toast.success(form.kind === "note" ? "Note saved" : "Document written");
    } catch (e) { toast.error(errMsg(e)); }
  };
  const remove = async (id) => {
    try { await api.delete(`/notes/${id}`); qc.invalidateQueries({ queryKey: ["notes", pid] }); qc.invalidateQueries({ queryKey: ["entity", pid] }); } catch (e) { toast.error(errMsg(e)); }
  };
  const toggleEntity = (id) => setForm({ ...form, entity_ids: form.entity_ids.includes(id) ? form.entity_ids.filter((x) => x !== id) : [...form.entity_ids, id] });

  return (
    <div className="grid md:grid-cols-[340px_1fr] gap-8" data-testid="notes-panel">
      <div className="space-y-3 bg-tome border border-line p-5">
        <div className="grid grid-cols-2 border border-line">
          {[["note", "Player note"], ["document", "In-world document"]].map(([k, l]) => (
            <button key={k} onClick={() => setForm({ ...form, kind: k })} data-testid={`notes-kind-${k}`}
              className={`py-2 text-xs ${form.kind === k ? "bg-gold/15 text-gold" : "text-ash"}`}>{l}</button>
          ))}
        </div>
        <p className="text-[11px] text-dust">{form.kind === "note" ? "Private, out-of-character notes. They never change the world." : "Something your character writes, such as a letter, diary entry or ledger. It's kept as their own account."}</p>
        <Input value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} placeholder="Title" className="bg-void border-line" data-testid="notes-title-input" />
        <Textarea value={form.body} onChange={(e) => setForm({ ...form, body: e.target.value })} rows={5} placeholder="Write…" className="bg-void border-line font-prose text-base" data-testid="notes-body-input" />
        <div className="flex flex-wrap gap-1">
          {entities.map((e) => (
            <button key={e.id} onClick={() => toggleEntity(e.id)} data-testid={`notes-link-${e.id}`}
              className={`text-[10px] px-2 py-0.5 border ${form.entity_ids.includes(e.id) ? "border-gold text-gold" : "border-line text-dust"}`}>{e.name}</button>
          ))}
        </div>
        <Button onClick={save} disabled={!form.title.trim()} className="w-full" data-testid="notes-save-button">Save</Button>
      </div>
      <ul className="space-y-4" data-testid="notes-list">
        {notes.length === 0 && <li className="text-sm text-dust">No notes or documents yet.</li>}
        {notes.map((n) => (
          <li key={n.note_id} className={`p-5 border ${n.kind === "document" ? "border-gold/30 bg-surface" : "border-line"}`} data-testid={`note-${n.note_id}`}>
            <div className="flex items-center gap-2 mb-2">
              {n.kind === "document" ? <FileText size={14} className="text-gold" /> : <StickyNote size={14} className="text-ash" />}
              <span className="text-parchment font-heading">{n.title}</span>
              <span className="text-[10px] font-mono text-dust ml-auto">turn {n.at_clock} · {fmtDate(n.campaign_date)}</span>
              <button onClick={() => remove(n.note_id)} data-testid={`note-delete-${n.note_id}`}><Trash2 size={13} className="text-dust hover:text-crimson" /></button>
            </div>
            <p className={`whitespace-pre-line text-ash ${n.kind === "document" ? "font-prose italic text-lg" : "text-sm"}`}>{n.body}</p>
            {n.entity_ids?.length > 0 && <p className="text-[10px] font-mono text-dust mt-2">Linked: {n.entity_ids.map((id) => entities.find((e) => e.id === id)?.name || id).join(", ")}</p>}
          </li>
        ))}
      </ul>
    </div>
  );
};
