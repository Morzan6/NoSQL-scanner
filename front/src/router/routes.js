const routes = [
  {
    path: '/scan',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/auth', component: () => import('pages/authpage/index.vue') },
      { path: '/scan', component: () => import('pages/scanspage/index.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
