import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default function TimesheetsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Timesheets"
        description="Track and approve staff timesheets"
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Timesheet list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
