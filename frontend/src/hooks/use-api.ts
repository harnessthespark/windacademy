"use client";

import { useState, useEffect, useCallback } from "react";
import api from "@/lib/api";

interface UseApiOptions {
  page?: number;
  pageSize?: number;
  search?: string;
  ordering?: string;
  filters?: Record<string, string>;
}

interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

interface UseApiResult<T> {
  data: T[];
  total: number;
  loading: boolean;
  error: string | null;
  refetch: () => void;
}

export function useApi<T>(
  endpoint: string,
  options: UseApiOptions = {}
): UseApiResult<T> {
  const { page = 1, pageSize = 20, search, ordering, filters } = options;
  const [data, setData] = useState<T[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const params: Record<string, string | number> = {
        page,
        page_size: pageSize,
      };
      if (search) params.search = search;
      if (ordering) params.ordering = ordering;
      if (filters) {
        Object.entries(filters).forEach(([key, value]) => {
          if (value) params[key] = value;
        });
      }

      const { data: responseData } = await api.get<PaginatedResponse<T>>(
        endpoint,
        { params }
      );
      setData(responseData.results);
      setTotal(responseData.count);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch data");
    } finally {
      setLoading(false);
    }
  }, [endpoint, page, pageSize, search, ordering, filters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, total, loading, error, refetch: fetchData };
}

export function useApiDetail<T>(endpoint: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const { data: responseData } = await api.get<T>(endpoint);
      setData(responseData);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch data");
    } finally {
      setLoading(false);
    }
  }, [endpoint]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
}
