import { useEffect, useRef } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { api } from "@/lib/api";
import { useAuth } from "@/context/AuthContext";

export default function AuthCallback() {
  const location = useLocation();
  const navigate = useNavigate();
  const { signIn } = useAuth();
  const processed = useRef(false);

  useEffect(() => {
    if (processed.current) return;
    processed.current = true;
    const sessionId = new URLSearchParams(location.hash.slice(1)).get("session_id");
    window.history.replaceState(null, "", window.location.pathname);
    api
      .post("/auth/google/session", { session_id: sessionId })
      .then(({ data }) => {
        signIn(data);
        navigate("/library", { replace: true, state: { user: data.user } });
      })
      .catch(() => {
        toast.error("Google sign-in failed. Please try again.");
        navigate("/login", { replace: true });
      });
  }, [location.hash, navigate, signIn]);

  return null;
}
