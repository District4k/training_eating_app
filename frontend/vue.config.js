const path = require('path');

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://backend:8885',
        changeOrigin: true
      }
    }
  },
  transpileDependencies: [
    'vuetify'
  ],
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
};
