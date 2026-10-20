import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { toast } from "sonner";
import { Plus, X } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";
import { PortraitPanel } from "@/components/PortraitPanel";
import { LAST_PLAY_KEY } from "@/components/AppShell";

const Section = ({ n, title, children }) => (
  <section className="space-y-4">
    <p className="tactical-label">{n} · {title}</p>
    {children}
  </section>
);

export default function CharacterCreator() {
  const { scenarioId } = useParams();
  const navigate = useNavigate();
  const { data: s } = useQuery({ queryKey: ["campaign", scenarioId], queryFn: () => api.get(`/campaigns/${scenarioId}`).then((r) => r.data) });
  const [name, setName] = useState("");
  const [bgId, setBgId] = useState(null);
  const [attrs, setAttrs] = useState({});
  const [desc, setDesc] = useState("");
  const [inv, setInv] = useState([]);
  const [newItem, setNewItem] = useState("");
  const [character, setCharacter] = useState(null);
  const [busy, setBusy] = useState(false);

  const bg = s?.character_backgrounds.find((b) => b.id === bgId);
  useEffect(() => { if (s && !bgId) { setBgId(s.character_backgrounds[0].id); setInv(s.default_inventory); } }, [s, bgId]);
  useEffect(() => { if (bg) setAttrs(bg.attributes); }, [bg]);
  const budget = useMemo(() => (bg ? Object.values(bg.attributes).reduce((a, b) => a + b, 0) + 4 : 0), [bg]);
  const spent = Object.values(attrs).reduce((a, b) => a + b, 0);

  if (!s) return <p className="p-12 tactical-label">Opening the campaign…</p>;
  if (s.locked) { navigate("/store"); return null; }

  const forge = async () => {
    setBusy(true);
    try {
      const { data } = await api.post("/characters", { scenario_id: s.id, name, background_id: bgId, attributes: attrs, inventory: inv, description: desc });
      setCharacter(data);
      toast.success(`${data.name} has been inscribed`);
    } catch (e) { toast.error(errMsg(e)); } finally { setBusy(false); }
  };

  const begin = async () => {
    setBusy(true);
    try {
      const { data } = await api.post("/playthroughs", { character_id: character.character_id });
      localStorage.setItem(LAST_PLAY_KEY, data.playthrough_id);
      navigate(`/play/${data.playthrough_id}`);
    } catch (e) { toast.error(errMsg(e)); setBusy(false); }
  };

  const locked = !!character;

  return (
    <div className="mx-auto max-w-[1400px] px-4 sm:px-8 py-12">
      <p className="tactical-label mb-3">{s.campaign_title}</p>
      <h1 className="font-heading text-4xl sm:text-5xl text-parchment mb-10">Forge your character</h1>
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
        <div className="lg:col-span-4">
          <PortraitPanel character={character} onChange={(url) => setCharacter({ ...character, portrait_url: url })} />
        </div>
        <div className="lg:col-span-5 space-y-10">
          <Section n="I" title="Name">
            <Input disabled={locked} value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Will atte Wode" className="h-12 bg-tome border-line font-prose text-xl" data-testid="character-name-input" />
          </Section>
          <Section n="II" title="Background">
            <div className="grid gap-3" data-testid="character-class-select">
              {s.character_backgrounds.map((b) => (
                <button key={b.id} disabled={locked} onClick={() => setBgId(b.id)} data-testid={`character-background-option-${b.id}`}
                  className={`text-left p-4 border transition-colors ${bgId === b.id ? "border-gold bg-gold/5" : "border-line hover:border-gold/40"}`}>
                  <p className="font-heading text-parchment">{b.label}</p>
                  <p className="text-sm text-ash mt-1">{b.description}</p>
                </button>
              ))}
            </div>
          </Section>
          <Section n="III" title={`Attributes · ${spent}/${budget} points`}>
            {Object.entries(attrs).map(([k, v]) => (
              <div key={k} className="grid grid-cols-[100px_1fr_32px] items-center gap-4">
                <span className="text-sm capitalize text-ash">{k}</span>
                <Slider disabled={locked} min={1} max={10} step={1} value={[v]} data-testid={`character-attr-slider-${k}`}
                  onValueChange={([nv]) => { if (spent - v + nv <= budget) setAttrs({ ...attrs, [k]: nv }); }} />
                <span className="font-mono font-bold text-gold text-right" data-testid={`character-attr-value-${k}`}>{v}</span>
              </div>
            ))}
          </Section>
          <Section n="IV" title="Appearance & history">
            <Textarea disabled={locked} value={desc} onChange={(e) => setDesc(e.target.value)} rows={3} placeholder="Weathered face, a scar across the brow…" className="bg-tome border-line font-prose text-lg" data-testid="character-description-input" />
          </Section>
        </div>
        <aside className="lg:col-span-3 space-y-8">
          <Section n="V" title="Inventory">
            <ul className="space-y-2" data-testid="character-inventory-list">
              {inv.map((it, i) => (
                <li key={`${it.item}-${i}`} className="flex items-center justify-between border-b border-line pb-2 text-sm">
                  <span className="text-parchment">{it.item}</span>
                  {!locked && <button onClick={() => setInv(inv.filter((_, j) => j !== i))} data-testid={`character-inventory-remove-${i}`}><X size={14} className="text-dust hover:text-crimson" /></button>}
                </li>
              ))}
            </ul>
            {!locked && inv.length < 8 && (
              <div className="flex gap-2">
                <Input value={newItem} onChange={(e) => setNewItem(e.target.value)} placeholder="Add a modest item" className="bg-tome border-line h-9" data-testid="character-inventory-input" />
                <Button size="sm" variant="outline" className="border-line" data-testid="character-inventory-add"
                  onClick={() => { if (newItem.trim()) { setInv([...inv, { item: newItem.trim(), qty: 1 }]); setNewItem(""); } }}><Plus size={14} /></Button>
              </div>
            )}
          </Section>
          {!character ? (
            <Button disabled={busy || !name.trim()} onClick={forge} className="w-full h-12 font-heading tracking-widest" data-testid="character-save-button">Inscribe character</Button>
          ) : (
            <Button disabled={busy} onClick={begin} className="w-full h-12 font-heading tracking-widest" data-testid="character-begin-button">
              {busy ? "Opening the tome…" : "Begin the chronicle"}
            </Button>
          )}
        </aside>
      </div>
    </div>
  );
}
