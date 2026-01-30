import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function InvoiceDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  return (
    <div className="space-y-6">
      <PageHeader
        title={`Invoice #${id}`}
        description="Invoice details."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Invoice detail will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
