import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function PlacementsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Placements"
        description="Manage placements with day rates, client fees, and commissions"
        actions={<Button>New Placement</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Placement list will appear here — includes day rate, client fee %, and resourcer commission columns.
        </CardContent>
      </Card>
    </div>
  );
}
