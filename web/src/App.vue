<template>
  <div id="app">
    <keep-alive>
    <router-view v-if="$route.meta.keepAlive"></router-view>
</keep-alive>
<router-view v-if="!$route.meta.keepAlive">
    <!--因为用的是v-if 所以下面还要创建一个未缓存的路由视图出口-->
</router-view>
  </div>
</template>

<style lang="less">
// @import "./assets/common/element-ui-2.4.11theme-chalkindex.css";
a {
  text-decoration: none;
}
.vue-particles {
  // z-index: 1;
}
</style>
<script>
export default {
  mounted() {
    // 检测浏览器路由改变页面不刷新问题,hash模式的工作原理是hashchange事件
    window.addEventListener(
      "hashchange",
      () => {
        let currentPath = window.location.hash.slice(1);
        //console.log(currentPath);
        if (this.$route.path !== currentPath) {
          this.$router.push(currentPath);
        }
      },
      false
    );
  },
};
</script>
