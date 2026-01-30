import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function SurveyDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return (
    <div className="space-y-6">
      <PageHeader title="Survey Detail" />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Survey #{id} details will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
