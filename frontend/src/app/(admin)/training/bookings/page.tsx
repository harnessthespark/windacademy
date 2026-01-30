import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function BookingsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Bookings"
        description="Manage your bookings"
        actions={<Button>New Booking</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Booking list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
