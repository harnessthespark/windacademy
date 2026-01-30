// Contact types: Delegate, Trainer, ClientContact

export type PersonTitle = 'Mr' | 'Mrs' | 'Ms' | 'Miss' | 'Dr' | 'Prof';

export interface PersonBase {
  id: string;
  created_at: string;
  updated_at: string;
  title: PersonTitle | '';
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  mobile: string;
  job_title: string;
  company_name: string;
  address_line_1: string;
  address_line_2: string;
  city: string;
  county: string;
  postcode: string;
  country: string;
  linkedin_url: string;
  gdpr_consent: boolean;
  gdpr_consent_date: string | null;
  marketing_opt_in: boolean;
  user: string | null;
}

export interface Delegate extends PersonBase {
  source: string;
  employer: string | null;
  dietary_requirements: string;
  accessibility_needs: string;
  emergency_contact_name: string;
  emergency_contact_phone: string;
  is_candidate: boolean;
  cv: string;
}

export type TrainerType = 'internal' | 'external' | 'associate';

export interface Trainer extends PersonBase {
  trainer_type: TrainerType;
  day_rate: string | null;
  specialisms: string;
  bio: string;
  photo: string;
  approved_courses: string[];
  dbs_expiry_date: string | null;
  insurance_expiry_date: string | null;
}

export interface ClientContact extends PersonBase {
  client: string;
  is_primary: boolean;
  is_billing: boolean;
  is_booking: boolean;
  department: string;
}
