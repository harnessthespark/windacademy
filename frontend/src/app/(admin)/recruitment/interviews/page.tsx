import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function InterviewsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Interviews"
        description="Schedule and manage candidate interviews"
        actions={<Button>Schedule Interview</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Interview list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
