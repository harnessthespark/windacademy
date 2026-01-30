import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function ClientContactsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Client Contacts"
        description="Manage your client contacts"
        actions={<Button>New Client Contact</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Client contact list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
