"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function InvoicesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="My Invoices"
        description="View your invoices and payments."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Invoices list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
