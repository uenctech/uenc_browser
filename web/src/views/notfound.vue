<template>
  <div class="notfound"  v-loading.fullscreen.lock="fullscreenLoading">
    <headertop></headertop>
    <div class="notzong">
      <!-- 搜索栏区域 -->
      <search></search>
      <div class="not">
        <img src="../assets/images/404/pr-04.png" alt="" />
        <p>{{ $t("notfound[0]") }}</p>
      </div>
      <v-footer></v-footer>
    </div>
  </div>
</template>

<script>
import Search from "@components/common/search.vue";
import VFooter from "@components/common/Footer.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "chart",
  data() {
    return {
      // 外部公共部分
      nowLang: "",

      fullscreenLoading: false,
      language: "",

      // 语言图片显示与隐藏

      choselanguage: ["中文", "EN"],
    };
  },
  components: { VFooter, Search, headertop },
  beforeDestory() {},
  created() {
    this.nowLang = this.$i18n.locale;
  },
  methods: {},
};
</script>

<style lang="less">
// 本页面
.notfound {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  margin-bottom: 20px;
  border-radius: 40px;
  .notzong {
    width: 1200px;
    height: 880px;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
  }
  .not {
    width: 1120px;
    height: 660px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    img {
      width: 533.38px;
      height: 400px;
      position: relative;
      left: 295px;
      top: 80px;
    }
    p {
      position: relative;
      left: 400px;
      top: 101px;
    }
  }
}
</style>
