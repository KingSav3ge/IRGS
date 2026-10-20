import { motion } from "framer-motion";
import { Brush, Loader2, Pause, Volume2 } from "lucide-react";
import { fileUrl } from "@/lib/api";

const INTENT_COLOR = { combat: "text-crimson border-crimson/40", move: "text-emerald border-emerald/40", rest: "text-mana border-mana/40" };

export const Waves = () => (
  <span className="flex items-end gap-[2px] h-3">
    {[0, 1, 2, 3].map((i) => <span key={i} className="w-[3px] h-full bg-mana wave-bar" style={{ animationDelay: `${i * 0.15}s` }} />)}
  </span>
);

export const SceneImage = ({ entry, onPaint, compact }) => {
  if (entry.image_url) {
    return <img src={fileUrl(entry.image_url)} alt="Scene" className={`w-full object-cover border border-line ${compact ? "h-40" : "aspect-[3/2]"}`} data-testid={`gameplay-scene-image-${entry.id}`} />;
  }
  if (entry.image_status === "painting") {
    return (
      <div className={`w-full grid place-items-center bg-surface border border-arcane/30 ${compact ? "h-40" : "aspect-[3/2]"}`} data-testid={`scene-painting-${entry.id}`}>
        <span className="tactical-label !text-arcane flex items-center gap-2 animate-pulse"><Loader2 size={14} className="animate-spin" /> Painting this moment…</span>
      </div>
    );
  }
  return (
    <button onClick={() => onPaint(entry.id)} data-testid={`paint-moment-btn-${entry.id}`}
      className="text-xs text-dust hover:text-arcane transition-colors flex items-center gap-1">
      <Brush size={12} /> {entry.image_status === "failed" ? "Painting failed — try again" : "Paint this moment"}
    </button>
  );
};

export const NarrativeEntry = ({ entry, index, narrator, voiceOpts, onPaint }) => {
  const text = entry.text;
  const playing = narrator.playingId === entry.id;
  return (
    <motion.article initial={{ opacity: 0, y: 14 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.45 }}
      className="space-y-4" data-testid={`gameplay-narrative-item-${index}`}>
      {entry.declaration && (
        <div className="flex items-start gap-3">
          <span className={`text-[10px] font-mono uppercase tracking-widest border px-2 py-0.5 ${INTENT_COLOR[entry.intent] || "text-gold border-gold/40"}`} data-testid={`gameplay-intent-${entry.id}`}>{entry.intent}</span>
          <p className="text-sm text-ash italic">“{entry.declaration}”</p>
        </div>
      )}
      {entry.kind === "opening_scene" && <h3 className="font-heading text-xl text-gold">{entry.title}</h3>}
      {(entry.image_url || entry.image_status === "painting") && <SceneImage entry={entry} onPaint={onPaint} />}
      <p className={`font-prose text-lg sm:text-xl leading-relaxed text-parchment/95 whitespace-pre-line ${index === 0 ? "drop-cap" : ""}`}>{text}</p>
      <div className="flex items-center gap-5 text-xs text-dust font-mono">
        <span>{entry.campaign_date || ""} {entry.campaign_time || ""}</span>
        <button onClick={() => narrator.speak(entry.id, text, voiceOpts)} data-testid={`gameplay-read-aloud-button-${entry.id}`}
          className={`flex items-center gap-2 transition-colors ${playing ? "text-mana" : "hover:text-mana"}`}>
          {narrator.loadingId === entry.id ? <Loader2 size={12} className="animate-spin" /> : playing ? <Pause size={12} /> : <Volume2 size={12} />}
          {playing ? <Waves /> : "Read aloud"}
        </button>
        {!entry.image_url && entry.image_status !== "painting" && <SceneImage entry={entry} onPaint={onPaint} />}
      </div>
      <div className="h-px bg-gradient-to-r from-gold/30 via-line to-transparent" />
    </motion.article>
  );
};
