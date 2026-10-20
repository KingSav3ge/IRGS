import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Check, Crown } from "lucide-react";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";
import { CheckoutDialog } from "@/components/CheckoutDialog";

const ItemCard = ({ item, onBuy }) => (
  <article className="bg-tome gold-frame flex flex-col overflow-hidden hover-glow" data-testid={`store-item-card-${item.id}`}>
    <img src={item.image} alt={item.title} className="h-44 w-full object-cover" />
    <div className="p-6 flex flex-col gap-3 flex-1">
      <p className="tactical-label">{item.kind === "subscription" ? "Monthly add-on" : item.kind}</p>
      <h3 className="font-heading text-xl text-parchment flex items-center gap-2">{item.kind === "subscription" && <Crown size={16} className="text-gold" />}{item.title}</h3>
      <p className="text-sm text-ash flex-1">{item.description}</p>
      <div className="flex items-center justify-between pt-2">
        <span className="font-mono font-bold text-gold" data-testid={`store-item-price-${item.id}`}>${item.price}{item.interval ? ` / ${item.interval}` : ""}</span>
        {item.owned ? (
          <span className="text-emerald text-sm flex items-center gap-1" data-testid={`store-item-owned-${item.id}`}><Check size={14} /> {item.kind === "subscription" ? "Active" : "Owned"}</span>
        ) : (
          <Button onClick={() => onBuy(item)} data-testid={`store-buy-btn-${item.id}`}>{item.kind === "subscription" ? "Subscribe" : "Purchase"}</Button>
        )}
      </div>
    </div>
  </article>
);

export default function Store() {
  const qc = useQueryClient();
  const [buying, setBuying] = useState(null);
  const { data } = useQuery({ queryKey: ["store"], queryFn: () => api.get("/store/items").then((r) => r.data) });
  const { data: ents = [] } = useQuery({ queryKey: ["entitlements"], queryFn: () => api.get("/store/entitlements").then((r) => r.data) });
  const { data: orders = [] } = useQuery({ queryKey: ["orders"], queryFn: () => api.get("/store/orders").then((r) => r.data) });

  const refresh = () => ["store", "entitlements", "orders", "campaigns", "voices"].forEach((k) => qc.invalidateQueries({ queryKey: [k] }));
  const cancel = async (id) => {
    try { await api.post(`/store/subscriptions/${id}/cancel`); refresh(); toast.success("Subscription cancelled"); } catch (e) { toast.error(errMsg(e)); }
  };

  return (
    <div className="mx-auto max-w-[1600px] px-4 sm:px-8 py-12 space-y-14">
      <div className="max-w-3xl">
        <p className="tactical-label mb-3">The Merchant's Bazaar</p>
        <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl text-parchment">Campaigns, voices & keepsakes</h1>
        <p className="font-prose text-xl text-ash mt-4">Standard narration is always free. Premium campaigns and ElevenLabs Narration expand the tome.</p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {(data?.items || []).map((i) => <ItemCard key={i.id} item={i} onBuy={setBuying} />)}
      </div>
      <div className="grid md:grid-cols-2 gap-10">
        <section className="space-y-4">
          <h2 className="font-heading text-base md:text-lg text-parchment">Your entitlements</h2>
          <ul className="space-y-2" data-testid="store-entitlements-list">
            {ents.length === 0 && <li className="text-sm text-dust">Nothing yet.</li>}
            {ents.map((e) => (
              <li key={e.item_id} className="flex items-center gap-3 border-b border-line pb-2 text-sm" data-testid={`store-entitlement-${e.item_id}`}>
                <span className="text-parchment flex-1">{e.title}</span>
                <span className={e.active ? "text-emerald" : "text-dust"}>{e.active ? (e.expires_at ? `renews ${new Date(e.expires_at).toLocaleDateString()}` : "owned") : "expired"}</span>
                {e.kind === "subscription" && e.active && (
                  <button onClick={() => cancel(e.item_id)} className="text-xs text-crimson/80 hover:text-crimson" data-testid={`store-cancel-sub-${e.item_id}`}>Cancel</button>
                )}
              </li>
            ))}
          </ul>
        </section>
        <section className="space-y-4">
          <h2 className="font-heading text-base md:text-lg text-parchment">Order history</h2>
          <ul className="space-y-2 text-sm" data-testid="store-orders-list">
            {orders.length === 0 && <li className="text-dust">No orders yet.</li>}
            {orders.map((o) => (
              <li key={o.order_id} className="flex gap-3 border-b border-line pb-2">
                <span className="flex-1 text-parchment">{o.title}</span>
                <span className="font-mono text-ash">{o.amount} {o.currency}</span>
                <span className="text-dust capitalize">{o.provider}{o.mocked ? " · test" : ""}</span>
              </li>
            ))}
          </ul>
        </section>
      </div>
      <CheckoutDialog item={buying} providers={data?.providers || []} onClose={() => setBuying(null)} onDone={refresh} />
    </div>
  );
}
