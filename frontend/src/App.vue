<template>
  <v-app>
    <!-- Navbar -->
    <NavBarComponent />

    <!-- Main Content -->
    <v-main>
      <v-container>
        <router-view /> <!-- Dynamically load the view based on the route -->
      </v-container>
    </v-main>

    <!-- Footer -->
    <FooterComponent />
  </v-app>
</template>

<script>
import NavBarComponent from "@/components/NavBarComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: 'App',
  components: { NavBarComponent, FooterComponent },
};
</script>

<style scoped>
.v-app {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Make sure the app takes full height */
}

.v-main {
  flex-grow: 1; /* Allow the content to grow and take the available space */
  padding-top: 64px; /* Ensure the content starts below the fixed navbar */
}

footer {
  margin-top: auto; /* Push the footer to the bottom */
}
</style>
