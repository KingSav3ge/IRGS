import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { toast } from "sonner";
import { ArrowLeft, AudioLines, GitBranch, Hexagon, Image as ImageIcon, Users } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";
import { useAuth } from "@/context/AuthContext";

const WORLDS = [
  { theme: "manuscript", title: "The Lancastrian Invasion", era: "1415 · Late Medieval", line: "Henry V's fleet waits at Southampton. Nothing has crossed the Channel yet.",
    img: "https://images.pexels.com/photos/2873895/pexels-photo-2873895.jpeg?auto=compress&cs=tinysrgb&h=1080&w=1920" },
  { theme: "tablet", title: "The Grain Fleet of Ostia", era: "58 BCE · Roman Republic", line: "Grain ships ride at anchor while the mob and the Senate weigh their next move.",
    img: "https://images.unsplash.com/photo-1724925742136-f620924e50b1?crop=entropy&cs=srgb&fm=jpg&q=85&w=1920" },
  { theme: "grimoire", title: "Shadows over Eldoria", era: "The Age of Ash", line: "The old king is three nights dead. The Riven Crown is still unclaimed.",
    img: "https://images.unsplash.com/photo-1514539079130-25950c84af65?crop=entropy&cs=srgb&fm=jpg&q=85&w=1920" },
  { theme: "pda", title: "Drift at Meridian Station", era: "2189 · Outer System", line: "The relay went dark three days ago. Air, water and loyalty are rationed.",
    img: "https://images.unsplash.com/photo-1774382137454-60281271e0a5?crop=entropy&cs=srgb&fm=jpg&q=85&w=1920" },
];

const FEATURES = [
  { icon: Users, title: "Living characters", text: "People remember, move, plot and gossip between your turns." },
  { icon: AudioLines, title: "Speak and listen", text: "Say your action out loud, and hear the story read back with a full cast." },
  { icon: ImageIcon, title: "Illustrated chronicle", text: "Big moments get painted, and any story can be shared as a storybook." },
  { icon: GitBranch, title: "Branch any moment", text: "Auto-saves, checkpoints and alternate timelines from any point." },
];

const googleLogin = () => {
  // REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
  const redirectUrl = window.location.origin + "/library";
  window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
};

const Brand = () => (
  <div className="flex items-center gap-3">
    <Hexagon className="text-gold" size={22} />
    <span className="font-heading tracking-[0.3em] text-gold text-sm">IRGS</span>
  </div>
);

const Showcase = ({ index }) => {
  const w = WORLDS[index];
  return (
    <div className="absolute inset-0 overflow-hidden" data-testid="auth-showcase">
      <AnimatePresence>
        <motion.img key={w.img} src={w.img} alt=""
          initial={{ opacity: 0, scale: 1.15 }} animate={{ opacity: 0.55, scale: 1.02 }} exit={{ opacity: 0 }}
          transition={{ opacity: { duration: 1.6 }, scale: { duration: 9, ease: "linear" } }}
          className="absolute inset-0 h-full w-full object-cover" />
      </AnimatePresence>
      <div className="absolute inset-0 bg-gradient-to-r from-void via-void/60 to-void/30" />
      <div className="absolute inset-0 bg-gradient-to-t from-void via-transparent to-void/40" />
    </div>
  );
};

const WorldTitle = ({ index, onPick }) => {
  const w = WORLDS[index];
  return (
    <div className="space-y-6 max-w-xl">
      <p className="tactical-label">Immersive roleplaying simulation</p>
      <AnimatePresence mode="wait">
        <motion.div key={w.title} data-theme={w.theme} className="!bg-transparent space-y-4"
          initial={{ opacity: 0, y: 24, filter: "blur(6px)" }} animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
          exit={{ opacity: 0, y: -16, filter: "blur(6px)" }} transition={{ duration: 0.7 }}>
          <p className="font-mono text-xs uppercase tracking-[0.3em] text-gold" data-testid="auth-world-era">{w.era}</p>
          <h1 className="font-heading text-4xl sm:text-5xl lg:text-6xl leading-[1.05] text-[#EDE3D1]" data-testid="auth-world-title">{w.title}</h1>
          <p className="font-prose text-xl text-[#EDE3D1]/80 italic">{w.line}</p>
        </motion.div>
      </AnimatePresence>
      <div className="flex gap-2 pt-2" data-testid="auth-world-dots">
        {WORLDS.map((x, i) => (
          <button key={x.title} onClick={() => onPick(i)} aria-label={x.title} data-testid={`auth-world-dot-${i}`}
            className={`h-1 transition-[width,background-color] duration-500 ${i === index ? "w-10 bg-gold" : "w-4 bg-line hover:bg-ash"}`} />
        ))}
      </div>
    </div>
  );
};

