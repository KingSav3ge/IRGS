import { useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Download, Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { usePaint, usePlaythrough } from "@/pages/Play";
import { SceneImage } from "@/components/play/NarrativeEntry";
import { fmtDate } from "@/lib/api";
import { ShareDialog } from "@/components/ShareDialog";
import { HistoryReference } from "@/components/HistoryReference";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";
import { EntityHistory } from "@/components/chronicle/EntityHistory";
import { NotesPanel } from "@/components/chronicle/NotesPanel";
import { DevelopmentPanel } from "@/components/chronicle/DevelopmentPanel";

const TAGS = ["all", "big", "npc", "move", "speak", "observe", "interact", "combat", "rest", "other"];

export default function Chronicle() {
  const { pid } = useParams();
  const { data: pt } = usePlaythrough(pid);
  const paint = usePaint(pid);
  const { data: entities = [] } = useQuery({ queryKey: ["entities", pid], queryFn: () => api.get(`/playthroughs/${pid}/entities`).then((r) => r.data) });
  const [q, setQ] = useState("");
  const [tag, setTag] = useState("all");

  const entries = useMemo(() => (pt?.chronicle || []).filter((e) =>
    (tag === "all" || (tag === "big" ? e.big_moment : e.intent === tag)) &&
    `${e.text} ${e.declaration || ""}`.toLowerCase().includes(q.toLowerCase())), [pt, q, tag]);

  if (!pt) return <p className="p-12 tactical-label">Opening the Chronicle…</p>;

  const exportJson = () => {
    const blob = new Blob([JSON.stringify(pt.chronicle, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `chronicle-${pid}.json`;
    a.click();
  };

  return (
    <div data-theme={pt.theme} className="themed" data-testid="chronicle-theme-scope">
    <div className="relative z-10 mx-auto max-w-5xl px-4 sm:px-8 py-12 space-y-10">
      <div className="flex flex-wrap items-end gap-4">
        <div>
          <p className="tactical-label mb-3">The Chronicle</p>
          <h1 className="font-heading text-4xl sm:text-5xl text-parchment">{pt.title}</h1>
        </div>
        <ShareDialog pid={pid} triggerClassName="ml-auto" />
        <Button variant="outline" className="border-line" onClick={exportJson} data-testid="chronicle-export-button"><Download size={14} className="mr-2" /> Export</Button>
      </div>
      <Tabs defaultValue="timeline" className="space-y-8">
        <TabsList className="bg-tome border border-line flex-wrap h-auto" data-testid="chronicle-tabs">
          <TabsTrigger value="timeline" data-testid="chronicle-tab-timeline">Timeline</TabsTrigger>
          <TabsTrigger value="entities" data-testid="chronicle-tab-entities">People & places</TabsTrigger>
          <TabsTrigger value="notes" data-testid="chronicle-tab-notes">Notes & documents</TabsTrigger>
          <TabsTrigger value="development" data-testid="chronicle-tab-development">Development & goals</TabsTrigger>
        </TabsList>
        <TabsContent value="timeline" className="space-y-10">
      <div className="flex flex-wrap gap-3 items-center">
        <div className="relative w-full sm:w-72">
          <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-dust" />
          <Input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search the record" className="pl-9 bg-tome border-line" data-testid="chronicle-search-input" />
        </div>
        {TAGS.map((t) => (
          <button key={t} onClick={() => setTag(t)} data-testid={`chronicle-filter-tag-${t}`}
            className={`text-[11px] font-mono uppercase tracking-widest px-3 py-1 border transition-colors ${tag === t ? "border-gold text-gold" : "border-line text-dust hover:text-ash"}`}>
            {t === "big" ? "big moments" : t === "npc" ? "others act" : t}
          </button>
        ))}
      </div>
      <ol className="relative border-l border-gold/25 ml-3 space-y-12" data-testid="chronicle-entries">
        {entries.map((e) => (
          <li key={e.id} className="pl-8 relative" data-testid={`chronicle-entry-${e.id}`}>
            <span className={`absolute -left-[7px] top-1 h-3 w-3 rotate-45 ${e.big_moment ? "bg-gold" : "bg-line"}`} />
            <p className="font-mono text-xs text-dust mb-2">{[`#${e.at}`, [fmtDate(e.campaign_date, pt.view.campaign_time.calendar), e.campaign_time].filter(Boolean).join(" "), e.intent || e.kind.replace("_", " ")].filter(Boolean).join(" · ")}</p>
            {e.declaration && <p className="text-sm text-ash italic mb-3">“{e.declaration}”</p>}
            <div className="grid gap-6 md:grid-cols-[1fr_260px]">
              <p className="font-prose text-lg leading-relaxed text-parchment/95 whitespace-pre-line">{e.text}</p>
              {e.kind !== "npc_action" && <SceneImage entry={e} onPaint={paint} compact />}
            </div>
          </li>
        ))}
        {entries.length === 0 && <li className="pl-8 text-dust text-sm" data-testid="chronicle-empty">No entries match.</li>}
      </ol>
      <HistoryReference pid={pid} />
        </TabsContent>
        <TabsContent value="entities"><EntityHistory pid={pid} entities={entities} /></TabsContent>
        <TabsContent value="notes"><NotesPanel pid={pid} entities={entities} /></TabsContent>
        <TabsContent value="development"><DevelopmentPanel pid={pid} /></TabsContent>
      </Tabs>
      <Link to={`/play/${pid}`} className="text-sm text-gold" data-testid="chronicle-back-to-play">← Return to play</Link>
    </div>
    </div>
  );
}
