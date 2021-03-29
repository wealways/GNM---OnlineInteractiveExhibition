module.exports = {
  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: true
    }
  },
  transpileDependencies: [
    'quasar'
  ],
  devServer: {
    // host: '0.0.0.0',
    // hot: true,
    // disableHostCheck: true,
    proxy:'http://localhost:8000'
  },
}
