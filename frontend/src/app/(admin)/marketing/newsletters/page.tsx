import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function NewslettersPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Newsletters"
        description="Manage your newsletters"
        actions={<Button>New Newsletter</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Newsletter list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
