<template>
  <div class="blockdetails">
   <headertop></headertop>
    <div class="blockdetailzong">
      <!-- 搜索栏区域 -->
      <search @test="ceshi"></search>
      <div class="detailstop">
        <p>{{ $t("publicsection[3]") }}</p>
        <ul>
          <li>
            <div class="deatillitop">
              <img
                src="../../assets/images/blockdetail/组 32.png"
                class="leftright left"
                @click="zijian"
              />
              <span class="linumber linumber1">
                {{ blockdetailslist[0].block_height }}
              </span>
              <img
                src="../../assets/images/blockdetail/组 33.png"
                class="leftright right"
                @click="zijia"
              />
            </div>
            <div class="detaillifooter">
              <img src="../../assets/images/blockdetail/区块高度.png" alt />
              <span>{{ $t("publicsection[3]") }}</span>
            </div>
          </li>
          <li>
            <p>
              {{ $t("publicsection[3]") }}:{{
                blockdetailslist[0].block_height
              }}
            </p>
            <p>
              {{ $t("publicsection[8]") }}:{{ blockdetailslist[0].block_time }}
            </p>
            <p>
              {{ $t("block.content3[0]") }}:{{ blockdetailslist[0].prevHash }}
            </p>
          </li>
        </ul>
      </div>
      <!-- 内容区域 -->
      <div class="detailscontent">
        <p class="title">
          {{ $t("transaction.content[0]") }}{{ $route.query.height }}
        </p>
        <table cellspacing="0" v-loading="loading">
          <thead>
            <tr class="tableheader">
              <td>{{ $t("transaction.content[1]") }}</td>
              <td>{{ $t("publicsection[6]") }}</td>
              <td>{{ $t("publicsection[7]") }}</td>
              <td>{{ $t("publicsection[5]") }}</td>
              <td>{{ $t("transaction.content[2]") }}</td>
              <td>{{ $t("home.cardleft[2]") }}</td>
            </tr>
          </thead>
          <tbody>
            <tr @click="gutotransactiondetail">
              <td v-if="tables">{{ maininfo[0].transaction_hash2 }}</td>
              <td>{{ maininfo[0].transaction_hash }}</td>
              <td>{{ maininfo[0].from_address }}</td>
              <td>{{ maininfo[0].to_address }}</td>
              <td>{{ maininfo[0].transaction_amount }}</td>
              <td>{{ gasinfo[0].transaction_gas }}</td>
              <td>{{ awardinfo[0].transaction_award }}</td>
            </tr>
            <tr @click="gutotransactiondetail2">
              <td v-if="tables">{{ gasinfo[0].transaction_hash2 }}</td>
              <td>{{ gasinfo[0].transaction_hash }}</td>
              <td>{{ gasinfo[0].from_address }}</td>
              <td>
                {{ gasinfo[0].sign_node }}
                <!-- <br />
                {{ gasinfo[0].sign_node2 }} -->
              </td>
              <td></td>
              <td>{{ gasinfo[0].transaction_gas }}</td>
              <td></td>
            </tr>
            <tr @click="gutotransactiondetail3">
              <td v-if="tables">{{ awardinfo[0].transaction_hash2 }}</td>
              <td>{{ awardinfo[0].transaction_hash }}</td>
              <td></td>
              <td>
                {{ awardinfo[0].sign_node }}
                <br />
                {{ awardinfo[0].sign_node2 }}
              </td>
              <td></td>
              <td></td>
              <td>{{ awardinfo[0].transaction_award }}</td>
            </tr>
          </tbody>
        </table>

        <!-- <el-table :data="detailData" style="width: 100%" class="addressltable">
          <el-table-column
            prop="qukuaihaxi"
            :label="$t('block.content2[3]')"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="cong"
            :label="$t('publicsection[6]')"
          ></el-table-column>
          <el-table-column
            prop="zhi"
            :label="$t('publicsection[7]')"
          ></el-table-column>
          <el-table-column
            prop="jiaoyie"
            :label="$t('publicsection[5]')"
          ></el-table-column>
           <el-table-column
            prop="jiaoyie"
            :label="$t('transaction.content[2]')"
          ></el-table-column>
           <el-table-column
            prop="jiaoyie"
            :label="$t('block.content2[0]')"
          ></el-table-column>
        </el-table>-->
        <!-- <div class="block">
          <el-pagination
            :current-page.sync="medianum"
            :page-size="20"
            :pager-count="5"
            layout="total,  prev, pager, next, jumper"
            :total="totalNum"
            @current-change="change"
            v-if="totalNum != 0"
            ref="pagination"
          ></el-pagination>
          <span class="shouye">{{ $t("page[0]") }}</span>
          <span class="weiye">{{ $t("page[1]") }}</span>
        </div>-->
      </div>
      <v-footer></v-footer>
    </div>
  </div>
</template>

