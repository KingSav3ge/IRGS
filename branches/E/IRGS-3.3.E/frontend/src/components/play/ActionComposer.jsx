import { useState } from "react";
import { Hourglass, Loader2, Mic, Send, Square } from "lucide-react";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { useRecorder } from "@/hooks/useRecorder";

const SPANS = [["hours", "A few hours"], ["day", "A day"], ["week", "A week"]];

const PassTime = ({ onPass, disabled }) => (
  <DropdownMenu>
    <DropdownMenuTrigger asChild>
      <Button type="button" variant="outline" disabled={disabled} className="border-line" data-testid="gameplay-pass-time-button">
        <Hourglass size={15} /><span className="ml-2 text-xs">Let time pass</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent className="bg-tome/95 backdrop-blur-md border-line">
      {SPANS.map(([k, label]) => (
        <DropdownMenuItem key={k} onClick={() => onPass(k)} data-testid={`gameplay-pass-time-${k}`}>{label}</DropdownMenuItem>
      ))}
    </DropdownMenuContent>
  </DropdownMenu>
);

export const ActionComposer = ({ onSubmit, onPass, busy, disabled }) => {
  const [text, setText] = useState("");
  const rec = useRecorder((t) => setText((prev) => (prev ? `${prev} ${t}` : t)));

  const submit = async () => {
    if (!text.trim() || busy) return;
    const ok = await onSubmit(text.trim());
    if (ok) setText("");
  };

  return (
    <div className="sticky bottom-0 z-20 border-t border-line bg-tome/90 backdrop-blur-md p-4 space-y-3" data-testid="gameplay-action-composer">
      <Textarea value={text} onChange={(e) => setText(e.target.value)} rows={2} disabled={disabled}
        onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submit(); } }}
        placeholder={disabled ? "This playthrough is archived." : "Declare your action… (Enter to commit, Shift+Enter for a new line)"}
        className="bg-void border-line font-prose text-lg resize-none focus-visible:ring-gold/50" data-testid="gameplay-action-input" />
      <div className="flex items-center gap-3">
        <Button type="button" variant="outline" onClick={rec.toggle} disabled={disabled || rec.state === "transcribing"}
          className={`border-line ${rec.state === "recording" ? "border-crimson text-crimson animate-pulse" : ""}`} data-testid="gameplay-voice-mic-button">
          {rec.state === "transcribing" ? <Loader2 size={15} className="animate-spin" /> : rec.state === "recording" ? <Square size={15} /> : <Mic size={15} />}
          <span className="ml-2 text-xs">{rec.state === "recording" ? "Stop" : rec.state === "transcribing" ? "Transcribing" : "Speak"}</span>
        </Button>
        <PassTime onPass={onPass} disabled={disabled || busy} />
        <span className="text-xs text-dust hidden xl:block">The engine validates and commits; the narrator only describes.</span>
        <Button onClick={submit} disabled={busy || disabled || !text.trim()} className="ml-auto font-heading tracking-widest active:scale-[0.98] transition-transform" data-testid="gameplay-submit-action-button">
          {busy ? <><Loader2 size={15} className="animate-spin mr-2" /> Resolving</> : <><Send size={14} className="mr-2" /> Commit</>}
        </Button>
      </div>
    </div>
  );
};
