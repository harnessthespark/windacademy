import Link from "next/link";
import { Wind } from "lucide-react";

export function PublicHeader() {
  return (
    <header className="sticky top-0 z-30 border-b bg-white">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-2">
          <Wind className="size-6 text-primary" />
          <span className="text-lg font-semibold">Wind Academy</span>
        </Link>
        <Link
          href="/login"
          className="text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          Login
        </Link>
      </div>
    </header>
  );
}
