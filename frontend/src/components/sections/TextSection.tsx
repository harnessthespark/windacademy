interface TextContent {
  heading?: string
  body: string
}

export function TextSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, body } = content as unknown as TextContent

  return (
    <section className="mx-auto max-w-3xl px-6 py-16">
      {heading && (
        <h2 className="text-3xl font-bold tracking-tight text-foreground">
          {heading}
        </h2>
      )}
      <div
        className="prose prose-neutral dark:prose-invert mt-6 max-w-none"
        dangerouslySetInnerHTML={{ __html: body }}
      />
    </section>
  )
}
