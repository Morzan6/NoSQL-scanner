const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    redirect: !localStorage.getItem("access_token") ? "/auth" : "/dashboard",
    children: [
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
        component: () =>
          !localStorage.getItem("access_token")
            ? import("pages/LoginFirst.vue")
            : import("pages/scanspage/index.vue"), // ternator to "Login first" page
      },
      {
        path: "/dashboard",
        component: () => 
        !localStorage.getItem("access_token")
            ? import("pages/LoginFirst.vue")
            : import("pages/dashboard/index.vue"), // ternator to "Login first" page
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
