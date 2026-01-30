interface FaqItem {
  question: string
  answer: string
}

interface FaqContent {
  heading?: string
  items: FaqItem[]
}

export function FaqSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, items } = content as unknown as FaqContent

  return (
    <section className="mx-auto max-w-3xl px-6 py-16">
      {heading && (
        <h2 className="mb-10 text-center text-3xl font-bold tracking-tight text-foreground">
          {heading}
        </h2>
      )}
      <div className="divide-y divide-border">
        {items?.map((item, index) => (
          <details key={index} className="group py-4">
            <summary className="flex cursor-pointer list-none items-center justify-between font-medium text-foreground">
              <span>{item.question}</span>
              <span className="ml-4 shrink-0 transition-transform group-open:rotate-45">
                +
              </span>
            </summary>
            <p className="mt-3 text-muted-foreground">{item.answer}</p>
          </details>
        ))}
      </div>
    </section>
  )
}
