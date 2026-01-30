import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function FeedbackPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Feedback"
        description="Manage your feedback"
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Feedback list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
