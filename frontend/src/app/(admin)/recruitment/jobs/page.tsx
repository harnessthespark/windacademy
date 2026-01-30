import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function JobsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Jobs"
        description="Manage your jobs"
        actions={<Button>New Job</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Job list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
