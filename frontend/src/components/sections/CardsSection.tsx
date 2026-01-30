import Link from "next/link"
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card"

interface CardItem {
  title: string
  description: string
  icon?: string
  link?: string
}

interface CardsContent {
  heading?: string
  cards: CardItem[]
}

export function CardsSection({
  content,
}: {
  content: Record<string, unknown>
}) {
  const { heading, cards } = content as unknown as CardsContent

  return (
    <section className="mx-auto max-w-6xl px-6 py-16">
      {heading && (
        <h2 className="mb-10 text-center text-3xl font-bold tracking-tight text-foreground">
          {heading}
        </h2>
      )}
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {cards?.map((card, index) => {
          const inner = (
            <Card
              key={index}
              className="transition-shadow hover:shadow-md"
            >
              <CardHeader>
                {card.icon && (
                  <span className="mb-2 text-3xl" aria-hidden="true">
                    {card.icon}
                  </span>
                )}
                <CardTitle>{card.title}</CardTitle>
                <CardDescription>{card.description}</CardDescription>
              </CardHeader>
            </Card>
          )

          if (card.link) {
            return (
              <Link key={index} href={card.link} className="block">
                {inner}
              </Link>
            )
          }

          return inner
        })}
      </div>
    </section>
  )
}
