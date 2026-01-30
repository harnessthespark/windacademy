export const NAV_ITEMS = {
  admin: [
    { label: "Dashboard", href: "/dashboard", icon: "LayoutDashboard" },
    { label: "Accounts", href: "/accounts", icon: "Building2" },
    {
      label: "Contacts",
      icon: "Users",
      children: [
        { label: "Delegates", href: "/contacts/delegates" },
        { label: "Trainers", href: "/contacts/trainers" },
        { label: "Client Contacts", href: "/contacts/client-contacts" },
      ],
    },
    { label: "Clients", href: "/clients", icon: "Briefcase" },
    {
      label: "Training",
      icon: "GraduationCap",
      children: [
        { label: "Courses", href: "/training/courses" },
        { label: "Instances", href: "/training/instances" },
        { label: "Bookings", href: "/training/bookings" },
        { label: "Feedback", href: "/training/feedback" },
      ],
    },
    {
      label: "Recruitment",
      icon: "UserSearch",
      children: [
        { label: "Jobs", href: "/recruitment/jobs" },
        { label: "Candidates", href: "/recruitment/candidates" },
        { label: "Placements", href: "/recruitment/placements" },
      ],
    },
    {
      label: "Marketing",
      icon: "Megaphone",
      children: [
        { label: "Campaigns", href: "/marketing/campaigns" },
        { label: "Newsletters", href: "/marketing/newsletters" },
        { label: "Recipients", href: "/marketing/recipients" },
        { label: "Surveys", href: "/marketing/surveys" },
      ],
    },
    { label: "Documents", href: "/documents", icon: "FileText" },
    { label: "Invoices", href: "/invoices", icon: "Receipt" },
    { label: "CMS Pages", href: "/cms/pages", icon: "Globe" },
  ],
  portal: [
    { label: "Home", href: "/portal" },
    { label: "Bookings", href: "/portal/bookings" },
    { label: "Courses", href: "/portal/courses" },
    { label: "Invoices", href: "/portal/invoices" },
    { label: "Documents", href: "/portal/documents" },
    { label: "Jobs", href: "/portal/jobs" },
    { label: "Profile", href: "/portal/profile" },
  ],
} as const;

export const STATUS_COLORS: Record<string, string> = {
  active: "bg-green-100 text-green-800",
  inactive: "bg-gray-100 text-gray-800",
  pending: "bg-yellow-100 text-yellow-800",
  confirmed: "bg-blue-100 text-blue-800",
  cancelled: "bg-red-100 text-red-800",
  completed: "bg-green-100 text-green-800",
  draft: "bg-gray-100 text-gray-800",
  published: "bg-green-100 text-green-800",
  sent: "bg-blue-100 text-blue-800",
  paid: "bg-green-100 text-green-800",
  overdue: "bg-red-100 text-red-800",
  open: "bg-blue-100 text-blue-800",
  closed: "bg-gray-100 text-gray-800",
  filled: "bg-green-100 text-green-800",
};
