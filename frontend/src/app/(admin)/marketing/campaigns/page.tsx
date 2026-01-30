import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function CampaignsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Campaigns"
        description="Manage your campaigns"
        actions={<Button>New Campaign</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Campaign list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
