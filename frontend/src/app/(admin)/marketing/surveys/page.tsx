import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function SurveysPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Surveys"
        description="Manage your surveys"
        actions={<Button>New Survey</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Survey list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
