import { HeroSection } from "./HeroSection"
import { TextSection } from "./TextSection"
import { CardsSection } from "./CardsSection"
import { CtaSection } from "./CtaSection"
import { FaqSection } from "./FaqSection"
import { ImageSection } from "./ImageSection"
import { TestimonialsSection } from "./TestimonialsSection"

export interface PageSection {
  id: number
  section_type:
    | "hero"
    | "text"
    | "cards"
    | "cta"
    | "faq"
    | "image"
    | "testimonials"
  order: number
  content: Record<string, unknown>
}

export function SectionRenderer({ section }: { section: PageSection }) {
  switch (section.section_type) {
    case "hero":
      return <HeroSection content={section.content} />
    case "text":
      return <TextSection content={section.content} />
    case "cards":
      return <CardsSection content={section.content} />
    case "cta":
      return <CtaSection content={section.content} />
    case "faq":
      return <FaqSection content={section.content} />
    case "image":
      return <ImageSection content={section.content} />
    case "testimonials":
      return <TestimonialsSection content={section.content} />
    default:
      return null
  }
}
