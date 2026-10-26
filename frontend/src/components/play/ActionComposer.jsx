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

const ReviewCard = ({ review, onConfirm, onEdit, onWithdraw, busy }) => (
  <div className="border border-gold/40 bg-void/70 p-4 space-y-3" data-testid="gameplay-review-card">
    <p className="tactical-label">Review your action</p>
    {review.loading ? (
      <p className="text-sm text-ash animate-pulse" data-testid="gameplay-review-loading">Checking what this would do…</p>
    ) : review.ok ? (
      <>
        <p className="text-sm text-parchment">Read as <span className="font-mono text-gold uppercase" data-testid="gameplay-review-intent">{review.intent}</span>
          {review.big_moment ? " · a big moment (it will be painted)" : ""}.</p>
        <p className="text-xs text-ash">{review.time_note} Other characters may react afterwards. Nothing has been committed yet.</p>
      </>
    ) : (
      <p className="text-sm text-crimson" data-testid="gameplay-review-rejected">{review.reason}</p>
    )}
    <div className="flex flex-wrap gap-2">
      {review.ok && <Button size="sm" onClick={onConfirm} disabled={busy} data-testid="gameplay-review-confirm-button">Confirm and submit action</Button>}
      <Button size="sm" variant="outline" className="border-line" onClick={onEdit} data-testid="gameplay-review-edit-button">Edit</Button>
      <Button size="sm" variant="ghost" className="text-dust" onClick={onWithdraw} data-testid="gameplay-review-withdraw-button">Withdraw</Button>
    </div>
  </div>
);

export const ActionComposer = ({ onSubmit, onReview, onPass, busy, disabled }) => {
  const [text, setText] = useState("");
  const [review, setReview] = useState(null);
  const rec = useRecorder((t) => setText((prev) => (prev ? `${prev} ${t}` : t)));

  const startReview = async () => {
    if (!text.trim() || busy) return;
    setReview({ loading: true });
    setReview(await onReview(text.trim()));
  };

  const confirm = async () => {
    setReview(null);
    const ok = await onSubmit(text.trim());
    if (ok) setText("");
  };

  return (
    <div className="sticky bottom-0 z-20 border-t border-line bg-tome/90 backdrop-blur-md p-4 space-y-3" data-testid="gameplay-action-composer">
      {review && <ReviewCard review={review} busy={busy} onConfirm={confirm} onEdit={() => setReview(null)} onWithdraw={() => { setReview(null); setText(""); }} />}
      <Textarea value={text} onChange={(e) => { setText(e.target.value); setReview(null); }} rows={2} disabled={disabled || !!review}
        onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); startReview(); } }}
        placeholder={disabled ? "This playthrough is archived." : "Declare your action… (Enter to review, Shift+Enter for a new line)"}
        className="bg-void border-line font-prose text-lg resize-none focus-visible:ring-gold/50" data-testid="gameplay-action-input" />
      <div className="flex items-center gap-3">
        <Button type="button" variant="outline" onClick={rec.toggle} disabled={disabled || rec.state === "transcribing"}
          className={`border-line ${rec.state === "recording" ? "border-crimson text-crimson animate-pulse" : ""}`} data-testid="gameplay-voice-mic-button">
          {rec.state === "transcribing" ? <Loader2 size={15} className="animate-spin" /> : rec.state === "recording" ? <Square size={15} /> : <Mic size={15} />}
          <span className="ml-2 text-xs">{rec.state === "recording" ? "Stop" : rec.state === "transcribing" ? "Transcribing" : "Speak"}</span>
        </Button>
        <PassTime onPass={onPass} disabled={disabled || busy} />
        <span className="text-xs text-dust hidden xl:block">The engine validates and commits; the narrator only describes.</span>
        <Button onClick={startReview} disabled={busy || disabled || !text.trim() || !!review} className="ml-auto font-heading tracking-widest active:scale-[0.98] transition-transform" data-testid="gameplay-submit-action-button">
          {busy ? <><Loader2 size={15} className="animate-spin mr-2" /> Resolving</> : <><Send size={14} className="mr-2" /> Review action</>}
        </Button>
      </div>
    </div>
  );
};
