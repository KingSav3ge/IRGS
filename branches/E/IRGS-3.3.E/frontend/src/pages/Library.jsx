import { useMemo, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { motion } from "framer-motion";
import { Lock, Play, Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { api } from "@/lib/api";
import { PlaythroughList } from "@/components/PlaythroughList";
import { EntryCatalogueDialog } from "@/components/EntryCatalogueDialog";

const GENRES = ["all", "historical", "fantasy", "scifi"];

const CampaignCard = ({ c, i }) => {
  const navigate = useNavigate();
  return (
    <motion.article data-theme={c.theme} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.08 }}
      className="group bg-tome gold-frame rounded-sm overflow-hidden flex flex-col hover-glow"
      data-testid={`library-campaign-card-${c.id}`}>
      <div className="relative h-52 overflow-hidden">
        <img src={c.cover_image} alt={c.title} className="h-full w-full object-cover group-hover:scale-105 transition-transform duration-700" />
        <div className="absolute inset-0 bg-gradient-to-t from-tome via-tome/30 to-transparent" />
        {c.premium && (
          <span className="absolute top-3 right-3 tactical-label bg-void/80 px-2 py-1 border border-gold/40">Premium</span>
        )}
      </div>
      <div className="p-6 flex flex-col gap-3 flex-1">
        <p className="tactical-label">{c.era} · {c.difficulty}</p>
        <h3 className="font-heading text-xl sm:text-2xl text-parchment">{c.title}</h3>
        <p className="text-xs text-dust">{c.campaign_title}</p>
        <p className="font-prose text-lg text-ash leading-relaxed flex-1">{c.summary}</p>
        <div className="flex flex-wrap gap-2">
          {c.tags.map((t) => <span key={t} className="text-[10px] font-mono uppercase tracking-wider text-dust border border-line px-2 py-0.5">{t}</span>)}
        </div>
        {c.entry_catalogue && <EntryCatalogueDialog scenarioId={c.id} />}
        {c.locked ? (
          <Button variant="outline" className="mt-2 border-gold/40 text-gold hover:bg-gold/10" onClick={() => navigate("/store")} data-testid={`library-buy-btn-${c.id}`}>
            <Lock size={14} className="mr-2" /> Unlock · ${c.price}
          </Button>
        ) : (
          <Button className="mt-2 font-heading tracking-widest active:scale-[0.98] transition-transform" onClick={() => navigate(`/create/${c.id}`)} data-testid={`library-play-btn-${c.id}`}>
            <Play size={14} className="mr-2" /> Begin campaign
          </Button>
        )}
      </div>
    </motion.article>
  );
};

export default function Library() {
  const [genre, setGenre] = useState("all");
  const [q, setQ] = useState("");
  const { data: campaigns = [], isLoading } = useQuery({ queryKey: ["campaigns"], queryFn: () => api.get("/campaigns").then((r) => r.data) });

  const shown = useMemo(() => campaigns.filter((c) =>
    (genre === "all" || c.genre === genre) &&
    (`${c.title} ${c.campaign_title} ${c.tags.join(" ")}`.toLowerCase().includes(q.toLowerCase()))), [campaigns, genre, q]);

  return (
    <div className="mx-auto max-w-[1600px] px-4 sm:px-8 py-12 space-y-16">
      <section className="max-w-3xl">
        <p className="tactical-label mb-4">The Content Library</p>
        <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl text-parchment">Choose the hour your story begins</h1>
        <p className="font-prose text-xl text-ash mt-5">Every campaign opens frozen at a dated cutoff. Nothing after it is decided — until you act.</p>
      </section>

      <PlaythroughList />

      <section className="space-y-8">
        <div className="flex flex-wrap items-center gap-4">
          <div className="flex border border-line" data-testid="library-genre-filter">
            {GENRES.map((g) => (
              <button key={g} onClick={() => setGenre(g)} data-testid={`library-genre-${g}`}
                className={`px-4 py-2 text-xs font-mono uppercase tracking-widest transition-colors ${genre === g ? "bg-gold text-void" : "text-ash hover:text-parchment"}`}>
                {g}
              </button>
            ))}
          </div>
          <div className="relative w-full sm:w-72">
            <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-dust" />
            <Input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search campaigns" className="pl-9 bg-tome border-line" data-testid="library-search-input" />
          </div>
          <Link to="/store" className="ml-auto text-sm text-ash hover:text-gold transition-colors" data-testid="library-store-link">Visit the Store →</Link>
        </div>
        {isLoading ? (
          <p className="tactical-label">Loading campaigns…</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
            {shown.map((c, i) => <CampaignCard key={c.id} c={c} i={i} />)}
          </div>
        )}
      </section>
    </div>
  );
}
