// Invoice and InvoiceLineItem types

export type InvoiceStatus =
  | 'draft'
  | 'sent'
  | 'viewed'
  | 'paid'
  | 'overdue'
  | 'cancelled';

export interface Invoice {
  id: string;
  created_at: string;
  updated_at: string;
  invoice_number: string;
  client: string;
  status: InvoiceStatus;
  issue_date: string;
  due_date: string;
  paid_date: string | null;
  subtotal: string;
  vat_rate: string;
  vat_amount: string;
  total: string;
  po_number: string;
  booking: string | null;
  placement: string | null;
  pdf: string;
  line_items?: InvoiceLineItem[];
}

export interface InvoiceLineItem {
  id: number;
  invoice: string;
  description: string;
  quantity: string;
  unit_price: string;
  line_total: string;
}
