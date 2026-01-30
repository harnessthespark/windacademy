import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function LeavePage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Leave Requests"
        description="View and manage staff leave requests"
        actions={<Button>New Request</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Leave request list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
