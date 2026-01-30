"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function JobsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Job Board"
        description="Browse available opportunities."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Job listings will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
