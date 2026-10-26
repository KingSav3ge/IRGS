import { Zap, Compass, ScrollText } from "lucide-react";

export const MODES = [
  { id: "quick", label: "Quick", icon: Zap, blurb: "Choose a name and a preset. The preset sets your attributes and gear, so you can start in under a minute." },
  { id: "guided", label: "Guided", icon: Compass, blurb: "Go one step at a time, with a short note at each stage explaining what it changes in the world." },
  { id: "detailed", label: "Detailed", icon: ScrollText, blurb: "Every field on one page: attributes, appearance, your own account and inventory." },
];

export const CreationModePicker = ({ onPick }) => (
  <div className="grid gap-5 md:grid-cols-3" data-testid="creation-mode-picker">
    {MODES.map(({ id, label, icon: Icon, blurb }, i) => (
      <button key={id} onClick={() => onPick(id)} data-testid={`creation-mode-${id}`}
        style={{ animationDelay: `${i * 80}ms` }}
        className="text-left bg-tome gold-frame p-6 space-y-3 hover-glow transition-transform hover:-translate-y-1 animate-in fade-in slide-in-from-bottom-2">
        <Icon size={22} className="text-gold" />
        <p className="font-heading text-2xl text-parchment">{label}</p>
        <p className="text-sm text-ash leading-relaxed">{blurb}</p>
        {id === "guided" && <p className="tactical-label">Recommended for first journeys</p>}
      </button>
    ))}
  </div>
);
