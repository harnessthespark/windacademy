"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  Building2,
  Users,
  Briefcase,
  GraduationCap,
  UserSearch,
  Megaphone,
  FileText,
  Receipt,
  Globe,
  ChevronDown,
  ChevronRight,
  Wind,
  ClipboardList,
} from "lucide-react";
import { cn } from "@/lib/utils";

interface NavItem {
  label: string;
  href: string;
  icon?: React.ComponentType<{ className?: string }>;
}

interface NavSection {
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  href?: string;
  children?: NavItem[];
}

const navigation: NavSection[] = [
  {
    label: "Dashboard",
    icon: LayoutDashboard,
    href: "/dashboard",
  },
  {
    label: "Accounts",
    icon: Building2,
    href: "/accounts",
  },
  {
    label: "Contacts",
    icon: Users,
    children: [
      { label: "Delegates", href: "/contacts/delegates" },
      { label: "Trainers", href: "/contacts/trainers" },
      { label: "Client Contacts", href: "/contacts/client-contacts" },
    ],
  },
  {
    label: "Clients",
    icon: Briefcase,
    href: "/clients",
  },
  {
    label: "Training",
    icon: GraduationCap,
    children: [
      { label: "Courses", href: "/training/courses" },
      { label: "Instances", href: "/training/instances" },
      { label: "Bookings", href: "/training/bookings" },
      { label: "Feedback", href: "/training/feedback" },
    ],
  },
  {
    label: "Recruitment",
    icon: UserSearch,
    children: [
      { label: "Jobs", href: "/recruitment/jobs" },
      { label: "Candidates", href: "/recruitment/candidates" },
      { label: "Interviews", href: "/recruitment/interviews" },
      { label: "Placements", href: "/recruitment/placements" },
    ],
  },
  {
    label: "Marketing",
    icon: Megaphone,
    children: [
      { label: "Campaigns", href: "/marketing/campaigns" },
      { label: "Newsletters", href: "/marketing/newsletters" },
      { label: "Recipients", href: "/marketing/recipients" },
      { label: "Surveys", href: "/marketing/surveys" },
    ],
  },
  {
    label: "HR",
    icon: ClipboardList,
    children: [
      { label: "Employees", href: "/hr/employees" },
      { label: "Leave Requests", href: "/hr/leave" },
      { label: "Timesheets", href: "/hr/timesheets" },
      { label: "Day Rates", href: "/hr/day-rates" },
    ],
  },
  {
    label: "Documents",
    icon: FileText,
    href: "/documents",
  },
  {
    label: "Invoices",
    icon: Receipt,
    href: "/invoices",
  },
  {
    label: "CMS Pages",
    icon: Globe,
    href: "/cms/pages",
  },
];

export function AdminSidebar() {
  const pathname = usePathname();
  const [expandedSections, setExpandedSections] = useState<
    Record<string, boolean>
  >(() => {
    const initial: Record<string, boolean> = {};
    for (const section of navigation) {
      if (section.children) {
        const isActive = section.children.some((child) =>
          pathname.startsWith(child.href)
        );
        if (isActive) {
          initial[section.label] = true;
        }
      }
    }
    return initial;
  });

  function toggleSection(label: string) {
    setExpandedSections((prev) => ({
      ...prev,
      [label]: !prev[label],
    }));
  }

  function isActive(href: string) {
    if (href === "/dashboard") {
      return pathname === "/dashboard";
    }
    return pathname.startsWith(href);
  }

  return (
    <aside className="fixed inset-y-0 left-0 z-30 hidden w-64 flex-col border-r bg-white lg:flex">
      {/* Logo */}
      <div className="flex h-16 items-center gap-2 border-b px-6">
        <Wind className="size-6 text-primary" />
        <span className="text-lg font-semibold">Wind Academy</span>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto px-3 py-4">
        <ul className="space-y-1">
          {navigation.map((section) => {
            const Icon = section.icon;
            const hasChildren = !!section.children;
            const isExpanded = expandedSections[section.label] ?? false;
            const sectionActive = section.href
              ? isActive(section.href)
              : section.children?.some((child) => isActive(child.href)) ??
                false;

            return (
              <li key={section.label}>
                {hasChildren ? (
                  <>
                    <button
                      onClick={() => toggleSection(section.label)}
                      className={cn(
                        "flex w-full items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-colors",
                        sectionActive
                          ? "text-primary"
                          : "text-muted-foreground hover:bg-accent hover:text-accent-foreground"
                      )}
                    >
                      <Icon className="size-4 shrink-0" />
                      <span className="flex-1 text-left">{section.label}</span>
                      {isExpanded ? (
                        <ChevronDown className="size-4 shrink-0" />
                      ) : (
                        <ChevronRight className="size-4 shrink-0" />
                      )}
                    </button>
                    {isExpanded && (
                      <ul className="ml-4 mt-1 space-y-1 border-l pl-3">
                        {section.children!.map((child) => (
                          <li key={child.href}>
                            <Link
                              href={child.href}
                              className={cn(
                                "block rounded-md px-3 py-1.5 text-sm transition-colors",
                                isActive(child.href)
                                  ? "bg-primary/10 font-medium text-primary"
                                  : "text-muted-foreground hover:bg-accent hover:text-accent-foreground"
                              )}
                            >
                              {child.label}
                            </Link>
                          </li>
                        ))}
                      </ul>
                    )}
                  </>
                ) : (
                  <Link
                    href={section.href!}
                    className={cn(
                      "flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-colors",
                      isActive(section.href!)
                        ? "bg-primary/10 text-primary"
                        : "text-muted-foreground hover:bg-accent hover:text-accent-foreground"
                    )}
                  >
                    <Icon className="size-4 shrink-0" />
                    <span>{section.label}</span>
                  </Link>
                )}
              </li>
            );
          })}
        </ul>
      </nav>
    </aside>
  );
}
