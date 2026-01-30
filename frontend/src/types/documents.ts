// Document types

export type DocType =
  | 'contract'
  | 'proposal'
  | 'certificate'
  | 'cv'
  | 'invoice'
  | 'report'
  | 'other';

export interface Document {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  doc_type: DocType;
  file: string;
  uploaded_by: string | null;
  visible_to_client: boolean;
  content_type: number | null;
  object_id: string | null;
}
