import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function InvoicesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Invoices"
        description="Manage your invoices"
        actions={<Button>New Invoice</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Invoice list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
