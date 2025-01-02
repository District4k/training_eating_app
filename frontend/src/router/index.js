import { createRouter, createWebHistory } from "vue-router";
import App from "@/App.vue";  // App.vue as the parent layout
import Main from "@/MainLayer.vue"; // Main component that will render the routed components
import Login from "@/views/LoginView.vue";
import Register from "@/views/RegisterView.vue";
import ForgotPassword from "@/views/ForgotPasswordView.vue";
import Profile from "@/views/ProfileView.vue";
import ResetPassword from "@/views/ResetPasswordView.vue";
import SignUp from "@/views/SignUpView.vue";

const routes = [
  {
    path: "/",
    component: App, // App.vue as the parent layout
    children: [
      {
        path: "",
        component: Main, // MainLayer.vue as a child of App, rendering the routed components
        children: [
          { path: "login", name: "Login", component: Login },
          { path: "register", name: "Register", component: Register },
          { path: "forgotpassword", name: "ForgotPassword", component: ForgotPassword },
          { path: "profile", name: "Profile", component: Profile },
          { path: "resetpassword", name: "ResetPassword", component: ResetPassword },
          { path: "signup", name: "SignUp", component: SignUp },
        ],
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
