<template>
  <div class="address" v-loading="fullscreenLoading">
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

            <p>
              {{ item.title }}
            </p>
          </li>
        </ul>
      </van-popup>
    </div>
    <v-search></v-search>
    <div class="addresstop">
      <p>
        {{ $t("address.content[0]") }}{{ $t("address.content[5]")
        }}<span>{{ totalNum }}</span
        >{{ $t("address.content[6]") }}
      </p>
    </div>
    <van-list
      v-model="listloading"
      :finished="finished"
      :immediate-check="false"
      finished-text="没有更多了"
      @load="onLoada"
      :offset="10"
      :loading-text="loadingtext"
    >
      <van-cell
        v-for="item in addressData"
        :key="item.id"
        @click="gototransactiondetails(item.wallet_address)"
      >
        <div class="pdetail">
          <p>
            <span>{{ $t("address.content[1]") }}:</span
            ><span>{{ item.row_num }}</span>
          </p>
          <p>
            <span>{{ $t("address.content[2]") }}:</span
            ><span>{{ item.wallet_address.substring(0, 18) + "..." }}</span>
          </p>
          <p>
            <span>{{ $t("publicsection[4]") }}:</span
            ><span>{{ item.transaction_num }}</span>
          </p>
          <p>
            <span>{{ $t("address.content[3]") }}:</span
            ><span>{{ item.amount }}</span>
          </p>
          <p>
            <span>{{ $t("address.content[4]") }}:</span
            ><span>{{ item.percentage + "%" }}</span>
          </p>
        </div>
      </van-cell>
    </van-list>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
export default {
  name: "address",
  data() {
    return {
      loadingtext: "",
      show_silde: false,
      listloading: false,
      addressData: [],
      finished: false,
      addressmedianum: 1, //请求第几页
      pageSize: 5, //每页请求的数量
      total: "", //总共的数据条数
      totalNum: "",
      loading: true,
      sticky2: false,
      tables: false,
      // 外部公共部分
      fullscreenLoading: true,
      cur: "",
      language: "",
      nowLang: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      // 搜索功能
      search: "",
      // 分页
      searchData: "",
      addresszong: "",
      fromname: "",
    };
  },
  components: { vSearch },
  // 页码设置
  watch: {},
  beforeRouteEnter(to, from, next) {
    // console.log('去的地方'+to.name);
    // console.log('来的地方'+from.name);
    localStorage.setItem("toname", to.name);
    localStorage.setItem("fromname", from.name);
    next();
  },
  created() {
    //  console.log(document.referrer);
    // console.log(window.location.href);
    // // 路由路径
    // console.log(this.$route.path);
    
    this.nowLang = this.$i18n.locale;
    this.cur = 3;
    this.addresssearch();
    if (this.nowLang == "en") {
      this.loadingtext = "Loading...";
    }
    if (this.nowLang == "cn") {
      this.loadingtext = "加载中...";
    }
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
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
    // 如果支持 popstate 一般移动端都支持了
    if (window.history && window.history.pushState) {
      // 往历史记录里面添加一条新的当前页面的url
      history.pushState(null, null, document.URL);
      // 给 popstate 绑定一个方法 监听页面刷新
      window.addEventListener("popstate", this.backChange, false); //false阻止默认事件
    }
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
    backChange() {
      const that = this;
      if (localStorage.getItem("fromname") == "index") {
        // alert(window.location.href + "回到首页");
      }
      this.$router.go(-1);
    },
    // 点击返回
    returnBack() {
     
      this.$router.go(-1);
    },
    onLoada() {
      // console.log(this.addressmedianum);
      if (this.addressmedianum <= this.total) {
        this.addressmedianum += 1;
        this.addresssearch();
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
    addresssearch() {
      let that = this;
      var blockData = [];
      that.$http
        .get("/get_address_list_for_all", {
          params: {
            pageNum: this.addressmedianum,
            pageSize: 10,
          },
        })
        .then((res) => {
          // console.log(res);
          this.fullscreenLoading = false;
          this.listloading = false;
          this.addressData = this.addressData.concat(
            res.data[0].wallet_address_list
          );
          this.totalNum = res.data[0].total_record[0].total_record;
          this.total = res.data[0].total_page[0].totalPageNum;
          // console.log(this.total);
        });
    },
    // 跳转到地址详情页
    gototransactiondetails(e) {
      this.$router.push({
        path: "/transactiondetails",
        query: { addressvalue: e },
      });
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
    showlist() {
      this.addresssearch();
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
    window.removeEventListener("popstate", this.backChange, false); //false阻止默认事件
  },
};
</script>
<style lang="less">
.address {
  width: 100%;
  height: auto;
  background: #f5f5f5;
  opacity: 1;
  .addresstop {
    width: 93.6%;
    height: 50px;
    line-height: 50px;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 11px;
    p {
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      color: #2860c2;
      opacity: 1;
      margin-left: 15px;
      position: relative;
      top: 15px;
    }
  }
  .van-list {
    width: 100%;
    margin-top: 15px;
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
      width: 95%;
      height: 170px;
      background: #f5f5f5;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;

      padding: 0;
      margin: 0 auto;
      margin-top: 1px;
      .van-cell__value {
        height: 170px;
        display: flex;
        flex-direction: row;
        img {
          width: 33px;
          height: 33px;
          position: relative;
          left: 15px;
          top: 69px;
        }
        .pdetail {
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
              position: relative;
              left: 10px;
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
}
</style>
