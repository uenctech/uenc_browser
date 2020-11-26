<template>
  <div class="addressed">
   <headertop></headertop>
    <div class="addresszong">
      <!-- 搜索栏区域 -->
      <search></search>
      <!-- 内容区域 -->
      <div class="addresscontent">
        <p class="title">
          {{ $t("address.content[0]") }}{{ $t("address.content[5]")
          }}{{ totalNum }}{{ $t("address.content[6]") }}
        </p>

        <el-table
          v-loading="loading"
          :data="addressData"
          style="width: 100%"
          class="addressltable"
          @row-click="gototransaction"
        >
          <el-table-column
            prop="rank"
            :label="$t('address.content[1]')"
          ></el-table-column>
          <el-table-column
            prop="wallet_address"
            :label="$t('address.content[2]')"
          ></el-table-column>
          <el-table-column
            prop="wallet_address2"
            :label="$t('address.content[2]')"
            v-if="tables"
          ></el-table-column>

          <el-table-column
            prop="transaction_num"
            :label="$t('publicsection[4]')"
          ></el-table-column>
          <el-table-column
            prop="amount"
            :label="$t('address.content[3]')"
          ></el-table-column>
          <el-table-column
            prop="percentage"
            :label="$t('address.content[4]')"
          ></el-table-column>
        </el-table>
        <div class="addressblock">
          <el-pagination
            :current-page.sync="addressmedianum"
            :page-size="20"
            :pager-count="5"
            layout="total,  prev, pager, next, jumper"
            :total="totalNum"
            @current-change="change"
            v-if="totalNum != 0"
            ref="addresspaginations"
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
import VFooter from "@components/common/Footer.vue";
import Search from "@components/common/search.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "addressed",
  data() {
    return {
      loading: true,
     
      tables: false,
      // 外部公共部分
      fullscreenLoading: false,
    
      language: "",
      nowLang: "",
    
      choselanguage: ["中文", "EN"],
      // 搜索功能
      search: "",
      // 分页
      addressmedianum: 1,
      totalNum: "",
      addressData: [],
      searchData: "",
      addresszong: "",
      // 页码设置
      blue1: false,
      blue2: false,
    };
  },
  components: { VFooter, Search,headertop },
  // 页码设置
  watch: {
    addressmedianum(val) {
      //console.log(val);
      if (val == 1) {
        this.blue1 = true;
      } else {
        this.blue1 = false;
      }
    },
  },
  created() {
    this.nowLang = this.$i18n.locale;
    
    this.addressmedianum = 1;
    if (this.addressmedianum == 1) {
      this.blue1 = true;
    }
    this.addresssearch();
    
  },
 
  mounted() {
    
  },
  methods: {
    async addresssearch() {
      let that = this;
      var blockData = [];
      await that.$http
        .get("/get_address_list_for_all", {
          params: {
            pageNum: this.addressmedianum,
            pageSize: 20,
          },
        })
        .then((res) => {
          this.loading = false;
          // console.log(res);
          this.totalNum = res.data[0].total_record[0].total_record;
          //console.log(this.totalNum);
          // table赋值
          var addresslist = res.data[0].wallet_address_list;
          // console.log(addresslist);
          for (var i = 0; i < addresslist.length + 1; i++) {
            var obj = {};
            let times = [];
            obj.rank = addresslist[i].row_num;
            obj.wallet_address =
              addresslist[i].wallet_address.substring(0, 11) + "...";
            obj.wallet_address2 = addresslist[i].wallet_address;
            // console.log(obj);
            obj.transaction_num = addresslist[i].transaction_num;
            obj.amount = addresslist[i].amount;
            obj.percentage = addresslist[i].percentage + "%";
            //console.log(obj);
            blockData[i] = obj;
            //console.log(blockData);
            this.addressData = blockData;
            //console.log(obj);
          }
          localStorage.setItem("lan", this.nowLang);
        })
        .catch((e) => {});
    },
    change(val) {
      // console.log(val);
      this.addressmedianum = val;
      this.addresssearch();
      this.setContextData("currentpage4", this.addressmedianum);
    },
    // 跳转到地址详情页
    gototransaction(row, event, column) {
      // this.tables=true
      this.$router.push({
        path: "/transactiondetails",
        query: { addressvalue: row.wallet_address2 },
      });
      // console.log(row, event, column);
    },
   
    showlist() {
      this.addresssearch();
    },
    // 去首页
    gotofirst() {
      this.addressmedianum = 1;
      this.blue2 = false;
      this.blue1 = true;
      this.addresssearch();
    },
    // 去尾页
    gotolast() {
      this.blue1 = false;
      this.blue2 = true;
      //console.log(parseInt(this.totalNum / 20));
      if (this.totalNum % 20 == 0) {
        this.addressmedianum = this.totalNum / 20;
      } else {
        this.addressmedianum = parseInt(this.totalNum / 20) + 1;
      }
      //console.log(this.blockmedianum );
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
   
  },
  destroyed() {
  
  },
};
</script>
<style lang="less">
// 本页面
.addressed {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  margin-bottom: 20px;
  opacity: 1;
  border-radius: 40px;
  .addresszong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }
  // 内容部分
  .addresscontent {
    width: 1120px;
    height: 1250.5px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    .table {
      table-layout: fixed;
    }
    .el-table__row td {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .el-table th,
    .el-table tr {
      background-color: rgba(40, 96, 194, 0.1);
      text-align: center;
    }
    .el-table__body tr td {
      text-align: center;
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
    .addressltable {
      position: relative;
      width: 1040px !important;
      height: 1069px;
      top: 50px;
      background: rgba(40, 96, 194, 0.1);
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
    .addressblock {
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
        cursor: pointer;
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
        cursor: pointer;
      }
     
    }
  }
}
</style>
