module.exports = {
  // 상대경로로 지정
  publicPath: '',
  // 음성파일 저장위치 변경
  chainWebpack: config => {
    config.module
      .rule('media')
      .use('url-loader')
      .tap(options => {
        options['fallback']['options']['name'] = 'sound/[name].[hash:8].[ext]'
        return options
      })
  },
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
    host: '0.0.0.0',
    hot: true,
    disableHostCheck: true,
    // proxy:'http://localhost:8000'
  },
}