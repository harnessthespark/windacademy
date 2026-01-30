// Marketing types: Campaign, Newsletter, CampaignRecipient

export type CampaignType = 'email' | 'linkedin' | 'phone' | 'event' | 'webinar';

export type CampaignStatus = 'draft' | 'active' | 'paused' | 'completed' | 'cancelled';

export interface Campaign {
  id: string;
  created_at: string;
  updated_at: string;
  name: string;
  campaign_type: CampaignType;
  status: CampaignStatus;
  start_date: string | null;
  end_date: string | null;
  budget: string;
  total_sent: number;
  total_opened: number;
  total_clicked: number;
  owner: string | null;
}

export interface CampaignRecipient {
  id: string;
  created_at: string;
  updated_at: string;
  campaign: string;
  delegate: string | null;
  client_contact: string | null;
  email: string;
  sent_at: string | null;
  opened_at: string | null;
  clicked_at: string | null;
  bounced: boolean;
  unsubscribed: boolean;
}

export type NewsletterStatus = 'draft' | 'scheduled' | 'sending' | 'sent' | 'cancelled';

export interface Newsletter {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  subject_line: string;
  body_html: string;
  body_text: string;
  status: NewsletterStatus;
  campaign: string | null;
  scheduled_send_at: string | null;
  sent_at: string | null;
  total_sent: number;
  total_opened: number;
  total_clicked: number;
}

// Survey types (placeholder for future implementation)
export type SurveyStatus = 'draft' | 'active' | 'closed';

export interface Survey {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  description: string;
  status: SurveyStatus;
  campaign: string | null;
  total_responses: number;
}
