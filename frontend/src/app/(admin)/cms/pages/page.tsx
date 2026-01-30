import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function CmsPagesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="CMS Pages"
        description="Manage your CMS pages"
        actions={<Button>New Page</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          CMS page list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
