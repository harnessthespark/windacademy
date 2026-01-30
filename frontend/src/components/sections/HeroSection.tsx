import Link from "next/link"
import { Button } from "@/components/ui/button"

interface HeroContent {
  heading: string
  subheading?: string
  cta_text?: string
  cta_link?: string
  background_image?: string
}

export function HeroSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, subheading, cta_text, cta_link, background_image } =
    content as unknown as HeroContent

  return (
    <section
      className="relative flex min-h-[480px] w-full items-center justify-center bg-cover bg-center px-6 py-24"
      style={
        background_image
          ? { backgroundImage: `url(${background_image})` }
          : undefined
      }
    >
      {background_image && (
        <div className="absolute inset-0 bg-black/50" aria-hidden="true" />
      )}
      <div className="relative z-10 mx-auto max-w-3xl text-center">
        <h1
          className={`text-4xl font-bold tracking-tight sm:text-5xl lg:text-6xl ${
            background_image ? "text-white" : "text-foreground"
          }`}
        >
          {heading}
        </h1>
        {subheading && (
          <p
            className={`mt-6 text-lg sm:text-xl ${
              background_image ? "text-white/90" : "text-muted-foreground"
            }`}
          >
            {subheading}
          </p>
        )}
        {cta_text && cta_link && (
          <div className="mt-10">
            <Button asChild size="lg">
              <Link href={cta_link}>{cta_text}</Link>
            </Button>
          </div>
        )}
      </div>
    </section>
  )
}
