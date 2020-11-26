<template>
  <div class="searchblockdetail">
    <headertop></headertop>
    <div class="searchblockdetailzong">
      <!-- 搜索栏区域 -->
      <search ref="searchheight" @test="ceshi"></search>
      <div class="detailtop">
        <p>{{ $t("publicsection[3]") }}</p>
        <br />
        <ul>
          <li>
            <div class="deatillitop">
              <img
                src="../../assets/images/blockdetail/组 32.png"
                class="leftright left"
                @click="zijian"
              />
              <span class="linumber linumber1">{{
                datalist[0].block_height
              }}</span>
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
            <div class="deatillitop">
              <span class="linumber">{{ datalist[0].transaction_award }}</span>
            </div>
            <div class="detaillifooter">
              <img src="../../assets/images/blockdetail/区块奖励.png" alt />
              <span>{{ $t("home.cardleft[2]") }}</span>
            </div>
          </li>
          <li>
            <div class="deatillitop">
              <span class="linumber">{{ datalist[0].transaction_num }}</span>
            </div>
            <div class="detaillifooter">
              <img src="../../assets/images/blockdetail/交易.png" alt />
              <span>{{ $t("publicsection[4]") }}</span>
            </div>
          </li>
          <li>
            <div class="deatillitop">
              <span class="linumber">{{ datalist[0].transaction_amount }}</span>
            </div>
            <div class="detaillifooter">
              <img src="../../assets/images/blockdetail/交易总额.png" alt />
              <span>{{ $t("block.content2[1]") }}</span>
            </div>
          </li>
        </ul>
      </div>
      <!-- 内容区域 -->
      <div class="detailcontent">
        <p class="title">{{ $t("block.content[0]") }}</p>
        <el-table
          v-loading="loading"
          :data="detailData"
          style="width: 100%"
          class="addressltable"
          @row-click="gotoblockdetails"
        >
          <el-table-column
            prop="block_hash2"
            :label="$t('block.content2[3]')"
            v-if="tables"
          ></el-table-column>
          <el-table-column
            prop="block_hash"
            :label="$t('block.content2[3]')"
          ></el-table-column>
          <el-table-column
            prop="time"
            :label="$t('publicsection[8]')"
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
            prop="transaction_amount"
            :label="$t('publicsection[5]')"
          ></el-table-column>
        </el-table>
        <div class="block">
          <el-pagination
            :current-page.sync="blockmedianum"
            :page-size="20"
            :pager-count="5"
            layout="total,  prev, pager, next, jumper"
            :total="totalNum"
            @current-change="change"
            v-if="totalNum != 0"
            ref="pagination"
          ></el-pagination>
          <!-- <span class="shouye" @click="gotofirst" :class="{ blue: blue1 }">{{
            $t("page[0]")
          }}</span>
          <span class="weiye" @click="gotolast" :class="{ blue: blue2 }">{{
            $t("page[1]")
          }}</span> -->
        </div>
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
  name: "searchblockdetail",
  data() {
    return {
      loading: true,
      shiyan: "",
      tables: false,

      blockmedianum: "",
      // 外部公共部分
      nowLang: "",
      fullscreenLoading: false,

      language: "",

      totalNum: "",
      blue1: false,
      blue2: false,
      // 语言图片显示与隐藏

      choselanguage: ["中文", "EN"],
      count: this.$store.state.count,
      detailData: [],
      datalist: [
        {
          block_height: "", //高度
          transaction_award: "", // 区块奖励
          transaction_num: "", // 交易笔数
          transaction_amount: "", // 交易总额
        },
      ],
      searchblock_height: [{ block_award: "" }],
      searchblock_list: [],
    };
  },
  components: { VFooter, Search, headertop },
  watch: {
    shiyan(newName, oldName) {
      // console.log(newName, oldName);
      if (newName !== oldName) {
        this.shiyan = newName;
        this.blocksearch();
      }
    },
    blockmedianum(val) {
      //console.log(val);
      if (val == 1) {
        this.blue1 = true;
      } else {
        this.blue1 = false;
      }
    },
  },
  created() {
    // console.log(this.$refs);
    this.nowLang = this.$i18n.locale;

    this.blockmedianum = 1;
    // console.log(this.blockmedianum);
    this.shiyan = this.$route.query.blockheight;
    // console.log(this.shiyan);
    // console.log(this.blockmedianum);
    if (this.blockmedianum == 1) {
      this.blue1 = true;
    }
    this.blocksearch();
  },

  methods: {
    ceshi(msg) {
      // console.log(msg);
      this.shiyan = msg;
      this.blocksearch();
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
            pageSize: 20,
          },
        })
        .then((res) => {
          this.loading = false;
          //  console.log(res);
          this.totalNum = res.data[0].total_record[0].total_record;
          // console.log(this.totalNum);
          //console.log(res.data[0].block_list);
          // 高度
          this.datalist[0].block_height =
            res.data[0].block_height[0].block_height;
          // 区块奖励
          this.datalist[0].transaction_award =
            res.data[0].block_height[0].block_award;
          // 交易笔数
          this.datalist[0].transaction_num = res.data[0].block_height[0].tx_num;
          // 交易总额
          this.datalist[0].transaction_amount = res.data[0].block_height[0].transaction_amount.toLocaleString();
          // table赋值
          //console.log(res.data[0].block_list.length);
          for (let i = 0; i < res.data[0].block_list.length + 1; i++) {
            var obj = {};
            //console.log(res.data[0].transaction_hash);
            //console.log(res.data[0].from_address);
            obj.block_hash2 = res.data[0].block_list[i].block_hash;
            obj.block_hash =
              res.data[0].block_list[i].block_hash.substring(0, 10) + "...";
            obj.time = this.timestampToTime(
              Number(res.data[0].block_list[i].time)
            );

            obj.transaction_amount =
              res.data[0].block_list[i].transaction_amount;
            if (
              res.data[0].block_list[i].to_address ==
                "0000000000000000000000000000000000" ||
              res.data[0].block_list[i].pledge == "1"
            ) {
              // 从
              obj.from_address =
                res.data[0].block_list[i].from_address.substring(0, 10) + "...";
              if (this.nowLang == "cn") {
                obj.to_address = "质押";
              } else {
                obj.to_address = "Pledge";
              }
            } else if (
              res.data[0].block_list[i].from_address ==
                res.data[0].block_list[i].to_address ||
              res.data[0].block_list[i].redeem == "1"
            ) {
              if (this.nowLang == "cn") {
                // 从
                obj.from_address = "质押";
              } else {
                obj.from_address = "Pledge";
              }
              // 至
              obj.to_address =
                res.data[0].block_list[i].to_address.substring(0, 10) + "...";
            } else {
              obj.from_address =
                res.data[0].block_list[i].from_address.substring(0, 10) + "...";
              obj.to_address =
                res.data[0].block_list[i].to_address.substring(0, 10) + "...";
            }
            obj.gas = res.data[0].block_list[i].gas;
            // console.log(obj);
            blockData[i] = obj;
            //console.log(blockData);
            this.detailData = blockData;
            //console.log(obj);
            //console.log(this.transactionData);
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    // 点击表格行显示数据
    gotoblockdetails(row, event, column) {
      this.$router.push({
        path: "/blockdetails",
        query: {
          // 高度
          blockhaxi: row.block_hash2,
        },
      });
      // console.log(row, event, column);
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
    // 页码设置
    // 去首页
    gotofirst() {
      this.blockmedianum = 1;
      this.blue2 = false;
      this.blue1 = true;
      this.blocksearch();
    },
    // 去尾页
    gotolast() {
      this.blue1 = false;
      this.blue2 = true;
      //console.log(parseInt(this.totalNum / 20));
      if (this.totalNum % 20 == 0) {
        this.blockmedianum = this.totalNum / 20;
      } else {
        this.blockmedianum = parseInt(this.totalNum / 20) + 1;
      }
      //console.log(this.blockmedianum );
      this.blocksearch();
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
      // console.log(val);
      this.blockmedianum = val;
      //console.log(this.medianum);
      this.blocksearch();
      this.setContextData("currentpage1", this.blockmedianum);
    },
    zijian() {
      // console.log('-');
      this.shiyan = Number(this.shiyan) - Number(1);
      // console.log(this.shiyan);
      if (this.shiyan <= 0) {
        this.shiyan = 0;
      }
      this.blocksearch();
    },
    zijia() {
      // console.log('+');
      this.shiyan = Number(this.shiyan) + Number(1);
      // console.log(this.shiyan);
      this.blocksearch();
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
.searchblockdetail {
  width: 1200px;
  opacity: 1;
  border-radius: 40px;
  height: auto;
  margin: 0 auto;
  .searchblockdetailzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }
  .detailtop {
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
  .detailcontent {
    width: 1120px;
    height: 1250.5px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    margin-top: 20px;
    .el-table th,
    .el-table tr {
      background-color: rgba(40, 96, 194, 0.1);
    }
    .has-gutter tr {
      background-color: rgba(40, 96, 194, 0.3) !important;
      border-radius: 15px;
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
      border-bottom-left-radius: 15px !important;
      border-bottom-right-radius: 15px !important;
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
    .addressltable {
      position: relative;
      width: 1040px !important;
      height: 1069px;
      top: 50px;
      background: rgba(40, 96, 194, 0.2);
      margin: 0 auto;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
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
      background: #d4dff3;
      margin: 0 auto;
      padding-left: 30%;
      border-top-left-radius: 0px;
      border-top-right-radius: 0px;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      .el-pagination {
        position: relative;
        top: 18px;
      }
      .el-pagination__total {
        // position: absolute;
        // top: 21px;
        left: 188px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        // color: rgba(40, 96, 194, 1);
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
