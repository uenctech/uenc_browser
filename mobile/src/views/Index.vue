<template>
  <div class="index">
    <div class="headertop" :class="{ sticky2: sticky2 }">
      <img
        src="@assets/images/transaction/组 202.png"
        @click="returnBack"
        id="slideleft"
      />
      <p class="header_title2">{{ $t("home.cardleft[4]") }}</p>
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
            top:50px;
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

            <p>{{ item.title }}</p>
          </li>
        </ul>
      </van-popup>
    </div>
    <v-search></v-search>
    <div class="indexchart">
      <div class="cardlefttop">
        <img src="@assets/images/index/uenc.png" />
        <div class="cardlefttopright">
          <p>UENC</p>
          <p>
            <span style="color: #ffc787">{{ money }}</span> USDT≈
            <span style="color: #ffc787">￥{{ money2 }}</span>
          </p>
        </div>
        <p class="ranliaoaverage">
          {{ $t("ranliaofeiaverage[0]") }}{{ average
          }}{{ $t("ranliaofeiaverage[1]") }}
        </p>
      </div>
      <div class="cardleftbottom">
        <ul>
          <li>
            <p>{{ $t("publicsection[3]") }}</p>
            <p>{{ blockheigth }}</p>
          </li>
          <li>
            <p>{{ $t("home.cardleft[0]") }}</p>
            <p>{{ transzoom }}</p>
          </li>
          <li>
            <p>{{ $t("home.cardleft[1]") }}</p>
            <p>{{ transmoney }}</p>
          </li>
          <li>
            <p>{{ $t("publicsection[4]") }}</p>
            <p>{{ transnumber }}</p>
          </li>
          <li>
            <p>{{ $t("home.cardleft[2]") }}</p>
            <p>{{ blockreward }}</p>
          </li>
          <li>
            <p>{{ $t("home.cardleft[3]") }}</p>
            <p>{{ blocklastreward }}</p>
          </li>
        </ul>
      </div>
    </div>
    <van-tabs v-model="active">
      <van-tab :title="$t('home.contenttop[0]')">
        <van-list
          v-model="listloading"
          :finished="finished"
          :immediate-check="false"
          :finished-text="finishedtext"
          @load="onLoad"
          :offset="300"
          :loading-text="loadingtext"
          v-loading.fullscreen.lock="fullscreenLoading"
        >
          <van-cell
            v-for="item in translist"
            :key="item.id"
            @click="gototransactiondetail(item.transaction_hash)"
          >
            <img src="@assets/images/index/-s-椭圆 2.png" />
            <div class="pdetail">
              <p>
                <span>{{ $t("home.contenttop[1]") }}:</span>
                <span>{{
                  item.transaction_hash.substring(0, 18) + "..."
                }}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[8]") }}:</span>
                <span>{{ item.transaction_time }}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[6]") }}:</span>
                <span>{{ item.from_address.substring(0, 18) + "..." }}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[7]") }}:</span>
                <span>{{ item.to_address}}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[5]") }}:</span>
                <span>{{ item.transaction_amount }}</span>
              </p>
            </div>
          </van-cell>
        </van-list>
      </van-tab>
      <van-tab :title="$t('home.contentbottom[0]')">
        <van-list
          v-model="listloading2"
          :finished="finished2"
          :immediate-check="false"
          :finished-text="finishedtext2"
          @load="onLoad2"
          :offset="1"
          :loading-text="loadingtext"
          v-loading="fullscreenLoading"
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
                <span>{{ $t("publicsection[12]") }}:</span>
                <span>{{ item.block_height }}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[8]") }}:</span>
                <span>{{ item.block_time }}</span>
              </p>
              <p>
                <span>{{ $t("publicsection[4]") }}:</span>
                <span>{{ item.transaction_num }}</span>
              </p>
            </div>
          </van-cell>
        </van-list>
      </van-tab>
    </van-tabs>
  </div>
</template>
<script>
import { Message } from "element-ui";
// // $(function() {
// //   console.log("haha");
// //   console.log($("path"));
// // });
axios.defaults.timeout = 10000; // 请求超时
// axios.interceptors.request.use(
//   function(config) {
//     // Do something before request is sent
//     return config;
//   },
//   function(error) {
//     // Do something with request error
//     return Promise.reject(error);
//   }
// );

