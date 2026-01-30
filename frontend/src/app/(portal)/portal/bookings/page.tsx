"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function BookingsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="My Bookings"
        description="View and manage your bookings."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Bookings list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
