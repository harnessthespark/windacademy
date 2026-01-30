// Client types

export type ClientStatus = 'prospect' | 'active' | 'inactive' | 'former';

export type ClientType = 'training' | 'recruitment' | 'both';

export interface Client {
  id: string;
  created_at: string;
  updated_at: string;
  name: string;
  trading_name: string;
  status: ClientStatus;
  client_type: ClientType;
  company_number: string;
  vat_number: string;
  website: string;
  industry: string;
  address_line_1: string;
  address_line_2: string;
  city: string;
  county: string;
  postcode: string;
  country: string;
  billing_email: string;
  payment_terms_days: number;
  account_manager: string | null;
  lifetime_value: string;
  portal_enabled: boolean;
}
