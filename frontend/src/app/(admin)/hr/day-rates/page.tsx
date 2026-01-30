import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function DayRatesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Day Rates"
        description="Manage day rates, client fees, and resourcer commissions"
        actions={<Button>Add Rate</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Day rates list will appear here — includes day rate, client fee %, and resourcer commission.
        </CardContent>
      </Card>
    </div>
  );
}
