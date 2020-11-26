<template>
  <div class="index">
    <headertop></headertop>
    <div class="indexzong">
      <!-- 搜索栏区域 -->
      <search></search>
      <!-- 卡片区域 -->
      <div class="card">
        <!-- 卡片左边 -->
        <div class="cardleft">
          <div class="cardlefttop">
            <img src="../assets/images/index/uenc.png" />
            <div class="cardlefttopright">
              <p>UENC</p>
              <p>
                <span style="color:#FFC787">{{ money }}</span> USDT≈<span
                  style="color:#FFC787"
                  >￥{{ money2 }}</span
                >
              </p>
            </div>
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
        <!-- 卡片右边 -->
        <div class="cardright" id="bar" v-show="card"></div>
        <div class="cardright" id="bars" v-show="card2"></div>
        <div class="cardright" id="barss" v-show="card3">
          <el-table :data="tableData3" height="203" border style="width:470px">
            <el-table-column
              prop="Sort_num"
              :label="$t('page[2]')"
              width="120"
              align="center"
            >
            </el-table-column>
            <el-table-column
              prop="count"
              :label="$t('page[3]')"
              width="180"
              align="center"
            >
            </el-table-column>
            <el-table-column prop="gas" :label="$t('page[4]')" align="center">
            </el-table-column>
          </el-table>
          <p class="number">{{ $t("page[3]") }}:{{ tabledataall }}</p>
          <p class="number2">{{ $t("page[5]") }}</p>
        </div>
        <div class="cardp">
          <p @click="cardclick1" :class="{ cardblue: card }">
            {{ $t("home.cardright[0]") }}
          </p>
          <p @click="cardclick2" :class="{ cardblue: card2 }">
            {{ $t("home.cardright[1]") }}
          </p>
          <p @click="cardclick3" :class="{ cardblue: card3 }">
            {{ $t("home.cardright[2]") }}
          </p>
        </div>
      </div>
      <!-- 内容区域 -->
      <div class="indexcontent">
        <p class="last">{{ $t("home.contenttop[0]") }}</p>
        <el-table
          v-loading="loading"
          :data="tableData"
          style="width: 100%"
          class="eltable1"
          @row-click="gototransactiondetail"
        >
          <el-table-column
            prop="transaction_hash2"
            :label="$t('home.contenttop[0]')"
            v-if="tables"
          ></el-table-column>
          <el-table-column
            prop="transaction_hash"
            :label="$t('home.contenttop[1]')"
          ></el-table-column>
          <el-table-column
            prop="date"
            :label="$t('publicsection[8]')"
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
            :label="$t('home.contenttop[2]')"
          ></el-table-column>
        </el-table>

        <p class="seemore" @click="gototransaction">
          {{ $t("publicsection[9]") }}
        </p>
        <p class="last">{{ $t("home.contentbottom[0]") }}</p>
        <el-table
          v-loading="loading"
          :data="tableData2"
          style="width: 100%"
          class="eltable2"
          @row-click="gotoblockdetail"
        >
          <el-table-column
            prop="block_height"
            :label="$t('publicsection[3]')"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="time"
            :label="$t('publicsection[8]')"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="tx_num"
            :label="$t('publicsection[4]')"
          ></el-table-column>
          <el-table-column
            prop="amount"
            :label="$t('publicsection[5]')"
          ></el-table-column>
          <el-table-column
            prop="award"
            :label="$t('home.cardleft[2]')"
          ></el-table-column>
        </el-table>
        <p class="seemore" @click="gotoblock">{{ $t("publicsection[9]") }}</p>
      </div>
      <!-- 底部区域 -->
      <div class="indexfooter">
        <div class="footertop">
          <img src="../assets/images/index/路径 88.png" alt />
          <span>UENC</span>
        </div>
        <div class="footercontent">
          <p>{{ $t("home.bottom[0]") }}</p>
        </div>
        <div class="footerfooter">
          <ul>
            <li>{{ $t("home.bottom[1]") }}2018-11-11</li>
            <li>{{ $t("home.bottom[2]") }}{{ $t("footerlast[0]") }}</li>
            <li>{{ $t("home.bottom[3]") }}{{ $t("footerlast[1]") }}</li>
            <li>{{ $t("home.bottom[4]") }}http://www.uenc.io</li>
          </ul>
        </div>
      </div>
      <v-footer></v-footer>
    </div>
  </div>
