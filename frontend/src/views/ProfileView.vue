<template>
  <v-container>
    <v-row class="profile-header">
      <v-col>
        <h1>User Profile</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="6">
        <v-card outlined>
          <v-card-title>Profile Information</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Name:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.name }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Surname:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.surname }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Birthday:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.birthday }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Weight:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.weight }} kg</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Height:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.height }} cm</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Email:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title><strong>Telephone:</strong></v-list-item-title>
                  <v-list-item-subtitle>{{ user.tel }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <!-- Edit Button -->
            <v-btn @click="isEditMode = true" color="primary" class="mt-4">Edit Profile</v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Edit Profile Form -->
    <v-row v-if="isEditMode">
      <v-col cols="12" sm="6">
        <v-card outlined>
          <v-card-title>Edit Profile Information</v-card-title>
          <v-card-text>
            <v-form v-model="valid" @submit.prevent="submitForm">
              <v-text-field
                v-model="user.name"
                label="Name"
                :rules="nameRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.surname"
                label="Surname"
                :rules="surnameRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.birthday"
                label="Birthday"
                type="date"
                :rules="birthdayRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.weight"
                label="Weight (kg)"
                type="number"
                :rules="weightRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.height"
                label="Height (cm)"
                type="number"
                :rules="heightRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.email"
                label="Email"
                type="email"
                :rules="emailRules"
                required
                outlined
              ></v-text-field>
              <v-text-field
                v-model="user.tel"
                label="Telephone"
                type="tel"
                :rules="telRules"
                required
                outlined
              ></v-text-field>
              <v-btn :disabled="!valid" color="primary" type="submit" block>
                Save Changes
              </v-btn>
              <v-btn @click="isEditMode = false" color="secondary" block>Cancel</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'ProfileView',
  data() {
    return {
      user: {
        name: 'John',
        surname: 'Doe',
        birthday: '1990-01-01',
        weight: 85,
        height: 183,
        email: 'john.doe@example.com',
        tel: '+123456789',
      },
      isEditMode: false,
      valid: false,
      // Validation rules for form fields
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 50) || 'Name must be less than 50 characters',
      ],
      surnameRules: [
        v => !!v || 'Surname is required',
        v => (v && v.length <= 50) || 'Surname must be less than 50 characters',
      ],
      birthdayRules: [
        v => !!v || 'Birthday is required',
      ],
      weightRules: [
        v => !!v || 'Weight is required',
        v => (v && v > 0) || 'Weight must be a positive number',
      ],
      heightRules: [
        v => !!v || 'Height is required',
        v => (v && v > 0) || 'Height must be a positive number',
      ],
      emailRules: [
        v => !!v || 'Email is required',
        v => /.+@.+\..+/.test(v) || 'Enter a valid email',
      ],
      telRules: [
        v => !!v || 'Telephone is required',
        v => /^\+?[0-9]{1,4}?[-.●]?\(?[0-9]{1,3}?\)?[-.●]?[0-9]{1,4}[-.●]?[0-9]{1,4}[-.●]?[0-9]{1,9}$/.test(v) || 'Enter a valid telephone number',
      ],
    };
  },
  methods: {
    submitForm() {
      // Handle saving profile changes (e.g., API call)
      alert('Profile updated successfully!');
      this.isEditMode = false;
    },
  },
};
</script>

<style scoped>
.profile-header {
  text-align: center;
  margin-bottom: 20px;
}
</style>
