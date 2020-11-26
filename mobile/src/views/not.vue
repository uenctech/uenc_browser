<template>
  <div class="notfound">
    <div class="headertop" :class="{ sticky2: sticky2 }">
      <img
        src="@assets/images/transaction/组 202.png"
        @click="returnBack"
        id="slideleft"
      />
      <p class="header_title">{{ $t("home.cardleft[4]") }}</p>
      <div id="topbutton">
        <img
          src="@assets/images/index/组 3.png"
          @click="openPop"
          id="slideright"
        />
        <div class="buttonline"></div>
        <img
          src="@assets/images/index/组 253.png"
          id="slideright2"
          @click="callBack"
        />
      </div>
      <van-popup
        v-model="show_silde"
        position="top"
        :overlay="true"
        overlay-class="popstyle"
      >
        <img src="@assets/images/index/关闭.png" @click="closePop" />
        <ul class="title_list">
          <li
            @click="jump(index, item.title)"
            :class="{ active: cur == index }"
            v-for="(item, index) in nav"
            :key="index"
          >
            <img :src="item.src2" v-if="cur == index" />
            <img :src="item.src" v-else />

            <p>
              {{ item.title }}
            </p>
          </li>
        </ul>
      </van-popup>
    </div>
    <v-search @test="ceshi"></v-search>
    <div class="not">
      <img src="@assets/images/404/组 222.png" class="notimg" />
      <p>{{ $t("notfound[1]") }}</p>
    </div>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
export default {
  name: "chart",
  data() {
    return {
      show_silde: false,
      sticky2: false,
      // 外部公共部分
      nowLang: "",
      cur: "",
      fullscreenLoading: false,
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
    };
  },
  components: { vSearch },
  created() {
   
    this.nowLang = this.$i18n.locale;
    if (this.nowLang == "en") {
      this.chose = "lan";
    }
    if (this.nowLang == "cn") {
      this.chose = "语言";
    }
    this.cur = 3;
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeRouteEnter(to, from, next) {
    // console.log('去的地方'+to.name);
    // console.log('来的地方'+from.name);
    localStorage.setItem("toname", to.name);
    localStorage.setItem("fromname", from.name);
    next();
  },
  computed: {
    nav: {
      get() {
        let navE = this.$t("nav");
        return navE;
      },
      set() {},
    },
  },
  methods: {
    callBack() {
      var u = navigator.userAgent;
      var isAndroid = u.indexOf("Android") > -1 || u.indexOf("Adr") > -1; //android终端
      var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/); //ios终端
      try {
        if (isiOS) {
          // console.log("ios");
          window.webkit.messageHandlers.returnBack.postMessage("ok");
        }
        if (isAndroid) {
         window.android.back();
          // console.log("android");
          // window.android.setUrl("http://www.uenc.io/");
        }
      } catch (e) {
        // console.log("出现错误, 如果在非android环境下访问, 出现该警告是正常的.");
      }
    },
    ceshi(msg) {
      //  console.log(msg);
    },
    returnBack() {
      // if (localStorage.getItem("fromname") == "index") {
      //   console.log(window.location.href + "回到首页");
      //   try {
      //     window.webkit.messageHandlers.returnBack.postMessage("ok");
      //   } catch (e) {
      //     console.log(
      //       "出现错误, 如果在非android环境下访问, 出现该警告是正常的."
      //     );
      //   }
      // }
      this.$router.go(-1);
    },
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
    },
    // 滚动固定区域
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      // console.log(scrollTop);
      if (scrollTop > 0) {
        this.sticky2 = true;
      }
      if (scrollTop < 10) {
        this.sticky2 = false;
      }

      // console.log(scrollTop);
    },
    // 外部公共部分
    chinese() {
      this.fullscreenLoading = true;
      this.$i18n.locale = "cn";
      localStorage.setItem("lang", "cn");
      setTimeout(() => {
        this.$router.go(0);
      }, 1500);
    },
    english() {
      this.fullscreenLoading = true;
      this.$i18n.locale = "en";
      localStorage.setItem("lang", "en");
      setTimeout(() => {
        this.$router.go(0);
      }, 1500);
    },
    switchLan2() {
      this.show = true;
    },
    // 选择语言
    switchLan() {
      this.show = !this.show;
    },
    // 页面的切换选择
    jump(index, title) {
      this.cur = 3;
      let localPath = this.$route.path;
      if (localPath != "/d") {
        switch (title) {
          case "首页":
            this.$router.push({
              name: "index",
            });
            break;
          case "区块":
            this.$router.push({
              name: "block",
            });
            break;
          case "交易":
            this.$router.push({
              name: "transaction",
            });
            break;

          case "地址":
            this.$router.push({
              name: "addressed",
            });
            break;

          // 英文路由
          case "Home":
            this.$router.push({
              name: "index",
            });
            break;
          case "Block":
            this.$router.push({
              name: "block",
            });
            break;
          case "Trans":
            this.$router.push({
              name: "transaction",
            });
            break;

          case "Address":
            this.$router.push({
              name: "addressed",
            });
            break;
        }
      }
    },
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>

<style lang="less">
.notfound {
  width: 100%;
  height: auto;
  min-height: 100vh;
  position: relative;
  background: #f5f5f5;
  .not {
    width: 250px;
    height: 188px;
    margin: 0 auto;
    margin-top: 103px;
    .notimg {
      width: 100%;
      height: 100%;
    }
    p {
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      color: #333333;
      opacity: 1;
    }
  }
}
</style>
