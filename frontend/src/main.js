import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Vuetify
import 'vuetify/styles'; // Global styles
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// Global Styles
import '@/assets/styles.scss';

// Create Vuetify instance
const vuetify = createVuetify({
  components,
  directives,
});

// Create and mount the Vue app
const app = createApp(App);

// Use the router and Vuetify plugin
app.use(router);
app.use(vuetify);

// Mount the app
app.mount('#app');
