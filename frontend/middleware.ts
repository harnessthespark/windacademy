import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const PROTECTED_PATHS = ["/dashboard", "/accounts", "/contacts", "/clients", "/training", "/recruitment", "/marketing", "/documents", "/invoices", "/cms"];
const PORTAL_PATHS = ["/portal"];
const AUTH_PATHS = ["/login"];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const accessToken = request.cookies.get("access_token")?.value;

  // For localStorage-based auth, we can't check tokens in middleware.
  // This middleware provides basic cookie-based protection if cookies are set.
  // The client-side auth provider handles the primary protection.

  const isProtectedPath = PROTECTED_PATHS.some((p) => pathname.startsWith(p));
  const isPortalPath = PORTAL_PATHS.some((p) => pathname.startsWith(p));
  const isAuthPath = AUTH_PATHS.some((p) => pathname.startsWith(p));

  // If user has a cookie token and tries to access login, redirect to home
  if (isAuthPath && accessToken) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  // For protected/portal routes without cookie token, let client-side handle it
  // (since auth is localStorage-based, middleware can't fully gate access)
  if ((isProtectedPath || isPortalPath) && !accessToken) {
    // Don't redirect here — let the client-side auth provider handle it
    // This avoids double-redirect issues with localStorage-based auth
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|api).*)",
  ],
};
