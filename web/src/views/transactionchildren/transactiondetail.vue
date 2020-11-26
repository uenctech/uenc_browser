<template>
  <div class="transactiondetail">
    <div
      v-html="transactionlist[0].from_address2"
      v-if="showmore3"
      id="from_information"
    ></div>
    <img
      src="../../assets/images/index/组 2.png"
      v-if="showmore3"
      @click="showmoredisplay3"
      id="from_information2"
    />
    <div
      v-html="transactionlist[0].to_address2"
      v-if="showmore"
      id="address_information"
    ></div>
    <img
      src="../../assets/images/index/组 2.png"
      v-if="showmore"
      @click="showmoredisplay"
      id="address_information2"
    />
    <div
      v-html="transactionlist[0].amount_detail2"
      v-if="showmore2"
      id="detail_information"
    ></div>
    <img
      src="../../assets/images/index/组 2.png"
      v-if="showmore2"
      @click="showmoredisplay2"
      id="detail_information2"
    />
    <headertop></headertop>
    <div class="transactiondetailzong">
      <!-- 搜索栏区域 -->
      <search @test="ceshi"></search>
      <div class="detailcontent">
        <div class="linezong">
          <div class="line line1" v-show="line1"></div>
          <div class="line line2" v-show="line2"></div>
          <div class="line line3" v-show="line3"></div>
        </div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane :label="$t('transaction.content2[2]')" name="first">
            <div class="jiaoyileft">
              <img
                src="../../assets/images/transaction/组 32.png"
                class="leftimg1 leftimg"
                @click="zijian"
              />
              <span class="leftspan1">{{
                transactionlist[0].block_height
              }}</span>
              <img
                src="../../assets/images/transaction/组 33.png"
                class="leftimg2 leftimg"
                @click="zijia"
              />
              <img
                src="../../assets/images/transaction/区块高度.png"
                class="leftimg3"
              />
              <span class="leftspan2">{{ $t("publicsection[3]") }}</span>
            </div>
            <div class="jiaoyiright">
              <div class="jiaoyirightcon">
                <div>
                  <p>{{ $t("transaction.content[1]") }}：</p>
                  <p>
                    {{ transactionlist[0].transaction_hash }}
                  </p>
                </div>
                <div>
                  <p>{{ $t("block.content2[3]") }}：</p>
                  <p>
                    {{ transactionlist[0].block_hash }}
                  </p>
                </div>
                <div>
                  <p>{{ $t("transaction.content2[5]") }}：</p>
                  <p>{{ transactionlist[0].transaction_time }}</p>
                </div>
                <div>
                  <p>{{ $t("publicsection[6]") }}:</p>
                  <p
                    class="toright"
                    v-html="transactionlist[0].from_address"
                  ></p>
                </div>
                <button
                  v-if="from_detail"
                  @click="showMoreInformation3"
                  class="more_button"
                >
                  {{ $t("footerlast[2]") }}
                </button>
                <!-- 去的地方 -->
                <div>
                  <p>{{ $t("publicsection[7]") }}:</p>
                  <p class="toright" v-html="transactionlist[0].to_address"></p>
                </div>

                <button
                  v-if="amount_detail"
                  @click="showMoreInformation"
                  class="more_button"
                >
                  {{ $t("footerlast[2]") }}
                </button>
                <!-- 交易明细 -->
                <div v-if="amount_detail">
                  <p>{{ $t("publicsection[12]") }}:</p>
                  <p
                    class="toright"
                    v-html="transactionlist[0].amount_detail"
                  ></p>
                </div>
                <div v-else></div>
                <button
                  v-if="amount_detail"
                  @click="showMoreInformation2"
                  class="more_button"
                >
                  {{ $t("footerlast[3]") }}
                </button>
                <div>
                  <p>{{ $t("publicsection[5]") }}:</p>
                  <p>{{ transactionlist[0].transaction_amount }}</p>
                </div>
                <div>
                  <p>{{ $t("transaction.content2[0]") }}</p>
                  <p>{{ transactionlist[0].extra }}</p>
                </div>
                <div id="big">
                  <p>{{ $t("transaction.content2[1]") }}</p>
                  <p>
                    {{ transactionlist[0].sign_node }}
                  </p>
                </div>
                <div>
                  <p>{{ $t("transaction.content[2]") }}：</p>
                  <p>{{ transactionlist[0].gas }}</p>
                </div>
                <div>
                  <p>{{ $t("block.content2[0]") }}：</p>
                  <p>{{ transactionlist[0].award }}</p>
                </div>
              </div>
            </div>
          </el-tab-pane>
          <el-tab-pane :label="$t('transaction.content2[3]')" name="second">
            <p>
              {{ $t("transaction.content[1]") }}:
              {{ transactionlist[0].transaction_hash2 }}
            </p>
            <div class="secondcontent">
              <el-table
                v-loading="loading"
                :data="detail1Data"
                style="width: 100%"
                class="addressltable"
                :span-method="arraySpanMethod"
                max-height="500"
              >
                <el-table-column
                  prop="transaction_time"
                  :label="$t('publicsection[8]')"
                  width="180"
                ></el-table-column>
                <el-table-column
                  prop="gas"
                  :label="$t('transaction.content[2]')"
                  width="120"
                ></el-table-column>
                <el-table-column
                  prop="sign_node"
                  :label="$t('transaction.content2[6]')"
                ></el-table-column>
                <el-table-column
                  prop="detail"
                  :label="$t('transaction.content2[7]')"
                ></el-table-column>
              </el-table>
            </div>
          </el-tab-pane>
          <el-tab-pane :label="$t('transaction.content2[4]')" name="third">
            <p>
              {{ $t("transaction.content[1]") }}:
              {{ transactionlist[0].transaction_hash3 }}
            </p>
            <div class="secondcontent2">
              <el-table
                v-loading="loading"
                :data="detail2Data"
                style="width: 100%"
                class="addressltable2"
                :span-method="arraySpanMethod"
                max-height="500"
              >
                <el-table-column
                  prop="transaction_time"
                  :label="$t('publicsection[8]')"
                  width="180"
                ></el-table-column>
                <el-table-column
                  prop="award"
                  :label="$t('home.cardleft[2]')"
                  width="180"
                ></el-table-column>
                <el-table-column
                  prop="sign_node"
                  :label="$t('transaction.content2[6]')"
                  width="400"
                ></el-table-column>
                <el-table-column
                  prop="detail"
                  :label="$t('transaction.content2[7]')"
                ></el-table-column>
              </el-table>
            </div>
          </el-tab-pane>
        </el-tabs>
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
      showmore: false,
      showmore2: false,
      showmore3: false,
      visible: false,
      collength: "",
      loading: true,
      sticky: false,
      shiyan: "",
      // 外部公共部分
      fullscreenLoading: false,
      cur: "",
      language: "",
      nowLang: "",
      chose: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      activeName: "",
      line1: false,
      line2: false,
      line3: false,
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
          from_address2: "",
          to_address: "",
          to_address2: "",
          amount_detail: "",
          amount_detail2: "",
          transaction_amount: "",
          extra: "",
          sign_node: "",
          gas: "",
          award: "",
        },
      ],
      detail1Data: [],
      detail2Data: [],
      // 交易详情
      amount_detail: false,
      from_detail: false,
    };
  },
  components: { VFooter, Search, headertop },
  created() {
    this.nowLang = this.$i18n.locale;
    this.line1 = true;
    this.shiyan = this.$route.query.transaction_hash;
    //console.log(this.shiyan);
    // console.log(this.shiyan);
    //根据交易易哈希查询信息
    this.transactiondetaillist();
    this.transactionlist[0].block_height = this.height;
  },
  // 监听高度的变化
  watch: {
    height(val, oldval) {
      // console.log(val);
      if (val !== oldval) {
      }
    },
  },
  methods: {
    showmoredisplay() {
      this.showmore = false;
    },
    showmoredisplay2() {
      this.showmore2 = false;
    },
    showmoredisplay3() {
      this.showmore3 = false;
    },
    showMoreInformation() {
      this.showmore = true;
    },
    showMoreInformation2() {
      this.showmore2 = true;
    },
    showMoreInformation3() {
      this.showmore3 = true;
    },
    arraySpanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        if (rowIndex % this.collength === 0) {
          return {
            rowspan: this.collength, //合并的行数
            colspan: 1, //合并的列数，设为０则直接不显示
          };
        } else {
          return {
            rowspan: 0,
            colspan: 0,
          };
        }
      }
      if (columnIndex === 1) {
        if (rowIndex % this.collength === 0) {
          return {
            rowspan: this.collength, //合并的行数
            colspan: 1, //合并的列数，设为０则直接不显示
          };
        } else {
          return {
            rowspan: 0,
            colspan: 0,
          };
        }
      }
    },
    ceshi(msg) {
      // console.log(msg);
      this.shiyan = msg;
      this.transactiondetaillist();
      // this.ranliaolist();
      // this.blockrewardlist();
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
    // 区块高度搜索
    async blocksearch() {
      let that = this;
      await that.$http
        .get("/search_blockHeight_for_height", {
          params: {
            block_height: this.transactionlist[0].block_height,
            pageNum: 1,
            pageSize: 3,
          },
        })
        .then((res) => {
          this.loading = false;
          // console.log(res);
        })
        .catch((e) => {});
    },
    // 根据交易易哈希查询相关交易易信息
    async transactiondetaillist() {
      let that = this;
      var blockData = [];
      var blockData2 = [];
      await that.$http
        .get("search_transactionHash_detailInfo", {
          params: {
            transaction_hash: this.shiyan,
          },
        })
        .then((res) => {
          this.loading = false;
          // console.log(res);
          if (res.data[0].select_id === 1) {
            this.activeName = "first";
            this.line1 = true;
            this.line2 = false;
            this.line3 = false;
          }
          if (res.data[0].select_id === 2) {
            this.activeName = "second";
            this.line1 = false;
            this.line2 = true;
            this.line3 = false;
          }
          if (res.data[0].select_id === 3) {
            this.activeName = "third";
            this.line1 = false;
            this.line2 = false;
            this.line3 = true;
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
            // 至
            this.transactionlist[0].from_address = res.data[0].search_main_transaction_detailInfo[0].from_address.split(
              ","
            );
            this.transactionlist[0].from_address2 = res.data[0].search_main_transaction_detailInfo[0].from_address.split(
              ","
            );
            this.transactionlist[0].to_address = res.data[0].search_main_transaction_detailInfo[0].to_address.split(
              ","
            );
            this.transactionlist[0].to_address2 = res.data[0].search_main_transaction_detailInfo[0].to_address.split(
              ","
            );
            // this.transactionlist[0].from_address.length=7;
            if (this.transactionlist[0].from_address.length >= 6) {
              this.from_detail = true;
              let from_address = [];
              let from_address2 = [];
              for (
                let m = 0;
                m < this.transactionlist[0].from_address2.length;
                m++
              ) {
                from_address2.push(
                  `<span style="color:blue">${m + 1}:</span>` +
                    this.transactionlist[0].from_address2[m] +
                    `</br>`
                );
              }

              this.transactionlist[0].from_address2 = from_address2
                .toString()
                .replaceAll(",", "");
              for (let c = 0; c < 6; c++) {
                from_address.push(
                  `<span style="color:blue">${c + 1}:</span>` +
                    this.transactionlist[0].from_address[c]
                );
              }
              this.transactionlist[0].from_address =
                from_address.toString() + "...";
            } else {
              // console.log("<6");
              this.transactionlist[0].from_address =
                res.data[0].search_main_transaction_detailInfo[0].from_address;
            }

            // 从
            // console.log(this.transactionlist[0].to_address);
            if (this.transactionlist[0].to_address.length > 6) {
              let to_address = [];
              let to_address2 = [];
              for (
                let a = 0;
                a < this.transactionlist[0].to_address2.length;
                a++
              ) {
                to_address2.push(
                  `<span style="color:blue">${a + 1}:</span>` +
                    this.transactionlist[0].to_address[a] +
                    `</br>`
                );
              }
              //console.log(to_address2);
              this.transactionlist[0].to_address2 = to_address2
                .toString()
                .replaceAll(",", "");
              //  this.transactionlist[0].to_address.length=5
              for (let s = 0; s < 6; s++) {
                to_address.push(
                  `<span style="color:blue">${s + 1}:</span>` +
                    this.transactionlist[0].to_address[s]
                );
              }
              this.transactionlist[0].to_address =
                to_address.toString() + "...";
              // 交易明细详情
              this.amount_detail = true;
              this.transactionlist[0].amount_detail = res.data[0].search_main_transaction_detailInfo[0].amount_detail.split(
                ","
              );
              this.transactionlist[0].amount_detail2 = res.data[0].search_main_transaction_detailInfo[0].amount_detail.split(
                ","
              );
              // console.log(this.transactionlist[0].amount_detail2);
              let amount_detail = [];
              let amount_detail2 = [];
              for (
                let b = 0;
                b < this.transactionlist[0].amount_detail2.length;
                b++
              ) {
                amount_detail2.push(
                  `<span style="color:blue">${b + 1}:</span>` +
                    this.transactionlist[0].amount_detail2[b] / 1000000 +
                    `</br>`
                );
              }
              this.transactionlist[0].amount_detail2 = amount_detail2
                .toString()
                .replaceAll(",", "");
              // console.log(this.transactionlist[0].amount_detail2);
              for (let k = 0; k < 6; k++) {
                amount_detail.push(
                  `<span style="color:blue">${k + 1}:</span>` +
                    this.transactionlist[0].amount_detail[k] / 1000000
                );
              }
              // console.log(to_address.toString());
              this.transactionlist[0].amount_detail =
                amount_detail.toString() + "...";
            } else {
              this.transactionlist[0].to_address =
                res.data[0].search_main_transaction_detailInfo[0].to_address;
              this.amount_detail = false;
            }
          }
          //  console.log(this.collength);
          //  console.log(res.data.length);
          for (
            let j = 0;
            j < res.data[0].search_award_transaction_detailInfo.length + 1;
            j++
          ) {
            var obj2 = {};
            let strtime =
              res.data[0].search_award_transaction_detailInfo[j]
                .transaction_time;
            obj2.transaction_time = this.transactionlist[0].transaction_time;
            obj2.award = this.transactionlist[0].award;
            obj2.detail =
              res.data[0].search_award_transaction_detailInfo[j].award;
            obj2.sign_node =
              res.data[0].search_award_transaction_detailInfo[j].sign_node;
            // console.log(obj);
            blockData2[j] = obj2;
            this.detail2Data = blockData2;
            var obj = {};
            let strtime2 =
              res.data[0].search_gas_transaction_detailInfo[j].transaction_time;
            obj.transaction_time = this.timestampToTime(Number(strtime2));
            // console.log(res.data.length)
            obj.gas = this.transactionlist[0].gas;
            obj.detail = res.data[0].search_gas_transaction_detailInfo[j].gas;
            obj.sign_node =
              res.data[0].search_gas_transaction_detailInfo[j].sign_node;
            // console.log(obj);
            blockData[j] = obj;
            this.detail1Data = blockData;
          }
          for (
            var i = 0;
            i < res.data[0].search_gas_transaction_detailInfo.length + 1;
            i++
          ) {}
        })
        .catch((e) => {});
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
      // this.blocksearch();
      // this.transactionlist[0].block_height -= 1;
      // this.transactiondetaillist();
      // this.ranliaolist();
      // this.blockrewardlist();
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
    handleClick(tab) {
      // console.log(tab);
      switch (tab.index) {
        case "0":
          this.line1 = true;
          this.line2 = false;
          this.line3 = false;
          break;
        case "1":
          this.line1 = false;
          this.line2 = true;
          this.line3 = false;
          break;
        case "2":
          this.line1 = false;
          this.line2 = false;
          this.line3 = true;
          break;
      }
    },
  },
};
</script>
<style lang="less">
.more_button {
  width: 100px;
  cursor: pointer;
  margin: 0 auto;
}
#from_information {
  width: 50%;
  height: 500px;
  position: fixed;
  top: 25%;
  left: 25%;
  overflow-y: scroll;
  z-index: 9999;
  background: #e8eaf3;
}
#from_information2 {
  position: fixed;
  top: 28%;
  left: 71%;
  z-index: 9999;
  cursor: pointer;
}
#address_information {
  width: 50%;
  height: 500px;
  position: fixed;
  top: 25%;
  left: 25%;
  overflow-y: scroll;
  z-index: 9999;
  background: #e8eaf3;
}
#address_information2 {
  position: fixed;
  top: 28%;
  left: 71%;
  z-index: 9999;
  cursor: pointer;
}
#detail_information {
  width: 50%;
  height: 500px;
  position: fixed;
  top: 25%;
  left: 25%;
  overflow-y: scroll;
  z-index: 9999;
  background: #e8eaf3;
}
#detail_information2 {
  position: fixed;
  top: 28%;
  left: 71%;
  z-index: 9999;
  cursor: pointer;
}

