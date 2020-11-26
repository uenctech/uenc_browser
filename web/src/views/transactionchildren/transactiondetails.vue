<template>
  <div class="transactiondetails">
    <headertop></headertop>
    <div class="transactionzong">
      <!-- 搜索栏区域 -->
      <search @test="ceshi"></search>
      <!-- 内容区域 -->
      <div class="transactioncontent">
        <p class="title">{{ $t("transaction.content[0]") }}</p>
        <br />
        <span class="haxi">{{ shiyan }}</span>
        <span class="yue">{{ $t("transaction.content[3]") }}:</span>
        <span class="yue2">{{ yue }}</span>
        <el-table
          v-loading="loading"
          :data="transactionData"
          style="width: 100%"
          class="addressltable"
          @row-click="gototransactiondetail"
        >
          <el-table-column
            prop="transaction_hash2"
            :label="$t('transaction.content[1]')"
            width="180"
            v-if="tables"
          ></el-table-column>
          <el-table-column
            prop="transaction_hash"
            :label="$t('transaction.content[1]')"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="time"
            :label="$t('publicsection[8]')"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="amount"
            :label="$t('publicsection[5]')"
          ></el-table-column>
          <el-table-column
            prop="from_address"
            :label="$t('publicsection[6]')"
          ></el-table-column>
          <el-table-column
            prop="to_address"
            :label="$t('publicsection[7]')"
          ></el-table-column>
          <el-table-column
            prop="gas"
            :label="$t('transaction.content[2]')"
          ></el-table-column>
        </el-table>
        <div class="block">
          <el-pagination
            :current-page.sync="transmedianum"
            :page-size="20"
            :pager-count="5"
            layout="total, prev, pager, next, jumper"
            :total="totalNum"
            @current-change="change"
            v-if="totalNum != 0"
            ref="transactionpagination"
          ></el-pagination>
          <!-- <span class="shouye" @click="gotofirst" :class="{ blue: blue1 }"
            >{{ $t("page[0]") }}</span
          >
          <span class="weiye" @click="gotolast" :class="{ blue: blue2 }"
            >{{ $t("page[1]") }}</span
          >-->
        </div>
      </div>
      <v-footer></v-footer>
    </div>
  </div>
</template>

