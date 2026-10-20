import { Clock, MapPin } from "lucide-react";
import { fileUrl, fmtDate } from "@/lib/api";

const Bar = ({ label, value, color, testid }) => (
  <div className="space-y-1" data-testid={testid}>
    <div className="flex justify-between text-xs"><span className="text-ash">{label}</span><span className="font-mono font-bold text-parchment">{value}</span></div>
    <div className="h-1.5 bg-void border border-line"><div className={`h-full ${color} transition-[width] duration-700`} style={{ width: `${value}%` }} /></div>
  </div>
);

export const StatusPanel = ({ pt }) => {
  const v = pt.view;
  const c = v.character.condition;
  return (
    <aside className="space-y-6 overflow-y-auto scroll-thin pr-1" data-testid="gameplay-status-panel">
      <div className="flex gap-4 items-center">
        <div className="h-20 w-16 bg-surface border border-gold/30 overflow-hidden shrink-0">
          {pt.portrait_url && <img src={fileUrl(pt.portrait_url)} alt="" className="h-full w-full object-cover" />}
        </div>
        <div>
          <p className="font-heading text-lg text-parchment" data-testid="gameplay-character-name">{v.character.name}</p>
          <p className="text-xs text-ash">{v.background}</p>
        </div>
      </div>
      <div className="bg-surface border border-line p-4 space-y-2">
        <p className="tactical-label">World clock</p>
        <p className="font-mono text-parchment flex items-center gap-2" data-testid="gameplay-world-clock-display">
          <Clock size={14} className="text-gold" /> {fmtDate(v.campaign_time.date, v.campaign_time.calendar)} · {v.campaign_time.time}
        </p>
        <p className="text-xs text-dust font-mono">Turn {v.clock} · {v.campaign_time.calendar} calendar</p>
        <p className="text-sm text-ash flex items-center gap-2"><MapPin size={13} className="text-gold" /> {v.character.location}</p>
      </div>
      <div className="space-y-3">
        <Bar label="Health" value={c.health} color="bg-crimson" testid="gameplay-hp-bar" />
        <Bar label="Stamina" value={c.stamina} color="bg-emerald" testid="gameplay-stamina-bar" />
        <Bar label="Morale" value={c.morale} color="bg-gold" testid="gameplay-morale-bar" />
      </div>
      <div className="grid grid-cols-2 gap-2">
        {Object.entries(v.attributes).map(([k, val]) => (
          <div key={k} className="border border-line px-3 py-2 flex justify-between text-xs">
            <span className="capitalize text-ash">{k}</span><span className="font-mono font-bold text-gold">{val}</span>
          </div>
        ))}
      </div>
      <div className="space-y-2">
        <p className="tactical-label">Inventory</p>
        <ul className="text-sm text-parchment space-y-1" data-testid="gameplay-inventory-list">
          {v.inventory.map((i, n) => <li key={n}>· {i.item}{i.qty > 1 ? ` ×${i.qty}` : ""}</li>)}
        </ul>
      </div>
      <div className="space-y-2">
        <p className="tactical-label">Known figures</p>
        <ul className="text-sm space-y-2">
          {v.known_actors.map((a) => <li key={a.id}><span className="text-parchment">{a.name}</span><span className="block text-xs text-dust">{a.role}</span></li>)}
        </ul>
      </div>
    </aside>
  );
};
