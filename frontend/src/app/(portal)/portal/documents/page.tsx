"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function DocumentsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="My Documents"
        description="Access your documents."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Documents list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
