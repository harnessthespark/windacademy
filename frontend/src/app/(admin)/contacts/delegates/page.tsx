import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function DelegatesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Delegates"
        description="Manage your delegates"
        actions={<Button>New Delegate</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Delegate list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
