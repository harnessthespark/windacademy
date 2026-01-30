import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function DocumentsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Documents"
        description="Manage your documents"
        actions={<Button>New Document</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Document list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
