"use client";

import { useState, useMemo } from "react";

interface UsePaginationOptions {
  initialPage?: number;
  pageSize?: number;
}

export function usePagination(
  total: number,
  options: UsePaginationOptions = {}
) {
  const { initialPage = 1, pageSize = 20 } = options;
  const [page, setPage] = useState(initialPage);

  const totalPages = useMemo(
    () => Math.max(1, Math.ceil(total / pageSize)),
    [total, pageSize]
  );

  const goToPage = (p: number) => {
    setPage(Math.max(1, Math.min(p, totalPages)));
  };

  const nextPage = () => goToPage(page + 1);
  const prevPage = () => goToPage(page - 1);

  return {
    page,
    pageSize,
    totalPages,
    setPage: goToPage,
    nextPage,
    prevPage,
    hasNext: page < totalPages,
    hasPrev: page > 1,
  };
}
