<template>
    <v-app-bar app>
        <v-toolbar-title>My Gym App</v-toolbar-title>
        <v-spacer></v-spacer>
        <template v-if="!isAuthenticated">
            <v-btn text @click="navigateToLogin">Login</v-btn>
            <v-btn text @click="navigateToRegister">Register</v-btn>
        </template>
        <template v-else>
            <v-btn text @click="navigateToProfile">Profile</v-btn>
            <v-btn text @click="logout">Logout</v-btn>
        </template>
        <v-btn icon @click="toggleDrawer">
            <v-icon>mdi-menu</v-icon>
        </v-btn>
    </v-app-bar>
</template>

<script>
import {Router} from "@/router/router";

export default {
    name: "NavBarComponent",
    props: {
        isAuthenticated: {
            type: Boolean,
            default: false,
        },
    },
    setup(props, ctx) {
        const router = Router(); // Access router using the useRouter hook

        const toggleDrawer = () => {
            ctx.$emit("toggle-drawer");
        };

        const navigateToLogin = () => {
            router.push("/login"); // Use router.push to navigate
        };

        const navigateToRegister = () => {
            router.push("/register");
        };

        const navigateToProfile = () => {
            router.push("/profile");
        };

        const logout = () => {
            ctx.$emit("logout"); // Emit logout event
        };

        return {
            toggleDrawer,
            navigateToLogin,
            navigateToRegister,
            navigateToProfile,
            logout,
        };
    },
};
</script>

<style scoped>
/* Optional custom styling for Navbar */
</style>

