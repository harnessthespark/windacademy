import { PageHeader } from "@/components/shared/PageHeader";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function AccountsPage() {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Accounts"
        description="Manage your accounts"
        actions={<Button>New Account</Button>}
      />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Account list will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
