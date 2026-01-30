import Link from "next/link"
import { Button } from "@/components/ui/button"

interface CtaContent {
  heading: string
  description?: string
  button_text: string
  button_link: string
}

export function CtaSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, description, button_text, button_link } =
    content as unknown as CtaContent

  return (
    <section className="bg-primary px-6 py-20">
      <div className="mx-auto max-w-3xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-primary-foreground">
          {heading}
        </h2>
        {description && (
          <p className="mt-4 text-lg text-primary-foreground/90">
            {description}
          </p>
        )}
        <div className="mt-8">
          <Button asChild size="lg" variant="secondary">
            <Link href={button_link}>{button_text}</Link>
          </Button>
        </div>
      </div>
    </section>
  )
}
