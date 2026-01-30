import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function RecipientsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Recipients"
        description="Manage your recipients"
        actions={<Button>New Recipient</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Recipient list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
