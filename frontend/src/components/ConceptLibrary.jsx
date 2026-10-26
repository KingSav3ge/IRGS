import { useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

const ConceptCard = ({ r }) => (
  <article data-theme={r.theme} className="bg-tome gold-frame p-5 space-y-2 hover-glow" data-testid={`concept-card-${r.id}`}>
    <p className="tactical-label">{r.id} · {r.tier}</p>
    <h3 className="font-heading text-lg text-parchment">{r.title}</h3>
    <p className="text-xs text-ash italic">{r.tagline}</p>
    <p className="text-xs text-dust">{r.setting} · {r.period}</p>
    <p className="text-sm text-ash line-clamp-3">{r.synopsis}</p>
    <div className="flex flex-wrap gap-1 pt-1">
      {r.genres.slice(0, 4).map((g) => <span key={g} className="text-[10px] font-mono uppercase text-dust border border-line px-1.5">{g}</span>)}
    </div>
    <p className={`text-[10px] font-mono uppercase tracking-widest ${r.playable ? "text-emerald" : "text-dust"}`}>
      {r.playable ? "Playable" : `Concept · ${r.status.replace("_", " ")} · not released`}
    </p>
  </article>
);

export const ConceptLibrary = ({ isAdmin }) => {
  const [tier, setTier] = useState("all");
  const [open, setOpen] = useState(false);
  const { data } = useQuery({ queryKey: ["catalogue"], queryFn: () => api.get("/catalogue").then((r) => r.data), enabled: isAdmin });
  const records = useMemo(() => (data?.records || []).filter((r) => tier === "all" || r.tier === tier), [data, tier]);
  if (!isAdmin || !data) return null;
  const tiers = ["all", ...new Set(data.records.map((r) => r.tier))];

  return (
    <section className="space-y-6 border-t border-line pt-10" data-testid="admin-concept-library">
      <div className="flex flex-wrap items-center gap-4">
        <h2 className="font-heading text-base md:text-lg text-parchment">Content Library v{data.version}: {data.counts.total} concepts</h2>
        <span className="tactical-label !text-crimson">Admin only · hidden from players until released</span>
        <button onClick={() => setOpen(!open)} className="ml-auto text-sm text-gold" data-testid="admin-concept-toggle">{open ? "Hide" : "Show"} concepts</button>
      </div>
      {open && (
        <>
          <div className="flex flex-wrap gap-2">
            {tiers.map((t) => (
              <button key={t} onClick={() => setTier(t)} data-testid={`concept-tier-${t.replace(/\s+/g, "-").toLowerCase()}`}
                className={`text-[11px] font-mono uppercase px-3 py-1 border ${tier === t ? "border-gold text-gold" : "border-line text-dust"}`}>{t}</button>
            ))}
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">{records.map((r) => <ConceptCard key={r.id} r={r} />)}</div>
        </>
      )}
    </section>
  );
};
