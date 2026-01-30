import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function DelegateDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return (
    <div className="space-y-6">
      <PageHeader title="Delegate Detail" />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Delegate #{id} details will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
