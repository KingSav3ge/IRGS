import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { MapPin, User } from "lucide-react";
import { api, fmtDate } from "@/lib/api";

const Detail = ({ pid, entity }) => {
  const { data } = useQuery({ queryKey: ["entity", pid, entity.id], queryFn: () => api.get(`/playthroughs/${pid}/entities/${entity.id}`).then((r) => r.data) });
  if (!data) return <p className="tactical-label">Gathering records…</p>;
  return (
    <div className="space-y-6" data-testid={`entity-detail-${entity.id}`}>
      <div>
        <h3 className="font-heading text-2xl text-parchment">{entity.name}</h3>
        <p className="text-sm text-ash">{entity.role}{entity.location ? ` · last seen at ${entity.location}` : ""}</p>
        {entity.type === "person" && <p className="text-xs font-mono mt-1 text-gold">Attitude toward you: {entity.disposition > 0 ? "+" : ""}{entity.disposition}
          {data.disposition_trend.length > 0 && ` (changes: ${data.disposition_trend.map((t) => t.disposition).join(" → ")})`}</p>}
      </div>
      {data.rumours.length > 0 && (
        <div className="space-y-1"><p className="tactical-label">Rumours they spread</p>
          {data.rumours.map((r, i) => <p key={i} className="text-sm italic text-ash">“{r.text}”</p>)}</div>
      )}
      {data.notes.length > 0 && (
        <div className="space-y-1"><p className="tactical-label">Your linked notes</p>
          {data.notes.map((n) => <p key={n.note_id} className="text-sm text-ash">· {n.title}</p>)}</div>
      )}
      <ol className="space-y-4 border-l border-gold/25 pl-5" data-testid="entity-events">
        {data.events.length === 0 && <li className="text-sm text-dust">Not yet mentioned in your story.</li>}
        {data.events.map((e) => (
          <li key={e.id} className="space-y-1">
            <p className="font-mono text-[11px] text-dust">#{e.at} · {fmtDate(e.campaign_date)} {e.campaign_time || ""} · {e.kind?.replace("_", " ")}</p>
            {e.declaration && <p className="text-xs italic text-ash">“{e.declaration}”</p>}
            <p className="text-sm text-parchment/90">{e.text}</p>
          </li>
        ))}
      </ol>
    </div>
  );
};

export const EntityHistory = ({ pid, entities }) => {
  const [sel, setSel] = useState(null);
  const current = entities.find((e) => e.id === sel) || entities[0];
  return (
    <div className="grid md:grid-cols-[260px_1fr] gap-8" data-testid="entity-history">
      <ul className="space-y-1">
        {entities.map((e) => (
          <li key={e.id}>
            <button onClick={() => setSel(e.id)} data-testid={`entity-item-${e.id}`}
              className={`w-full text-left px-3 py-2 border flex items-center gap-2 text-sm ${current?.id === e.id ? "border-gold/60 bg-gold/5 text-parchment" : "border-transparent text-ash hover:text-parchment"}`}>
              {e.type === "person" ? <User size={13} /> : <MapPin size={13} />}
              <span className="flex-1 truncate">{e.name}</span>
              <span className="font-mono text-[10px] text-dust">{e.mentions}</span>
            </button>
          </li>
        ))}
      </ul>
      {current && <Detail key={current.id} pid={pid} entity={current} />}
    </div>
  );
};
