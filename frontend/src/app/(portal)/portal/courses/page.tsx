"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function CoursesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="My Courses"
        description="Access your enrolled courses."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Courses list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
