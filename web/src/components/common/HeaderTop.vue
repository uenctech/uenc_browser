<template>
  <div class="headertop" :class="{ sticky: sticky }">
    <div class="headerzong">
      <div class="header-left">
        <img src="@assets/images/header/logo.png" />
      </div>
      <ul class="header-right">
        <li
          v-for="(item, i) in nav"
          :class="{ nav_li: active === i }"
          :key="i"
          @click="gorouter(item.path)"
          class="lifirst"
        >
          <ul class="lili">
            <img
              src="@assets/images/header/按下.png"
              v-if="active == i"
              class="anxia"
            />
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
import cn from "../../i18n/cn";
import en from "../../i18n/en";
export default {
  name: "headertop",
  data() {
    return {
      active: "",
      fullscreenLoading: false,
      nav: [],
      sticky: false,
      show: true,
      nowLang: "",

      chose: "",
    };
  },
  created() {
    this.nowLang = this.$i18n.locale;

    // console.log(this.nowLang);
    if (this.nowLang === "cn") {
      this.nav = cn.nav;
      this.chose = "语言";
    }
    if (this.nowLang === "en") {
      this.nav = en.nav;
      this.chose = "lan";
    }
    this.nav.forEach((v, i) => {
      //  console.log(this.active);
      //  console.log(i);
      // console.log(v.path);
      // console.log(this.$route.path);
      if (this.$route.path == "/transactiondetail") {
        this.active = 2;
      }
      if (this.$route.path == "/transactiondetails") {
        this.active = 2;
      }
      if (this.$route.path == "/blockdetail") {
        this.active = 1;
      }
      if (this.$route.path == "/blockdetails") {
        this.active = 1;
      }
      if (this.$route.path == "/notfound") {
        this.active = 10;
      }
      // console.log(this.$route.path);
      if (v.path === this.$route.path) {
        this.active = i;
      }
    });
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },

  methods: {
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 0) {
        this.sticky = true;
      }
      if (scrollTop < 10) {
        this.sticky = false;
      }
      // console.log(scrollTop);
    },
    gorouter(index) {
      this.$router.push({ path: index });
    },
    switchLan2() {
      this.show = true;
    },
    // 选择语言
    switchLan() {
      this.show = !this.show;
    },
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
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>

<style lang="less">
.tuqi {
  width: 136px !important;
  height: 60px;
  position: absolute;
  top: 30px;
  // background: rgba(234, 235, 243, 0.8);
  box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8);
  border-radius: 16px;
}
.sticky {
  width: 1200px !important;
  height: 120px !important;
  position: fixed !important;
  top: 0px !important;
  margin: 0 auto !important;
}
// 外部头部区域
li {
  list-style: none;
}

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
.anxia {
  width: 136px !important;
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
  z-index: 40;

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
      left: 21px;
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
          width: 136px;
          position: relative;
          line-height: 115px;
          display: flex;
          flex-direction: row;

          .title {
            position: absolute;
            left: 55px;
            top: 7px;
          }

          img {
            width: 136px;
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
