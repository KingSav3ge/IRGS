import { useMemo, useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { Heart } from "lucide-react";
import { toast } from "sonner";
import { Switch } from "@/components/ui/switch";
import { api, errMsg } from "@/lib/api";

const HeartButton = ({ r, onToggle }) => (
  <button onClick={() => onToggle(r)} aria-label={r.wishlisted ? "Remove from wishlist" : "Add to wishlist"}
    data-testid={`concept-wishlist-btn-${r.id}`}
    className="absolute top-4 right-4 p-1.5 transition-transform hover:scale-110 active:scale-95">
    <Heart size={18} className={r.wishlisted ? "fill-crimson text-crimson" : "text-dust hover:text-crimson"} />
  </button>
);

const ConceptCard = ({ r, isAdmin, onToggle }) => (
  <article data-theme={r.theme} className="relative bg-tome gold-frame p-5 space-y-2 hover-glow" data-testid={`concept-card-${r.id}`}>
    {!r.playable && <HeartButton r={r} onToggle={onToggle} />}
    <p className="tactical-label pr-8">{r.id} · {r.tier}</p>
    <h3 className="font-heading text-lg text-parchment">{r.title}</h3>
    <p className="text-xs text-ash italic">{r.tagline}</p>
    <p className="text-xs text-dust">{r.setting} · {r.period}</p>
    <p className="text-sm text-ash line-clamp-3">{r.synopsis}</p>
    <div className="flex flex-wrap gap-1 pt-1">
      {r.genres.slice(0, 4).map((g) => <span key={g} className="text-[10px] font-mono uppercase text-dust border border-line px-1.5">{g}</span>)}
    </div>
    <div className="flex items-center justify-between">
      <p className={`text-[10px] font-mono uppercase tracking-widest ${r.playable ? "text-emerald" : "text-dust"}`}>
        {r.playable ? "Playable" : isAdmin ? `Concept · ${r.status.replace("_", " ")}` : "Coming later"}
      </p>
      {isAdmin && !r.playable && (
        <span className="text-[10px] font-mono uppercase text-gold" data-testid={`concept-wishlist-count-${r.id}`}>
          {r.wishlist_count} wished
        </span>
      )}
    </div>
  </article>
);

const Pill = ({ active, onClick, testid, children }) => (
  <button onClick={onClick} data-testid={testid}
    className={`text-[11px] font-mono uppercase px-3 py-1 border transition-colors ${active ? "border-gold text-gold" : "border-line text-dust hover:text-ash"}`}>{children}</button>
);

export const ConceptLibrary = ({ isAdmin }) => {
  const qc = useQueryClient();
  const [tier, setTier] = useState("all");
  const [tab, setTab] = useState("all");
  const [open, setOpen] = useState(!isAdmin);
  const { data } = useQuery({ queryKey: ["catalogue"], queryFn: () => api.get("/catalogue").then((r) => r.data) });
  const upcoming = useMemo(() => (data?.records || []).filter((r) => isAdmin || !r.playable), [data, isAdmin]);
  const records = useMemo(() => upcoming.filter((r) => (tier === "all" || r.tier === tier) && (tab === "all" || r.wishlisted)), [upcoming, tier, tab]);
  if (!data || (!isAdmin && !data.concepts_visible)) return null;
  const tiers = ["all", ...new Set(upcoming.map((r) => r.tier))];
  const wishedCount = upcoming.filter((r) => r.wishlisted).length;
  const totalWishes = upcoming.reduce((a, r) => a + (r.wishlist_count || 0), 0);

  const patch = (id, wishlisted) => qc.setQueryData(["catalogue"], (d) => ({
    ...d, records: d.records.map((x) => x.id === id ? { ...x, wishlisted, ...(isAdmin ? { wishlist_count: x.wishlist_count + (wishlisted ? 1 : -1) } : {}) } : x),
  }));
  const toggle = async (r) => {
    patch(r.id, !r.wishlisted);
    try {
      await (r.wishlisted ? api.delete(`/catalogue/${r.id}/wishlist`) : api.post(`/catalogue/${r.id}/wishlist`));
      if (!r.wishlisted) toast.success(`${r.title} added to your wishlist`);
    } catch (e) { patch(r.id, r.wishlisted); toast.error(errMsg(e)); }
  };
  const setVisible = async (v) => {
    try {
      await api.put("/admin/catalogue/visibility", { show_to_players: v });
      qc.setQueryData(["catalogue"], (d) => ({ ...d, concepts_visible: v }));
      toast.success(v ? "Upcoming campaigns are now shown to players" : "Upcoming campaigns are hidden from players");
    } catch (e) { toast.error(errMsg(e)); }
  };

  return (
    <section className="space-y-6 border-t border-line pt-10" data-testid={isAdmin ? "admin-concept-library" : "player-concept-library"}>
      <div className="flex flex-wrap items-center gap-4">
        <h2 className="font-heading text-base md:text-lg text-parchment">
          {isAdmin ? `Content Library v${data.version}: ${data.counts.total} concepts` : "Coming to IRGS"}
        </h2>
        {isAdmin ? (
          <>
            <span className="tactical-label" data-testid="admin-total-wishes">{totalWishes} wishes in total</span>
            <label className="flex items-center gap-2 text-xs text-ash">
              <Switch checked={data.concepts_visible} onCheckedChange={setVisible} data-testid="admin-concept-visibility-switch" />
              Show upcoming campaigns to players
            </label>
          </>
        ) : <span className="text-sm text-ash">Heart the campaigns you want next. It helps us choose what to build.</span>}
        {isAdmin && <button onClick={() => setOpen(!open)} className="ml-auto text-sm text-gold" data-testid="admin-concept-toggle">{open ? "Hide" : "Show"} concepts</button>}
      </div>
      {open && (
        <>
          <div className="flex flex-wrap gap-2">
            <Pill active={tab === "all"} onClick={() => setTab("all")} testid="concept-tab-all">All upcoming</Pill>
            <Pill active={tab === "wishlist"} onClick={() => setTab("wishlist")} testid="concept-tab-wishlist">My Wishlist · {wishedCount}</Pill>
            <span className="w-px bg-line mx-2" />
            {tiers.map((t) => (
              <Pill key={t} active={tier === t} onClick={() => setTier(t)} testid={`concept-tier-${t.replace(/\s+/g, "-").toLowerCase()}`}>{t}</Pill>
            ))}
          </div>
          {records.length === 0 ? (
            <p className="text-sm text-dust" data-testid="concept-empty">{tab === "wishlist" ? "Your wishlist is empty. Tap a heart to add a campaign." : "No concepts in this tier."}</p>
          ) : (
            <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">{records.map((r) => <ConceptCard key={r.id} r={r} isAdmin={isAdmin} onToggle={toggle} />)}</div>
          )}
        </>
      )}
    </section>
  );
};
