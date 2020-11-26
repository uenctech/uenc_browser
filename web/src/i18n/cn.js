import zhLocale from "element-ui/lib/locale/lang/zh-CN";
const cn = {
  nav: [
    {
      path: "/",
      title: "首页",
      src: require("../assets/images/header/home.png")
    },
    {
      path: "/block",
      title: "区块",
      src: require("../assets/images/header/block.png")
    },
    {
      path: "/transaction",
      title: "交易",
      src: require("../assets/images/header/transaction.png")
    },
    {
      path: "/chart",
      title: "图表",
      src: require("../assets/images/header/chart.png")
    },
    {
      path: "/address",
      title: "地址",
      src: require("../assets/images/header/address.png")
    },
    {
      path: "/wallet",
      title: "Fastoken",
      src: require("../assets/images/header/wallet.png")
    },

  ],
  footerlast:['2亿','6000万','更多','更多详情'],
  page:['首页','尾页','排名','节点数量','燃料费数值','(设置有效燃料费节点)'],
  publicsection: ['UENC主网', '搜索', '搜索地址，交易/区块哈希，区块高度等', '区块高度',
    '交易笔数', '交易额', '从', '至',
    '时间', '查看更多', '首页', '尾页','交易详情'],
  home: {
    cardleft: ['24H交易笔数', '24H交易总额', '区块奖励', '剩余区块奖励'],
    cardright: ['交易燃料费平均值(前100块)', '每日交易笔数','燃料费分布图'],
    contenttop: ['最新交易', '交易哈希', '燃料费',],
    contentbottom: ['最新出块', '块区块奖励'],
    bottom: ['UENC是一个以跨链研究为技术方向的可扩展的区块链基础公链系统，通过在区块链底层技术和架构上进行优化和创新，支持不同区块链网络之间的价值传递，并提升其安全性。UENC通过研发基于DHT技术、交叉式并行存储技术 (CPS) 、可信任区域技术 (TA) 的混合式点对点网络，建立高效的节点组合结构，进而快速提升区块链交易速度。',
      '发行时间:',
      '发行总量:', '流通总量:', '官网:'
    ]
  },
  block: {
    content: ['区块列表', '块区块奖励',],
    content2: ['区块奖励', '交易总额', '区块列表', '区块哈希'],
    content3: ['前置哈希']
  },
  transaction: {
    content: ['交易列表', '交易哈希', '燃料费','余额','交易列表'],
    content2: ['共识数:', '交易签名节点:', '交易信息', '燃料费信息', '区块奖励信息', '交易时间', '签名节点', '详情']
  },
  chart: ['每日UENC交易指数（USDT）',' 每日交易笔数','每日交易总额',' 每日区块总数','交易燃料费平均值（前100块）'],
  address: {
    content: ['UENC地址：', '排名', '地址', '金额', '占百分比','共','条']
  },
  notfound:['抱歉,未能找到您要的数据，请重新搜索...'],
  wallet: ['管理您的数字资产','Fastoken 是一款数字资产管理软件，为普通用户及矿工提供安全放心、简单好用、功能强大的钱包应用，目前UENC主网已经上线。','Fastoken提供转账交易、安全存储及快捷支付等功能，转账交易快速且安全有保障，目前公测阶段实现1秒完成一笔交易，钱包账户中历史交易记录一目了然。通过采用去中心化的设计，钱包为矿工提供便捷公平挖矿功能以及用户可以自由选择稳定的节点进行广播交易。'],
  ...zhLocale
};

export default cn;
