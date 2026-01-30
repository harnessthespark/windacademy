import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function CourseInstancesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Course Instances"
        description="Manage your course instances"
        actions={<Button>New Instance</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Course instance list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