<script>
import bus from "@/bus.js";
import VFooter from "@components/common/Footer.vue";
import Search from "@components/common/search.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "blockdetail",
  data() {
    return {
      loading: true,
     
      shiyan: "",
      tables: false,
      // 外部公共部分
      nowLang: "",
      fullscreenLoading: false,
    
      language: "",
     
      // 语言图片显示与隐藏
     
      height: "",
      choselanguage: ["中文", "EN"],
      detailData: [],
      blockdetailslist: [{ block_height: "", block_time: "", prevHash: "" }],
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
  components: { VFooter, Search,headertop },
  created() {
    this.nowLang = this.$i18n.locale;
   
    this.shiyan = this.$route.query.blockhaxi;
    this.medianum = this.getContextData("currentpage1") || 1;
    this.blockhaxisearch();
   
  },
 
  methods: {
    gutotransactiondetail() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.maininfo[0].transaction_hash2 },
      });
    },
    gutotransactiondetail2() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.gasinfo[0].transaction_hash2 },
      });
    },
    gutotransactiondetail3() {
      this.$router.push({
        path: "/transactiondetail",
        query: { transaction_hash: this.awardinfo[0].transaction_hash2 },
      });
    },
    ceshi(msg) {
      // console.log(msg);
      this.shiyan = msg;
      this.blockhaxisearch();
    },
    // 区块哈希搜索
    async blockhaxisearch() {
      let that = this;
      var blockData = [];
      await that.$http
        .get("/search_blockInfo_blockHash", {
          params: {
            block_hash: this.shiyan,
          },
        })
        .then((res) => {
          // console.log(res);
          this.loading = false;
          // console.log(res.data[0].search_blockInfo);
          var common = res.data[0].search_blockInfo[0];
          // 区块高度
          this.blockdetailslist[0].block_height = common.block_height;
          // console.log(this.blockdetailslist[0].block_height);
          // 时间
          this.blockdetailslist[0].block_time = this.timestampToTime(
            Number(common.block_time)
          );
          // 前置哈希
          this.blockdetailslist[0].prevHash = common.prevHash;
          // // table赋值
          // 第一行
          this.maininfo[0].transaction_hash2 =
            res.data[0].search_main_transactionInfo[0].transaction_hash;
          this.maininfo[0].transaction_hash =
            res.data[0].search_main_transactionInfo[0].transaction_hash.substring(
              0,
              10
            ) + "...";
          // console.log(this.maininfo[0].transaction_hash2);
          // console.log(this.maininfo[0].transaction_hash);
          if (
            res.data[0].search_main_transactionInfo[0].to_address ==
              "0000000000000000000000000000000000" ||
            res.data[0].search_main_transactionInfo[0].pledge == "1"
          ) {
            // 从
            this.maininfo[0].from_address =
              res.data[0].search_main_transactionInfo[0].from_address.substring(
                0,
                10
              ) + "...";
            if (this.nowLang == "cn") {
              this.maininfo[0].to_address = "质押";
            } else {
              this.maininfo[0].to_address = "Pledge";
            }
          } else if (
            res.data[0].search_main_transactionInfo[0].from_address ==
              res.data[0].search_main_transactionInfo[0].to_address ||
            res.data[0].search_main_transactionInfo[0].redeem == "1"
          ) {
            if (this.nowLang == "cn") {
              // 从
              this.maininfo[0].from_address = "质押";
            } else {
              this.maininfo[0].from_address = "Pledge";
            }
            // 至
            this.maininfo[0].to_address =
              res.data[0].search_main_transactionInfo[0].to_address.substring(
                0,
                10
              ) + "...";
          } else {
            this.maininfo[0].from_address =
              res.data[0].search_main_transactionInfo[0].from_address.substring(
                0,
                10
              ) + "...";
            this.maininfo[0].to_address =
              res.data[0].search_main_transactionInfo[0].to_address.substring(
                0,
                10
              ) + "...";
          }
          this.maininfo[0].transaction_amount =
            res.data[0].search_main_transactionInfo[0].transaction_amount;
          // 第二行
          this.gasinfo[0].from_address =
            res.data[0].search_gas_transactionInfo[0].from_address.substring(
              0,
              10
            ) + "...";
          this.gasinfo[0].transaction_hash2 =
            res.data[0].search_gas_transactionInfo[0].transaction_hash;
          this.gasinfo[0].transaction_hash =
            res.data[0].search_gas_transactionInfo[0].transaction_hash.substring(
              0,
              10
            ) + "...";
          this.gasinfo[0].sign_node =
            res.data[0].search_gas_transactionInfo[0].sign_node.substring(
              0,
              35
            ) + "...";
          this.gasinfo[0].sign_node2 =
            res.data[0].search_gas_transactionInfo[0].sign_node.substring(
              35,
              45
            ) + "...";
          // this.gasinfo[0].sign_node = res.data[0].search_gas_transactionInfo[0].sign_node.substring(
          //   0,
          //   34
          // );
          // this.gasinfo[0].sign_node2 = res.data[0].search_gas_transactionInfo[0].sign_node.substring(
          //   35
          // );
          this.gasinfo[0].transaction_gas =
            res.data[0].search_gas_transactionInfo[0].transaction_gas;
          // 第三行
          this.awardinfo[0].transaction_hash2 =
            res.data[0].search_award_transactionInfo[0].transaction_hash;
          // console.log(this.awardinfo[0].transaction_hash2);
          this.awardinfo[0].transaction_hash =
            res.data[0].search_award_transactionInfo[0].transaction_hash.substring(
              0,
              10
            ) + "...";
          this.awardinfo[0].sign_node =
            res.data[0].search_award_transactionInfo[0].sign_node.substring(
              0,
              10
            ) + "...";
          this.awardinfo[0].sign_node2 =
            res.data[0].search_award_transactionInfo[0].sign_node.substring(
              35,
              45
            ) + "...";
          // this.awardinfo[0].sign_node = res.data[0].search_award_transactionInfo[0].sign_node.substring(
          //   0,
          //   34
          // );
          // this.awardinfo[0].sign_node2 = res.data[0].search_award_transactionInfo[0].sign_node.substring(
          //   35
          // );
          this.awardinfo[0].transaction_award =
            res.data[0].search_award_transactionInfo[0].transaction_award;
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
    change(val) {
      //console.log(val);
      this.medianum = val;
      //console.log(this.medianum);
      this.blockhaxisearch();
      this.setContextData("currentpage1", this.medianum);
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
    
   
  },
 
};
</script>
<style lang="less">
th div {
  text-align: center;
}
.el-table__body tr td {
  text-align: center;
}
.transaction .transactioncontent .block .el-pagination__jump {
  font-size: 16px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 22px;
  color: rgba(102, 102, 102, 1);
  opacity: 1;
}
.blue {
  color: rgba(40, 96, 194, 1) !important;
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
// 本页面
.blockdetails {
  width: 1200px;
  opacity: 1;
  border-radius: 40px;
  height: auto;
  margin: 0 auto;
  .blockdetailzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }

  .detailstop {
    width: 1120px;
    height: 256px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    position: relative;
    p {
      position: relative;
      left: 40px;
      top: 30px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
    }
    ul {
      position: relative;
      left: 40px;
      top: 58px;
      display: flex;
      flex-direction: row;
      li:nth-child(2) {
        width: 785px;
        height: 138px;
        background: rgba(232, 234, 243, 1);
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        opacity: 1;
        border-radius: 20px;
        p {
          font-size: 16px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 22px;
          color: rgba(51, 51, 51, 1);
          opacity: 1;
        }
      }
      li {
        width: 235px;
        height: 138px;
        background: rgba(232, 234, 243, 1);
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        opacity: 1;
        border-radius: 20px;
        margin-left: 20px;
        // 左右箭头
        .leftright {
          width: 9.83px;
          height: 16.83px;
          position: relative;
          top: 10px !important;
          cursor: pointer;
        }
        .left {
          left: 30px;
        }
        .right {
          left: 58px;
        }
        .linumber {
          font-size: 40px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 56px;
          color: rgba(51, 51, 51, 1);
          opacity: 1;
          position: relative;
          left: 30px;
          top: 16px;
        }
        .linumber1 {
          position: relative;
          left: 49px;
          top: 16px;
        }
        img {
          width: 22.82px;
          height: 22.82px;
          position: relative;
          left: 30px;
          top: 29px;
        }
        .detaillifooter span {
          position: relative;
          left: 38px;
          top: 20px;
          font-size: 16px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 22px;
          color: rgba(102, 102, 102, 1);
          opacity: 1;
        }
      }
      li:nth-child(1) {
        margin-left: 0px;
      }
    }
  }
  .detailscontent {
    width: 1120px;
    height: 1250.5px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    margin-top: 20px;
    table {
      width: 1040px;
      height: 200px;
      position: relative;
      top: 60px;
      margin: 0 auto;
      tr {
        height: 50px;
        cursor: pointer;
      }
      tbody tr:hover {
        background-color: rgba(255, 255, 255, 1);
      }
      .tableheader {
        background-color: #b2c7ea;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
        td:nth-child(1) {
          border-top-left-radius: 15px;
        }
        td:nth-child(6) {
          border-top-right-radius: 15px;
        }
      }
      tbody td {
        border-bottom: 1px solid rgba(102, 102, 102, 0.1);
      }
      tr {
        text-align: center;
        background-color: #d4dff3;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
      }
    }
    .el-table th,
    .el-table tr {
      background-color: #d5e1f4;
    }

    .has-gutter {
      background-color: #2860c2 !important;
      opacity: 0.8;
      outline: none;
      border: none;
    }
    .el-table__header-wrapper {
      background-color: #2860c2 !important;
      width: 100%;
      border-radius: 15px;
    }
    .has-gutter tr {
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
      th div {
        // text-align: center;
      }
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
      .el-pagination__total {
        position: absolute;
        top: 21px;
        left: 188px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
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
      .btn-prev {
        position: absolute;
        top: 21px;
        left: 371px;
      }
      .el-pager {
        position: relative;
        top: 19px;
        left: 62px;
      }
      .btn-next {
        position: relative;
        top: 19px;
        left: 60px;
      }
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
      .el-pagination__jump {
        position: relative;
        top: 15px;
        left: 182px;
      }
    }
  }
}
</style>
