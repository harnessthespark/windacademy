export const ENDPOINTS = {
  auth: {
    token: '/api/v1/auth/token/',
    refresh: '/api/v1/auth/token/refresh/',
    me: '/api/v1/auth/me/',
  },
  accounts: {
    list: '/api/v1/accounts/',
    detail: (id: number) => `/api/v1/accounts/${id}/`,
  },
  contacts: {
    delegates: {
      list: '/api/v1/contacts/delegates/',
      detail: (id: number) => `/api/v1/contacts/delegates/${id}/`,
    },
    trainers: {
      list: '/api/v1/contacts/trainers/',
      detail: (id: number) => `/api/v1/contacts/trainers/${id}/`,
    },
    clientContacts: {
      list: '/api/v1/contacts/client-contacts/',
      detail: (id: number) => `/api/v1/contacts/client-contacts/${id}/`,
    },
  },
  clients: {
    list: '/api/v1/clients/',
    detail: (id: number) => `/api/v1/clients/${id}/`,
  },
  training: {
    courses: {
      list: '/api/v1/training/courses/',
      detail: (id: number) => `/api/v1/training/courses/${id}/`,
    },
    instances: {
      list: '/api/v1/training/instances/',
      detail: (id: number) => `/api/v1/training/instances/${id}/`,
    },
    bookings: {
      list: '/api/v1/training/bookings/',
      detail: (id: number) => `/api/v1/training/bookings/${id}/`,
    },
    modules: {
      detail: (id: number) => `/api/v1/training/modules/${id}/`,
    },
    assessments: {
      detail: (id: number) => `/api/v1/training/assessments/${id}/`,
    },
    feedback: {
      list: '/api/v1/training/feedback/',
    },
  },
  recruitment: {
    jobs: {
      list: '/api/v1/recruitment/jobs/',
      detail: (id: number) => `/api/v1/recruitment/jobs/${id}/`,
    },
    candidates: {
      list: '/api/v1/recruitment/candidates/',
      detail: (id: number) => `/api/v1/recruitment/candidates/${id}/`,
    },
    interviews: {
      list: '/api/v1/recruitment/interviews/',
      detail: (id: number) => `/api/v1/recruitment/interviews/${id}/`,
    },
    placements: {
      list: '/api/v1/recruitment/placements/',
      detail: (id: number) => `/api/v1/recruitment/placements/${id}/`,
    },
  },
  hr: {
    employees: {
      list: '/api/v1/hr/employees/',
      detail: (id: number) => `/api/v1/hr/employees/${id}/`,
    },
    dayRates: {
      list: '/api/v1/hr/day-rates/',
      detail: (id: number) => `/api/v1/hr/day-rates/${id}/`,
    },
    leave: {
      list: '/api/v1/hr/leave/',
      detail: (id: number) => `/api/v1/hr/leave/${id}/`,
    },
    timesheets: {
      list: '/api/v1/hr/timesheets/',
      detail: (id: number) => `/api/v1/hr/timesheets/${id}/`,
    },
  },
  marketing: {
    campaigns: {
      list: '/api/v1/marketing/campaigns/',
      detail: (id: number) => `/api/v1/marketing/campaigns/${id}/`,
    },
    newsletters: {
      list: '/api/v1/marketing/newsletters/',
      detail: (id: number) => `/api/v1/marketing/newsletters/${id}/`,
    },
    recipients: {
      list: '/api/v1/marketing/recipients/',
    },
    surveys: {
      list: '/api/v1/marketing/surveys/',
      detail: (id: number) => `/api/v1/marketing/surveys/${id}/`,
    },
  },
  documents: {
    list: '/api/v1/documents/',
    detail: (id: number) => `/api/v1/documents/${id}/`,
  },
  invoices: {
    list: '/api/v1/invoices/',
    detail: (id: number) => `/api/v1/invoices/${id}/`,
  },
  pages: {
    list: '/api/v1/pages/',
    detail: (id: number) => `/api/v1/pages/${id}/`,
    bySlug: (slug: string) => `/api/v1/pages/by-slug/${slug}/`,
  },
  dashboard: {
    stats: '/api/v1/dashboard/stats/',
  },
} as const;
