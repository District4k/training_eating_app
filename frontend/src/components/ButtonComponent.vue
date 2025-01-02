<template>
  <v-btn :color="color" :disabled="disabled" @click="onClick">
    <slot></slot> <!-- Slot allows you to pass custom content inside the button -->
  </v-btn>
</template>

<script>
export default {
  name: "ButtonComponent",
  props: {
    color: {
      type: String,
      default: "primary", // Default button color
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    onClick() {
      this.$emit("click"); // Emit click event for external handling
    },
  },
};
</script>

<style scoped>
/* Optional custom styling */
</style>
