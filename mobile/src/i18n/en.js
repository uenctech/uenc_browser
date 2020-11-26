import enLocale from "element-ui/lib/locale/lang/en";
const en = {
  nav: [
    {
      PageTo: "首页",
      title: "Home",
      src: require("../assets/images/index/首页.png"),
      src2: require("../assets/images/index/首页(1).png")
    },
    {
      PageTo: "区块",
      title: "Block",
      src: require("../assets/images/index/区块.png"),
      src2: require("../assets/images/index/区块(1).png")
    },
    {
      PageTo: "交易",
      title: "Trans",
      src: require("../assets/images/index/交易.png"),
      src2: require("../assets/images/index/交易(1).png")
    },

    {
      PageTo: "地址",
      title: "Address",
      src: require("../assets/images/index/地址.png"),
      src2: require("../assets/images/index/地址(1).png")
    },


  ],
  ranliaofeiaverage:['（Average fuel cost:',')'],
  page: ['first', 'last'],
  publicsection: ['UENC Mainnet', 'Search', 'Search Address, Transaction/block hash, Block Height, etc.', 'Block Height',
    'TX Amount', 'TX volume', 'From', 'To',
    'Time', 'View More', 'Home Page', 'End Page','Block Height','amount_detail'],
  home: {
    cardleft: ['24H TX Amount', '24H TX volume', 'Block Reward', ' Remaining Reward','Block explorer'],
    cardright: ['Average value of transaction fuel fee (first 100 blocks)', 'Number of transactions per day'],
    contenttop: ['Latest Transaction', ' TxHash', 'Gas Fee',],
    contentbottom: ['Latest Block', 'Block Reward'],
    bottom: ['UENC is a scalable blockchain-based public chain system with cross-chain research as its technical direction. Through optimization and innovation on the underlying technology and architecture of the blockchain, it supports the communication between different blockchain networks. Value transfer and improve its security. UENC establishes an efficient node combination structure by developing a hybrid point-to-point network based on DHT technology, cross-parallel storage technology (CPS), and trusted zone technology (TA), thereby rapidly increasing the speed of blockchain transactions. ',
      'Publish time:',
      'Total circulation:', 'Total circulation:', 'Official website:'
    ]
  },
  block: {
    content: ['Block List', 'Block Block Reward',],
    content2: ['Block Reward', 'TX volume', 'Block List', 'Block Hash'],
    content3: ['Pre-hash']
  },
  transaction: {
    content: ['Transaction List', 'TxHash', 'Gas Fee', 'Balance', 'Trans List'],
    content2: ['Award:', 'Sign_node:', 'Transaction', 'Gas Fee ', 'Block Reward', 'Trans_time', 'Signature Node', 'Details']
  },
  chart: ['Daily UENC Transaction Index (USDT)', 'Daily Transaction Number', 'Daily Transaction Total', 'Daily Block Total', 'Average Transaction Fuel Fee (First 100 Blocks)'],
  address: {
    content: ['UENC address:', 'Ranking', 'Address', 'Amount', 'Percentage', 'Total', 'Item']
  },
  notfound: ['Sorry, the data you want could not be found, please search again...','Loading failed, please check the network or try again later'],
  wallet: ['Manage your digital assets', 'Fastoken is a digital asset management software that provides a safe, secure, easy-to-use, and powerful wallet application for ordinary users and miners. It is currently in the second phase of the public beta. ', 'Fastoken provides functions such as transfer transactions, secure storage and fast payment. Transfer transactions are fast and safe and secure. At the current public beta phase, a transaction can be completed in 1 second, and the historical transaction records in the wallet account are clear at a glance. By adopting a decentralized design, the wallet provides convenient and fair mining functions for miners and users can freely choose stable nodes for broadcast transactions. '],
  ...enLocale
};

export default en;
