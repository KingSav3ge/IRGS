import { NavLink, Outlet, useLocation, useNavigate } from "react-router-dom";
import { Hexagon, LogOut } from "lucide-react";
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { useAuth } from "@/context/AuthContext";

export const LAST_PLAY_KEY = "irgs_last_playthrough";

const Link = ({ to, children, testid }) => (
  <NavLink to={to} data-testid={testid}
    className={({ isActive }) => `px-3 py-2 text-sm tracking-wide transition-colors ${isActive ? "text-gold" : "text-ash hover:text-parchment"}`}>
    {children}
  </NavLink>
);

export const AppShell = () => {
  const { user, signOut } = useAuth();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const last = pathname.match(/^\/(?:play|chronicle|saves)\/([^/]+)/)?.[1] || localStorage.getItem(LAST_PLAY_KEY);

  return (
    <div className="min-h-screen bg-void grain">
      <header className="sticky top-0 z-40 backdrop-blur-xl bg-void/80 border-b border-line" data-testid="nav-header">
        <div className="mx-auto max-w-[1600px] h-16 px-4 sm:px-8 flex items-center gap-3 sm:gap-6">
          <NavLink to="/library" className="flex items-center gap-2" data-testid="nav-logo-link">
            <Hexagon size={18} className="text-gold" />
            <span className="font-heading tracking-[0.25em] text-gold text-sm hidden sm:inline">IRGS</span>
          </NavLink>
          <nav className="flex items-center overflow-x-auto min-w-0 flex-1 whitespace-nowrap scroll-thin" data-testid="nav-links">
            <Link to="/library" testid="nav-library-link">Library</Link>
            {last && <Link to={`/play/${last}`} testid="nav-play-link">Play</Link>}
            {last && <Link to={`/chronicle/${last}`} testid="nav-chronicle-link">Chronicle</Link>}
            {last && <Link to={`/saves/${last}`} testid="nav-saves-link">Saves</Link>}
            <Link to="/store" testid="nav-store-link">Store</Link>
            <Link to="/marketplace" testid="nav-marketplace-link">Marketplace</Link>
          </nav>
          <div className="ml-auto shrink-0">
            <DropdownMenu>
              <DropdownMenuTrigger className="flex items-center gap-2 rounded-full border border-line px-1 py-1 pr-3 hover:border-gold/50 transition-colors" data-testid="nav-user-profile-menu">
                {user?.picture ? (
                  <img src={user.picture} alt="" className="h-7 w-7 rounded-full" />
                ) : (
                  <span className="h-7 w-7 rounded-full bg-surface grid place-items-center font-heading text-gold text-xs">
                    {(user?.name || "?")[0]}
                  </span>
                )}
                <span className="text-sm text-ash hidden sm:inline" data-testid="nav-user-name">{user?.name}</span>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="bg-tome/95 backdrop-blur-md border-line">
                <DropdownMenuLabel className="text-xs text-dust">{user?.email}<span className="block font-mono text-[10px] mt-1" data-testid="nav-version-label">IRGS 3.3.E</span></DropdownMenuLabel>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={() => navigate("/store")} data-testid="nav-account-entitlements">Purchases & subscriptions</DropdownMenuItem>
                <DropdownMenuItem onClick={async () => { await signOut(); navigate("/login"); }} data-testid="nav-logout-button">
                  <LogOut size={14} className="mr-2" /> Sign out
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </header>
      <main className="relative z-10"><Outlet /></main>
    </div>
  );
};
