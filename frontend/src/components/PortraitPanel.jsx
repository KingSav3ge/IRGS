import { useRef, useState } from "react";
import { toast } from "sonner";
import { Sparkles, Upload, UserRound } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { api, errMsg, fileUrl } from "@/lib/api";

export const PortraitPanel = ({ character, onChange }) => {
  const [prompt, setPrompt] = useState("");
  const [busy, setBusy] = useState(null);
  const fileRef = useRef(null);
  const disabled = !character || !!busy;

  const generate = async () => {
    setBusy("generate");
    try {
      const { data } = await api.post(`/characters/${character.character_id}/portrait/generate`, { prompt }, { timeout: 120000 });
      onChange(data.portrait_url);
      toast.success("Portrait painted");
    } catch (e) { toast.error(errMsg(e, "Portrait failed")); } finally { setBusy(null); }
  };

  const upload = async (file) => {
    if (!file) return;
    setBusy("upload");
    const fd = new FormData();
    fd.append("file", file);
    try {
      const { data } = await api.post(`/characters/${character.character_id}/portrait`, fd);
      onChange(data.portrait_url);
      toast.success("Portrait uploaded");
    } catch (e) { toast.error(errMsg(e, "Upload failed")); } finally { setBusy(null); }
  };

  return (
    <div className="space-y-4 lg:sticky lg:top-24">
      <div className="aspect-[3/4] bg-tome gold-frame relative overflow-hidden grid place-items-center" data-testid="character-portrait-preview">
        {character?.portrait_url ? (
          <img src={fileUrl(character.portrait_url)} alt="Portrait" className="h-full w-full object-cover" data-testid="character-portrait-image" />
        ) : (
          <UserRound size={64} className="text-line" />
        )}
        {busy === "generate" && (
          <div className="absolute inset-0 bg-void/70 grid place-items-center tactical-label animate-pulse">Painting your likeness…</div>
        )}
      </div>
      {!character && <p className="text-xs text-dust">Inscribe your character first, then paint or upload a portrait.</p>}
      <Input disabled={disabled} value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Portrait details (optional)" className="bg-tome border-line" data-testid="character-portrait-prompt-input" />
      <div className="grid grid-cols-2 gap-3">
        <Button disabled={disabled} onClick={generate} variant="outline" className="border-arcane/50 text-parchment hover:bg-arcane/10" data-testid="character-generate-portrait-button">
          <Sparkles size={14} className="mr-2 text-arcane" /> Paint (AI)
        </Button>
        <Button disabled={disabled} onClick={() => fileRef.current?.click()} variant="outline" className="border-line" data-testid="character-upload-portrait-button">
          <Upload size={14} className="mr-2" /> Upload
        </Button>
      </div>
      <input ref={fileRef} type="file" accept="image/png,image/jpeg,image/webp,image/gif" hidden onChange={(e) => upload(e.target.files?.[0])} data-testid="character-portrait-file-input" />
    </div>
  );
};
