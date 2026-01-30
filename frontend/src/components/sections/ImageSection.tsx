import Image from "next/image"

interface ImageContent {
  src: string
  alt?: string
  caption?: string
}

export function ImageSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { src, alt, caption } = content as unknown as ImageContent

  return (
    <section className="mx-auto max-w-4xl px-6 py-16">
      <figure className="text-center">
        <div className="relative aspect-video w-full overflow-hidden rounded-lg">
          <Image
            src={src}
            alt={alt || ""}
            fill
            className="object-cover"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 80vw, 896px"
          />
        </div>
        {caption && (
          <figcaption className="mt-4 text-sm text-muted-foreground">
            {caption}
          </figcaption>
        )}
      </figure>
    </section>
  )
}
