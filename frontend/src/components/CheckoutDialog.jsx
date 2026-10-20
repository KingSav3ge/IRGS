import { useState } from "react";
import { toast } from "sonner";
import { Loader2 } from "lucide-react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";

export const CheckoutDialog = ({ item, providers, onClose, onDone }) => {
  const [busy, setBusy] = useState(null);

  const pay = async (provider) => {
    setBusy(provider);
    try {
      await api.post("/store/checkout", { item_id: item.id, provider });
      toast.success(`${item.title} unlocked`);
      onDone();
      onClose();
    } catch (e) {
      toast.error(errMsg(e, "Checkout failed"));
    } finally {
      setBusy(null);
    }
  };

  return (
    <Dialog open={!!item} onOpenChange={(o) => !o && onClose()}>
      <DialogContent className="bg-tome border-gold/30" data-testid="store-checkout-dialog">
        <DialogHeader>
          <DialogTitle className="font-heading text-parchment">{item?.title}</DialogTitle>
          <DialogDescription className="text-ash">Choose how you would like to pay.</DialogDescription>
        </DialogHeader>
        <p className="text-xs font-mono uppercase tracking-widest text-crimson border border-crimson/40 px-3 py-2" data-testid="store-checkout-test-mode-banner">
          Test mode: payments are simulated, so no real charge is made.
        </p>
        <div className="space-y-3">
          {providers.map((p) => (
            <Button key={p.id} variant="outline" disabled={!!busy} onClick={() => pay(p.id)}
              className="w-full h-12 justify-between border-line hover:border-gold/60" data-testid={`store-checkout-${p.id}-btn`}>
              <span className="font-semibold">{p.label}</span>
              <span className="font-mono text-gold">
                {busy === p.id ? <Loader2 size={14} className="animate-spin" /> : `${p.symbol}${(item?.price * (p.rate || 1)).toFixed(2)} ${p.currency}`}
              </span>
            </Button>
          ))}
        </div>
      </DialogContent>
    </Dialog>
  );
};