<script>
import VFooter from "@components/common/Footer.vue";
import Search from "@components/common/search.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "transaction",
  data() {
    return {
      loading: true,

      shiyan: "",
      tables: false,
      yue: "",
      // 外部公共部分
      language: "",

      // 语言图片显示与隐藏

      choselanguage: ["中文", "EN"],
      nowLang: "",

      fullscreenLoading: false,
      // 分页
      transmedianum: 1,
      totalNum: "",
      transactionData: [],
      blue1: false,
      blue2: false,
    };
  },
  // 页码设置
  watch: {
    transmedianum(val) {
      //console.log(val);
      if (val == 1) {
        this.blue1 = true;
      } else {
        this.blue1 = false;
      }
    },
  },
  components: { VFooter, Search, headertop },
  created() {
    this.nowLang = this.$i18n.locale;

    this.shiyan = this.$route.query.addressvalue;
    this.transmedianum = 1;
    // console.log(this.transmedianum);
    // console.log(this.shiyan);
    this.addresssearch();

    if (this.transmedianum == 1) {
      this.blue1 = true;
    }
  },

  methods: {
    ceshi(msg) {
      // console.log(msg);
      this.shiyan = msg;
      this.addresssearch();
    },
    //地址搜索
    async addresssearch() {
      let that = this;
      var blockData = [];
      await that.$http
        .get("/search_transactionInfo_walletAddress", {
          params: {
            wallet_address: this.shiyan,
            pageNum: this.transmedianum,
            pageSize: 20,
          },
        })
        .then((res) => {
          // console.log(res);
          this.loading = false;
          // console.log(res);
          // console.log(res.data[0].search_wallet_balance_for_walletAddress[0].account_balance);
          // 余额
          this.yue =
            res.data[0].search_wallet_balance_for_walletAddress[0]
              .account_balance + "\n\nUENC";
          // 总条数
          this.totalNum = res.data[0].total_record[0].total_record;
          // // table赋值
          // console.log(
          //   res.data[0].search_transaction_list_for_walletAddress.length
          // );
          var translist = res.data[0].search_transaction_list_for_walletAddress;
          if (this.nowLang == "cn") {
            for (let i = 0; i < translist.length + 1; i++) {
              var obj = {};
              let date = [];
              let strdate = translist[i].time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - strdate; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              // console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  date.push("刚刚");
                } else {
                  date.push(parseInt(fenzhong) + "分钟前");
                }
                obj.time = date;
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                date.push(parseInt(fenzhong / 60) + "小时前");
                obj.time = date;
              }
              if (fenzhong > 1440) {
                date.push(parseInt(fenzhong / 1440) + "天前");
                obj.time = date;
              }
              // date.push(this.timestampToTime(Number(strdate)));
              obj.transaction_hash2 = translist[i].transaction_hash;
              obj.transaction_hash =
                translist[i].transaction_hash.substring(0, 10) + "...";
              // obj.time = this.timestampToTime(Number(strdate));
              obj.amount = translist[i].amount;
              if (
                translist[i].to_address ==
                  "0000000000000000000000000000000000" ||
                translist[i].pledge == "1"
              ) {
                // 从
                obj.from_address =
                  translist[i].from_address.substring(0, 10) + "...";
                if (this.nowLang == "cn") {
                  obj.to_address = "质押";
                } else {
                  obj.to_address = "Pledge";
                }
              } else if (
                translist[i].from_address == translist[i].to_address ||
                translist[i].redeem == "1"
              ) {
                if (this.nowLang == "cn") {
                  // 从
                  obj.from_address = "质押";
                } else {
                  obj.from_address = "Pledge";
                }
                // 至
                obj.to_address =
                  translist[i].to_address.substring(0, 10) + "...";
              } else {
                obj.from_address =
                  translist[i].from_address.substring(0, 10) + "...";
                obj.to_address =
                  translist[i].to_address.substring(0, 10) + "...";
              }
              // obj.to_address = translist[i].to_address.substring(0, 10) + "...";
              obj.gas = translist[i].gas;
              // console.log(obj);
              blockData[i] = obj;
              //console.log(blockData);
              this.transactionData = blockData;
              // console.log(obj);
              // console.log(this.transactionData);
            }
          } else {
            for (let i = 0; i < translist.length + 1; i++) {
              var obj = {};
              let date = [];
              let strdate = translist[i].time;
              let timestamp = Date.parse(new Date()) / 1000;
              let s = timestamp - strdate; //9.20
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              // console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  date.push("just");
                } else {
                  date.push(parseInt(fenzhong) + "minutes ago");
                }
                obj.time = date;
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                date.push(parseInt(fenzhong / 60) + "hour ago");
                obj.time = date;
              }
              if (fenzhong > 1440) {
                date.push(parseInt(fenzhong / 1440) + "days ago");
                obj.time = date;
              }
              // date.push(this.timestampToTime(Number(strdate)));
              obj.transaction_hash2 = translist[i].transaction_hash;
              obj.transaction_hash =
                translist[i].transaction_hash.substring(0, 10) + "...";
              // obj.time = this.timestampToTime(Number(strdate));
              obj.amount = translist[i].amount;
              obj.from_address =
                translist[i].from_address.substring(0, 10) + "...";
              obj.to_address = translist[i].to_address.substring(0, 10) + "...";
              obj.gas = translist[i].gas;
              // console.log(obj);
              blockData[i] = obj;
              //console.log(blockData);
              this.transactionData = blockData;
              // console.log(obj);
              // console.log(this.transactionData);
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

    // 页码设置
    // 去首页
    gotofirst() {
      this.transmedianum = 1;
      this.blue2 = false;
      this.blue1 = true;
      this.transactionlist();
    },
    // 去尾页
    gotolast() {
      this.blue1 = false;
      this.blue2 = true;
      //console.log(parseInt(this.totalNum / 20));
      if (this.totalNum % 20 == 0) {
        this.transmedianum = this.totalNum / 20;
      } else {
        this.transmedianum = parseInt(this.totalNum / 20) + 1;
      }
      //console.log(this.blockmedianum );
      this.transactionlist();
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
    change(val) {
      //console.log(val);
      this.transmedianum = val;
      //console.log(this.medianum);
      this.setContextData("currentpage2", this.transmedianum);
      this.addresssearch();
    },
  },
};
</script>
<style lang="less">
.blue {
  color: rgba(40, 96, 194, 1) !important;
}
.transaction .transactioncontent .block .el-pagination__jump {
  font-size: 16px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 22px;
  color: rgba(102, 102, 102, 1);
  opacity: 1;
}
// 页码全局设置
.el-dialog,
.el-pager li {
  background: rgba(40, 96, 194, 0.01);
}
.el-pagination .btn-next,
.el-pagination .btn-prev {
  background: none;
}
.el-pagination button:disabled {
  background: none;
}
.sticky {
  width: 1200px !important;
  height: 120px !important;
  position: fixed;
  top: 0px;
  margin: 0 auto !important;
}

// 本页面
.transactiondetails {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  margin-bottom: 20px;
  opacity: 1;
  border-radius: 40px;
  .transactionzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }

  // 内容部分
  .transactioncontent {
    width: 1120px;
    height: 1298.5px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    .haxi {
      position: relative;
      left: 42px;
      top: 30px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
    }
    .yue {
      position: relative;
      left: 224px;
      top: 30px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(51, 51, 51, 1);
    }
    .yue2 {
      position: relative;
      left: 254px;
      top: 30px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(51, 51, 51, 1);
    }
    .el-table__header-wrapper {
      background-color: #2860c2 !important;
      width: 100%;
      border-radius: 15px;
    }
    .el-table__body tr td {
      text-align: center;
    }
    .el-table td,
    .el-table th.is-leaf {
      border-bottom: 1px solid gray;
    }
    .has-gutter {
      background-color: #2860c2 !important;
      opacity: 0.8;
      outline: none;
      border: none;
    }
    .has-gutter tr {
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
      th div {
        text-align: center;
      }
    }
    .el-table th,
    .el-table tr {
      background-color: #d5e1f4;
    }
    .title {
      position: relative;
      left: 42px;
      top: 30px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
    }
    .addressltable {
      position: relative;
      width: 1040px !important;
      height: 1069px;
      top: 50px;
      background: rgba(40, 96, 194, 0.2);
      margin: 0 auto;
      border-top-left-radius: 15px !important;
      border-top-right-radius: 15px !important;
      cursor: pointer;
      .el-table__row {
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
        height: 51px;
      }
    }
    // 页码设置
    .block {
      position: relative;
      top: 50px;
      width: 1040px !important;
      height: 64px;
      line-height: 64px;
      background: rgba(40, 96, 194, 0.1);
      margin: 0 auto;
      padding-left: 30%;
      border-top-left-radius: 0px;
      border-top-right-radius: 0px;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      //.el-pagination__total {
      // position: absolute;
      // top: 21px;
      // left: 188px;
      //   font-size: 16px;
      //   font-family: "苹方-简";
      //   font-weight: normal;
      //   line-height: 22px;
      //   color: rgba(40, 96, 194, 1);
      //   opacity: 1;
      // }
      .el-pagination {
        position: relative;
        top: 18px;
      }
      .shouye {
        position: absolute;
        top: 21px;
        left: 309px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(102, 102, 102, 1);
        opacity: 1;
      }
      // .btn-prev {
      //   position: absolute;
      //   top: 21px;
      //   left: 371px;
      // }
      // .el-pager {
      //   position: relative;
      //   top: 19px;
      //   left: 62px;
      // }
      // .btn-next {
      //   position: relative;
      //   top: 19px;
      //   left: 60px;
      // }
      .weiye {
        position: absolute;
        top: 21px;
        left: 600px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(102, 102, 102, 1);
        opacity: 1;
      }
      // .el-pagination__jump {
      //   position: relative;
      //   top: 15px;
      //   left: 182px;
      // }
    }
  }
}
</style>
