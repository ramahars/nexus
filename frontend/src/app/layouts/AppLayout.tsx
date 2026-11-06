import { NavLink, Outlet } from 'react-router'

function AppLayout() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 md:flex">
      {/* Sidebar */}
      <aside className="w-64 border-r border-slate-800 p-6">
        <h1 className="mb-10 text-2xl font-bold tracking-wider">NEXUS</h1>

        <nav className="flex flex-col gap-2">
          <NavLink to="/" end className={getNavLinkClass}>
            Dashboard
          </NavLink>

          <NavLink to="/network" className={getNavLinkClass}>
            Network Explorer
          </NavLink>

          <NavLink to="/communities" className={getNavLinkClass}>
            Communities
          </NavLink>

          <NavLink to="/trends" className={getNavLinkClass}>
            Trends
          </NavLink>
        </nav>
      </aside>

      {/* Main application area */}
      <div className="min-w-0 flex-1">
        <header className="border-b border-slate-800 px-8 py-5">
          <span className="text-sm text-slate-400">Social Network Intelligence Platform</span>
        </header>

        <main className="p-8">
          <Outlet />
        </main>
      </div>
    </div>
  )
}

function getNavLinkClass({ isActive }: { isActive: boolean }) {
  const base = 'rounded-lg px-4 py-3 text-sm transition-colors'

  return isActive
    ? `${base} bg-indigo-500/15 text-indigo-300`
    : `${base} text-slate-400 hover:bg-slate-800 hover:text-white`
}

export default AppLayout
