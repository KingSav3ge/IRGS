import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { Eye, GitBranch, RotateCcw } from "lucide-react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { api, fmtDate } from "@/lib/api";

const Body = ({ sid, onLoad, onBranch }) => {
  const { data: p } = useQuery({ queryKey: ["save-preview", sid], queryFn: () => api.get(`/saves/${sid}/preview`).then((r) => r.data) });
  if (!p) return <p className="tactical-label">Inspecting…</p>;
  const c = p.character.condition;
  return (
    <div className="space-y-5" data-testid="save-preview-body">
      <div className="grid grid-cols-2 gap-3 text-sm">
        <p className="text-ash">Turn <span className="text-parchment font-mono">{p.clock}</span> · {fmtDate(p.campaign_time?.date, p.campaign_time?.calendar)} {p.campaign_time?.time}</p>
        <p className="text-ash">At <span className="text-parchment">{p.character.location}</span></p>
        <p className="text-ash col-span-2 font-mono text-xs">Health {c.health} · Stamina {c.stamina} · Morale {c.morale} · {p.event_count} events · {p.inventory.length} items</p>
      </div>
      <div className="space-y-2">
        <p className="tactical-label">Last moments in this save</p>
        {p.last_events.map((e) => (
          <div key={e.id} className="border-l border-line pl-3">
            {e.declaration && <p className="text-xs italic text-ash">“{e.declaration}”</p>}
            <p className="text-xs text-parchment/80">{e.text}</p>
          </div>
        ))}
      </div>
      <div className={`p-3 border text-xs ${p.events_replaced ? "border-crimson/40 text-crimson" : "border-line text-ash"}`} data-testid="save-preview-impact">
        {p.events_replaced
          ? `Loading replaces ${p.events_replaced} later event(s) in this playthrough (e.g. ${p.replaced_preview.filter(Boolean).join("; ")}). A safety save of your current position is made first, so you can return.`
          : "Nothing later would be replaced. This save matches your current position."}
      </div>
      <div className="flex gap-3">
        <Button onClick={onLoad} data-testid="save-preview-load-button"><RotateCcw size={13} className="mr-1" /> Load this save</Button>
        <Button variant="outline" className="border-arcane/40 text-arcane" onClick={onBranch} data-testid="save-preview-branch-button"><GitBranch size={13} className="mr-1" /> Branch instead</Button>
      </div>
    </div>
  );
};

export const SavePreviewDialog = ({ save, onLoad, onBranch }) => {
  const [open, setOpen] = useState(false);
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button size="sm" variant="ghost" className="text-ash" data-testid={`saves-preview-button-${save.save_id}`}><Eye size={13} className="mr-1" /> Preview</Button>
      </DialogTrigger>
      <DialogContent className="bg-tome border-line" data-testid="save-preview-dialog">
        <DialogHeader>
          <DialogTitle className="font-heading text-parchment">{save.label}</DialogTitle>
          <DialogDescription className="text-ash">Check what this save contains before you restore it.</DialogDescription>
        </DialogHeader>
        {open && <Body sid={save.save_id} onLoad={() => { setOpen(false); onLoad(); }} onBranch={() => { setOpen(false); onBranch(); }} />}
      </DialogContent>
    </Dialog>
  );
};
