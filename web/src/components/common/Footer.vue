<template>
  <div class="uenc_foot">
    <div class="footer">
      <p>Copyright©2015-2018 UENC.All Rights Reserved UENC</p>
    </div>
  </div>
</template>
<script>
export default {
  name: "foot",
  data() {
    return {
      nowLang: "en",
      show: false,
    };
  },
  created() {},
  mounted() {},
  methods: {},
};
</script>
<style lang="less">
.uenc_foot {
  width: 1200px;
  height: 115px;
  position: relative;
  margin: 0 auto;
  .footer {
    width: 1175px;
    height: 115px;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    background: url("../../assets/images/footer/Icon 3(1).png") no-repeat
      center/100% 100%;
    p {
      width: 100%;
     position: relative;
     top: 48px;
      text-align: center;
      font-size: 12px;
      font-family: "苹方-简";
      font-weight: normal;
      line-height: 17px;
      color: rgba(255, 255, 255, 1);
      opacity: 1;
    }
  }
}
.foot_word {
  font-size: 18px;
  color: #fff;
}
</style>
