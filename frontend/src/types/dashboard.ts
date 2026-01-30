// Dashboard stats and widget types

export interface DashboardStats {
  total_clients: number;
  active_clients: number;
  total_delegates: number;
  total_bookings: number;
  upcoming_courses: number;
  revenue_this_month: string;
  revenue_this_year: string;
  outstanding_invoices: number;
  outstanding_amount: string;
  open_jobs: number;
  active_placements: number;
  active_campaigns: number;
}

export interface RevenueDataPoint {
  month: string;
  training_revenue: string;
  recruitment_revenue: string;
  total_revenue: string;
}

export interface BookingsByStatus {
  status: string;
  count: number;
}

export interface UpcomingCourse {
  id: string;
  course_title: string;
  course_code: string;
  start_date: string;
  end_date: string;
  venue: string;
  trainer_name: string;
  bookings_count: number;
  max_delegates: number;
}

export interface RecentActivity {
  id: string;
  action: string;
  description: string;
  user: string;
  created_at: string;
  content_type: string;
  object_id: string;
}

export interface DashboardWidget {
  id: string;
  type: 'stats' | 'chart' | 'table' | 'list';
  title: string;
  position: number;
  config: Record<string, unknown>;
}
