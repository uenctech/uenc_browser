<template>
  <div class="headertop">
    <div class="headerzong">
      <div class="header-left">
        <img src="@assets/images/header/logo.png" alt />
      </div>
      <ul class="header-right">
        <li
          @click="jump(index, item.title)"
          :class="{ active: cur == index }"
          v-for="(item, index) in nav"
          :key="index"
          class="lifirst"
        >
          <ul class="lili">
            <img src="@assets/images/header/按下.png" v-if="cur == index" />
            <div class="tuqi" v-else></div>
            <li>
              <img :src="item.src" />
              <span class="title">{{ item.title }}</span>
            </li>
          </ul>
        </li>
      </ul>
      <div
        class="searchlanguage"
        @mouseenter="switchLan()"
        @mouseleave="switchLan2()"
      >
        <img
          src="@assets/images/header/中英文.png"
          class="qiehuan"
          v-if="show"
        />
        <img src="@assets/images/header/中英文2.png" class="qiehuan2" v-else />
        <img
          src="@assets/images/header/right.png"
          class="righticon"
          v-if="show"
        />
        <span
          class="headerselect"
          v-loading.fullscreen.lock="fullscreenLoading"
          >{{ chose }}</span
        >
        <img
          src="@assets/images/header/right.png"
          class="righticon2"
          v-if="!show"
        />
        <ul class="language" v-if="!show">
          <li @click="chinese" v-loading.fullscreen.lock="fullscreenLoading">
            中文
          </li>
          <li @click="english" v-loading.fullscreen.lock="fullscreenLoading">
            EN
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import bus from "@/bus.js";
export default {
  name: "headertop",
  data() {
    return {
      fullscreenLoading: false,
      cur: 0,
      language: "",
      nowLang: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
    };
  },
  watch: {
    cur(e) {
      localStorage.setItem("cur", e);
    },
  },
  mounted() {},
  created() {
    this.nowLang = this.$i18n.locale;
    if (this.nowLang == "en") {
      this.chose = "language";
    }
    if (this.nowLang == "cn") {
      this.chose = "语言";
    }
    //console.log(this.nowLang);
    this.getSession();
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
      this.cur = index;
      //console.log(this.cur);
      sessionStorage.setItem("cur", index);
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
          case "图表":
            this.$router.push({
              name: "chart",
            });
            break;
          case "地址":
            this.$router.push({
              name: "addressed",
            });
            break;
          case "钱包":
            this.$router.push({
              name: "Fastoken",
            });
            break;
          // 英文路由
          case "home":
            this.$router.push({
              name: "index",
            });
            break;
          case "block":
            this.$router.push({
              name: "block",
            });
            break;
          case "transaction":
            this.$router.push({
              name: "transaction",
            });
            break;
          case "chart":
            this.$router.push({
              name: "chart",
            });
            break;
          case "address":
            this.$router.push({
              name: "addressed",
            });
            break;
          case "Fastoken":
            this.$router.push({
              name: "Fastoken",
            });
            break;
        }
      }
    },
    getSession() {
      this.cur = sessionStorage.getItem("cur");
    },
  },
};
</script>

<style lang="less">
.language {
  width: 50px;
  height: 50px;
  position: absolute;
  top: 91px;
  right: 68px;
  font-size: 18px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 25px;
  color: rgba(40, 96, 194, 1);
  opacity: 1;
  cursor: pointer;
  li {
    margin-top: 6px;
  }
}
.headerselect {
  position: absolute;
  top: 47px;
  right: 78px;
  font-size: 20px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 28px;
  color: rgba(40, 96, 194, 1);
  opacity: 1;
  cursor: pointer;
}
.righticon {
  position: absolute;
  right: 60px;
  width: 9px;
  height: 15px;
  top: 55px;
}
.righticon2 {
  position: absolute;
  right: 62px;
  width: 9px;
  height: 15px;
  top: 55px;
  transform: rotate(90deg);
}
.tuqi {
  width: 121px;
  height: 60px;
  position: absolute;
  top: 30px;
  background: rgba(234, 235, 243, 1);
  box-shadow: -5px -5px 15px rgba(255, 255, 255, 0.8);
  opacity: 1;
  border-radius: 16px;
}

// 头部
.headertop {
  width: 100%;
  height: 120px;
  position: relative;
  margin-top: 23px;
  margin-bottom: 42px;
  display: flex;
  flex-direction: row;
  .headerzong {
    width: 1200px;
    height: 120px;
    position: relative;
    background: rgba(234, 235, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    //头部左侧
    .header-left {
      position: relative;
      left: 13px;
      img {
      }
    }
    //头部右侧
    .header-right {
      width: 928px;
      position: relative;
      left: 31px;
      display: flex;
      flex-direction: row;
      align-items: center;
      .active {
      }
      .lifirst {
        width: 160px;
        height: 115px;
        line-height: 115px;
        font-size: 18px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 25px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
        cursor: pointer;
        display: flex;
        flex-direction: row;
        .lili {
          width: 121px;
          position: relative;
          line-height: 115px;
          display: flex;
          flex-direction: row;
          .title {
            position: absolute;
            left: 65px;
            top: 7px;
          }
          img {
            width: 121px;
            height: 60px;
            position: relative;
            top: 30px;
            // border: 1px solid red;
          }
          li img {
            position: absolute;
            left: 19px;
            width: 32px;
            height: 34.19px;
            top: 43px;
          }
        }
      }
    }
    // 选择语言
    .searchlanguage {
      width: 200px;
      height: 150px;
      position: relative;
      .qiehuan {
        position: absolute;
        right: 13px;
        top: 5px;
        cursor: pointer;
      }
      .qiehuan2 {
        position: absolute;
        right: 13px;
        top: 5px;
        cursor: pointer;
      }
    }
  }
}
</style>
