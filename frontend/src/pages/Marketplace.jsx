import { Store as StoreIcon, Upload, Users } from "lucide-react";

const SLOTS = [
  { icon: Users, title: "Community campaigns", text: "Campaigns made by other players in the Campaign Workshop, once they pass publication review." },
  { icon: Upload, title: "Publish your own", text: "Package a Workshop project, set its rights and provenance, and submit it for approval." },
  { icon: StoreIcon, title: "Creator credits", text: "Authoring credits and rewards for published work, kept separate from the official Store." },
];

export default function Marketplace() {
  return (
    <div className="mx-auto max-w-[1400px] px-4 sm:px-8 py-12 space-y-12" data-testid="marketplace-page">
      <div className="max-w-3xl">
        <p className="tactical-label mb-3">Marketplace · Stage Three</p>
        <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl text-parchment">Coming later</h1>
        <p className="font-prose text-xl text-ash mt-4">
          The Marketplace will host community-made campaigns, separate from the official Store. It opens once the Campaign Workshop and publication review are ready.
        </p>
      </div>
      <div className="grid md:grid-cols-3 gap-6">
        {SLOTS.map((s, i) => (
          <div key={s.title} className="border border-dashed border-line p-8 space-y-3 opacity-80" data-testid={`marketplace-slot-${i}`}>
            <s.icon size={22} className="text-gold" />
            <h3 className="font-heading text-xl text-parchment">{s.title}</h3>
            <p className="text-sm text-ash">{s.text}</p>
            <span className="inline-block text-[10px] font-mono uppercase tracking-widest text-dust border border-line px-2 py-0.5">Placeholder</span>
          </div>
        ))}
      </div>
    </div>
  );
}
