import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Copy, Link2, Share2, X } from "lucide-react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";

const shareUrl = (id) => `${window.location.origin}/story/${id}`;

const copy = async (id) => {
  try {
    await navigator.clipboard.writeText(shareUrl(id));
    toast.success("Link copied");
  } catch {
    toast(shareUrl(id));
  }
};

export const ShareDialog = ({ pid, triggerClassName = "" }) => {
  const qc = useQueryClient();
  const [busy, setBusy] = useState(null);
  const { data: shares = [] } = useQuery({
    queryKey: ["shares", pid],
    queryFn: () => api.get(`/playthroughs/${pid}/shares`).then((r) => r.data),
  });

  const create = async (mode) => {
    setBusy(mode);
    try {
      const { data } = await api.post(`/playthroughs/${pid}/shares`, { mode });
      qc.invalidateQueries({ queryKey: ["shares", pid] });
      copy(data.share_id);
    } catch (e) { toast.error(errMsg(e)); } finally { setBusy(null); }
  };

  const revoke = async (id) => {
    try {
      await api.delete(`/shares/${id}`);
      qc.invalidateQueries({ queryKey: ["shares", pid] });
      toast.success("Sharing turned off for that link");
    } catch (e) { toast.error(errMsg(e)); }
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" className={`border-line ${triggerClassName}`} data-testid="share-storybook-open-button">
          <Share2 size={14} className="mr-2" /> Share storybook
        </Button>
      </DialogTrigger>
      <DialogContent className="bg-tome border-line" data-testid="share-storybook-dialog">
        <DialogHeader>
          <DialogTitle className="font-heading text-parchment">Share as an illustrated storybook</DialogTitle>
          <DialogDescription className="text-ash">Anyone with the link can read it. They can't edit anything.</DialogDescription>
        </DialogHeader>
        <div className="grid grid-cols-2 gap-3">
          <Button disabled={!!busy} onClick={() => create("snapshot")} data-testid="share-create-snapshot-button" className="h-auto py-3 flex-col items-start">
            <span>Snapshot</span><span className="text-[11px] opacity-80 font-normal">Frozen at this moment</span>
          </Button>
          <Button disabled={!!busy} variant="outline" onClick={() => create("live")} data-testid="share-create-live-button" className="h-auto py-3 flex-col items-start border-line">
            <span>Live link</span><span className="text-[11px] text-ash font-normal">Updates as you play</span>
          </Button>
        </div>
        <ul className="space-y-2" data-testid="share-links-list">
          {shares.length === 0 && <li className="text-xs text-dust">No active links.</li>}
          {shares.map((s) => (
            <li key={s.share_id} className="flex items-center gap-2 border border-line px-3 py-2 text-xs" data-testid={`share-link-${s.share_id}`}>
              <Link2 size={12} className="text-gold" />
              <span className="uppercase font-mono text-gold">{s.mode}</span>
              <a href={shareUrl(s.share_id)} target="_blank" rel="noreferrer" className="truncate flex-1 text-ash hover:text-parchment">{shareUrl(s.share_id)}</a>
              <button onClick={() => copy(s.share_id)} data-testid={`share-copy-${s.share_id}`}><Copy size={13} className="text-ash hover:text-parchment" /></button>
              <button onClick={() => revoke(s.share_id)} data-testid={`share-revoke-${s.share_id}`}><X size={13} className="text-crimson" /></button>
            </li>
          ))}
        </ul>
      </DialogContent>
    </Dialog>
  );
};