// // Add a response interceptor
// axios.interceptors.response.use(
//   function(response) {
//     // Do something with response data
//     return response;
//   },
//   function(error) {
//     // if (this.nowLang == "cn") {
//       // Do something with response error
//       return Promise.reject(
//         Message({
//           showClose: true,
//           message: "加载失败，请稍后再试",
//           type: "error",
//         }),
//       )
//     // } else {
//     //   return Promise.reject(
//     //     Message({
//     //       showClose: true,
//     //       message: "Loading failed, please try again later",
//     //       type: "error",
//     //     })
//     //   );
//     // }
//   }
// );
import vSearch from "@components/common/search";
export default {
  name: "index",
  inject: ["reload"],
  data() {
    return {
      // 交易列表
      loadingtext: "",
      finishedtext: "",
      finishedtext2: "",
      translist: [],
      listloading: false,
      finished: false,
      transmedianum: 1, //请求第几页
      pageSize: 5, //每页请求的数量
      total: "", //总共的数据条数
      // 区块列表
      translist2: [],
      listloading2: false,
      finished2: false,
      blockmedianum: 1, //请求第几页
      pageSize2: 5, //每页请求的数量
      total2: "", //总共的数据条数
      // 本页面
      // 所有交易数据
      tableData: [],
      // 所有出块数据
      tableData2: [],
      active: 0,
      show_silde: false,
      loading: true,
      // 固定设置
      sticky2: false,
      // 外部公共部分
      fullscreenLoading: true,
      nowLang: "",
      cur: "",
      language: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      money: "",
      money2: "",
      // 卡片左边所有的数据
      // 区块高度
      blockheigth: "",
      // 24小时交易笔数?
      transzoom: "",
      // 24小时交易总额?
      transmoney: "",
      //  交易笔数
      transnumber: "",
      // 区块奖励
      blockreward: "",
      // 剩余区块奖励
      blocklastreward: "",
      average: "",
      responseTimeMs: "",
    };
  },
  watch: {},
  components: { vSearch },

  beforeCreate() {
    if (localStorage.getItem("toname") == "index") {
    }
  },
  beforeRouteEnter(to, from, next) {
    next();
  },
  created() {
    //  console.log(window.location.href);
    // //  路由路径
    //   console.log(this.$route.path);
    this.nowLang = this.$i18n.locale;
    // console.log(this.nowLang);
    this.cur = 0;
    // 获取首页数据
    this.indexlist();
    this.transactionlist();
    this.blocklist();
    if (this.nowLang == "en") {
      this.finishedtext = "Can't load more";
      this.finishedtext2 = "Can't load more";
      this.loadingtext = "Loading...";
    }
    if (this.nowLang == "cn") {
      this.finishedtext = "无法加载更多";
      this.finishedtext2 = "无法加载更多";
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
  },
  activated() {
    if (this.$route.meta.keepAlive) {
      // console.log('有缓存');
      //这是页面缓存的情况进入，接下来就是你自己的逻辑
    }
  },
  methods: {
    // 解析地址
    //获取url中的参数方法
    getQueryString(name) {
      let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
      if (window.location.hash.indexOf("?") < 0) {
        return null;
      }
      let r = window.location.hash.split("?")[1].match(reg);
      if (r != null) return decodeURIComponent(r[2]);
      return null;
    },
    //使用
    // 邀请码设置

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
          // console.log("android");
          window.android.back();
          // window.android.setUrl("http://www.uenc.io/");
        }
      } catch (e) {
        // console.log("出现错误, 如果在非android环境下访问, 出现该警告是正常的.");
      }
    },
    returnBack() {
      // 触发ios事件
      // window.webkit.messageHandlers.returnBack.postMessage("ok");
      // this.$router.go(-1);
    },
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
    // 跳转交易详情页
    gototransactiondetail(e) {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: e },
      });
    },
    // 跳转块详情页
    gotoblockdetail(e) {
      this.$router.push({
        path: "/blockdetail",
        query: { blockheight: e },
      });
    },
    onLoad() {
      this.transmedianum += 1;
      if (this.transmedianum <= this.total) {
        this.transactionlist();
      } else {
        return false;
      }
    },
    onLoad2() {
      this.blockmedianum += 1;
      if (this.blockmedianum <= this.total2) {
        this.blocklist();
      } else {
        this.finished2 = true;
        return false;
      }
    },
    //获取MEDIA
    transactionlist() {
      let that = this;
      that.$http
        .get("/search_transaction_list_all", {
          params: {
            pageNum: this.transmedianum,
            pageSize: 5,
          },
        })
        .then((res) => {
          //  console.log(res);
          this.fullscreenLoading = false;
          this.listloading = false;
          this.total = res.data[0].total_page[0].totalPageNum;
           for (
            let j = 0;
            j < res.data[0].transaction_list_results.length;
            j++
          ) {
            if (
              res.data[0].transaction_list_results[j].to_address ==
              "0000000000000000000000000000000000"
            ) {
              if (this.nowLang == "cn") {
                res.data[0].transaction_list_results[j].to_address = "质押";
              }
              if (this.nowLang == "en") {
                res.data[0].transaction_list_results[j].to_address = "Pledge";
              }
            } else {
              res.data[0].transaction_list_results[j].to_address =
                res.data[0].transaction_list_results[j].to_address.substring(
                  0,
                  10
                ) + "...";
            }
          }
          this.translist = this.translist.concat(
            res.data[0].transaction_list_results
          );
          if (this.nowLang == "cn") {
            for (
              let i = 0;
              i < res.data[0].transaction_list_results.length + 1;
              i++
            ) {
              let times = [];
              let blocktime =
                res.data[0].transaction_list_results[i].transaction_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].transaction_list_results[i].transaction_time =
                    "刚刚";
                } else {
                  res.data[0].transaction_list_results[i].transaction_time =
                    fenzhong + "分钟前";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].transaction_list_results[i].transaction_time =
                  parseInt(fenzhong / 60) + "小时前";
              }
              if (fenzhong > 1440) {
                res.data[0].transaction_list_results[i].transaction_time =
                  parseInt(fenzhong / 1440) + "天前";
              }
            }
          } else {
            for (
              let i = 0;
              i < res.data[0].transaction_list_results.length + 1;
              i++
            ) {
              let times = [];
              let blocktime =
                res.data[0].transaction_list_results[i].transaction_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].transaction_list_results[i].transaction_time =
                    "Just";
                } else {
                  res.data[0].transaction_list_results[i].transaction_time =
                    fenzhong + "Minutes ago";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].transaction_list_results[i].transaction_time =
                  parseInt(fenzhong / 60) + "Hours ago";
              }
              if (fenzhong > 1440) {
                res.data[0].transaction_list_results[i].transaction_time =
                  parseInt(fenzhong / 1440) + "Days ago";
              }
            }
          }
        })
        .catch((err) => {
          if (err.config.timeout >= 10000) {
            if (this.nowLang == "cn") {
              // this.$message({
              //   type: "error",
              //   message: " 加载失败，请稍后再试",
              // });

              this.$router.push({
                path: "/not",
              });
            } else {
              // this.$message({
              //   type: "error",
              //   message: "Loading failed, please try again later",
              // });

              this.$router.push({
                path: "/not",
              });
            }
          } else {
            // console.log(err);
          }
        });
    },
    //获取MEDIA
    async blocklist() {
      let that = this;
      await that.$http
        .get("/get_block_list_for_all", {
          params: {
            pageNum: this.blockmedianum,
            pageSize: 5,
          },
        })
        .then((res) => {
          // console.log(res);
          this.listloading2 = false;
          this.translist2 = this.translist2.concat(res.data[0].block_list);
          this.total2 = res.data[0].total_page[0].totalPageNum;
          if (this.nowLang == "cn") {
            for (let j = 0; j < res.data[0].block_list.length + 1; j++) {
              let blocktime = res.data[0].block_list[j].block_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].block_list[j].block_time = "刚刚";
                } else {
                  res.data[0].block_list[j].block_time = fenzhong + "分钟前";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].block_list[j].block_time =
                  parseInt(fenzhong / 60) + "小时前";
              }
              if (fenzhong > 1440) {
                res.data[0].block_list[j].block_time =
                  parseInt(fenzhong / 1440) + "天前";
              }
            }
          } else {
            for (let j = 0; j < res.data[0].block_list.length + 1; j++) {
              let blocktime = res.data[0].block_list[j].block_time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - blocktime; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  res.data[0].block_list[j].block_time = "Just";
                } else {
                  res.data[0].block_list[j].block_time =
                    fenzhong + "Minutes ago";
                }
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                res.data[0].block_list[j].block_time =
                  parseInt(fenzhong / 60) + "Hours ago";
              }
              if (fenzhong > 1440) {
                res.data[0].block_list[j].block_time =
                  parseInt(fenzhong / 1440) + "Days ago";
              }
            }
          }
        })
        .catch((e) => {});
    },
    openPop() {
      this.show_silde = true;
    },
    closePop() {
      this.show_silde = false;
    },
    //获取首页数据
    async indexlist() {
      let that = this;
      await that.$http
        .get("")
        .then((res) => {
          this.loading = false;
          // console.log(res.data[0].get_avgGas_for_100[0].block_height_for_100);
          this.average = res.data[0].get_avgGas_for_100[0].block_height_for_100;
          this.money = res.data[0].usdt[0].usdt;
          this.money2 = res.data[0].usdt[0].rmb;
          // 获取首页数据集合
          var cardleftinformation = res.data[0];
          //console.log(cardleftinformation);
          // 区块高度
          this.blockheigth =
            cardleftinformation.block_height_all[0].block_height;
          // 区块奖励
          this.blockreward =
            cardleftinformation.count_block_award_for_all[0].award_total;
          // 剩余区块奖励
          this.blocklastreward =
            cardleftinformation.count_block_award_for_all[0].award_balance;
          //  交易笔数
          this.transnumber =
            cardleftinformation.transaction_num_for_all[0].transaction_num;
          // 最新交易数据
          this.tableData = cardleftinformation.transaction_info_for_index;
          // 最新出块数据
          this.tableData2 = cardleftinformation.block_new;
          //24小时交易笔数?
          this.transzoom =
            cardleftinformation.transaction_num_for_24h[0].transaction_num;
          // 24小时交易总额?
          this.transmoney =
            cardleftinformation.transaction_amount_for_24h[0].transaction_amount_24h;
        })
        .catch((e) => {});
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
    // 页面的切换选择
    jump(index, title) {
      this.cur = 0;
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
.van-tabs .van-tab__pane {
  width: 100%;
  border-radius: 15px;
}
.van-tab--active {
  font-size: 15px;
  font-family: "苹方-简";
  font-weight: normal;
  color: #333333;
  opacity: 1;
}
.van-tab span {
  border: none;
}
.van-tabs--line .van-tabs__wrap {
  border: none;
}
.van-tabs__nav {
  background: #f5f5f5 !important;
  opacity: 1;
  border: 1px solid transparent;
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
  width: 100%;
  position: absolute;

  top: 55px;
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
.active {
  color: rgba(68, 137, 247, 1) !important;
  width: 60px;
  height: 64px;
  background: rgba(255, 255, 255, 1);
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}
.index {
  width: 100%;
  height: auto;
  background: #f5f5f5;
  .van-tabs__line {
    width: 30px !important;
    left: 30px !important;
  }
  .header_title2 {
    font-size: 18px;
    font-family: "苹方-简";
    font-weight: normal;
    line-height: 33px;
    color: rgba(51, 51, 51, 1);
    opacity: 1;
    position: relative;
    left: 30px;
  }
  .van-list {
    width: 100%;
    border-radius: 15px;
  }
  .van-tabs__line {
    width: 30px;
    height: 0px;
    border: 2px solid rgba(68, 137, 247, 1);
    opacity: 1;
  }
  .van-cell:nth-child(1) {
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
  }
  .van-cell {
    width: 98%;
    height: 170px;
    margin-top: 1px;
    margin: 0 auto;
    background: #f5f5f5;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    padding: 0;
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
        font-size: 14px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 20px;
        opacity: 1;
        position: absolute;
        left: 63px;
        top: 0px;
        p {
          margin-top: 10px;
          span:nth-child(1) {
            display: inline-block;
            width: 80px;
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
  .vancell2 {
    height: 110px;
    .van-cell__value {
      img {
        position: absolute;
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
        top: 0px;
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
  .van-tabs__content {
    width: 93.6%;
    height: auto;
    margin: 0 auto;
    margin-top: 16px;
    border-radius: 15px;
  }
  .van-tab__pane {
    height: auto !important;
  }
  .indexchart {
    width: 93.6%;
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
          left: 15px;
          top: 13px;
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
        left: 10px;
        top: 43px;
      }
    }
    .cardleftbottom {
      width: 100%;
      ul {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
        li {
          width: 110px;
          margin-top: 15px;
          text-align: center;
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
