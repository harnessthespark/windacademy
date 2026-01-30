import { PageHeader } from "@/components/shared/PageHeader";
import { Card, CardContent } from "@/components/ui/card";

export default async function CmsPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  return (
    <div className="mx-auto max-w-3xl space-y-6 p-6">
      <PageHeader title={`CMS page: ${slug}`} />
      <Card>
        <CardContent className="py-10 text-center text-muted-foreground">
          Content for &ldquo;{slug}&rdquo; will appear here.
        </CardContent>
      </Card>
    </div>
  );
}
