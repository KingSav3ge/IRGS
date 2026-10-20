import "@/App.css";
import { BrowserRouter, Navigate, Route, Routes, useLocation } from "react-router-dom";
import { Toaster } from "sonner";
import { AuthProvider, ProtectedRoute } from "@/context/AuthContext";
import { AppShell } from "@/components/AppShell";
import AuthPage from "@/pages/AuthPage";
import AuthCallback from "@/pages/AuthCallback";
import Library from "@/pages/Library";
import CharacterCreator from "@/pages/CharacterCreator";
import Play from "@/pages/Play";
import Chronicle from "@/pages/Chronicle";
import Saves from "@/pages/Saves";
import Store from "@/pages/Store";
import Storybook from "@/pages/Storybook";

function AppRouter() {
  const location = useLocation();
  if (location.hash?.includes("session_id=")) return <AuthCallback />;
  return (
    <Routes>
      <Route path="/login" element={<AuthPage />} />
      <Route path="/story/:shareId" element={<Storybook />} />
      <Route element={<ProtectedRoute><AppShell /></ProtectedRoute>}>
        <Route path="/library" element={<Library />} />
        <Route path="/create/:scenarioId" element={<CharacterCreator />} />
        <Route path="/play/:pid" element={<Play />} />
        <Route path="/chronicle/:pid" element={<Chronicle />} />
        <Route path="/saves/:pid" element={<Saves />} />
        <Route path="/store" element={<Store />} />
      </Route>
      <Route path="*" element={<Navigate to="/library" replace />} />
    </Routes>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRouter />
        <Toaster theme="dark" position="bottom-right" toastOptions={{ style: { background: "#12141A", border: "1px solid #2D3245", color: "#F0E6D2" } }} />
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
