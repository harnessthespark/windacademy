import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function BookingDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  return (
    <div className="space-y-6">
      <PageHeader
        title={`Booking #${id}`}
        description="Booking details."
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Booking detail will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
