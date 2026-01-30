// Generic API response and error types

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface ApiError {
  detail?: string;
  [key: string]: unknown;
}

export interface ApiValidationError {
  [field: string]: string[];
}

export interface ApiRequestParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
}
