import { Routes, Route, Navigate } from 'react-router'

import AppLayout from '../layouts/AppLayout'

import DashboardPage from '../../features/dashboard/DashboardPage'
import NetworkExplorerPage from '../../features/network-explorer/NetworkExplorerPage'
import CommunitiesPage from '../../features/communities/CommunitiesPage'
import TrendsPage from '../../features/trends/TrendsPage'

function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route index element={<DashboardPage />} />
        <Route path="network" element={<NetworkExplorerPage />} />
        <Route path="communities" element={<CommunitiesPage />} />
        <Route path="trends" element={<TrendsPage />} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default AppRoutes