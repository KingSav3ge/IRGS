import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { toast } from "sonner";
import { Plus, X, ArrowLeft, ArrowRight } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";
import { PortraitPanel } from "@/components/PortraitPanel";
import { LAST_PLAY_KEY } from "@/components/AppShell";
import { CreationModePicker, MODES } from "@/components/CreationModePicker";

const Section = ({ n, title, children }) => (
  <section className="space-y-4">
    <p className="tactical-label">{n} · {title}</p>
    {children}
  </section>
);

const GUIDE = {
  name: "This is what the people of the world will call you. They may shorten it or mishear it.",
  background: "Your background sets your starting standing, how strangers read you and your base attributes.",
  attributes: "You have a few spare points. Higher values make related actions more likely to succeed, but they never guarantee it.",
  appearance: "A short description helps the narrator and the portrait painter picture you.",
  testimony: "This is your own account of your past. The world hears it as your claim, not as proven fact.",
  inventory: "Keep it modest. What you carry is what you can use from the first scene.",
};

export default function CharacterCreator() {
  const { scenarioId } = useParams();
  const navigate = useNavigate();
  const { data: s } = useQuery({ queryKey: ["campaign", scenarioId], queryFn: () => api.get(`/campaigns/${scenarioId}`).then((r) => r.data) });
  const [mode, setMode] = useState(null);
  const [step, setStep] = useState(0);
  const [name, setName] = useState("");
  const [bgId, setBgId] = useState(null);
  const [attrs, setAttrs] = useState({});
  const [desc, setDesc] = useState("");
  const [testimony, setTestimony] = useState({ origin: "", family: "", career: "" });
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
    const quick = mode === "quick";
    try {
      const { data } = await api.post("/characters", {
        scenario_id: s.id, name, background_id: bgId, creation_mode: mode,
        attributes: quick ? bg.attributes : attrs, inventory: quick ? s.default_inventory : inv,
        description: quick ? "" : desc, testimony: quick ? {} : testimony,
      });
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

  const nameField = (
    <Input disabled={locked} value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Will atte Wode" className="h-12 bg-tome border-line font-prose text-xl" data-testid="character-name-input" />
  );
  const backgroundField = (
    <div className="grid gap-3" data-testid="character-class-select">
      {s.character_backgrounds.map((b) => (
        <button key={b.id} disabled={locked} onClick={() => setBgId(b.id)} data-testid={`character-background-option-${b.id}`}
          className={`text-left p-4 border transition-colors ${bgId === b.id ? "border-gold bg-gold/5" : "border-line hover:border-gold/40"}`}>
          <p className="font-heading text-parchment">{b.label}</p>
          <p className="text-sm text-ash mt-1">{b.description}</p>
          {mode === "quick" && (
            <p className="text-[11px] font-mono uppercase text-dust mt-2">
              {Object.entries(b.attributes).map(([k, v]) => `${k} ${v}`).join(" · ")}
            </p>
          )}
        </button>
      ))}
    </div>
  );
  const attributesField = Object.entries(attrs).map(([k, v]) => (
    <div key={k} className="grid grid-cols-[100px_1fr_32px] items-center gap-4">
      <span className="text-sm capitalize text-ash">{k}</span>
      <Slider disabled={locked} min={1} max={10} step={1} value={[v]} data-testid={`character-attr-slider-${k}`}
        onValueChange={([nv]) => { if (spent - v + nv <= budget) setAttrs({ ...attrs, [k]: nv }); }} />
      <span className="font-mono font-bold text-gold text-right" data-testid={`character-attr-value-${k}`}>{v}</span>
    </div>
  ));
  const appearanceField = (
    <Textarea disabled={locked} value={desc} onChange={(e) => setDesc(e.target.value)} rows={3} placeholder="Weathered face, a scar across the brow…" className="bg-tome border-line font-prose text-lg" data-testid="character-description-input" />
  );
  const testimonyField = (
    <>
      <p className="text-xs text-dust -mt-2">This is your character's own story of where they come from. The world treats it as their account, not proven fact, and it grants no skills or rank.</p>
      {[["origin", "Identity & origin", "Born in Kent, son of a fletcher…"], ["family", "Family", "Two sisters; a father lost at sea…"], ["career", "Career intent", "Hopes to earn a place in a lord's household…"]].map(([k, label, ph]) => (
        <div key={k} className="space-y-1">
          <span className="text-xs text-ash">{label}</span>
          <Textarea disabled={locked} rows={2} value={testimony[k]} placeholder={ph}
            onChange={(e) => setTestimony({ ...testimony, [k]: e.target.value })}
            className="bg-tome border-line font-prose text-base" data-testid={`character-testimony-${k}`} />
        </div>
      ))}
    </>
  );
  const inventoryField = (
    <>
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
    </>
  );

  const actionButton = !character ? (
    <Button disabled={busy || !name.trim()} onClick={forge} className="w-full h-12 font-heading tracking-widest" data-testid="character-save-button">Inscribe character</Button>
  ) : (
    <Button disabled={busy} onClick={begin} className="w-full h-12 font-heading tracking-widest" data-testid="character-begin-button">
      {busy ? "Opening the tome…" : "Begin the chronicle"}
    </Button>
  );

  const steps = [
    ["name", "Name", nameField], ["background", "Background", backgroundField],
    ["attributes", `Attributes · ${spent}/${budget} points`, attributesField], ["appearance", "Appearance & history", appearanceField],
    ["testimony", "Your own account (optional)", testimonyField], ["inventory", "Inventory", inventoryField],
  ];
  const ROMAN = ["I", "II", "III", "IV", "V", "VI"];
  const modeLabel = MODES.find((m) => m.id === mode)?.label;

  const header = (
    <div className="flex flex-wrap items-end gap-4 mb-10">
      <h1 className="font-heading text-4xl sm:text-5xl text-parchment">Forge your character</h1>
      {mode && (
        <span className="tactical-label pb-2" data-testid="creation-mode-current">
          {modeLabel} creation
          {!locked && <button onClick={() => { setMode(null); setStep(0); }} className="ml-3 text-gold normal-case" data-testid="creation-mode-change">Change</button>}
        </span>
      )}
    </div>
  );

  const body = () => {
    if (!mode) return <CreationModePicker onPick={setMode} />;
    if (mode === "quick") return (
      <div className="space-y-10" data-testid="creation-quick">
        <Section n="I" title="Name">{nameField}</Section>
        <Section n="II" title="Preset">{backgroundField}</Section>
        <p className="text-xs text-dust">The preset's attributes and the campaign's standard gear are used as they are. You can still add a portrait.</p>
        {actionButton}
      </div>
    );
    if (mode === "guided") {
      const [key, title, field] = steps[step];
      const last = step === steps.length - 1;
      return (
        <div className="space-y-8" data-testid="creation-guided">
          <div className="flex gap-1" data-testid="guided-progress">
            {steps.map((_, i) => <span key={i} className={`h-1 flex-1 transition-colors ${i <= step ? "bg-gold" : "bg-line"}`} />)}
          </div>
          <p className="tactical-label" data-testid="guided-step-label">Step {step + 1} of {steps.length}</p>
          <Section n={ROMAN[step]} title={title}>
            <p className="text-sm text-ash italic -mt-1" data-testid="guided-step-hint">{GUIDE[key]}</p>
            {field}
          </Section>
          <div className="flex gap-3">
            <Button variant="outline" className="border-line" disabled={step === 0 || locked} onClick={() => setStep(step - 1)} data-testid="guided-back-button"><ArrowLeft size={14} className="mr-2" />Back</Button>
            {!last && <Button disabled={key === "name" && !name.trim()} onClick={() => setStep(step + 1)} data-testid="guided-next-button">Next<ArrowRight size={14} className="ml-2" /></Button>}
          </div>
          {last && actionButton}
        </div>
      );
    }
    return (
      <div className="grid grid-cols-1 lg:grid-cols-8 gap-10" data-testid="creation-detailed">
        <div className="lg:col-span-5 space-y-10">
          {steps.slice(0, 5).map(([k, title, field], i) => <Section key={k} n={ROMAN[i]} title={title}>{field}</Section>)}
        </div>
        <aside className="lg:col-span-3 space-y-8">
          <Section n="VI" title="Inventory">{inventoryField}</Section>
          {actionButton}
        </aside>
      </div>
    );
  };

  return (
    <div data-theme={s.theme} className="themed" data-testid="character-theme-scope">
      <div className="relative z-10 mx-auto max-w-[1400px] px-4 sm:px-8 py-12">
        <p className="tactical-label mb-3">{s.campaign_title}</p>
        {header}
        {!mode ? body() : (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
            <div className="lg:col-span-4">
              <PortraitPanel character={character} onChange={(url) => setCharacter({ ...character, portrait_url: url })} />
            </div>
            <div className="lg:col-span-8">{body()}</div>
          </div>
        )}
      </div>
    </div>
  );
}
