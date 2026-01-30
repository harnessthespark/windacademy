import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function ClientsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Clients"
        description="Manage your clients"
        actions={<Button>New Client</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Client list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
