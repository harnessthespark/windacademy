from django.db import models
from apps.core.models import TimeStampedModel


class Page(TimeStampedModel):
    """A customisable page that the client can build with sections."""

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    is_homepage = models.BooleanField(
        default=False,
        help_text="If true, this page is used as the landing page.",
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Section(TimeStampedModel):
    """An ordered content block within a Page."""

    class SectionType(models.TextChoices):
        HERO = "hero", "Hero Banner"
        TEXT = "text", "Text Block"
        IMAGE = "image", "Image"
        IMAGE_TEXT = "image_text", "Image + Text"
        VIDEO = "video", "Video Embed"
        GALLERY = "gallery", "Gallery"
        CTA = "cta", "Call to Action"
        CARDS = "cards", "Card Grid"
        TESTIMONIALS = "testimonials", "Testimonials"
        FAQ = "faq", "FAQ"
        FORM = "form", "Form Embed"
        HTML = "html", "Custom HTML"
        SPACER = "spacer", "Spacer"

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255, blank=True)
    section_type = models.CharField(
        max_length=20, choices=SectionType.choices, default=SectionType.TEXT
    )
    content = models.JSONField(
        default=dict,
        blank=True,
        help_text="Structured content for this section (varies by section_type).",
    )
    is_visible = models.BooleanField(default=True)
    css_class = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional CSS classes for custom styling.",
    )

    class Meta:
        ordering = ["page", "order"]
        unique_together = ("page", "order")

    def __str__(self):
        label = self.title or self.get_section_type_display()
        return f"{self.page.title} — {label} (#{self.order})"
