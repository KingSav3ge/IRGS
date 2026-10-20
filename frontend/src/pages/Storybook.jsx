import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { motion } from "framer-motion";
import { Feather } from "lucide-react";
import { api, fileUrl, fmtDate } from "@/lib/api";

const Entry = ({ e, first }) => {
  if (e.kind === "npc_action") {
    return (
      <aside className="border-l-2 border-gold/50 pl-5 font-prose italic text-lg text-ash" data-testid={`story-npc-${e.id}`}>
        <span className="not-italic tactical-label mr-2">{e.actor}</span>{e.text}
      </aside>
    );
  }
  return (
    <div className="space-y-5" data-testid={`story-entry-${e.id}`}>
      {e.declaration && <p className="text-center text-sm text-dust italic">“{e.declaration}”</p>}
      {e.image_url && (
        <motion.img initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} viewport={{ once: true }}
          src={fileUrl(e.image_url)} alt="" className="w-full aspect-[3/2] object-cover gold-frame" data-testid={`story-image-${e.id}`} />
      )}
      <p className={`font-prose text-xl leading-[1.8] text-parchment/95 whitespace-pre-line ${first ? "drop-cap" : ""}`}>{e.text}</p>
    </div>
  );
};

export default function Storybook() {
  const { shareId } = useParams();
  const { data: b, isError } = useQuery({
    queryKey: ["story", shareId],
    queryFn: () => api.get(`/public/stories/${shareId}`).then((r) => r.data),
    refetchInterval: (q) => (q.state.data?.mode === "live" ? 20000 : false),
    retry: false,
  });

  if (isError) {
    return (
      <div className="min-h-screen grid place-items-center bg-void text-center p-8" data-testid="story-unavailable">
        <div><p className="font-heading text-3xl text-parchment">This storybook has been closed.</p>
          <p className="text-ash mt-3">The author is no longer sharing it.</p></div>
      </div>
    );
  }
  if (!b) return <div className="min-h-screen grid place-items-center bg-void tactical-label">Binding the pages…</div>;

  return (
    <div data-theme={b.theme} className="themed min-h-screen grain" data-testid="storybook-page">
      <div className="relative z-10">
        <header className="relative h-[80vh] min-h-[520px] overflow-hidden" data-testid="story-cover">
          <img src={b.cover_image} alt="" className="absolute inset-0 h-full w-full object-cover opacity-50" />
          <div className="absolute inset-0 bg-gradient-to-b from-void/30 via-void/60 to-void" />
          <div className="relative h-full mx-auto max-w-3xl px-6 flex flex-col items-center justify-end pb-16 text-center gap-6">
            {b.portrait_url && <img src={fileUrl(b.portrait_url)} alt={b.character.name} className="h-40 w-32 object-cover gold-frame" data-testid="story-portrait" />}
            <p className="tactical-label">{b.campaign_title} · {b.era}</p>
            <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl text-parchment" data-testid="story-title">{b.scenario_title}</h1>
            <p className="font-prose text-xl text-ash italic">The chronicle of {b.character.name}, {b.character.background}</p>
            <p className="text-xs font-mono text-dust">
              {b.turns} {b.turns === 1 ? "turn" : "turns"} · {b.mode === "live" ? "live, updated as they play" : `snapshot from ${new Date(b.shared_at).toLocaleDateString()}`}
            </p>
          </div>
        </header>
        <main className="mx-auto max-w-2xl px-6 pb-32 space-y-24">
          {b.chapters.map((c, ci) => (
            <section key={ci} className="space-y-10" data-testid={`story-chapter-${ci}`}>
              <div className="text-center space-y-2">
                <p className="tactical-label">{fmtDate(c.date, b.calendar)}</p>
                <h2 className="font-heading text-base md:text-lg text-gold tracking-[0.3em] uppercase">{c.title}</h2>
                <div className="mx-auto h-px w-24 bg-gold/40" />
              </div>
              {c.entries.map((e, i) => <Entry key={e.id} e={e} first={ci === 0 && i === 0} />)}
            </section>
          ))}
          <footer className="text-center text-xs text-dust flex items-center justify-center gap-2">
            <Feather size={12} className="text-gold" /> Written in play with IRGS
          </footer>
        </main>
      </div>
    </div>
  );
}
