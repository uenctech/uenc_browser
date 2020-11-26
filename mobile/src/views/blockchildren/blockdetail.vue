<template>
  <div class="searchblockdetail">
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
    <div class="blockdetailheight">
      <p></p>
      <div>{{ $t("publicsection[3]") }}</div>
    </div>
    <ul class="transinformation">
      <li>
        <p>{{ $t("publicsection[3]") }}:</p>
        <div id="jiajian">
          <span>{{ datalist[0].block_height }}</span>
          <p class="line"></p>
          <img src="@assets/images/blockdetail/组 191.png" @click="zijian" />
          <p class="line2"></p>
          <img src="@assets/images/blockdetail/组 226.png" @click="zijia" />
        </div>
      </li>
      <li>
        <p>{{ $t("block.content2[0]") }}:</p>
        <p>{{ datalist[0].block_award }}</p>
      </li>
      <li>
        <p>{{ $t("publicsection[4]") }}:</p>
        <p>{{ datalist[0].tx_num }}</p>
      </li>
      <li>
        <p>{{ $t("block.content2[1]") }}:</p>
        <p>{{ datalist[0].transaction_amount }}</p>
      </li>
    </ul>
    <div class="blockdetail2height">
      <p></p>
      <div>{{ $t("block.content[0]") }}</div>
    </div>
    <van-list
      v-model="listloading"
      :finished="finished"
      :immediate-check="false"
      finished-text="没有更多了"
      @load="onLoad"
      :offset="1"
    >
      <van-cell
        v-for="item in blockdetaillist"
        :key="item.id"
        @click="gotoblockdetails(item.block_hash)"
      >
        <div class="pdetail">
          <p>
            <span>{{ $t("block.content2[3]") }}:</span>
            <span>{{ item.block_hash.substring(0, 18) + "..." }}</span>
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
            <sapn>{{ item.to_address.substring(0, 18) + "..." }}</sapn>
          </p>
          <p>
            <span>{{ $t("publicsection[5]") }}:</span>
            <sapn>{{ item.transaction_amount }}</sapn>
          </p>
        </div>
      </van-cell>
    </van-list>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
