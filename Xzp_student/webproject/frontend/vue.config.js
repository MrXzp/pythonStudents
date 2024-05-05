module.exports = {
  // 配置开发服务器
  devServer: {
    port: 8088, // 设置开发服务器端口号为 8080
    proxy: {
      // 设置代理，解决跨域请求问题
      '/api': {
        target: 'http://127.0.0.1:8000/', // 将请求代理到本地的 3000 端口
        changeOrigin: true, // 允许跨域
        pathRewrite: {
          '^/api': '' // 将请求路径中的 '/api' 替换为空
        }
      }
    }
  },
  // 配置构建输出目录
  outputDir: 'dist', // 设置构建输出目录为 dist 文件夹
  // 其他配置项...
};
