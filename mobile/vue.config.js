const webpack = require("webpack");
const path = require("path");
 const UglifyPlugin = require('uglifyjs-webpack-plugin');
const CompressionPlugin = require("compression-webpack-plugin");
const AddAssetHtmlPlugin = require("add-asset-html-webpack-plugin");
let { version, version_lib, openGzip, library } = require("./package.json");
module.exports = {
  publicPath: "./", // 基本路径
  outputDir: "en", // 输出文件目录
  assetsDir: "static",
  lintOnSave: false, // eslint-loader 是否在保存的时候检查
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md
  // webpack配置

  chainWebpack: config => {
    config.module
      .rule('iview')
      .test(/iview.src.*?js$/)
      .use('babel')
      .loader('babel-loader')
      .end()

    // 修复HMR
    config.resolve.symlinks(true);
    // 别名配置
    config.resolve.alias
      .set("@", path.resolve(__dirname, "./src"))
      .set("@assets", path.resolve(__dirname, "./src/assets"))
      .set("@network", path.resolve(__dirname, "./src/network"))
      .set("@components", path.resolve(__dirname, "./src/components"))
      .set("@views", path.resolve(__dirname, "./src/views"))
      .set("@store", path.resolve(__dirname, "./src/store"))

  },
  configureWebpack: {
    externals: {
      'vue': 'Vue',
      'vue-router': 'VueRouter',
      'element-ui': 'ELEMENT',
      'axios': 'axios'
    },
    plugins: [
      new webpack.ProvidePlugin({
        jQuery: "jquery",
        $: "jquery",
        "windows.jQuery": "jquery"
      }),
      new UglifyPlugin({
        uglifyOptions: {
          compress: {
            drop_debugger: true,
            drop_console: true,  //生产环境自动删除console
          },
          warnings: false,
        },
        sourceMap: false,
        parallel: true,//使用多进程并行运行来提高构建速度。默认并发运行数：os.cpus().length - 1。
      })
      // gzip压缩
      // new CompressionPlugin({
      //   test: /\.(js|css)(\?.*)?$/i,//需要压缩的文件正则
      //   threshold: 10240,//文件大小大于这个值时启用压缩
      //   deleteOriginalAssets: false//压缩后保留原文件
      // })
    ],

  },

  productionSourceMap: false, // 生产环境是否生成 sourceMap 文件
  parallel: require("os").cpus().length > 1, // 是否为 Babel 或 TypeScript 使用 thread-loader。该选项在系统的 CPU 有多于一个内核时自动启用，仅作用于生产构建。
  pwa: {
    iconPaths: {
      favicon32: "favicon.ico",
      favicon16: "favicon.ico",
      appleTouchIcon: "favicon.ico",
      maskIcon: "favicon.ico",
      msTileImage: "favicon.ico"
    }
  }, // PWA 插件相关配置 see https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
  // webpack-dev-server 相关配置
  devServer: {
    open: true,
    host: "0.0.0.0", // 允许外部ip访问
    port: 8080, // 端口
    https: false, // 启用https
    overlay: {
      warnings: true,
      errors: true
    }, // 错误、警告在页面弹出
    proxy: {
      "/api": {
        target: `http://www.baidu.com`,
        changeOrigin: true, // 允许websockets跨域
        // ws: true,
        pathRewrite: {
          "^/api": ""
        }
      }
    } // 代理转发配置，用于调试环境
  }, // 第三方插件配置
  pluginOptions: {}
};
