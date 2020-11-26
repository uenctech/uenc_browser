<template>
  <!-- 搜索栏区域 -->
  <div
    class="indexsearch"
    :class="{ sticky2: sticky2 }"
    v-loading.fullscreen.lock="fullscreenLoading"
  >
    <div class="searchleft">
      <select
        v-model="value"
        placeholder="UENC主网"
        @change="searchchange"
        @click="right"
      >
        <option
          v-for="item in select"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        ></option>
      </select>
      <img
        src="../../assets/images/index/right.png"
        class="right"
        v-if="righticon"
      />
      <img src="../../assets/images/index/right.png" class="rightxia" v-else />
      <!-- <span>{{ $t("publicsection[0]") }}</span>
      <img src="../../assets/images/index/right.png" alt="" />-->
    </div>
    <div class="searchcenter">
      <input
        type="text"
        :placeholder="$t('publicsection[2]')"
        v-model="inputvalue"
        ref="search"
        @keyup="keyup"
      />
    </div>
    <div class="searchright">
      <button @click="searchselect">
        {{ $t("publicsection[1]") }}
      </button>
    </div>
  </div>
</template>
<script>
export default {
  name: "foot",
  data() {
    return {
      fullscreenLoading: false,
      nowLang: "en",
      show: false,
      sticky2: false,
      inputvalue: "",
      // 搜索下拉列表
      select: "",
      value: "",
      righticon: true,
      // 请求返回的数值
      // 地址
      // 高度
      block_height: "",
      transaction_award: "",
      block_list: [],
      // 交易哈希
      transactionhaxisearch: [],
      // 区块哈希
    };
  },
  watch: {
    inputvalue: {
      handler(newName, oldName) {
        // console.log(newName);
      },
    },
  },
  created() {
    //console.log(this.$i18n.locale);
    if (this.$i18n.locale == "cn") {
      this.select = [
        {
          value: "0",
          label: "UENC地址",
        },
        {
          value: "1",
          label: "区块高度",
        },
        {
          value: "2",
          label: "交易哈希",
        },
        {
          value: "3",
          label: "区块哈希",
        },
      ];
    }
    if (this.$i18n.locale == "en") {
      this.select = [
        {
          value: "0",
          label: "Address",
        },
        {
          value: "1",
          label: "Height",
        },
        {
          value: "2",
          label: "Transaction",
        },
        {
          value: "3",
          label: "Block",
        },
      ];
    }
    if (this.value == "") {
      this.value = "0";
    }
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    keyup(event) {
      // console.log(event);
      if (this.inputvalue !== "") {
        if (event.keyCode == "13") {
          this.searchselect();
        }
      }
    },
    right() {
      this.righticon = !this.righticon;
    },
    searchchange() {
      // console.log(this.value);
    },
    searchselect() {
      // console.log("点击了");
      this.$emit("test", this.$refs.search._value);
      // console.log(this.$refs.search._value);
      switch (this.value) {
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
          // console.log(res);
          if (res.data[0].total_record[0].total_record !== 0) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/transactiondetails",
              query: { addressvalue: this.inputvalue },
            });
          } else {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/notfound",
              query: {},
            });
          }
        }).catch((err)=>{
          ;
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
          } else {
             this.fullscreenLoading = false;
            this.$router.push({
              path: "/notfound",
              query: {},
            });
          }
        }).catch((err)=>{
          ;
        });;
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
          } else {
             this.fullscreenLoading = false;
            this.$router.push({
              path: "/notfound",
              query: {},
            });
          }
        }).catch((err)=>{
          ;
        });;
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
          if (res.data[0].search_main_transactionInfo.length !==0) {
            this.fullscreenLoading = false;
            this.$router.push({
              path: "/blockdetails",
              query: { blockhaxi: this.inputvalue },
            });
          } else {
             this.fullscreenLoading = false;
            this.$router.push({
              path: "/notfound",
              query: {},
            });
          }
        }).catch((err)=>{
          ;
        });;
    },
    handleScroll() {
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 10) {
        this.sticky2 = true;
      }
      if (scrollTop < 20) {
        this.sticky2 = false;
      }
      // console.log(scrollTop);
    },
  },
};
</script>
<style lang="less">
.el-input__inner {
  background-color: #eaebf3 !important;
}
.el-input .el-input--suffix .is-focus {
  height: 50px !important;
}
.el-select-dropdown__list {
  background-color: #eaebf3 !important;
}
.popper__arrow {
  display: none !important;
}
select {
  width: 146px;
  height: 50px;
  top: 29px;
  position: relative;
  padding-left: 15px;
  left: 27px;
  border-radius: 15px;
  border: none !important;
  outline: none !important;
  font-size: 20px !important;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 28px;
  color: rgba(40, 96, 194, 1);
  opacity: 1;
  background-color: #eaebf3;
  border: none !important;
  cursor: pointer;
  // #eaebf3
}
/* --ie清除--*/

