import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function JobDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  return (
    <div className="space-y-6">
      <PageHeader
        title={`Job #${id}`}
        description="Job details."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Job detail will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
