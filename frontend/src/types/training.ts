// Training types: Course, CourseInstance, Booking, Module, Lesson, Assessment, Feedback

export type CourseDeliveryMethod = 'classroom' | 'virtual' | 'blended' | 'elearning';

export interface Course {
  id: string;
  created_at: string;
  updated_at: string;
  title: string;
  code: string;
  category: string;
  description: string;
  objectives: string;
  duration_days: string;
  max_delegates: number;
  min_delegates: number;
  delivery_method: CourseDeliveryMethod;
  price_per_delegate: string;
  price_bespoke: string;
  accreditation_body: string;
  accreditation_number: string;
}

export type CourseInstanceStatus =
  | 'scheduled'
  | 'confirmed'
  | 'in_progress'
  | 'completed'
  | 'cancelled';

export interface CourseInstance {
  id: string;
  created_at: string;
  updated_at: string;
  course: string;
  status: CourseInstanceStatus;
  start_date: string;
  end_date: string;
  start_time: string | null;
  end_time: string | null;
  venue: string;
  virtual_link: string;
  trainer: string | null;
  client: string | null;
  price_override: string | null;
}

export type BookingStatus =
  | 'provisional'
  | 'confirmed'
  | 'attended'
  | 'no_show'
  | 'cancelled';

export interface Booking {
  id: string;
  created_at: string;
  updated_at: string;
  course_instance: string;
  delegate: string;
  booked_by_client: string | null;
  booked_by_contact: string | null;
  status: BookingStatus;
  price: string;
  discount_percent: string;
  po_number: string;
  certificate_issued: boolean;
  certificate_number: string;
}

export interface Module {
  id: string;
  created_at: string;
  updated_at: string;
  course: string;
  order: number;
  title: string;
  description: string;
}

export type LessonType = 'theory' | 'practical' | 'discussion' | 'activity';

export type LessonDeliveryMethod =
  | 'face_to_face'
  | 'video'
  | 'vr'
  | 'elearning'
  | 'webinar'
  | 'blended';

export interface Lesson {
  id: string;
  created_at: string;
  updated_at: string;
  module: string;
  order: number;
  title: string;
  description: string;
  duration_minutes: number;
  lesson_type: LessonType;
  delivery_method: LessonDeliveryMethod;
  materials: string;
}

export type AssessmentType = 'quiz' | 'practical' | 'written' | 'observation';

export interface Assessment {
  id: string;
  created_at: string;
  updated_at: string;
  course: string;
  title: string;
  assessment_type: AssessmentType;
  description: string;
  pass_mark: string;
  max_score: string;
  is_mandatory: boolean;
}

export interface AssessmentResult {
  id: string;
  created_at: string;
  updated_at: string;
  assessment: string;
  booking: string;
  score: string | null;
  passed: boolean;
  assessed_by: string | null;
  assessed_at: string | null;
  comments: string;
}

export interface Feedback {
  id: string;
  created_at: string;
  updated_at: string;
  booking: string;
  overall_rating: number;
  trainer_rating: number | null;
  content_rating: number | null;
  venue_rating: number | null;
  comments: string;
  suggestions: string;
  is_anonymous: boolean;
  submitted_at: string;
}
