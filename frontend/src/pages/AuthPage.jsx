import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { toast } from "sonner";
import { Feather } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { api, errMsg } from "@/lib/api";
import { useAuth } from "@/context/AuthContext";

const COVERS = [
  "https://images.pexels.com/photos/2873895/pexels-photo-2873895.jpeg?auto=compress&cs=tinysrgb&h=650&w=940",
  "https://images.unsplash.com/photo-1774382137454-60281271e0a5?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
  "https://images.unsplash.com/photo-1724925742136-f620924e50b1?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
  "https://images.unsplash.com/photo-1514539079130-25950c84af65?crop=entropy&cs=srgb&fm=jpg&q=85&w=940",
];

const googleLogin = () => {
  // REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
  const redirectUrl = window.location.origin + "/library";
  window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
};

export default function AuthPage() {
  const { user, signIn } = useAuth();
  const navigate = useNavigate();
  const [mode, setMode] = useState("login");
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [busy, setBusy] = useState(false);

  if (user) return <Navigate to="/library" replace />;

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

  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value });

  return (
    <div className="min-h-screen grid lg:grid-cols-12 bg-void grain">
      <div className="relative hidden lg:block lg:col-span-7 overflow-hidden">
        <div className="absolute inset-0 grid grid-cols-2 grid-rows-2" data-testid="auth-hero-mosaic">
          {COVERS.map((src, i) => (
            <motion.img key={src} src={src} alt="" initial={{ opacity: 0, scale: 1.05 }} animate={{ opacity: 0.6, scale: 1 }}
              transition={{ delay: i * 0.15, duration: 0.8 }} className="h-full w-full object-cover" />
          ))}
        </div>
        <div className="absolute inset-0 bg-gradient-to-r from-void/20 via-void/40 to-void" />
        <div className="absolute bottom-16 left-14 max-w-lg">
          <p className="tactical-label mb-4">Immersive Roleplaying Simulation · history, fantasy, science fiction</p>
          <blockquote className="font-prose italic text-3xl leading-snug text-parchment">
            “Nothing beyond this moment has been decided. The world unfolds only through what you choose.”
          </blockquote>
        </div>
      </div>
      <div className="lg:col-span-5 flex items-center justify-center p-6 sm:p-12 relative z-10">
        <motion.form
          onSubmit={submit}
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-md bg-tome gold-frame rounded-sm p-8 sm:p-10 space-y-6"
          data-testid="auth-form"
        >
          <div className="flex items-center gap-3">
            <Feather className="text-gold" size={22} />
            <span className="font-heading tracking-[0.3em] text-gold text-sm">IRGS</span>
          </div>
          <h1 className="font-heading text-4xl sm:text-5xl text-parchment">
            {mode === "login" ? "Welcome back" : "Create your account"}
          </h1>
          <Button type="button" variant="outline" onClick={googleLogin}
            className="w-full h-11 border-line bg-surface hover:border-gold/60 hover:bg-surface"
            data-testid="auth-google-login-button">
            Continue with Google
          </Button>
          <div className="flex items-center gap-3 text-dust text-xs tactical-label !text-dust">
            <span className="h-px flex-1 bg-line" /> or with email <span className="h-px flex-1 bg-line" />
          </div>
          {mode === "register" && (
            <Input placeholder="Name" value={form.name} onChange={set("name")} className="h-11 bg-void border-line" data-testid="auth-name-input" />
          )}
          <Input type="email" required placeholder="Email" value={form.email} onChange={set("email")} className="h-11 bg-void border-line" data-testid="auth-email-input" />
          <Input type="password" required minLength={6} placeholder="Password" value={form.password} onChange={set("password")} className="h-11 bg-void border-line" data-testid="auth-password-input" />
          <Button type="submit" disabled={busy} className="w-full h-11 font-heading tracking-widest active:scale-[0.98] transition-transform" data-testid="auth-submit-button">
            {busy ? "Please wait…" : mode === "login" ? "Sign in" : "Create account"}
          </Button>
          <button type="button" onClick={() => setMode(mode === "login" ? "register" : "login")}
            className="text-sm text-ash hover:text-gold transition-colors" data-testid="auth-switch-mode-button">
            {mode === "login" ? "New here? Create an account" : "Already have an account? Sign in"}
          </button>
        </motion.form>
      </div>
    </div>
  );
}
