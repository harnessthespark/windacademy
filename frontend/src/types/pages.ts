// CMS Page and Section types

export type PageStatus = 'draft' | 'published' | 'archived';

export interface Page {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  slug: string;
  description: string;
  status: PageStatus;
  is_homepage: boolean;
  sections?: PageSection[];
}

export type SectionType =
  | 'hero'
  | 'text'
  | 'image'
  | 'image_text'
  | 'video'
  | 'gallery'
  | 'cta'
  | 'cards'
  | 'testimonials'
  | 'faq'
  | 'form'
  | 'html'
  | 'spacer';

export interface PageSection {
  id: string;
  created_at: string;
  updated_at: string;
  page: string;
  order: number;
  title: string;
  section_type: SectionType;
  content: Record<string, unknown>;
  is_visible: boolean;
  css_class: string;
}
