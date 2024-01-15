const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/auth", 
        component: () => import("pages/authpage/index.vue"),
        beforeEnter: (to, from, next) => {
          if (localStorage.access_token) {
            next('/dashboard');
          } else {
            next();
          }
        },
      },
      { path: "/scan", component: () => import("pages/scanspage/index.vue") },
      { path: "/dashboard", component: () => import("pages/dashboard/index.vue") },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
