<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<style lang="less">
@import "./assets/css/header.less";
@import "./assets/css/ivew.css";
a {
  text-decoration: none;
}
#app {
  background-color: #f5f5f5;
  padding-top: 38px;
}
.vue-particles {
  // z-index: 1;
}
</style>
<script>
export default {
  data() {
    return {};
  },
  methods: {},
  mounted() {
    // 检测浏览器路由改变页面不刷新问题,hash模式的工作原理是hashchange事件
    //   window.addEventListener(
    //     "hashchange",
    //     () => {
    //       let currentPath = window.location.hash.slice(1);
    //       //console.log(currentPath);
    //       if (this.$route.path !== currentPath) {
    //         this.$router.push(currentPath);
    //       }
    //     },
    //     false
    //   );
  },
  // 回到顶部
  watch: {
    $route: function(to, from) {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    },
  },
};
</script>
