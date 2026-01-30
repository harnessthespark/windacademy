// Recruitment types: Job, Candidate, Placement

export type JobStatus =
  | 'draft'
  | 'open'
  | 'interviewing'
  | 'offered'
  | 'filled'
  | 'closed';

export type JobType = 'permanent' | 'contract' | 'temp' | 'temp_to_perm';

export interface Job {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  reference: string;
  client: string;
  status: JobStatus;
  job_type: JobType;
  description: string;
  requirements: string;
  location: string;
  salary_min: string | null;
  salary_max: string | null;
  fee_percent: string;
  consultant: string | null;
}

export type CandidateStage =
  | 'sourced'
  | 'applied'
  | 'screening'
  | 'shortlisted'
  | 'submitted'
  | 'interviews'
  | 'offer'
  | 'placed'
  | 'rejected'
  | 'withdrawn';

export interface Candidate {
  id: string;
  created_at: string;
  updated_at: string;
  job: string;
  delegate: string | null;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  stage: CandidateStage;
  cv: string;
  rating: number | null;
  salary_expectation: string | null;
}

export type PlacementStatus =
  | 'pending_start'
  | 'started'
  | 'probation'
  | 'confirmed'
  | 'cancelled';

export interface Placement {
  id: string;
  created_at: string;
  updated_at: string;
  job: string;
  candidate: string;
  status: PlacementStatus;
  start_date: string | null;
  end_date: string | null;
  agreed_salary: string | null;
  fee_amount: string;
  guarantee_period_days: number;
}
