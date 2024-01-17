const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    redirect: "/dashboard",
    children: [
      {
        path: "/403",
        component: () => import("pages/LoginFirst.vue"),
      },
      {
        path: "/auth",
        component: () => import("pages/authpage/index.vue"),
        beforeEnter: (to, from, next) => {
          if (localStorage.getItem("access_token")) {
            next("/dashboard");
          } else {
            next();
          }
        },
      },
      {
        path: "/scans",
        component: () => import("pages/scanspage/index.vue"), // ternator to "Login first" page
      },
      {
        path: "/dashboard",
        component: () => import("pages/dashboard/index.vue"), // ternator to "Login first" page
      },
      {
        path: "/report/:id",
        component: () => import("pages/reportpage/index.vue"),
        props: true,
      },
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
