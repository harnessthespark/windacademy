import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function CandidatesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Candidates"
        description="Manage your candidates"
        actions={<Button>New Candidate</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Candidate list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
