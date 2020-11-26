<template>
  <div
    class="search"
    v-loading.fullscreen.lock="fullscreenLoading"
    :class="{ sticky: sticky }"
  >
    <div class="headersearch">
      <div class="search_left">
        <div class="search_leftz">
          <span @click="openSearchPop" v-html="select"></span>
          <img src="@assets/images/index/组 202.png" />
        </div>

        <van-popup
          v-model="show_search"
          position="bottom"
          :overlay="true"
          v-if="show_search"
        >
          <img
            src="@assets/images/index/关闭.png"
            class="error"
            @click="closeSearchPop"
          />
          <ul class="selectul">
            <li
              class="selectlist"
              v-for="item in selectList"
              :key="item"
              @click="selectSearch(item.id)"
              :class="{ active2: item.id == selectindex }"
            >
              {{ item.name }}
            </li>
          </ul>
        </van-popup>
      </div>
      <div class="search_right">
        <img src="@assets/images/index/搜索.png" @click="searchBlur" />
        <input
          type="search"
          :placeholder="serachinformation"
          v-model="inputvalue"
          ref="search"
          @focus="clear"
          @keypress="searchGoods"
        />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "foot",
  data() {
    return {
      fullscreenLoading: false,
      serachinformation: "",
      sticky: false,
      translist: [],
      listloading: false,
      finished: false,
      transmedianum: 1, //请求第几页
      pageSize: 5, //每页请求的数量
      total: "", //总共的数据条数
      translist2: [],
      listloading2: false,
      finished2: false,
      blockmedianum: 1, //请求第几页
      pageSize2: 5, //每页请求的数量
      total2: "", //总共的数据条数
      // 本页面
      tableData: [],
      tableData2: [],
      active: 0,
      inputvalue: "",
      selectindex: "",
      show_silde: false,
      show_search: false,
      select: "UENC地址",
      selectList: [],
      loading: true,
    };
  },
  watch: {},
  created() {
   
    this.nowLang = this.$i18n.locale;
    if (this.nowLang == "en") {
      this.serachinformation = "Search related records";
      this.selectindex = "0";
      this.select = "Address";
      this.selectList = [
        { name: "Address", id: "0" },
        { name: "Height", id: "1" },
        { name: "TxHash", id: "2" },
        { name: "Block Hash", id: "3" },
      ];
    }

    if (this.nowLang == "cn") {
      this.serachinformation = "搜索相关记录";
      this.selectindex = "0";
      this.select = "UENC地址";
      this.selectList = [
        { name: "UENC地址", id: "0" },
        { name: "区块高度", id: "1" },
        { name: "交易哈希", id: "2" },
        { name: "区块哈希", id: "3" },
      ];
    }

    // console.log(this.selectindex);
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    searchGoods(event) {
      if (event.keyCode == 13) {
        event.preventDefault();
        //如果按的是enter键 13是enter
        this.searchBlur();
        // 软键盘收回
        document.activeElement.blur();
      }
    },
    clear() {
      this.$refs.search.value = "";
    },
    // 滚动固定区域
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 10) {
        this.sticky = true;
      }
      if (scrollTop < 10) {
        this.sticky = false;
      }
      // console.log(scrollTop);
    },
    searchBlur() {
      // console.log("点击了");
      this.$emit("test", this.$refs.search._value);
      // console.log(this.$refs.search._value);
      switch (this.selectindex) {
        // 地址搜索
        case "0":
          // console.log('0');
          if (this.inputvalue !== "") {
            this.fullscreenLoading = true;
            this.addresssearch();
          }
          break;
        case "1":
          //  console.log('1');
          // 区块高度
          if (this.inputvalue !== "") {
            this.fullscreenLoading = true;
            this.blocksearch();
          }
          break;
        // 交易哈希
        case "2":
          //  console.log('2');
          if (this.inputvalue !== "") {
            this.fullscreenLoading = true;
            this.transactiondetaillist();
          }
          break;
        // 区块哈希
        case "3":
          //  console.log('3');
          if (this.inputvalue !== "") {
            this.fullscreenLoading = true;
            this.blockhaxisearch();
          }

          break;
      }
    },
    selectSearch(index) {
      // console.log(index);
      switch (index) {
        // 地址搜索
        case "0":
          this.show_search = false;
          if (this.nowLang == "cn") {
            this.selectindex = "0";
            this.select = "UENC地址";
          } else {
            this.selectindex = "0";
            this.select = "Address";
          }
          break;
        case "1":
          this.show_search = false;
          if (this.nowLang == "cn") {
            this.selectindex = "1";
            this.select = "区块高度";
          } else {
            this.selectindex = "1";
            this.select = "Height";
          }
          break;
        // 交易哈希
        case "2":
          this.show_search = false;
          if (this.nowLang == "cn") {
            this.selectindex = "2";
            this.select = "交易哈希";
          } else {
            this.selectindex = "2";
            this.select = "TxHash";
          }
          break;
        // 区块哈希
        case "3":
          this.show_search = false;
          if (this.nowLang == "cn") {
            this.selectindex = "3";
            this.select = "区块哈希";
          } else {
            this.selectindex = "3";
            this.select = "Block Hash";
          }
          break;
      }
    },
    //地址搜索
    async addresssearch() {
      let that = this;
      await that.$http
        .get("/search_transactionInfo_walletAddress", {
          params: {
            wallet_address: this.inputvalue,
            pageNum: 1,
            pageSize: 20,
          },
        })
        .then((res) => {
          if (res.data[0].total_record[0].total_record !== 0) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/transactiondetails",
              query: { addressvalue: this.inputvalue },
            });
            this.inputvalue = "";
          } else {
            this.$router.push({
              path: "/notfound",
              query: {},
            });
            this.fullscreenLoading = false;
          }
        });
    },
    // 区块高度搜索
    async blocksearch() {
      let that = this;
      await that.$http
        .get("/search_blockHeight_for_height", {
          params: {
            block_height: this.inputvalue,
            pageNum: 1,
            pageSize: 20,
          },
        })
        .then((res) => {
          //  console.log(res);
          if (res.data[0].total_record[0].total_record !== 0) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/blockdetail",
              query: {
                blockheight: this.inputvalue,
                // transaction_award:this.transaction_award
              },
            });
            this.inputvalue = "";
          } else {
            this.$router.push({
              path: "/notfound",
              query: {},
            });
            this.fullscreenLoading = false;
          }
        });
    },
    // 根据交易易哈希查询相关交易易信息
    async transactiondetaillist() {
      let that = this;
      await that.$http
        .get("/search_transactionHash_detailInfo", {
          params: {
            transaction_hash: this.inputvalue,
          },
        })
        .then((res) => {
          //  console.log(res);
          if (res.data[0].select_status === 1) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/transactiondetail",
              query: {
                transaction_hash: this.inputvalue,
                // transaction_award:this.transaction_award
              },
            });
            this.inputvalue = "";
            // console.log(this.$refs);
          } else {
            this.$router.push({
              path: "/notfound",
              query: {},
            });
            this.fullscreenLoading = false;
          }
        });
    },
    // 区块哈希搜索
    async blockhaxisearch() {
      let that = this;
      var blockData = [];
      await that.$http
        .get("/search_blockInfo_blockHash", {
          params: {
            block_hash: this.inputvalue,
          },
        })
        .then((res) => {
          // console.log(res);
          if (res.data[0].search_main_transactionInfo.length !== 0) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/blockdetails",
              query: { blockhaxi: this.inputvalue },
            });
            this.inputvalue = "";
          } else {
            this.$router.push({
              path: "/notfound",
              query: {},
            });
            this.fullscreenLoading = false;
          }
        });
    },
    openPop() {
      this.show_silde = true;
    },
    openSearchPop() {
      this.show_search = true;
    },

    closePop() {
      this.show_silde = false;
    },
    closeSearchPop() {
      this.show_search = false;
    },
  },
};
</script>
<style lang="less">
.sticky {
  position: fixed;
  top: 35px;
  z-index: 20 !important;
  // width: 100% !important;
  // height: 36px !important;
  // background: rgba(255, 255, 255, 1) !important;
  // border: 1px solid rgba(68, 137, 247, 1) !important;
  // border-radius: 8px !important;
  // text-align: center !important;
  margin: 0 auto !important;
}
.search {
  width: 100%;
  height: 40px;
  margin: 0 auto;
  background: #f5f5f5 !important;
  margin-top: 17px;
}
.headersearch {
  width: 93.6%;
  height: 36px;
  background: rgba(255, 255, 255, 1);
  border: 1px solid rgba(68, 137, 247, 1);
  border-radius: 8px;
  text-align: center;
  margin: 0 auto;
  // margin-top: 21px;
  display: flex;
  flex-direction: row;
  .search_left {
    height: 36px;
    .search_leftz {
      width: 102px;
      height: 36px;
      line-height: 36px;
      border-top-left-radius: 8px;
      border-bottom-left-radius: 8px;
      border-right: 1px solid rgba(0, 0, 0, 0.1);
      span {
        font-size: 14px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 20px;
        color: rgba(40, 96, 194, 1);
        margin-left: 15px;
      }
      img {
        width: 5.41px;
        height: 9.41px;
        margin-left: 4px;
      }
    }
  }
  .search_right {
    display: flex;
    flex-direction: row;
    width: 249px;
    height: 36px;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    img {
      width: 16px;
      height: 16px;
      margin-left: 10px;
      margin-top: 10px;
    }
    input {
      width: 100%;
      height: 34px;
      border: none;
      border-top-right-radius: 8px;
      border-bottom-right-radius: 8px;
      padding-left: 10px;
    }
    input::-webkit-input-placeholder {
      /* WebKit browsers */
      font-size: 14px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 20px;
      color: rgba(51, 51, 51, 1);
      opacity: 0.5;
    }
  }
}
</style>
