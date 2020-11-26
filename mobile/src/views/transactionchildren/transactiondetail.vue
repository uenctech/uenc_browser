<template>
  <div class="transactiondetail">
    <div class="headertop" :class="{ sticky2: sticky2 }">
      <img
        src="@assets/images/transaction/组 202.png"
        @click="returnBack"
        id="slideleft"
      />
      <p class="header_title">{{ $t("nav[2].title") }}</p>
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
    <van-tabs v-model="activeName">
      <van-tab :title="$t('transaction.content2[2]')">
        <ul class="transinformation">
          <li>
            <p>{{ $t("publicsection[3]") }}:</p>
            <div id="jiajian">
              <span>{{ transactionlist[0].block_height }}</span>
              <p class="line"></p>
              <img
                src="@assets/images/blockdetail/组 191.png"
                @click="zijian"
              />
              <p class="line2"></p>
              <img src="@assets/images/blockdetail/组 226.png" @click="zijia" />
            </div>
          </li>
          <li>
            <p>{{ $t("home.contenttop[1]") }}:</p>
            <p>{{ transactionlist[0].transaction_hash }}</p>
          </li>
          <li>
            <p>{{ $t("block.content2[3]") }}:</p>
            <p>{{ transactionlist[0].block_hash }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[5]") }}:</p>
            <p>{{ transactionlist[0].transaction_time }}</p>
          </li>
          <li>
            <p>{{ $t("publicsection[6]") }}:</p>
            <p>{{ transactionlist[0].from_address }}</p>
          </li>
          <li>
            <p>{{ $t("publicsection[7]") }}:</p>
            <p class="toright" v-html="transactionlist[0].to_address"></p>
          </li>
          <li v-if="amount_detail">
            <p>{{ $t("publicsection[13]") }}:</p>
            <p class="toright" v-html="transactionlist[0].amount_detail"></p>
          </li>
          <li v-else></li>
          <li>
            <p>{{ $t("publicsection[5]") }}:</p>
            <p>{{ transactionlist[0].transaction_amount }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[0]") }}</p>
            <p>{{ transactionlist[0].extra }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[1]") }}</p>
            <p>{{ transactionlist[0].sign_node }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content[2]") }}:</p>
            <p>{{ transactionlist[0].gas }}</p>
          </li>
          <li>
            <p>{{ $t("home.cardleft[2]") }}:</p>
            <p>{{ transactionlist[0].award }}</p>
          </li>
        </ul>
      </van-tab>
      <van-tab :title="$t('transaction.content2[3]')">
        <ul class="transinformation2">
          <li>
            <p>{{ $t("home.contenttop[1]") }}:</p>
            <p>{{ transactionlist2[0].transaction_hash_gas }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[5]") }}:</p>
            <p>{{ transactionlist[0].transaction_time }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content[2]") }}:</p>
            <p>{{ transactionlist[0].gas }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[1]") }}</p>
            <p>
              <span v-for="item in transactionlist2sign" :key="item">
                {{ item }}
              </span>
            </p>
          </li>

          <li>
            <p>{{ $t("transaction.content2[7]") }}:</p>
            <p>
              <span v-for="item in transactionlist2gas" :key="item">
                {{ item }}
              </span>
            </p>
          </li>
        </ul>
      </van-tab>
      <van-tab :title="$t('transaction.content2[4]')">
        <ul class="transinformation3">
          <li>
            <p>{{ $t("home.contenttop[1]") }}:</p>
            <p>{{ transactionaward[0].transaction_hash_award }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[5]") }}:</p>
            <p>{{ transactionlist[0].transaction_time }}</p>
          </li>
          <li>
            <p>{{ $t("block.content2[0]") }}:</p>
            <p>{{ transactionlist[0].award }}</p>
          </li>
          <li>
            <p>{{ $t("transaction.content2[6]") }}:</p>
            <p>
              <span v-for="item in transactionaward2sign" :key="item">
                {{ item }}
              </span>
            </p>
          </li>

          <li>
            <p>{{ $t("transaction.content2[7]") }}:</p>
            <p>
              <span v-for="item in transactionaward2award" :key="item">
                {{ item }}
              </span>
            </p>
          </li>
        </ul>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import vSearch from "@components/common/search";
import { Loading } from "element-ui";
export default {
  name: "transdetail",
  data() {
    return {
      sticky: false,
      tables: false,
      show_silde: false,
      collength: "",
      sticky2: false,
      shiyan: "",
      // 外部公共部分
      fullscreenLoading: true,
      cur: "",
      language: "",
      nowLang: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      activeName: "",
      // 交易数据请求
      transaction_hash: "",
      height: "",
      // 交易列表
      transactionlist: [
        {
          block_height: "",
          transaction_hash: "",
          transaction_hash2: "",
          transaction_hash3: "",
          block_hash: "",
          transaction_time: "",
          from_address: "",
          to_address: "",
          transaction_amount: "",
          extra: "",
          sign_node: "",
          gas: "",
          award: "",
        },
      ],
      transactionlist2: [],
      transactionlist2sign: [],
      transactionlist2gas: [],
      transactionaward: [],
      transactionaward2sign: [],
      transactionaward2award: [],
      amount_detail: false,
    };
  },
  components: { vSearch },
  created() {
    
    Loading.service({
      lock: true, //是否锁定
      text: "", //显示在加载图标下方的加载文案
      background: "rgba(0,0,0,)", //遮罩背景色
    });
    this.nowLang = this.$i18n.locale;
    this.transactionlist2sign = [];
    this.transactionlist2gas = [];
    this.transactionaward2sign = [];
    this.transactionaward2award = [];
    if (this.nowLang == "en") {
    }
    if (this.nowLang == "cn") {
    }
    this.cur = 2;
    this.line1 = true;
    this.shiyan = this.$route.query.transaction_hash;

    //根据交易易哈希查询信息
    this.transactiondetaillist();
    this.transactionlist[0].block_height = this.height;
  },
  // 监听高度的变化
  watch: {},
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
      this.height -= 1;
      this.transactionlist[0].block_height = this.height;
      this.$router.push({
        path: "blockdetail",
        query: {
          // 高度
          blockheight: this.transactionlist[0].block_height,
        },
      });
    },
    // 高度加
    zijia() {
      this.height += 1;
      if (this.heigth <= 0) {
        this.height = 0;
      }
      this.transactionlist[0].block_height = this.height;
      this.$router.push({
        path: "blockdetail",
        query: {
          // 高度
          blockheight: this.transactionlist[0].block_height,
        },
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
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
    },
    ceshi(msg) {
      this.transactionlist2sign = [];
      this.transactionlist2gas = [];
      this.transactionaward2sign = [];
      this.transactionaward2award = [];
      this.shiyan = msg;
      this.transactiondetaillist();
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
    // 根据交易易哈希查询相关交易易信息
    async transactiondetaillist() {
      let that = this;
      await that.$http
        .get("search_transactionHash_detailInfo", {
          params: {
            transaction_hash: this.shiyan,
          },
        })
        .then((res) => {
          let loadingInstance = Loading.service({
            lock: true, //是否锁定
            text: "拼命加载中...", //显示在加载图标下方的加载文案
            background: "rgba(0,0,0,.7)", //遮罩背景色
          });
          this.$nextTick(() => {
            // 以服务的方式调用的 Loading 需要异步关闭
            loadingInstance.close();
          });
          // if(res.status=='200'){
          // this.fullscreenLoading=false
          // };
          //  console.log(res);
          if (res.data[0].select_id === 1) {
            this.activeName = "0";
          }
          if (res.data[0].select_id === 2) {
            this.activeName = "1";
          }
          if (res.data[0].select_id === 3) {
            this.activeName = "2";
          }
          // 区块高度
          this.transactionlist[0].block_height =
            res.data[0].search_main_transaction_detailInfo[0].block_height;
          this.height = this.transactionlist[0].block_height;
          // 交易哈希
          this.transactionlist[0].transaction_hash =
            res.data[0].search_main_transaction_detailInfo[0].transaction_hash;
          this.transactionlist[0].transaction_hash2 =
            res.data[0].search_gas_transaction_detailInfo[0].transaction_hash_gas;
          this.transactionlist[0].transaction_hash3 =
            res.data[0].search_award_transaction_detailInfo[0].transaction_hash_award;
          // 区块哈希、列表
          this.transactionlist[0].block_hash =
            res.data[0].search_main_transaction_detailInfo[0].block_hash;
          // 交易时间
          this.transactionlist[0].transaction_time = this.timestampToTime(
            res.data[0].search_main_transaction_detailInfo[0].transaction_time
          );
          if (
            res.data[0].search_main_transaction_detailInfo[0].to_address ==
              "0000000000000000000000000000000000" ||
            res.data[0].search_main_transaction_detailInfo[0].pledge == "1"
          ) {
            // 从
            this.transactionlist[0].from_address =
              res.data[0].search_main_transaction_detailInfo[0].from_address;
            if (this.nowLang == "cn") {
              this.transactionlist[0].to_address = "质押";
            } else {
              this.transactionlist[0].to_address = "Pledge";
            }
          } else if (
            res.data[0].search_main_transaction_detailInfo[0].from_address ==
              res.data[0].search_main_transaction_detailInfo[0].to_address ||
            res.data[0].search_main_transaction_detailInfo[0].redeem == "1"
          ) {
            if (this.nowLang == "cn") {
              // 从
              this.transactionlist[0].from_address = "质押";
            } else {
              this.transactionlist[0].from_address = "Pledge";
            }
            // 至
            this.transactionlist[0].to_address =
              res.data[0].search_main_transaction_detailInfo[0].to_address;
          } else {
            // 从
            this.transactionlist[0].from_address =
              res.data[0].search_main_transaction_detailInfo[0].from_address;
            // 至
            this.transactionlist[0].to_address = res.data[0].search_main_transaction_detailInfo[0].to_address.split(
              ","
            );
            // console.log(this.transactionlist[0].to_address);
            if (this.transactionlist[0].to_address.length > 1) {
              let to_address = [];
              //  this.transactionlist[0].to_address.length=5
              for (let s = 0; s < 6; s++) {
                to_address.push(
                  `<span style="color:blue">${s + 1}:</span>` +
                    this.transactionlist[0].to_address[s]
                );
              }
              this.transactionlist[0].to_address =
                to_address.toString() + "......";
              // 交易明细详情
              this.amount_detail = true;
              this.transactionlist[0].amount_detail = res.data[0].search_main_transaction_detailInfo[0].amount_detail.split(
                ","
              );
              let amount_detail = [];
              for (let k = 0; k < 6; k++) {
                amount_detail.push(
                  `<span style="color:blue">${k + 1}:</span>` +
                    this.transactionlist[0].amount_detail[k] / 1000000
                );
              }
              // console.log(to_address.toString());
              this.transactionlist[0].amount_detail =
                amount_detail.toString() + "......";
            } else {
              this.transactionlist[0].to_address =
                res.data[0].search_main_transaction_detailInfo[0].to_address;
              this.amount_detail = false;
            }
          }
          // 交易额
          this.transactionlist[0].transaction_amount =
            res.data[0].search_main_transaction_detailInfo[0].transaction_amount;
          // 共识数
          this.transactionlist[0].extra =
            res.data[0].search_main_transaction_detailInfo[0].extra;
          // 交易签名节点
          this.transactionlist[0].sign_node =
            res.data[0].search_main_transaction_detailInfo[0].sign_node;
          // 燃料费
          this.transactionlist[0].gas =
            res.data[0].search_main_transaction_detailInfo[0].gas;
          // 区块奖励
          this.transactionlist[0].award =
            res.data[0].search_main_transaction_detailInfo[0].award;
          this.collength = res.data[0].search_gas_transaction_detailInfo.length;
          this.transactionlist2 = res.data[0].search_gas_transaction_detailInfo;
          this.transactionaward =
            res.data[0].search_award_transaction_detailInfo;
          // console.log(res.data[0].search_gas_transaction_detailInfo);
          for (
            let i = 0;
            i < res.data[0].search_gas_transaction_detailInfo.length + 1;
            i++
          ) {
            this.transactionlist2sign.push(
              res.data[0].search_gas_transaction_detailInfo[i].sign_node + ","
            );
            // console.log(this.transactionlist2sign);
            this.transactionlist2gas.push(
              res.data[0].search_gas_transaction_detailInfo[i].gas + ","
            );
            this.transactionaward2sign.push(
              res.data[0].search_award_transaction_detailInfo[i].sign_node + ","
            );
            this.transactionaward2award.push(
              res.data[0].search_award_transaction_detailInfo[i].award + ","
            );
          }
        })
        .catch((e) => {});
    },
    // 滚动固定区域
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      // console.log(scrollTop);
      if (scrollTop > 10) {
        this.sticky2 = true;
      }
      if (scrollTop < 10) {
        this.sticky2 = false;
      }
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
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>
<style lang="less">
.van-tabs__content {
  margin-top: 16px;
}
.van-tabs__nav {
  background: none;
}
.van-tab--active {
  font-size: 15px;
  font-family: "苹方-简";
  font-weight: normal;

  color: #333333;
  opacity: 1;
}
#jiajian {
  width: 235px;
  height: 30px;
  line-height: 30px;
  background: white;
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
    position: absolute;
    left: 261px;
  }
  .line2 {
    width: 0px;
    height: 12px;
    border: 1px solid rgba(204, 204, 204, 1);
    opacity: 1;
    position: relative;
    top: 7.5px;
    left: 149px;
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
    left: 160px;
  }
}
.transactiondetail {
  background: #f5f5f5;
  opacity: 1;
  height: auto;
  min-height: 110vh;
  .van-tabs__line {
    width: 30px !important;
    height: 0px;
    border: 2px solid rgba(68, 137, 247, 1);
    opacity: 1;
    left: 15px !important;
  }
  .transinformation {
    width: 93%;
    height: auto;
    min-height: 512px;
    background: rgba(245, 245, 245, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
    margin: 0 auto;
    font-size: 14px;
    font-family: "苹方-简";
    font-weight: normal;
    line-height: 20px;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    li {
      width: 100%;
      height: auto;
      display: flex;
      flex-direction: row;
      margin-top: 15px;
      p:nth-child(1) {
        position: relative;
        left: 15px;
        width: 100px;
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
  .transinformation2,
  .transinformation3 {
    width: 93%;
    height: auto;
    min-height: 466px;
    background: rgba(245, 245, 245, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
    margin: 0 auto;
    font-size: 14px;
    font-family: "苹方-简";
    font-weight: normal;
    line-height: 20px;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    li {
      width: 100%;
      height: auto;
      display: flex;
      flex-direction: row;
      p:nth-child(1) {
        position: relative;
        left: 15px;
        width: 100px;
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
}
</style>
