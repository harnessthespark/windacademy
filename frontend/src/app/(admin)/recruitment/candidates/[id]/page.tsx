import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function CandidateDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return (
    <div className="space-y-6">
      <PageHeader title="Candidate Detail" />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Candidate #{id} details will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
