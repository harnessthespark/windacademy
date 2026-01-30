// Account (company account) types

export type AccountStatus = 'active' | 'inactive' | 'suspended';

export interface Account {
  id: string;
  created_at: string;
  updated_at: string;
  name: string;
  status: AccountStatus;
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
  phone: string;
  notes: string;
}
