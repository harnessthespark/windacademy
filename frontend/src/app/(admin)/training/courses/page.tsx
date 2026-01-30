import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function CoursesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Courses"
        description="Manage your courses"
        actions={<Button>New Course</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Course list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
