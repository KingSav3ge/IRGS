import { useQuery } from "@tanstack/react-query";
import { ScrollText } from "lucide-react";
import { api, fmtDate } from "@/lib/api";

export const HistoryReference = ({ pid }) => {
  const { data } = useQuery({
    queryKey: ["history", pid],
    queryFn: () => api.get(`/playthroughs/${pid}/history-reference`).then((r) => r.data),
  });
  if (!data?.available) return null;

  return (
    <aside className="bg-tome gold-frame p-6 space-y-4" data-testid="history-reference-panel">
      <div className="flex items-center gap-2">
        <ScrollText size={16} className="text-gold" />
        <h2 className="font-heading text-base md:text-lg text-parchment">What the historical record says</h2>
      </div>
      <p className="text-xs text-ash">{data.note} This is a read-only comparison. Nothing here is scheduled to happen in your story.</p>
      <ul className="space-y-4">
        {data.events.map((e) => {
          const passed = data.current_date >= e.date;
          return (
            <li key={e.id} className="border-l border-line pl-4 space-y-1" data-testid={`history-event-${e.id}`}>
              <p className="font-mono text-xs text-dust">
                {fmtDate(e.date)} · {e.classification}
                <span className={`ml-2 ${passed ? "text-emerald" : "text-dust"}`}>{passed ? "your story has passed this date" : "not yet reached"}</span>
              </p>
              <p className="text-parchment text-sm">{e.title}</p>
              <p className="text-xs text-ash">{e.description}</p>
              {e.recorded_outcome && <p className="text-xs italic text-ash">Recorded outcome: {e.recorded_outcome}</p>}
            </li>
          );
        })}
      </ul>
      <ul className="text-[11px] text-dust space-y-1">
        {data.sources.map((s) => <li key={s.id}>· {s.url ? <a href={s.url} target="_blank" rel="noreferrer" className="hover:text-gold underline">{s.title}</a> : s.title}</li>)}
      </ul>
    </aside>
  );
};
