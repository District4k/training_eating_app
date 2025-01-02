<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card>
          <v-card-title class="headline">Register</v-card-title>
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
            <v-text-field
              v-model="confirmPassword"
              label="Confirm Password"
              type="password"
              :rules="confirmPasswordRules"
              required
              outlined
            ></v-text-field>
            <v-btn :disabled="!valid" color="primary" type="submit" block>
              Register
            </v-btn>
          </v-form>
          <v-divider></v-divider>
          <v-btn text @click="navigateToLogin" block>
            Already have an account? Login
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useRouter } from "vue-router";

export default {
    name: "Register",
    data() {
        return {
            username: "",
            password: "",
            confirmPassword: "",
            valid: false,
            usernameRules: [
                v => !!v || "Username or Email is required",
                v => /.+@.+\..+/.test(v) || "Enter a valid email",
            ],
            passwordRules: [
                v => !!v || "Password is required",
                v => v.length >= 6 || "Password must be at least 6 characters",
            ],
            confirmPasswordRules: [
                v => !!v || "Please confirm your password",
                v => v === this.password || "Passwords do not match",
            ],
        };
    },
    setup() {
        const router = useRouter();

        const navigateToLogin = () => {
            router.push("/login");
        };

        const submitForm = () => {
            // Handle the registration logic here (e.g., API call)
            alert("Registration successful!");
        };

        return {
            navigateToLogin,
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
