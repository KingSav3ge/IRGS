import { useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { CalendarRange, Lock, Play } from "lucide-react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { api } from "@/lib/api";

const EntryRow = ({ e, featured, onPlay }) => (
  <li className={`flex items-start gap-4 border-b border-line py-3 ${e.playable ? "" : "opacity-70"}`} data-testid={`entry-point-${e.id}`}>
    <span className={`font-mono text-sm w-12 shrink-0 ${featured ? "text-gold" : "text-ash"}`}>{e.year}</span>
    <div className="flex-1 min-w-0">
      <p className="text-parchment text-sm">{e.title} <span className="text-[10px] font-mono uppercase tracking-wider text-dust ml-2">{e.type}</span></p>
      <p className="text-xs text-ash mt-1">{e.description}</p>
    </div>
    {e.playable ? (
      <Button size="sm" onClick={onPlay} data-testid={`entry-point-play-${e.id}`}><Play size={12} className="mr-1" /> Begin</Button>
    ) : (
      <span className="text-[10px] font-mono uppercase text-dust flex items-center gap-1 shrink-0"><Lock size={10} /> Proposed</span>
    )}
  </li>
);

export const EntryCatalogueDialog = ({ scenarioId }) => {
  const navigate = useNavigate();
  const { data } = useQuery({
    queryKey: ["entries", scenarioId],
    queryFn: () => api.get(`/campaigns/${scenarioId}/entries`).then((r) => r.data),
  });
  if (!data) return null;
  const featured = new Set(data.featured_years);

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" className="border-line w-full" data-testid={`library-entry-points-btn-${scenarioId}`}>
          <CalendarRange size={14} className="mr-2" /> {data.entries.length} entry points · {data.period}
        </Button>
      </DialogTrigger>
      <DialogContent className="bg-tome border-line max-w-2xl max-h-[85vh] overflow-y-auto scroll-thin" data-testid="entry-catalogue-dialog">
        <DialogHeader>
          <DialogTitle className="font-heading text-parchment">{data.title}: choose an entry point</DialogTitle>
          <DialogDescription className="text-ash">
            The 1415 opening is fully researched. The other dates are proposals and can't be played yet. Later history is never scripted; it unfolds only through play.
          </DialogDescription>
        </DialogHeader>
        {data.periods.map((p) => (
          <section key={p.id} className="space-y-1" data-testid={`entry-period-${p.id}`}>
            <p className="tactical-label pt-3">{p.name} · {p.range}</p>
            <ul>
              {data.entries.filter((e) => e.period_id === p.id).map((e) => (
                <EntryRow key={e.id} e={e} featured={featured.has(e.year)} onPlay={() => navigate(`/create/${e.scenario_id}`)} />
              ))}
            </ul>
          </section>
        ))}
      </DialogContent>
    </Dialog>
  );
};