.el-button {
  z-index: 999;
}
.el-tabs {
  height: auto !important;
}
th div {
  text-align: center;
}
.el-table__body tr td {
  text-align: center;
}
// 本页面
.transactiondetail {
  min-height: 980px;
  margin: 0 auto;
  margin-bottom: 20px;
  border-radius: 40px;
  position: relative;
  top: 0;
  .sticky {
    width: 100% !important;
    height: 120px !important;
    position: fixed;
    top: 0px;
    margin: 0 auto !important;
  }
  .transactiondetailzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }
  .detailcontent {
    width: 1120px;
    height: auto;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    .el-table__row {
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(51, 51, 51, 1);
      opacity: 1;
      height: 51px;
    }
    .addressltable {
      background-color: #d5e1f4;
    }
    .addressltable2 {
      background-color: #d5e1f4;
    }
    .el-table {
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      border: none;
      outline: none;
    }
    .el-table__header-wrapper {
      width: 100%;
      border-radius: 15px;
    }
    .el-table td,
    .el-table th.is-leaf {
      border-bottom: 1px solid gray;
    }
    .el-tabs__item {
      line-height: 88px;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      color: rgba(102, 102, 102, 1);
      opacity: 1;
      position: relative;
    }
    .el-tabs__nav {
      left: 40px;
    }
    #tab-second {
      position: relative;
      left: 50px;
    }
    #tab-third {
      position: relative;
      left: 100px;
    }
    .el-tabs__item.is-active {
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
    }
    .linezong {
      display: flex;
      flex-direction: row;
      .line {
        width: 80px;
        height: 2px;
        background-color: rgba(40, 96, 194, 1);
        z-index: 10;
      }
      .line1 {
        position: relative;
        left: 40px;
        top: 79px;
      }
      .line2 {
        position: relative;
        left: 220px;
        top: 79px;
      }
      .line3 {
        position: relative;
        left: 420px;
        top: 79px;
      }
    }
    .el-tabs__content {
      width: 100%;
      // overflow: visible;
      height: auto;
      margin: 0 auto;
      min-height: 600px;
    }
    .el-tabs__header {
      height: 88px;
      margin: 0;
    }
    .el-tabs__item {
      height: 50px !important;
    }
    .el-tabs__active-bar {
      height: 0px !important;
    }
    #pane-first {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    // 交易信息左边
    .jiaoyileft {
      width: 235px;
      height: 138px;
      background: rgba(232, 234, 243, 1);
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      border-radius: 20px;
      float: left;
      position: relative;
      left: 38px;
      top: 27px;
      .leftimg {
        width: 9.83px;
        height: 16.83px;
        cursor: pointer;
      }
      .leftimg1 {
        position: relative;
        left: 10px;
        top: 15px;
      }
      .leftimg2 {
        position: relative;
        left: 30px;
        top: 15px;
      }
      .leftimg3 {
        position: absolute;
        left: 30px;
        top: 86px;
      }
      .leftspan1 {
        position: relative;
        left: 20px;
        top: 20px;
        font-size: 40px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 56px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
      }
      .leftspan2 {
        position: absolute;
        left: 59px;
        top: 86px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(102, 102, 102, 1);
        opacity: 1;
      }
    }
    .jiaoyiright {
      width: 785px;
      height: auto;
      background: rgba(232, 234, 243, 1);
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      border-radius: 20px;
      margin-right: 20px;
      // float: right;
      p {
        position: relative;
        left: 30px;
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
        margin-top: 10px;
      }
      .jiaoyirightcon {
        width: 100%;
        height: auto;
        margin-top: 30px;
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        #big {
          height: auto;
          p:nth-child(2) {
            width: 600px;
            word-break: break-all;
            word-wrap: break-word;
          }
        }
        div {
          width: 100%;
          display: flex;
          flex-direction: row;
          // justify-content: space-between;
          margin: 0 auto;
          p:nth-child(1) {
            width: 80px;
          }
          p:nth-child(2) {
            position: relative;
            left: 60px;
          }
          .toright {
            width: 637px;
            word-break: break-all;
            word-wrap: break-word;
            // position: absolute;
            // left: 60px;
          }
        }
      }
    }
    .el-table th,
    .el-table tr {
      background-color: #d5e1f4;
    }
    #pane-second {
      height: auto;
      p {
        position: relative;
        left: 42px;
        top: 26px;
        font-size: 20px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 28px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
      }
      .secondcontent {
        position: relative;
        left: 40px;
        top: 53px;
        width: 1040px;
        height: auto;
        border-radius: 15px;
        .has-gutter tr {
          border-radius: 15px;
          font-size: 16px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 22px;
          color: rgba(40, 96, 194, 1);
          opacity: 1;
          background-color: #a1bae5 !important;
        }
        .el-table {
          width: 1040px !important;
          margin: 0 auto;
          outline: none;
          border: none;
          background-color: #d5e1f4;
          border-top-left-radius: 15px;
          border-top-right-radius: 15px;
          cursor: pointer;
          .has-gutter {
            background-color: #a1bae5 !important;
          }
        }
      }
    }
    #pane-third {
      position: relative;
      p {
        position: relative;
        left: 42px;
        top: 26px;
        font-size: 20px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 28px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
      }
      .secondcontent2 {
        position: relative;
        left: 40px;
        top: 53px;
        width: 1040px;
        height: 166px;
        border-radius: 15px;
        .has-gutter {
          background-color: rgba(144, 173, 224, 0.9);
        }
        .has-gutter tr {
          border-radius: 15px;
          font-size: 16px;
          font-family: "苹方-简";
          font-weight: normal;
          line-height: 22px;
          color: rgba(40, 96, 194, 1);
          opacity: 1;
        }
        .el-table {
          width: 1040px !important;
          margin: 0 auto;
          outline: none;
          border: none;
          background-color: #d5e1f4;
          border-top-left-radius: 15px;
          border-top-right-radius: 15px;
          cursor: pointer;
        }
      }
    }
  }
}
</style>
