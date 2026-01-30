"use client";

import { AuthProvider } from "@/hooks/use-auth";
import { ToastProvider } from "@/providers/ToastProvider";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      <ToastProvider>{children}</ToastProvider>
    </AuthProvider>
  );
}
