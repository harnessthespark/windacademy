"use client";

import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function ProfilePage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Profile"
        description="Manage your account details."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Profile settings will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
