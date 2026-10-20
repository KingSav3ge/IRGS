import { useState } from "react";
import { Link } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { toast } from "sonner";
import { BookOpen, Crown, GitBranch, Save } from "lucide-react";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { api, errMsg } from "@/lib/api";
import { ShareDialog } from "@/components/ShareDialog";

const Sel = ({ value, onChange, items, testid }) => (
  <Select value={value} onValueChange={onChange}>
    <SelectTrigger className="bg-void border-line" data-testid={testid}><SelectValue /></SelectTrigger>
    <SelectContent className="bg-tome/95 backdrop-blur-md border-line">
      {items.map((i) => <SelectItem key={i.value} value={i.value} data-testid={`${testid}-option-${i.value}`}>{i.label}</SelectItem>)}
    </SelectContent>
  </Select>
);

export const ControlPanel = ({ pt, onSettings }) => {
  const [label, setLabel] = useState("");
  const { data: prov } = useQuery({ queryKey: ["providers"], queryFn: () => api.get("/ai/providers").then((r) => r.data) });
  const { data: voices } = useQuery({ queryKey: ["voices"], queryFn: () => api.get("/voice/options").then((r) => r.data) });
  const premium = voices?.premium_active;
  const eleven = pt.voice_engine === "elevenlabs" && premium !== false;
  const voiceItems = eleven
    ? (voices?.elevenlabs || []).map((v) => ({ value: v.id, label: `${v.label} — ${v.style}` }))
    : (voices?.openai || []).map((v) => ({ value: v, label: v[0].toUpperCase() + v.slice(1) }));

  const save = async (kind) => {
    try {
      await api.post(`/playthroughs/${pt.playthrough_id}/saves`, { kind, label: label || undefined });
      setLabel("");
      toast.success(kind === "checkpoint" ? "Checkpoint sealed" : "Game saved");
    } catch (e) { toast.error(errMsg(e)); }
  };

  const setEngine = (engine) => onSettings({ voice_engine: engine, narrator_voice: engine === "elevenlabs" ? "el-bard" : "fable" });

  return (
    <aside className="space-y-7 overflow-y-auto scroll-thin pr-1" data-testid="gameplay-control-panel">
      <div className="space-y-2">
        <p className="tactical-label !text-mana">Narrator intelligence</p>
        <Sel testid="nav-ai-provider-selector" value={pt.provider} onChange={(p) => onSettings({ provider: p })}
          items={(prov?.providers || []).map((p) => ({ value: p.id, label: `${p.label} · ${p.model_label}` }))} />
      </div>
      <div className="space-y-2">
        <p className="tactical-label !text-mana">Narration voice</p>
        <div className="grid grid-cols-2 border border-line" data-testid="gameplay-voice-provider-select">
          <button onClick={() => setEngine("openai")} data-testid="voice-engine-openai"
            className={`py-2 text-xs transition-colors ${!eleven ? "bg-mana/15 text-mana" : "text-ash hover:text-parchment"}`}>Standard · free</button>
          <button onClick={() => (premium ? setEngine("elevenlabs") : toast("ElevenLabs Narration is a premium add-on", { description: "Subscribe in the Store to unlock cinematic voices." }))}
            data-testid="voice-engine-elevenlabs"
            className={`py-2 text-xs flex items-center justify-center gap-1 transition-colors ${eleven ? "bg-gold/15 text-gold" : "text-ash hover:text-parchment"}`}>
            <Crown size={11} /> ElevenLabs
          </button>
        </div>
        {voiceItems.length > 0 && <Sel testid="gameplay-voice-select" value={eleven || !(pt.narrator_voice || "").startsWith("el-") ? pt.narrator_voice : "fable"} onChange={(v) => onSettings({ narrator_voice: v })} items={voiceItems} />}
        {!premium && <Link to="/store" className="text-xs text-gold/80 hover:text-gold" data-testid="gameplay-upgrade-voice-link">Unlock ElevenLabs Narration →</Link>}
        {eleven && !voices?.elevenlabs_configured && <p className="text-[11px] text-dust">Preview mode: premium voices are simulated until ElevenLabs is connected.</p>}
      </div>
      {eleven && (
        <div className="space-y-2" data-testid="gameplay-voice-cast">
          <p className="tactical-label !text-mana">Character voices · full cast</p>
          {Object.entries(pt.voice_cast || {}).map(([name, v]) => (
            <div key={name} className="grid grid-cols-[1fr_120px] items-center gap-2">
              <span className="text-xs text-ash truncate">{name}</span>
              <Sel testid={`gameplay-cast-voice-${name.toLowerCase().replace(/[^a-z0-9]+/g, "-")}`} value={v}
                onChange={(nv) => onSettings({ voice_cast: { [name]: nv } })}
                items={(voices?.openai || []).map((o) => ({ value: o, label: o[0].toUpperCase() + o.slice(1) }))} />
            </div>
          ))}
        </div>
      )}
      <div className="space-y-2">
        <p className="tactical-label">Saves · auto-save on every turn</p>
        <Input value={label} onChange={(e) => setLabel(e.target.value)} placeholder="Label (optional)" className="bg-void border-line h-9" data-testid="gameplay-save-label-input" />
        <div className="grid grid-cols-2 gap-2">
          <Button variant="outline" className="border-line" onClick={() => save("manual")} data-testid="gameplay-quick-save-button"><Save size={13} className="mr-1" /> Save</Button>
          <Button variant="outline" className="border-gold/40 text-gold" onClick={() => save("checkpoint")} data-testid="gameplay-checkpoint-button">Checkpoint</Button>
        </div>
        <Link to={`/saves/${pt.playthrough_id}`} className="flex items-center gap-2 text-sm text-ash hover:text-arcane" data-testid="gameplay-branch-checkpoint-button"><GitBranch size={13} /> Load or branch a timeline</Link>
        <ShareDialog pid={pt.playthrough_id} triggerClassName="w-full" />
        <Link to={`/chronicle/${pt.playthrough_id}`} className="flex items-center gap-2 text-sm text-ash hover:text-gold" data-testid="gameplay-open-chronicle-link"><BookOpen size={13} /> Open the full Chronicle</Link>
      </div>
      <div className="space-y-2">
        <p className="tactical-label">Recent chronicle</p>
        <ul className="space-y-2 text-xs">
          {pt.chronicle.slice(-5).reverse().map((e) => (
            <li key={e.id} className="border-l border-gold/30 pl-3 text-ash"><span className="font-mono text-dust">#{e.at}</span> {e.declaration || e.title}</li>
          ))}
        </ul>
      </div>
    </aside>
  );
};
