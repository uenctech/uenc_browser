<template>
  <div class="block" v-loading.fullscreen.lock="fullscreenLoading">
    <div class="headertop" :class="{ sticky2: sticky2 }">
      <img
        src="@assets/images/transaction/组 202.png"
        @click="returnBack"
        id="slideleft"
      />
      <p class="header_title">{{ $t("nav[1].title") }}</p>
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
        <!-- <button
          @click="languageSelect"
          style="
            width: 50px;
            height: 20px;
            position: absolute;
            right: 0px;
            line-height: 20px;
            background: white;
            border: none;
          "
        >
          中/En
        </button> -->
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
    <v-search></v-search>

    <van-list
      v-model="listloading2"
      :finished="finished2"
      :immediate-check="false"
      :finished-text="finishedtext"
      @load="onLoad2"
      :offset="20"
      :loading-text="loadingtext"
    >
      <van-cell
        v-for="item in translist2"
        :key="item.id"
        class="vancell2"
        @click="gotoblockdetail(item.block_height)"
      >
        <img src="@assets/images/index/-s-组 1.png" />
        <div class="pdetail2">
          <p>
            <span> {{ $t("publicsection[12]") }}:</span
            ><span>{{ item.block_height }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[8]") }}:</span
            ><span>{{ item.block_time }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[4]") }}:</span
            ><span>{{ item.transaction_num }}</span>
          </p>
        </div>
      </van-cell>
    </van-list>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
export default {
  name: "transaction",
  data() {
    return {
      loadingtext: "",
      finishedtext: "",
      translist2: [],
      listloading2: false,
      finished2: false,
      blockmedianum: 1, //请求第几页
      pageSize2: 5, //每页请求的数量
      total2: "", //总共的数据条数
      loading: true,
      sticky2: false,
      tables: false,
      show_silde: false,
      // 外部公共部分
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      nowLang: "",
      cur: "",
      fullscreenLoading: true,
      scroll: "",
    };
  },
  // 页码设置
  watch: {},
  components: { vSearch },
  created() {

    this.nowLang = this.$i18n.locale;
    this.cur = 1;
    this.blocklist();
    if (this.nowLang == "en") {
      this.finishedtext = "Can't load more";
      this.loadingtext = "Loading...";
    }
    if (this.nowLang == "cn") {
      this.finishedtext = "无法加载更多";
      this.loadingtext = "加载中...";
    }
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeRouteEnter(to, from, next) {
    // console.log('去的地方'+to.name);
    // console.log("来的地方" + from.name);
    localStorage.setItem("toname", to.name);
    localStorage.setItem("fromname", from.name);
    next();
  },
  methods: {
     languageSelect() {
      if (this.nowLang == "cn") {
        this.$i18n.locale = "en";
        localStorage.setItem("lang", "en");
        this.reload();
      } else if (this.nowLang == "en") {
        this.$i18n.locale = "cn";
        localStorage.setItem("lang", "cn");
        this.reload();
      }
    },
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
    // 跳转块详情页
    gotoblockdetail(e) {
      //  console.log(e);
      this.$router.push({
        path: "/blockdetail",
        query: { blockheight: e },
      });
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
    onLoad2() {
      this.blockmedianum += 1;
      if (this.blockmedianum < this.total2) {
        this.blocklist();
      } else {
        return false;
      }
    },
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
    },
    //获取MEDIA
    async blocklist() {
      let that = this;
      await that.$http
        .get("/get_block_list_for_all", {
          params: {
            pageNum: this.blockmedianum,
            pageSize: 10,
          },
        })
        .then((res) => {
          // console.log(res);
          this.fullscreenLoading = false;
          this.listloading2 = false;
          this.total2 = res.data[0].total_page[0].totalPageNum;
          // console.log(this.total2);
          this.translist2 = this.translist2.concat(res.data[0].block_list);
          if (this.nowLang == "cn") {
            for (let i = 0; i < res.data[0].block_list.length + 1; i++) {
              let times = [];
              let blocktime = res.data[0].block_list[i].block_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].block_list[i].block_time = "刚刚";
                } else {
                  res.data[0].block_list[i].block_time = fenzhong + "分钟前";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].block_list[i].block_time =
                  parseInt(fenzhong / 60) + "小时前";
              }
              if (fenzhong > 1440) {
                res.data[0].block_list[i].block_time =
                  parseInt(fenzhong / 1440) + "天前";
              }
            }
          } else {
            for (let i = 0; i < res.data[0].block_list.length + 1; i++) {
              let times = [];
              let blocktime = res.data[0].block_list[i].block_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].block_list[i].block_time = "Just";
                } else {
                  res.data[0].block_list[i].block_time =
                    fenzhong + "Minutes ago";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].block_list[i].block_time =
                  parseInt(fenzhong / 60) + "Hours ago";
              }
              if (fenzhong > 1440) {
                res.data[0].block_list[i].block_time =
                  parseInt(fenzhong / 1440) + "Days ago";
              }
            }
          }
        })
        .catch((e) => {});
    },
    // 页面的切换选择
    jump(index, title) {
      this.cur = 1;
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
    // 滚动固定区域
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      this.scroll = scrollTop;
      // console.log(scrollTop);
      if (scrollTop > 0) {
        this.sticky2 = true;
      }
      if (scrollTop < 10) {
        this.sticky2 = false;
      }
    },
    //给sessionStorage存值,分页返回时准确位置
    setContextData: function(key, value) {
      if (typeof value == "string") {
        sessionStorage.setItem(key, value);
      } else {
        sessionStorage.setItem(key, JSON.stringify(value));
      }
    },
    // 从sessionStorage取值
    getContextData: function(key) {
      const str = sessionStorage.getItem(key);
      if (typeof str == "string") {
        try {
          return JSON.parse(str);
        } catch (e) {
          return str;
        }
      }
      return;
    },
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
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>
<style lang="less">
.active {
  color: rgba(68, 137, 247, 1) !important;
  width: 60px;
  height: 64px;
  background: rgba(255, 255, 255, 1);
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}
.block {
  width: 100%;
  height: auto;
  background: #f5f5f5;
  .van-cell:nth-child(1) {
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    margin-top: 0px;
  }
  .van-cell {
    width: 93.6%;
    height: 111px;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    padding: 0;
    margin: 0 auto;
    .van-cell__value {
      height: 170px;
      display: flex;
      flex-direction: row;
      img {
        width: 33px;
        height: 33px;
        position: relative;
        left: 15px;
        top: 39px;
      }
      .pdetail2 {
        font-size: 14px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 20px;
        opacity: 1;
        position: absolute;
        left: 63px;

        p {
          margin-top: 10px;
          span:nth-child(1) {
            display: inline-block;
            width: 100px;
            font-size: 14px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 20px;
            color: rgba(40, 96, 194, 1);
            opacity: 1;
          }
          span:nth-child(2) {
            display: inline-block;
            width: 160px;
            font-size: 14px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 20px;
          }
        }
      }
    }
  }
  .van-list {
    width: 93.6%;
    height: auto;
    position: relative;
    top: 15px;
    margin: 0 auto;
  }
  .van-tabs__line {
    width: 30px;
    height: 0px;
    border: 2px solid rgba(68, 137, 247, 1);
    opacity: 1;
  }
  .van-tabs__content {
    width: 93.6%;
    height: auto;
    margin: 0 auto;
  }
  .van-tab__pane {
    height: auto !important;
  }
  .active2 {
    width: 335px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    margin: 0 auto;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 8px;
    font-size: 18px;
    font-family: "苹方-简";
    font-weight: normal;
    color: rgba(68, 137, 247, 1) !important;
  }
  .selectul {
    margin-top: 20px;
    .selectlist {
      width: 335px;
      height: 50px;
      line-height: 50px;
      margin: 0 auto;
      color: rgba(153, 153, 153, 1);
      text-align: center;
    }
  }
  .error {
    width: 16.41px !important;
    height: 16.41px !important;
    position: absolute;
    left: 19px;
    top: 19px;
  }
  .van-popup--top {
    height: 116px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 0px 0px 8px 8px;
  }
  .van-popup--bottom {
    height: 286px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 8px 8px 0px 0px;
  }

  .indexchart {
    width: 351px;
    height: 183px;
    background: rgba(40, 96, 194, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 10px;
    .cardlefttop {
      width: 100%;
      display: flex;
      flex-direction: row;
      img {
        width: 26px;
        height: 29px;
        position: relative;
        left: 25px;
        top: 19px;
      }
      .cardlefttopright {
        p:nth-child(1) {
          font-size: 12px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 28px;
          color: rgba(255, 255, 255, 1);
          opacity: 1;
          position: relative;
          left: 30px;
          top: 15px;
        }
        p:nth-child(2) {
          font-size: 12px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 17px;
          color: rgba(255, 255, 255, 1);
          opacity: 1;
          position: relative;
          left: 30px;
          top: 10px;
        }
      }
      .ranliaoaverage {
        font-size: 10px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 14px;
        color: rgba(255, 255, 255, 1);
        opacity: 1;
        position: relative;
        left: 22px;
        top: 40px;
      }
    }
    .cardleftbottom {
      ul {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
        li {
          width: 80px;
          margin-top: 15px;
          margin-left: 15px;
          text-align: left;
          p:nth-child(1) {
            font-size: 12px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 25px;
            color: rgba(255, 255, 255, 1);
            opacity: 1;
          }
          p:nth-child(2) {
            font-size: 12px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 25px;
            color: rgba(255, 199, 135, 1);
            opacity: 1;
          }
        }
      }
    }
  }
}
</style>
