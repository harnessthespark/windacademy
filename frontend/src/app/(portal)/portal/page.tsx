"use client";

import { useAuth } from "@/hooks/use-auth";
import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";
import {
  CalendarDays,
  GraduationCap,
  Receipt,
  FileText,
  Briefcase,
} from "lucide-react";
import Link from "next/link";

const quickLinks = [
  {
    title: "My Bookings",
    description: "View and manage your bookings",
    href: "/portal/bookings",
    icon: CalendarDays,
  },
  {
    title: "My Courses",
    description: "Access your enrolled courses",
    href: "/portal/courses",
    icon: GraduationCap,
  },
  {
    title: "My Invoices",
    description: "View your invoices and payments",
    href: "/portal/invoices",
    icon: Receipt,
  },
  {
    title: "Documents",
    description: "Access your documents",
    href: "/portal/documents",
    icon: FileText,
  },
  {
    title: "Job Board",
    description: "Browse available opportunities",
    href: "/portal/jobs",
    icon: Briefcase,
  },
];

export default function PortalHomePage() {
  const { user } = useAuth();

  return (
    <div className="space-y-6">
      <PageHeader
        title={`Welcome back, ${user?.username ?? "User"}`}
        description="Access your bookings, courses, and more from your portal."
      />

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {quickLinks.map((link) => {
          const Icon = link.icon;
          return (
            <Link key={link.href} href={link.href}>
              <Card className="transition-shadow hover:shadow-md">
                <CardContent className="flex items-start gap-4 p-6">
                  <Icon className="mt-0.5 h-6 w-6 shrink-0 text-primary" />
                  <div>
                    <h3 className="font-semibold">{link.title}</h3>
                    <p className="text-sm text-muted-foreground">
                      {link.description}
                    </p>
                  </div>
                </CardContent>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
