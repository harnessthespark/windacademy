export function PublicFooter() {
  return (
    <footer className="border-t bg-white">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-center px-4 sm:px-6 lg:px-8">
        <p className="text-sm text-muted-foreground">
          &copy; {new Date().getFullYear()} Wind Academy. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
