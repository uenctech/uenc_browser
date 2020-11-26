<template>
  <div class="wallet">
   <headertop></headertop>
    <div class="walletzong">
      <!-- 搜索栏区域 -->
      <search></search>
      <div class="walletcontent">
        <span class="span1">
          {{ $t("wallet[0]") }}
        </span>
        <img src="../assets/images/wallet/组 57.png" class="erwei" />
        <img
          src="../assets/images/wallet/手机样机-酷豆旗舰店-002.png"
          class="walletimg1"
        />
        <img
          src="../assets/images/wallet/手机样机-酷豆旗舰店-020.png"
          class="walletimg2"
        />
        <span class="span2">
          {{ $t("wallet[1]") }}
        </span>
        <span class="span3">
          {{ $t("wallet[2]") }}
        </span>
        <img
          src="../assets/images/wallet/手机样机-酷豆旗舰店-021.png"
          class="walletimg3"
        />
      </div>
      <v-footer></v-footer>
    </div>
  </div>
</template>

<script>
import VFooter from "@components/common/Footer.vue";
import Search from "@components/common/search.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "wallet",
  data() {
    return {
     

      // 外部公共部分
      fullscreenLoading: false,
     
      language: "",
      nowLang: "",
     
      // 语言图片显示与隐藏
     
      count: this.$store.state.count,
    };
  },
  components: { VFooter, Search,headertop },
  created() {
    this.nowLang = this.$i18n.locale;
   
    
  },
  mounted() {
   
  },
 
  methods: {
   
    
  },
  destroyed() {
 
  },
};
</script>
<style lang="less">

// 本页面
.wallet {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  .walletzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }

  .walletcontent {
    width: 1120px;
    height: 1948px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    position: relative;
    .span1 {
      position: absolute;
      left: 80px;
      top: 117px;
      font-size: 40px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 56px;
      color: rgba(51, 51, 51, 1);
    }
    .span2 {
      width: 411px;
      height: 90px;
      position: absolute;
      left: 589px;
      top: 746px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 30px;
      color: rgba(51, 51, 51, 1);
    }
    .span3 {
      width: 411px;
      height: 90px;
      position: absolute;
      left: 80px;
      top: 1460px;
      width: 421px;
      height: 179px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 30px;
      color: rgba(51, 51, 51, 1);
    }
    .erwei {
      position: absolute;
      left: 71px;
      top: 214px;
    }
    .walletimg1 {
      position: absolute;
      left: 469px;
      top: 30px;
    }
    .walletimg2 {
      position: absolute;
      left: 70px;
      top: 668px;
    }
    .walletimg3 {
      position: absolute;
      left: 562px;
      top: 1305px;
    }
  }
}

</style>
