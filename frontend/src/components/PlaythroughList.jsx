import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Archive, ArchiveRestore, GitBranch } from "lucide-react";
import { Button } from "@/components/ui/button";
import { api, errMsg, fileUrl } from "@/lib/api";

export const PlaythroughList = () => {
  const [status, setStatus] = useState("active");
  const navigate = useNavigate();
  const qc = useQueryClient();
  const { data = [] } = useQuery({
    queryKey: ["playthroughs", status],
    queryFn: () => api.get("/playthroughs", { params: { status } }).then((r) => r.data),
  });

  const toggle = async (p) => {
    try {
      await api.post(`/playthroughs/${p.playthrough_id}/${status === "active" ? "archive" : "restore"}`);
      qc.invalidateQueries({ queryKey: ["playthroughs"] });
      toast.success(status === "active" ? "Playthrough archived" : "Playthrough restored");
    } catch (e) {
      toast.error(errMsg(e));
    }
  };

  return (
    <section className="space-y-5" data-testid="library-playthroughs">
      <div className="flex items-center gap-4">
        <h2 className="font-heading text-base md:text-lg text-parchment tracking-wide">Your chronicles</h2>
        {["active", "archived"].map((s) => (
          <button key={s} onClick={() => setStatus(s)} data-testid={`library-playthrough-tab-${s}`}
            className={`text-xs font-mono uppercase tracking-widest ${status === s ? "text-gold" : "text-dust hover:text-ash"}`}>{s}</button>
        ))}
      </div>
      {data.length === 0 ? (
        <p className="text-sm text-dust" data-testid="library-playthroughs-empty">
          {status === "active" ? "No chronicles yet. Begin a campaign below." : "Nothing archived."}
        </p>
      ) : (
        <div className="flex gap-4 overflow-x-auto pb-2 scroll-thin">
          {data.map((p) => (
            <div key={p.playthrough_id} className="min-w-[280px] bg-surface border border-line hover:border-gold/50 transition-colors p-4 flex gap-4" data-testid={`library-playthrough-${p.playthrough_id}`}>
              <div className="h-16 w-16 shrink-0 bg-tome border border-line overflow-hidden">
                {p.portrait_url && <img src={fileUrl(p.portrait_url)} alt="" className="h-full w-full object-cover" />}
              </div>
              <div className="flex-1 min-w-0 space-y-1">
                <p className="font-heading text-sm text-parchment truncate">{p.title}</p>
                <p className="text-[11px] font-mono text-dust">Turn {p.clock} · {p.campaign_time.date} · {p.campaign_time.time}</p>
                {p.branched_from && <p className="text-[11px] text-arcane flex items-center gap-1"><GitBranch size={11} /> branch</p>}
                <div className="flex gap-2 pt-1">
                  {status === "active" && (
                    <Button size="sm" className="h-7 text-xs" onClick={() => navigate(`/play/${p.playthrough_id}`)} data-testid={`library-resume-btn-${p.playthrough_id}`}>Resume</Button>
                  )}
                  <Button size="sm" variant="ghost" className="h-7 text-xs text-ash" onClick={() => toggle(p)} data-testid={`library-archive-toggle-${p.playthrough_id}`}>
                    {status === "active" ? <Archive size={12} /> : <><ArchiveRestore size={12} className="mr-1" /> Restore</>}
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
};
