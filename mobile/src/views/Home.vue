<template>
  <div class="home">
    <!-- <back-top></back-top> -->
    <!-- <header-top></header-top> -->
    <keep-alive v-if="$route.meta.keepAlive && isRouterAlive">
      <router-view> </router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive">
      <!-- 这里是不被缓存的视图组件 -->
    </router-view>
    <!-- <v-footer></v-footer> -->
  </div>
</template>

<script>
// import headerTop from "@components/content/HeaderTop.vue";
// import BackTop from "@components/common/BackTop.vue";
//import VFooter from "@components/common/Footer.vue";
export default {
  name: "Home",
  data() {
    return { isRouterAlive: true };
  },
  provide() {
    return {
      reload: this.reload,
    };
  },
  components: {
    //  headerTop,
    //VFooter
  },
  created() {},
  mounted() {},
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(function() {
        this.isRouterAlive = true;
      });
    },
  },
};
</script>
<style lang="less">
.home {
  font-size: 16px;
  height: 100%;
  // z-index: 3;
}
</style>
