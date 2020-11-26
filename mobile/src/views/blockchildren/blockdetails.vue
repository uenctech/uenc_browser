<template>
  <div class="blockdetails">
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

            <p>
              {{ item.title }}
            </p>
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
          <span>{{ blockdetailslist[0].block_height }}</span>
          <p class="line"></p>
          <img src="@assets/images/blockdetail/组 191.png" @click="zijian" />
          <p class="line2"></p>
          <img src="@assets/images/blockdetail/组 226.png" @click="zijia" />
        </div>
      </li>
      <li>
        <p>{{ $t("block.content2[3]") }}:</p>
        <p>{{ blockdetailslist[0].block_hash.substring(0, 18) + "..." }}</p>
      </li>
      <li>
        <p>{{ $t("publicsection[8]") }}:</p>
        <p>{{ blockdetailslist[0].block_time }}</p>
      </li>
      <li>
        <p>{{ $t("block.content3[0]") }}:</p>
        <p>{{ blockdetailslist[0].prevHash.substring(0, 18) + "..." }}</p>
      </li>
    </ul>
    <div class="blockdetail2height">
      <p></p>
      <div>{{ $t("transaction.content[0]") }}</div>
    </div>
    <ul class="detailsdetail">
      <li @click="gototransactiondetail">
        <p>
          <span>{{ $t("home.contenttop[1]") }}:</span
          ><span>{{
            maininfo[0].transaction_hash.substring(0, 18) + "..."
          }}</span>
        </p>

        <p>
          <span>{{ $t("publicsection[6]") }}:</span
          ><span>{{ maininfo[0].from_address.substring(0, 18) + "..." }}</span>
        </p>
        <p>
          <span>{{ $t("publicsection[7]") }}:</span
          ><span>{{ maininfo[0].to_address.substring(0, 18) + "..." }}</span>
        </p>
        <p>
          <span>{{ $t("publicsection[5]") }}:</span
          ><sapn>{{ maininfo[0].transaction_amount }}</sapn>
        </p>
        <p>
          <span>{{ $t("transaction.content[2]") }}:</span
          ><span>{{ gasinfo[0].transaction_gas }}</span>
        </p>
        <p>
          <span>{{ $t("home.cardleft[2]") }}</span
          ><span>{{ awardinfo[0].transaction_award }}</span>
        </p>
      </li>
      <li @click="gototransactiondetail2">
        <p>
          <span>{{ $t("home.contenttop[1]") }}:</span
          ><span>{{
            gasinfo[0].transaction_hash.substring(0, 18) + "..."
          }}</span>
        </p>
        <p>
          <span>{{ $t("publicsection[6]") }}:</span
          ><span>{{ gasinfo[0].from_address.substring(0, 18) + "..." }}</span>
        </p>
        <p>
          <span>{{ $t("publicsection[7]") }}:</span
          ><span>{{ gasinfo[0].sign_node }}</span>
        </p>
        <p>
          <span>{{ $t("transaction.content[2]") }}:</span
          ><span>{{ gasinfo[0].transaction_gas }}</span>
        </p>
      </li>
      <li @click="gototransactiondetail3">
        <p>
          <span>{{ $t("home.contenttop[1]") }}:</span
          ><span>{{
            awardinfo[0].transaction_hash.substring(0, 20) + "..."
          }}</span>
        </p>
        <p>
          <span>{{ $t("publicsection[7]") }}:</span
          ><span>{{ awardinfo[0].sign_node }}</span>
        </p>
        <p>
          <span>{{ $t("home.cardleft[2]") }}:</span
          ><span>{{ awardinfo[0].transaction_award }}</span>
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
export default {
  name: "blockdetail",
  data() {
    return {
      show_silde: false,
      loading: true,
      sticky2: false,
      shiyan: "",
      tables: false,
      // 外部公共部分
      nowLang: "",
      fullscreenLoading: false,
      cur: "",
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      height: "",
      choselanguage: ["中文", "EN"],
      detailData: [],
      blockdetailslist: [
        { block_height: "", block_hash: "", block_time: "", prevHash: "" },
      ],
      maininfo: [
        {
          transaction_hash2: "",
          transaction_hash: "",
          from_address: "",
          to_address: "",
          transaction_gas: "",
        },
      ],
      gasinfo: [
        {
          transaction_hash2: "",
          transaction_hash: "",
          from_address: "",
          sign_node: [],
          sign_node2: "",
          transaction_gas: "",
        },
      ],
      awardinfo: [
        {
          transaction_hash2: "",
          transaction_hash: "",
          transaction_award: "",
          sign_node: "",
          sign_node2: "",
        },
      ],
    };
  },
  components: { vSearch },
  created() {
 
    this.nowLang = this.$i18n.locale;
    this.cur = 1;
    this.shiyan = this.$route.query.blockhaxi;
    this.medianum = this.getContextData("currentpage1") || 1;
    this.blockhaxisearch();
    //console.log(this.height);
    if (this.nowLang == "en") {
    }
    if (this.nowLang == "cn") {
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
    // 高度减
    zijian() {
      this.blockdetailslist[0].block_height =
        this.blockdetailslist[0].block_height - 1;
      this.$router.push({
        path: "blockdetail",
        query: {
          // 高度
          blockheight: this.blockdetailslist[0].block_height,
        },
      });
    },
    // 高度加
    zijia() {
      this.blockdetailslist[0].block_height =
        this.blockdetailslist[0].block_height + 1;
      this.$router.push({
        path: "blockdetail",
        query: {
          // 高度
          blockheight: this.blockdetailslist[0].block_height,
        },
      });
    },
    onLoad() {
      this.blockmedianum += 1;
      if (this.blockmedianum <= this.total) {
        this.blocksearch();
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
    ceshi(msg) {
      this.shiyan = msg;
      this.blockhaxisearch();
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
    gototransactiondetail() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.maininfo[0].transaction_hash },
      });
    },
    gototransactiondetail2() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.gasinfo[0].transaction_hash },
      });
    },
    gototransactiondetail3() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.awardinfo[0].transaction_hash },
      });
    },
    // 区块哈希搜索
    async blockhaxisearch() {
      let that = this;
      await that.$http
        .get("/search_blockInfo_blockHash", {
          params: {
            block_hash: this.shiyan,
          },
        })
        .then((res) => {
          // console.log(res);
          // console.log(res.data[0].search_blockInfo);
          var common = res.data[0].search_blockInfo[0];
          // // 区块高度
          this.blockdetailslist[0].block_height = common.block_height;
          // // 时间
          this.blockdetailslist[0].block_time = this.timestampToTime(
            Number(common.block_time)
          );
          // 区块哈希
          this.blockdetailslist[0].block_hash = common.block_hash;
          // // 前置哈希
          this.blockdetailslist[0].prevHash = common.prevHash;
          // // // table赋值
          // // 第一行
          this.maininfo[0].transaction_hash2 =
            res.data[0].search_main_transactionInfo[0].transaction_hash;
          this.maininfo[0].transaction_hash =
            res.data[0].search_main_transactionInfo[0].transaction_hash;
          this.maininfo[0].from_address =
            res.data[0].search_main_transactionInfo[0].from_address;
          this.maininfo[0].to_address =
            res.data[0].search_main_transactionInfo[0].to_address;
          this.maininfo[0].transaction_amount =
            res.data[0].search_main_transactionInfo[0].transaction_amount;
          // // 第二行
          this.gasinfo[0].from_address =
            res.data[0].search_gas_transactionInfo[0].from_address;
          this.gasinfo[0].transaction_hash2 =
            res.data[0].search_gas_transactionInfo[0].transaction_hash;
          this.gasinfo[0].transaction_hash =
            res.data[0].search_gas_transactionInfo[0].transaction_hash;
          this.gasinfo[0].sign_node =
            res.data[0].search_gas_transactionInfo[0].sign_node;
          this.gasinfo[0].transaction_gas =
            res.data[0].search_gas_transactionInfo[0].transaction_gas;
          // // 第三行
          this.awardinfo[0].transaction_hash2 =
            res.data[0].search_award_transactionInfo[0].transaction_hash;
          // console.log(this.awardinfo[0].transaction_hash2);
          this.awardinfo[0].transaction_hash =
            res.data[0].search_award_transactionInfo[0].transaction_hash;
          this.awardinfo[0].sign_node =
            res.data[0].search_award_transactionInfo[0].sign_node;

          this.awardinfo[0].transaction_award =
            res.data[0].search_award_transactionInfo[0].transaction_award;
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
.blockdetails {
  width: 100%;
  height: auto;
  position: relative;

  background: rgba(245, 245, 245, 0.5);
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
  .detailsdetail {
    width: 93.6%;
    height: auto;
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 10px;
    margin-bottom: 30px;
    overflow: hidden;
    li {
      width: 100%;
      min-height: 200px;
      height: auto;
      margin-top: 30px;
      background: #f5f5f5;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      flex-wrap: wrap;
      word-wrap: break-word;
      align-items: flex-start;
      p {
        width: 100%;
        height: auto;
        span:nth-child(1) {
          display: inline-block;
          width: 100px;
          height: 20px;
          font-size: 14px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 20px;
          color: #2860c2;
          opacity: 1;
          margin-left: 15px;
        }
        span:nth-child(2) {
          display: inline-block;
          width: 200px;
          font-size: 14px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 20px;
          color: #333333;
          opacity: 1;
          flex-wrap: wrap;
          word-wrap: break-word;
        }
      }
    }
  }
}
</style>
