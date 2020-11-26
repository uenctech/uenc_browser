<template>
  <div class="transactiondetails" v-loading.fullscreen.lock="fullscreenLoading">
    <div class="headertop" :class="{ sticky2: sticky2 }">
      <img
        src="@assets/images/transaction/组 202.png"
        @click="returnBack"
        id="slideleft"
      />
      <p class="header_title">{{ $t("nav[3].title") }}</p>
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

            <p>{{ item.title }}</p>
          </li>
        </ul>
      </van-popup>
    </div>
    <v-search @test="ceshi"></v-search>
    <div class="detailstop">
      <p>{{ shiyan }}</p>
      <p>
        <span>{{ $t("transaction.content[3]") }}:</span>
        {{ yue }}
      </p>
    </div>
    <van-list
      v-model="listloading2"
      :finished="finished2"
      :immediate-check="false"
      finished-text="没有更多了"
      @load="onLoad2"
      :offset="10"
      :loading-text="loadingtext"
    >
      <van-cell
        v-for="item in transactionData"
        :key="item.id"
        class="vancell2"
        @click="gotoblockdetail(item.transaction_hash)"
      >
        <div class="pdetail2">
          <p>
            <span>{{ $t("home.contenttop[1]") }}:</span>
            <span>{{ item.transaction_hash.substring(0, 18) + "..." }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[8]") }}:</span>
            <span>{{ item.time }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[6]") }}:</span>
            <span>{{ item.from_address.substring(0, 18) + "..." }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[7]") }}:</span>
            <span>{{ item.to_address.substring(0, 18) + "..." }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[5]") }}:</span>
            <span>{{ item.amount }}</span>
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
      show_silde: false,
      listloading2: false,
      finished2: false,
      blockmedianum: 1, //请求第几页
      pageSize2: 6, //每页请求的数量
      total2: "", //总共的数据条数
      loading: true,
      sticky2: false,
      shiyan: "",
      tables: false,
      yue: "",
      // 外部公共部分
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      nowLang: "",
      cur: "",
      fullscreenLoading: true,
      // 分页
      transmedianum: 1,
      totalNum: "",
      transactionData: [],
    };
  },
  // 页码设置
  watch: {},
  components: { vSearch },
  created() {
   
    // 路由路径
    // console.log(this.$route.path);
    // console.log(window.location.href);
    // console.log(this.$route.query);
    this.transactionData = [];
    this.nowLang = this.$i18n.locale;
    this.cur = 2;
    this.shiyan = this.$route.query.addressvalue;
    this.transmedianum = 1;
    this.addresssearch();
    // this.transactionlist();
    if (this.nowLang == "en") {
      this.loadingtext = "Loading...";
    }
    if (this.nowLang == "cn") {
      this.loadingtext = "加载中...";
    }
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
    // 跳转块详情页
    gotoblockdetail(e) {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: e },
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
      // console.log(this.transmedianum);
      // console.log(this.total2);
      if (this.transmedianum < this.total2 + Number(1)) {
        this.transmedianum += 1;
        this.addresssearch();
      } else {
        this.listloading2 = false;
        // this.finished2 = true;
        return false;
      }
    },
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
    },
    ceshi(msg) {
      this.shiyan = msg;
      // console.log(this.shiyan);
      this.transmedianum = 1;
      this.transactionData = [];
      this.addresssearch();
    },
    //地址搜索
    async addresssearch() {
      let that = this;
      await that.$http
        .get("/search_transactionInfo_walletAddress", {
          params: {
            wallet_address: this.shiyan,
            pageNum: this.transmedianum,
            pageSize: 5,
          },
        })
        .then((res) => {
          // console.log(res);
          // console.log("加载中");
          this.fullscreenLoading = false;
          this.listloading2 = false;
          this.total2 = res.data[0].total_page[0].totalPageNum;
          // console.log(this.total2);
          this.transactionData = this.transactionData.concat(
            res.data[0].search_transaction_list_for_walletAddress
          );
          // 余额
          this.yue =
            res.data[0].search_wallet_balance_for_walletAddress[0]
              .account_balance + "\n\nUENC";
          // 总条数
          this.totalNum = res.data[0].total_record[0].total_record;
          if (this.nowLang == "cn") {
            for (
              let i = 0;
              i <
              res.data[0].search_transaction_list_for_walletAddress.length + 1;
              i++
            ) {
              let blocktime =
                res.data[0].search_transaction_list_for_walletAddress[i].time;

              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].search_transaction_list_for_walletAddress[
                    i
                  ].time = "刚刚";
                } else {
                  res.data[0].search_transaction_list_for_walletAddress[
                    i
                  ].time = fenzhong + "分钟前";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].search_transaction_list_for_walletAddress[i].time =
                  parseInt(fenzhong / 60) + "小时前";
              }
              if (fenzhong > 1440) {
                res.data[0].search_transaction_list_for_walletAddress[i].time =
                  parseInt(fenzhong / 1440) + "天前";
              }
            }
          } else {
            for (
              let i = 0;
              i <
              res.data[0].search_transaction_list_for_walletAddress.length + 1;
              i++
            ) {
              let blocktime =
                res.data[0].search_transaction_list_for_walletAddress[i].time;

              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].search_transaction_list_for_walletAddress[
                    i
                  ].time = "Just";
                } else {
                  res.data[0].search_transaction_list_for_walletAddress[
                    i
                  ].time = fenzhong + "Minutes ago";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].search_transaction_list_for_walletAddress[i].time =
                  parseInt(fenzhong / 60) + "Hours ago";
              }
              if (fenzhong > 1440) {
                res.data[0].search_transaction_list_for_walletAddress[i].time =
                  parseInt(fenzhong / 1440) + "Days ago";
              }
            }
          }
        })
        .catch((e) => {});
    },
    timestampToTime(timestamp) {
      var date = new Date(timestamp * 1000); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
      var Y = date.getFullYear() + "-";
      var M =
        (date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1) + "-";
      var D = date.getDate() + " ";
      var h = date.getHours() + ":";
      var m = date.getMinutes() + ":";
      var s = date.getSeconds();
      return Y + M + D + h + m + s;
    },
    // 滚动固定区域
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 0) {
        this.sticky2 = true;
      }
      if (scrollTop < 10) {
        this.sticky2 = false;
      }

      // console.log(scrollTop);
    },

    // 点击表格行显示数据
    gototransactiondetail(row, event, column) {
      this.$router.push({
        path: "/transactiondetail",
        query: {
          // 高度
          transaction_hash: row.transaction_hash2,
        },
      });
      // console.log(row, event, column);
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

    // 页面的切换选择
    jump(index, title) {
      this.cur = 2;
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
.transactiondetails {
  width: 100%;
  height: auto;
  background: #f5f5f5;
  opacity: 1;
  min-height: 100vh;
  .detailstop {
    width: 93.6%;
    height: 79px;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 11px;
    padding-left: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    p:nth-child(1) {
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      color: #2860c2;
      opacity: 1;
    }
    p:nth-child(2) {
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      color: #333333;
      opacity: 1;

      span {
        font-size: 14px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 20px;
        color: #2860c2;
        opacity: 1;
        margin-right: 38px;
      }
    }
  }
  .van-cell:nth-child(1) {
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    margin-top: 15px;
  }
  .van-cell:nth-last-child(1) {
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
  }
  .van-cell {
    width: 93.6%;
    height: 170px;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;

    padding: 0;
    margin-top: 1px;
    margin: 0 auto;
    .van-cell__value {
      height: 170px;
      display: flex;
      flex-direction: row;
      .pdetail2 {
        height: 100%;
        font-size: 14px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 20px;
        opacity: 1;
        position: absolute;
        left: 15px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        p {
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
            width: 100px;
            font-size: 14px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 20px;
          }
        }
      }
    }
  }
}
</style>