const AuthCard = () => {
  const { signIn } = useAuth();
  const navigate = useNavigate();
  const [mode, setMode] = useState("choose");
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [busy, setBusy] = useState(false);
  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    try {
      const { data } = await api.post(mode === "login" ? "/auth/login" : "/auth/register", form);
      signIn(data);
      navigate("/library");
    } catch (err) {
      toast.error(errMsg(err, "Could not sign in"));
    } finally {
      setBusy(false);
    }
  };

  const glass = "w-full max-w-md rounded-sm p-8 sm:p-10 bg-[#1C1714]/55 backdrop-blur-2xl border border-white/10 shadow-[0_30px_80px_-30px_rgba(0,0,0,0.9)]";

  if (mode === "choose") {
    return (
      <motion.div key="choose" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 }}
        className={`${glass} space-y-8`} data-testid="auth-choice-card">
        <Brand />
        <h2 className="font-heading text-3xl sm:text-4xl text-parchment leading-tight" data-testid="auth-choice-question">
          Do you have a journey to return to? Or are you setting about your first?
        </h2>
        <div className="grid grid-cols-2 gap-4">
          <Button onClick={() => setMode("login")} className="h-12 font-heading tracking-widest active:scale-[0.98] transition-transform" data-testid="auth-choose-signin-button">Sign in</Button>
          <Button variant="outline" onClick={() => setMode("register")} className="h-12 font-heading tracking-widest bg-transparent border-white/20 hover:border-gold/60 hover:bg-white/5 active:scale-[0.98] transition-transform" data-testid="auth-choose-signup-button">Sign up</Button>
        </div>
      </motion.div>
    );
  }

  return (
    <motion.form key={mode} onSubmit={submit} initial={{ opacity: 0, x: 24 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.4 }}
      className={`${glass} space-y-5`} data-testid="auth-form">
      <button type="button" onClick={() => setMode("choose")} className="flex items-center gap-1 text-xs text-ash hover:text-gold transition-colors" data-testid="auth-back-button">
        <ArrowLeft size={13} /> Back
      </button>
      <Brand />
      <h2 className="font-heading text-4xl text-parchment" data-testid="auth-form-title">{mode === "login" ? "Welcome back" : "Create your account"}</h2>
      <Button type="button" variant="outline" onClick={googleLogin} className="w-full h-11 bg-white/5 border-white/15 hover:border-gold/60 hover:bg-white/10" data-testid="auth-google-login-button">
        Continue with Google
      </Button>
      <div className="flex items-center gap-3 tactical-label !text-dust">
        <span className="h-px flex-1 bg-white/10" /> or {mode === "login" ? "with your account" : "with email"} <span className="h-px flex-1 bg-white/10" />
      </div>
      {mode === "register" && <Input placeholder="Name" value={form.name} onChange={set("name")} className="h-11 bg-void/60 border-white/10" data-testid="auth-name-input" />}
      <Input type={mode === "login" ? "text" : "email"} required autoComplete="username" placeholder={mode === "login" ? "Email or username" : "Email"}
        value={form.email} onChange={set("email")} className="h-11 bg-void/60 border-white/10" data-testid="auth-email-input" />
      <Input type="password" required minLength={mode === "register" ? 6 : undefined} placeholder="Password" value={form.password} onChange={set("password")}
        className="h-11 bg-void/60 border-white/10" data-testid="auth-password-input" />
      <Button type="submit" disabled={busy} className="w-full h-11 font-heading tracking-widest active:scale-[0.98] transition-transform" data-testid="auth-submit-button">
        {busy ? "Please wait…" : mode === "login" ? "Sign in" : "Create account"}
      </Button>
      <button type="button" onClick={() => setMode(mode === "login" ? "register" : "login")} className="text-sm text-ash hover:text-gold transition-colors" data-testid="auth-switch-mode-button">
        {mode === "login" ? "New here? Create an account" : "Already have an account? Sign in"}
      </button>
    </motion.form>
  );
};

export default function AuthPage() {
  const { user } = useAuth();
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const t = setInterval(() => setIndex((i) => (i + 1) % WORLDS.length), 7000);
    return () => clearInterval(t);
  }, [index]);

  if (user) return <Navigate to="/library" replace />;

  return (
    <div className="bg-void grain">
      <section className="relative min-h-screen flex items-center" data-testid="auth-hero">
        <Showcase index={index} />
        <div className="relative z-10 w-full mx-auto max-w-[1500px] px-6 sm:px-12 py-16 grid lg:grid-cols-12 gap-12 items-center">
          <div className="lg:col-span-7"><WorldTitle index={index} onPick={setIndex} /></div>
          <div className="lg:col-span-5 flex lg:justify-end"><AuthCard /></div>
        </div>
        <p className="absolute bottom-6 left-1/2 -translate-x-1/2 z-10 tactical-label !text-dust animate-pulse">Scroll · what IRGS does</p>
      </section>
      <section className="relative z-10 border-t border-line" data-testid="auth-features-strip">
        <div className="mx-auto max-w-[1500px] px-6 sm:px-12 py-20 grid sm:grid-cols-2 lg:grid-cols-4 gap-10">
          {FEATURES.map((f, i) => (
            <motion.div key={f.title} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}
              transition={{ delay: i * 0.1 }} className="space-y-3" data-testid={`auth-feature-${i}`}>
              <f.icon size={22} className="text-gold" />
              <h3 className="font-heading text-xl text-parchment">{f.title}</h3>
              <p className="text-sm text-ash leading-relaxed">{f.text}</p>
            </motion.div>
          ))}
        </div>
        <p className="text-center pb-12 font-prose italic text-ash text-lg">“Nothing beyond this moment has been decided. The world unfolds only through what you choose.”</p>
      </section>
    </div>
  );
}
