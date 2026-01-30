import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function EmployeesPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Employees"
        description="Manage internal staff records"
        actions={<Button>Add Employee</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Employee list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