</template>
<script>
import Search from "@components/common/search.vue";
import VFooter from "@components/common/Footer.vue";
import headertop from "@components/common/HeaderTop";
export default {
  name: "index",
  data() {
    return {
      loading: true,
      // 固定设置
      sticky: false,
      tables: false,
      // 外部公共部分
      fullscreenLoading: false,
      nowLang: "",
      language: "",
      // 语言图片显示与隐藏
      show: true,
      choselanguage: ["中文", "EN"],
      card: true,
      card2: false,
      card3: false,
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
      echartsed: [],
      // 本页面
      tableData: [
        {
          transaction_hash: "",
          transaction_hash2: "",
          date: "",
          amount: "",
          from_address: "",
          to_address: "",
          gas: "",
        },
      ],
      tableData2: [
        {
          block_height: "",
          time: "",
          tx_num: "",
          amount: "",
          award: "",
        },
      ],
      tabledataall: "",
      tableData3: [
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
        {
          Sort_num: "",
          count: "",
          gas: "",
        },
      ],
    };
  },
  watch: {},
  components: { VFooter, Search, headertop },
  created() {
    // 时间的验证
    // let timestamp = Date.parse(new Date())/1000;
    // console.log(timestamp); //1597150172000 1597150210000   1597192326000
    // let s = 1597192326000 - 1597150172000; //9.20
    // let fenzhong = parseInt((s / 86400000) * 24 * 60);
    // console.log(fenzhong);
    // console.log(parseInt(fenzhong/60));
    // console.log(this.timestampToTime2(1595692800));
    this.nowLang = this.$i18n.locale;
    // console.log(this.nowLang);
    this.indexlist();
    this.rank();
    // 获取首页数据
  },
  mounted() {
    this.drawLine();
    // 基于准备好的dom，初始化echarts折线图实例
    // var myChart = echarts.init(document.getElementById("bar"));
    // var option = this.option;
    // myChart.setOption(option);
    // var myChart = echarts.init(document.getElementById("bars"));
    // var options = this.options;
    // myChart.setOption(options);
  },
  methods: {
    drawLine() {
      // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(document.getElementById("bar"));
      let myChart2 = echarts.init(document.getElementById("bars"));
      // let myChart3 = echarts.init(document.getElementById("barss"));
      var data = [];
      // 绘制图表
      myChart.setOption({
        title: {
          x: "left", //水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
          y: "top", //垂直安放位置，默认为top，可选为：'top' | 'bottom' | 'center' | {number}（y坐标，单位px）
          padding: 30, //标题内边距，单位px，默认各方向内边距为5，接受数组分别设定上右下左边距
          itemGap: 30, //主副标题纵向间隔，单位px，默认为10
        },
        tooltip: {
          trigger: "axis",
          // trigger: "item",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "line", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        xAxis: {
          type: "category",
          splitLine: { show: false }, //去除网格线
          boundaryGap: false,
          data: [],
          axisLabel: {
            interval: 36,
            formatter: function(value) {
              //x轴的文字改为竖版显示
              var str = value.split(" ");
              return str.join("\n");
            },
          },
          axisLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
        },
        yAxis: {
          type: "value",
          splitLine: { show: false }, //去除网格线
          position: "right",
          axisLine: {
            //y轴
            show: false,
          },
          axisTick: {
            //y轴刻度线
            show: true,
          },
        },
        series: [
          {
            data: [],
            type: "line",
            areaStyle: {},
            symbol: "circle", //拐点样式
            smooth: true, //true 为平滑曲线，false为直线
            itemStyle: {
              normal: {
                color: "fff",
                borderColor: "blue",
                borderWidth: 2,
                label: {
                  show: true,
                  position: "left",
                  textStyle: {
                    fontSize: 10,
                    color: "#fff",
                    width: 30,
                    height: 27,
                    backgroundColor: "blue",
                  },
                },
              },
              lineStyle: {
                // 系列级个性化折线样式
                width: 3,
                type: "solid",
                color: "#0180ff", //折线的颜色
              },
            },
            areaStyle: {
              normal: {
                color: " #FFE0BE", //改变区域颜色
              },
            },
            lineStyle: {
              color: "#FE9D67", //改变折线颜色
            },
          },
        ],
      });
      myChart2.setOption({
        title: {
          x: "left", //水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
          y: "top", //垂直安放位置，默认为top，可选为：'top' | 'bottom' | 'center' | {number}（y坐标，单位px）
          padding: 30, //标题内边距，单位px，默认各方向内边距为5，接受数组分别设定上右下左边距
          itemGap: 30, //主副标题纵向间隔，单位px，默认为10
        },
        tooltip: {
          trigger: "axis",
          // trigger: "item",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "line", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        xAxis: {
          type: "category",
          splitLine: { show: false }, //去除网格线
          boundaryGap: false,
          data: [],
          axisLine: {
            //y轴
            show: false,
          },
          axisTick: {
            //y轴刻度线
            show: false,
          },
        },

        yAxis: {
          type: "value",
          splitLine: { show: false }, //去除网格线
          position: "right",
          axisLine: {
            //y轴
            show: false,
          },
          axisTick: {
            //y轴刻度线
            show: false,
          },
        },
        series: [
          {
            data: [],
            type: "line",
            areaStyle: {},
            symbol: "circle", //拐点样式
            smooth: true, //true 为平滑曲线，false为直线
            itemStyle: {
              normal: {
                color: "fff",
                borderColor: "blue",
                borderWidth: 5,
                label: {
                  show: true,
                  position: "left",
                  textStyle: {
                    fontSize: 10,
                    color: "#fff",
                    width: 30,
                    height: 27,
                    backgroundColor: "blue",
                  },
                },
              },
              lineStyle: {
                // 系列级个性化折线样式
                width: 3,
                type: "solid",
                color: "green", //折线的颜色
              },
            },
            areaStyle: {
              normal: {
                color: " #FFE0BE", //改变区域颜色
              },
            },
            lineStyle: {
              color: "green", //改变折线颜色
            },
          },
        ],
      });
      // 异步加载数据
      let that = this;
      // 燃料费平均值
      var ranliaoaverage = [];
      // 时间
      var shijianchuo = [];
      // 每日交易笔数
      var transaction_num_for_7 = [];
      // 时间
      var transaction_num_for_7time = [];
      //  燃料费分布
      var ranliaofei = [];
      that.$http
        .get("")
        .then((res) => {
          // console.log(res);
          for (var i = 0; i < res.data[0].get_avgGas_for_100.length + 1; i++) {
            ranliaoaverage.unshift(
              res.data[0].get_avgGas_for_100[i].block_height_for_100
            );
            shijianchuo.unshift(
              this.timestampToTime2(
                res.data[0].get_avgGas_for_100[i].date
              ).substring(5)
            );
            //  console.log(ranliaoaverage);
            //  console.log(shijianchuo);
            // 填入数据
            myChart.setOption({
              xAxis: {
                data: shijianchuo,
              },
              series: [
                {
                  data: ranliaoaverage,
                  type: "line",
                  symbolSize: 0.001,
                  areaStyle: {},
                  symbol: "circle", //拐点样式
                  smooth: true, //true 为平滑曲线，false为直线
                  itemStyle: {
                    normal: {
                      color: "#fff",
                      borderColor: "blue",
                      borderWidth: 3,
                      label: {
                        show: true,
                        position: "left",
                        textStyle: {
                          fontSize: 16,
                          color: "#fff",
                          // width: 54,
                          // height: 27,
                          backgroundColor: "blue",
                        },
                        formatter: (params) => {
                          //  console.log(params);
                          // console.log(this.option.series[0].data.length);
                          if (ranliaoaverage.length - 1 == params.dataIndex) {
                            return params.value;
                          } else {
                            return "";
                          }
                        },
                      },
                    },
                  },
                  areaStyle: {
                    normal: {
                      color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: "#FFDAAF" },
                        { offset: 0.4, color: "#FFDAAF" },
                        { offset: 1, color: "#fff" },
                      ]),
                    },
                  },
                  lineStyle: {
                    color: "#FE9D67", //改变折线颜色
                  },
                },
              ],
            });
          }
        })
        .catch((e) => {});
      that.$http
        .get("")
        .then((res) => {
          // console.log(res);
          for (
            var i = 0;
            i < res.data[0].transaction_num_for_7.length + 1;
            i++
          ) {
            transaction_num_for_7.unshift(
              res.data[0].transaction_num_for_7[i].transaction_num_for_7
            );
            transaction_num_for_7time.unshift(
              this.timestampToTime2(
                res.data[0].transaction_num_for_7[i].date
              ).substring(5, 10)
            );
            //  console.log(ranliaoaverage);
            //  console.log(shijianchuo);
            // 填入数据
            myChart2.setOption({
              xAxis: {
                data: transaction_num_for_7time,
              },
              series: [
                {
                  data: transaction_num_for_7,
                  type: "line",
                  symbolSize: 0.001,
                  areaStyle: {},
                  symbol: "circle", //拐点样式
                  smooth: true, //true 为平滑曲线，false为直线
                  itemStyle: {
                    normal: {
                      color: "#fff",
                      borderColor: "blue",
                      borderWidth: 3,
                      label: {
                        show: true,
                        position: "left",
                        textStyle: {
                          fontSize: 16,
                          color: "#fff",
                          // width: 54,
                          // height: 27,
                          backgroundColor: "blue",
                        },
                        formatter: (params) => {
                          // console.log(params);
                          // console.log(this.option.series[0].data.length);
                          if (
                            transaction_num_for_7time.length - 1 ==
                            params.dataIndex
                          ) {
                            return params.value;
                          } else {
                            return "";
                          }
                        },
                      },
                    },
                  },
                  areaStyle: {
                    normal: {
                      color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: "green" },
                        { offset: 0.4, color: "green" },
                        { offset: 1, color: "#fff" },
                      ]),
                    },
                  },
                  lineStyle: {
                    color: "green", //改变折线颜色
                  },
                },
              ],
            });
          }
        })
        .catch((e) => {});
    },
    async rank() {
      let that = this;
      await that.$http.get("/search_top_n").then((res) => {
        // console.log(res);
        this.tabledataall = res.data.count[0].count;

        for (let i = 0; i < res.data.topN.length; i++) {
          this.tableData3[i].Sort_num = "Top" + res.data.topN[i].Sort_num;
          this.tableData3[i].count = res.data.topN[i].count;
          this.tableData3[i].gas = res.data.topN[i].gas / 1000000;
          // this.tableData3[i].
        }
      });
    },
    //获取首页数据
    async indexlist() {
      let that = this;
      await that.$http
        .get("")
        .then((res) => {
          this.loading = false;
          // console.log(res);
          // 获取首页数据集合
          var cardleftinformation = res.data[0];
          //console.log(cardleftinformation);
          // 区块高度
          // 最新交易数据
          this.tableData = cardleftinformation.transaction_info_for_index;
          //  console.log(this.tableData);
          // 最新出块数据
          this.tableData2 = cardleftinformation.block_new;
          // console.log(this.tableData.length);
          // 时间戳的处理
          if (this.nowLang == "cn") {
            for (var i = 0; i < this.tableData.length; i++) {
              let date = [];
              let strdate = this.tableData[i].date;
              // console.log(strdate + "shuju");
              // 当前日期转时间戳
              let timestamp = Date.parse(new Date()) / 1000;
              // console.log(timestamp + "xianzai");
              let s = timestamp - strdate; //9.20
              // console.log(s+'相差');
              // console.log(s/86400000 + "天数");
              // console.log(parseInt(s/86400000*24*60) + "fenzhong");
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              //  console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  date.push("刚刚");
                } else {
                  date.push(parseInt(fenzhong) + "分钟前");
                }

                this.tableData[i].date = date;
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                date.push(parseInt(fenzhong / 60) + "小时前");
                this.tableData[i].date = date;
              }
              if (fenzhong > 1440) {
                date.push(parseInt(fenzhong / 1440) + "天前");
                this.tableData[i].date = date;
              }
              // console.log(this.tableData[i].date);
              this.tableData[i].transaction_hash2 = this.tableData[
                i
              ].transaction_hash;
              this.tableData[i].transaction_hash =
                this.tableData[i].transaction_hash.substring(0, 10) + "...";
              this.tableData[i].from_address =
                this.tableData[i].from_address.substring(0, 10) + "...";
              if (
                this.tableData[i].to_address ==
                "0000000000000000000000000000000000"
              ) {
                if (this.nowLang == "cn") {
                  this.tableData[i].to_address = "质押";
                }
                if (this.nowLang == "en") {
                  this.tableData[i].to_address = "Pledge";
                }
              } else {
                this.tableData[i].to_address =
                  this.tableData[i].to_address.substring(0, 10) + "...";
              }
            }
            //console.log(this.tableData2.length);
            for (var j = 0; j < this.tableData2.length; j++) {
              let times = [];
              let strtime = this.tableData2[j].time;
              // 当前日期转时间戳
              let timestamp = Date.parse(new Date()) / 1000;
              // console.log(timestamp + "xianzai");
              let s = timestamp - strtime; //9.20
              // console.log(s+'相差');
              // console.log(s/86400000 + "天数");
              // console.log(parseInt(s/86400000*24*60) + "fenzhong");
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              // console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  times.push("刚刚");
                } else {
                  times.push(parseInt(fenzhong) + "分钟前");
                }

                this.tableData2[j].time = times;
              }

              if (fenzhong >= 60 && fenzhong <= 1440) {
                times.push(parseInt(fenzhong / 60) + "小时前");
                this.tableData2[j].time = times;
              }
              if (fenzhong > 1440) {
                times.push(parseInt(fenzhong / 1440) + "天前");
                this.tableData2[j].time = times;
              }
              // console.log(times);
              // console.log(strtime);
              // times.push(this.timestampToTime(Number(strtime)));
              // console.log(times);
            }
          } else {
            for (var i = 0; i < this.tableData.length; i++) {
              let date = [];
              let strdate = this.tableData[i].date;
              // console.log(strdate + "shuju");
              // 当前日期转时间戳
              let timestamp = Date.parse(new Date()) / 1000;
              // console.log(timestamp + "xianzai");
              let s = timestamp - strdate; //9.20
              // console.log(s+'相差');
              // console.log(s/86400000 + "天数");
              // console.log(parseInt(s/86400000*24*60) + "fenzhong");
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              //  console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  date.push("just");
                } else {
                  date.push(parseInt(fenzhong) + "minutes ago");
                }

                this.tableData[i].date = date;
              }
              if (fenzhong >= 60 && fenzhong <= 1440) {
                date.push(parseInt(fenzhong / 60) + "hour ago");
                this.tableData[i].date = date;
              }
              if (fenzhong > 1440) {
                date.push(parseInt(fenzhong / 1440) + "days ago");
                this.tableData[i].date = date;
              }
              // console.log(this.tableData[i].date);
              this.tableData[i].transaction_hash2 = this.tableData[
                i
              ].transaction_hash;
              this.tableData[i].transaction_hash =
                this.tableData[i].transaction_hash.substring(0, 10) + "...";
              this.tableData[i].from_address =
                this.tableData[i].from_address.substring(0, 10) + "...";
              this.tableData[i].to_address =
                this.tableData[i].to_address.substring(0, 10) + "...";
            }
            //console.log(this.tableData2.length);
            for (var j = 0; j < this.tableData2.length; j++) {
              let times = [];
              let strtime = this.tableData2[j].time;
              // 当前日期转时间戳
              let timestamp = Date.parse(new Date()) / 1000;
              // console.log(timestamp + "xianzai");
              let s = timestamp - strtime; //9.20
              // console.log(s+'相差');
              // console.log(s/86400000 + "天数");
              // console.log(parseInt(s/86400000*24*60) + "fenzhong");
              let fenzhong = parseInt((s / 86400) * 24 * 60);
              // console.log(fenzhong);
              if (fenzhong < 60) {
                if (fenzhong == 0) {
                  times.push("just");
                } else {
                  times.push(parseInt(fenzhong) + "minutes ago");
                }

                this.tableData2[j].time = times;
              }

              if (fenzhong >= 60 && fenzhong <= 1440) {
                times.push(parseInt(fenzhong / 60) + "hour ago");
                this.tableData2[j].time = times;
              }
              if (fenzhong > 1440) {
                times.push(parseInt(fenzhong / 1440) + "days ago");
                this.tableData2[j].time = times;
              }
              // console.log(times);
              // console.log(strtime);
              // times.push(this.timestampToTime(Number(strtime)));
              // console.log(times);
            }
          }
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
          this.money = res.data[0].usdt[0].usdt;
          this.money2 = res.data[0].usdt[0].rmb;
          //24小时交易笔数?
          this.transzoom =
            cardleftinformation.transaction_num_for_24h[0].transaction_num;
          // console.log(this.transzoom);
          // 24小时交易总额?
          this.transmoney =
            cardleftinformation.transaction_amount_for_24h[0].transaction_amount_24h;

          // console.log(this.transmoney);
          // console.log(res.data[0].block_height_all[0].block_height);
          //this.totalNum = res.data.result.total;
          //console.log(this.totalNum);
          // table赋值
          //for (let i = 0; i < res.data.result.list.length + 1; i++) {
          //var obj = {};
          //obj.height = res.data.result.list[i].content_id;
          //console.log(obj);
          //blockData[i] = obj;
          //console.log(blockData);
          //this.blockData = blockData;
          //console.log(obj);
          //}
          localStorage.setItem("lan", this.nowLang);
        })
        .catch((e) => {});
    },
    timestampToTime(timestamp) {
      var date = new Date(timestamp); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
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
    timestampToTime2(timestamp) {
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
    //日期转时间戳
    transdate(time) {
      var date = new Date();
      date.setFullYear(time.substring(0, 4));
      date.setMonth(time.substring(5, 7) - 1);
      date.setDate(time.substring(8, 10));
      date.setHours(time.substring(11, 13));
      date.setMinutes(time.substring(14, 16));
      date.setSeconds(time.substring(17, 19));
      return Date.parse(date) / 1000;
    },
    // 点击卡片切换
    cardclick1() {
      this.card3 = false;
      this.card2 = false;
      this.card = true;
    },
    cardclick2() {
      this.card2 = true;
      this.card = false;
      this.card3 = false;
    },
    cardclick3() {
      this.card2 = false;
      this.card = false;
      this.card3 = true;
    },

    // 首页跳转到交易详情页
    gototransactiondetail(row, event, column) {
      this.$router.push({
        path: "transactiondetail",
        query: { transaction_hash: row.transaction_hash2 },
      });
      // console.log(row, event, column);
    },
    // 首页跳转到块详情页
    gotoblockdetail(row, event, column) {
      this.$router.push({
        path: "/blockdetail",
        query: { blockheight: row.block_height },
      });
      //  console.log(row, event, column);
    },
    // 转到交易界面
    gototransaction() {
      this.$router.push({ path: "/transaction" });
    },
    // 转到区块界面
    gotoblock() {
      this.$router.push({ path: "/block" });
    },
  },
 
};
</script>
<style lang="less">
#barss {
  .number {
    position: relative;
    left: 70%;
    top: 90%;
    font-size: 14px;
  }
  .el-table--border td {
    border-right: none !important;
  }
  .number2 {
    position: relative;
    left: 70%;
    top: 88%;
    font-size: 12px;
  }
  .el-table td {
    border: none !important;
  }
  .el-table {
    position: absolute !important;
    top: 54px !important;
    height: 220px !important;
    left: 50px !important;
    width: 470px;
    background: #ffffff;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 15px;
  }
  .has-gutter {
    line-height: 36px !important;
    font-size: 16px;
    font-family: "苹方-简";
    font-weight: normal;
    color: #333333;
    opacity: 1;
  }
  .el-table .cell {
    line-height: 35px !important;
  }
  .el-table td,
  .el-table th {
    padding: 0px !important;
  }
}
// 本页面
.index {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  margin-bottom: 20px;
  opacity: 1;
  border-radius: 40px;
  .el-table td {
    border-bottom: 1px solid rgba(51, 51, 51, 0.1);
  }
  // .el-table th {
  //   background: rgba(40, 96, 149, 0.1) !important;
  // }
  .el-table__header tr th {
    background: rgba(40, 96, 194, 0.001) !important;
  }
  .cardblue {
    color: rgba(40, 96, 194, 1) !important;
  }
  .indexzong {
    width: 1200px;
    height: auto;
    background: rgba(232, 234, 243, 1);
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 40px;
    margin: 0 auto;
  }
  .card {
    width: 100%;
    display: flex;
    flex-direction: row;
    position: relative;
    // 卡片左边
    .cardleft {
      width: 550px;
      height: 305px;
      background: rgba(40, 96, 194, 1);
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      border-radius: 20px;
      position: relative;
      left: 45px;
      .cardlefttop {
        display: flex;
        flex-direction: row;
        position: relative;
        img {
          position: absolute;
          left: 40px;
          top: 30px;
        }
        .cardlefttopright {
          p:nth-child(1) {
            position: absolute;
            left: 91px;
            top: 30px;
            font-size: 16px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 28px;
            color: rgba(255, 255, 255, 1);
            opacity: 1;
          }
          p:nth-child(2) {
            position: absolute;
            left: 91px;
            top: 58px;
            font-size: 20px;
            font-family: "苹方-简";
            font-weight: normal;
            line-height: 17px;
            color: rgba(255, 255, 255, 1);
            opacity: 1;
          }
        }
      }
      .cardleftbottom {
        width: 470px;
        height: 160px;
        background: rgba(77, 121, 242, 1);
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        opacity: 1;
        border-radius: 15px;
        position: absolute;
        left: 40px;
        top: 115px;
        ul {
          display: flex;
          flex-direction: row;
          justify-content: space-around;
          flex-wrap: wrap;
          li {
            width: 140px;
            margin-top: 15px;
            margin-left: 15px;
            text-align: left;
            p:nth-child(1) {
              font-size: 18px;
              font-family: "苹方-简";
              font-weight: normal;
              line-height: 25px;
              color: rgba(255, 255, 255, 1);
              opacity: 1;
            }
            p:nth-child(2) {
              font-size: 16px;
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
    // 卡片右边
    .cardright {
      width: 550px;
      height: 305px;
      background: rgba(255, 255, 255, 1);
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      opacity: 1;
      border-radius: 20px;
      position: relative;
      left: 66px;
    }
    .cardp {
      width: 550px;
      position: absolute;
      left: 620px;
      top: 30px;
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      cursor: pointer;
      p {
      }
      p:nth-child(2) {
      }
    }
  }
  .indexcontent {
    width: 1120px;
    height: 915px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    opacity: 1;
    border-radius: 20px;
    margin: 0 auto;
    margin-top: 20px;
    position: relative;
    // 最新
    .last {
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 28px;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
      position: relative;
      left: 40px;
      top: 30px;
      margin-bottom: 50px;
    }
    // 查看更多
    .seemore {
      width: 1040px !important;
      margin: 0 auto;
      height: 61px;
      line-height: 61px !important;
      text-align: center;
      font-size: 20px;
      font-family: "苹方-简";
      font-weight: normal;
      color: rgba(40, 96, 194, 1);
      opacity: 1;
      cursor: pointer;
      background: #d5e1f4;
      border-top: 1px solid rgba(51, 51, 51, 0.1);
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
    }
    .el-table__row {
      height: 51px;
      line-height: 51px;
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(51, 51, 51, 1);
    }
    .el-table {
      background: rgba(40, 96, 194, 0.1) !important;
    }
    .el-table tr {
      background: rgba(40, 96, 194, 0.1) !important;
      //  background: rgba(40, 96, 149) !important;
    }
    // 表格1
    .eltable1 {
      width: 1040px !important;
      margin: 0 auto;
      position: relative;
      height: 304px;
      outline: none;
      border: none;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
      cursor: pointer;
      .el-table__body tr td {
        text-align: center;
      }
      .has-gutter tr {
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
        background-color: rgba(40, 96, 194, 0.2) !important;
        th div {
          text-align: center;
        }
      }
    }
    // 表格2
    .eltable2 {
      width: 1040px !important;
      margin: 0 auto;
      height: 304px;
      outline: none;
      border: none;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
      cursor: pointer;
      .el-table__body tr td {
        text-align: center;
      }
      .has-gutter tr {
        font-size: 16px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 22px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
        border: 1px solid rgba(51, 51, 51, 0.1);
        background-color: rgba(40, 96, 194, 0.2) !important;
        th div {
          text-align: center;
        }
      }
    }
    .el-table__header-wrapper {
      width: 100%;
      border-radius: 15px;
    }
  }
  // 内容底部
  .indexfooter {
    width: 1175px;
    height: 277px;
    position: relative;
    margin: 0 auto;
    background: url("../assets/images/index/Icon 3.png") no-repeat center/100%
      100%;
    .footertop {
      position: relative;
      left: 70px;
      top: 57px;
      span {
        position: relative;
        left: 10px;
        top: -5px;
        font-size: 20px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 28px;
        color: rgba(51, 51, 51, 1);
        opacity: 1;
      }
    }
    .footercontent p {
      position: relative;
      width: 1030px;
      top: 63px;
      left: 80px;
      text-indent: 2em;
      font-size: 16px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 22px;
      color: rgba(51, 51, 51, 1);
      opacity: 1;
    }
    .footerfooter ul {
      width: 1030px;
      position: relative;
      top: 74px;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      margin: 0 auto;
      li {
        font-size: 20px;
        font-family: "苹方-简";
        font-weight: normal;
        line-height: 28px;
        color: rgba(40, 96, 194, 1);
        opacity: 1;
      }
    }
  }
}
</style>