export default {
  name: "searchblockdetail",
  data() {
    return {
      listloading: false,
      finished: false,
      blockmedianum: "", //请求第几页
      pageSize: 5, //每页请求的数量
      total: "", //总共的数据条数
      show_silde: false,
      loading: true,
      shiyan: "",
      tables: false,
      sticky2: false,
      // 外部公共部分
      nowLang: "",
      fullscreenLoading: false,
      cur: "",
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      detailData: [],
      datalist: [],
      blockdetaillist: [],
    };
  },
  components: { vSearch },
  created() {
 
    this.nowLang = this.$i18n.locale;
    this.cur = 1;
    this.blockmedianum = 1;
    this.shiyan = this.$route.query.blockheight;
    this.blocksearch();
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
  },
  beforeRouteEnter(to, from, next) {
    // console.log('去的地方'+to.name);
    // console.log("来的地方" + from.name);
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
    ceshi(msg) {
      this.shiyan = msg;
      this.blocksearch();
    },
    zijian() {
      this.blockmedianum = 1;
      this.shiyan = Number(this.shiyan) - Number(1);
      if (this.shiyan <= 0) {
        this.shiyan = 0;
      }
      this.blocksearch();
    },
    zijia() {
      this.blockmedianum = 1;
      this.shiyan = Number(this.shiyan) + Number(1);
      this.blocksearch();
    },
    onLoad() {
      this.blockmedianum += 1;
      // console.log(this.blockmedianum);
      // console.log(this.total);
      if (this.blockmedianum < this.total + 1) {
        this.blocksearch();
      } else {
        this.listloading = false;
        // this.finished = true;
      }
    },
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
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
    // 区块高度搜索
    async blocksearch() {
      let that = this;
      var blockData = [];
      await that.$http
        .get("/search_blockHeight_for_height", {
          params: {
            block_height: this.shiyan,
            pageNum: this.blockmedianum,
            pageSize: 10000,
          },
        })
        .then((res) => {
          //  console.log(res);
          this.listloading = false;
          this.total = res.data[0].total_page[0].totalPageNum;
          // console.log(this.total);
          this.datalist = res.data[0].block_height;
          for (let i = 0; i < res.data[0].block_list.length + 1; i++) {
            res.data[0].block_list[i].time = this.timestampToTime(
              res.data[0].block_list[i].time
            );
            this.blockdetaillist = res.data[0].block_list;
          }
          // console.log(this.blockdetaillist);
        })
        .catch((e) => {});
    },
    // 点击表格行显示数据
    gotoblockdetails(e) {
      this.$router.push({
        path: "/blockdetails",
        query: {
          // 高度
          blockhaxi: e,
        },
      });
    },
    timestampToTime(timestamp) {
      var date = new Date(timestamp * 1000); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
      var Y = date.getFullYear() + "-";
      var M =
        (date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1) + "-";
      var D = date.getDate();
      if (D < 10) {
        D = "0" + D + "  ";
      } else {
        D = D + "  ";
      }
      var h = date.getHours();
      if (h < 10) {
        h = "0" + h + ":";
      } else {
        h = h + ":";
      }
      var m = date.getMinutes();
      if (m < 10) {
        m = "0" + m + ":";
      } else {
        m = m + ":";
      }
      var s = date.getSeconds();
      if (s < 10) {
        s = "0" + s;
      } else {
        s = s;
      }
      return Y + M + D + h + m + s;
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
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>
<style lang="less">
.van-cell:nth-child(1) {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  margin-top: 15px;
}
.van-cell:nth-last-child(1) {
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}
.van-list {
  border-radius: 15px;
  overflow: hidden;
}
.searchblockdetail {
  width: 100%;
  height: auto;
  min-height: 100vh;
  position: relative;
  background: #f5f5f5;
  .blockdetailheight {
    width: 93.6%;
    display: flex;
    flex-direction: row;
    margin-top: 20px !important;
    margin: 0 auto;
    p {
      width: 3px;
      height: 20px;
      background: rgba(68, 137, 247, 1);
      opacity: 1;
    }
    div {
      font-size: 17px;
      position: relative;
      left: 5px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 24px;
      color: rgba(51, 51, 51, 1);
      opacity: 1;
    }
  }
  .blockdetail2height {
    width: 93.6%;
    display: flex;
    flex-direction: row;
    margin-top: 20px !important;
    margin: 0 auto;
    p {
      width: 3px;
      height: 20px;
      background: rgba(68, 137, 247, 1);
      opacity: 1;
    }
    div {
      font-size: 17px;
      position: relative;
      left: 5px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 24px;
      color: rgba(51, 51, 51, 1);
      opacity: 1;
    }
  }
  .transinformation {
    width: 93.6%;
    height: 155px;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    li {
      width: 100%;
      height: 20px;
      line-height: 20px;
      display: flex;
      flex-direction: row;
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      #jiajian {
        width: 251px;
        height: 30px;
        line-height: 30px;
        background: rgba(255, 255, 255, 1);
        border: 1px solid rgba(68, 137, 247, 1);
        opacity: 1;
        border-radius: 5px;
        display: flex;
        flex-direction: row;
        span {
          position: relative;
          left: 15px;
        }
        .line {
          width: 0px;
          height: 29px;
          border: 1px solid rgba(204, 204, 204, 1);
          opacity: 1;
          position: relative;
          left: 131px;
        }
        .line2 {
          width: 0px;
          height: 12px;
          border: 1px solid rgba(204, 204, 204, 1);
          opacity: 1;
          position: relative;
          top: 7.5px;
          left: 159px;
        }
        img {
          position: relative;
          top: 5px;
          width: 9.83px;
          height: 16.83px;
        }
        img:nth-child(3) {
          position: relative;
          left: 146px;
        }
        img:nth-child(5) {
          position: relative;
          left: 170px;
        }
      }
      p:nth-child(1) {
        position: relative;
        left: 15px;
        width: 88px;
        color: rgba(40, 96, 194, 1);
      }
      p:nth-child(2) {
        position: relative;
        left: 10px;
        height: auto;
        word-wrap: break-word;
        width: 228px;
      }
    }
  }
  .van-list {
    width: 100%;
    height: auto;
    margin: 0 auto;
    .van-cell:nth-child(1) {
      margin-top: 10px;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
    }
    .van-cell:nth-last-child(1) {
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      margin-bottom: 20px;
    }
    .van-cell {
      margin-top: 20px;
      margin-bottom: 20px;
      width: 95%;
      height: 170px;
      background: #f5f5f5;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      margin: 0 auto;

      border-bottom: 1px solid rgba(0, 0, 0, 0.1);
      padding: 0;
      .van-cell__value {
        height: 170px;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        .pdetail {
          font-size: 14px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 20px;
          opacity: 1;
          position: absolute;
          left: 15px;
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
              width: 200px;
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
