import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function TrainersPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Trainers"
        description="Manage your trainers"
        actions={<Button>New Trainer</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Trainer list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
