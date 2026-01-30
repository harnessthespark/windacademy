import { Card, CardContent } from "@/components/ui/card"

interface Testimonial {
  quote: string
  author: string
  role?: string
}

interface TestimonialsContent {
  heading?: string
  testimonials: Testimonial[]
}

export function TestimonialsSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, testimonials } =
    content as unknown as TestimonialsContent

  return (
    <section className="mx-auto max-w-6xl px-6 py-16">
      {heading && (
        <h2 className="mb-10 text-center text-3xl font-bold tracking-tight text-foreground">
          {heading}
        </h2>
      )}
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {testimonials?.map((testimonial, index) => (
          <Card key={index}>
            <CardContent>
              <blockquote className="text-foreground">
                <p className="before:content-['\201C'] after:content-['\201D']">
                  {testimonial.quote}
                </p>
              </blockquote>
              <div className="mt-4">
                <p className="font-semibold text-foreground">
                  {testimonial.author}
                </p>
                {testimonial.role && (
                  <p className="text-sm text-muted-foreground">
                    {testimonial.role}
                  </p>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  )
}
