<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card>
          <v-card-title class="headline">Login</v-card-title>
          <v-form v-model="valid" @submit.prevent="submitForm">
            <v-text-field
              v-model="username"
              label="Username or Email"
              :rules="usernameRules"
              required
              outlined
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              :rules="passwordRules"
              required
              outlined
            ></v-text-field>
            <v-btn :disabled="!valid" color="primary" type="submit" block>
              Login
            </v-btn>
          </v-form>
          <v-divider></v-divider>
          <v-btn text @click="navigateToRegister" block>
            Don't have an account? Register
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      valid: false,
      usernameRules: [
        v => !!v || "Username or Email is required",
        v => /.+@.+\..+/.test(v) || "Enter a valid email",
      ],
      passwordRules: [
        v => !!v || "Password is required",
        v => v.length >= 6 || "Password must be at least 6 characters",
      ],
    };
  },
  setup() {
    const router = useRouter();

    const navigateToRegister = () => {
      router.push("/register");
    };

    const submitForm = () => {
      // Handle the login logic here (e.g., API call)
      alert("Login successful!");
    };

    return {
      navigateToRegister,
      submitForm,
    };
  },
};
</script>

<style scoped>
.v-card {
  max-width: 400px; /* Limit card width on larger screens */
  margin: 0 auto;
}

.v-btn {
  font-size: 16px; /* Ensure buttons are large enough */
}

.v-text-field input {
  font-size: 16px; /* Make sure input text is readable */
}
</style>