select::-ms-expand {
  display: none;
}

/* --火狐、谷歌清除--*/

select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  padding-right: 10px;
}
option {
  border: none !important;
}
option:hover {
  color: #fff;
  background-color: #1e90ff;
}
.right {
  position: relative;
  left: 0px;
  top: 30px !important;
}
.rightxia {
  position: relative;
  left: 0px;
  top: 30px !important;
  transform: rotate(90deg);
}
/* --箭头就用自己设计的箭头，padding 空出箭头的位置--*/
option {
  border-radius: 15px;
}
.el-select-dropdown {
  position: relative;
  top: 259px !important;
}

.el-select .el-input .el-select__caret {
  color: blue !important;
}
.indexsearch .searchleft span {
  color: blue !important;
  width: 14.83px !important;
  height: 8.83px !important;
  position: relative;
  left: 54px !important;
  top: -19px !important;
}
.el-select-dropdown__item span {
  font-size: 20px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 28px;
  color: rgba(40, 96, 194, 1);
  opacity: 1;
}
.el-select input::placeholder {
  background-color: #eaebf3;
  font-size: 20px;
  font-family: "苹方-简";
  font-weight: normal;
  line-height: 28px;
  color: rgba(40, 96, 194, 1);
  opacity: 1;
}
.sticky2 {
  width: 1200px !important;
  height: 120px;
  position: fixed;
  top: 90px;
  margin: 0 auto !important;
}
// 搜索栏
.indexsearch {
  width: 1200px;
  height: 120px;
  // position: sticky;
  // top: 100px;
  z-index: 40;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  background: url("../../assets/images/index/Up.png") no-repeat center/100% 100%;
  .el-input__inner {
    font-size: 20px !important;
    font-family: "苹方-简" !important;
    font-weight: normal !important;
    line-height: 28px !important;
    color: rgba(40, 96, 194, 1) !important;
    border: none !important;
    outline: none !important;
  }
  .searchleft {
    width: 200px;
    height: 105px;
    position: relative;
    left: 8px;
    top: 8px;
    background: url("../../assets/images/index/Icon 1.png") no-repeat
      center/100% 100%;
    span {
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      position: relative;
      left: 40px;
      top: 40px;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
    }
    img {
      position: relative;
      right: -50px;
      top: 40px;
    }
  }
  .searchcenter {
    width: 819px;
    height: 50px;
    position: relative;
    display: flex;
    flex-direction: row;
    top: 36px;
    left: -2px;
    background: url("../../assets/images/index/Down.png") no-repeat center/100%
      100%;

    input {
      width: 818px;
      height: 47px;
      position: relative;
      left: 1px;
      top: 2px;
      border: none;
      background-color: rgba(255, 255, 255, 0.5);
      outline: none;
      border-radius: 11px;
      padding-left: 30px;
    }
  }
  .searchright {
    button {
      width: 126px;
      height: 50px;
      position: relative;
      right: -12px;
      top: 35px;
      background: rgba(40, 96, 194, 1);
      box-shadow: -5px -5px 15px rgba(255, 255, 255, 0.8);
      border-radius: 12px;
      border: none;
      outline: none;
      cursor: pointer;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(255, 255, 255, 1);
      opacity: 1;
    }
  }
}
</style>
