import enLocale from "element-ui/lib/locale/lang/en";
const en = {
  nav: [
    {
      path: "/",
      title: "Home",
      src: require("../assets/images/header/home.png")
    },
    {
      path: "/block",
      title: "Block",
      src: require("../assets/images/header/block.png")
    },
    {
      path: "/transaction",
      title: "Trans",
      src: require("../assets/images/header/transaction.png")
    },
    {
      path: "/chart",
      title: "Chart",
      src: require("../assets/images/header/chart.png")
    },
    {
      path: "/address",
      title: "Address",
      src: require("../assets/images/header/address.png")
    },
    {
      path: "/wallet",
      title: "Fastoken",
      src: require("../assets/images/header/wallet.png")
    },

  ],
  footerlast:['0.2 Billion','60 Million','More','More Details'],
  page:['first','last','Rank','Node Number','fuel cost value','(Set effective fuel cost node)'],
  publicsection: ['UENC Mainnet', 'Search', 'Search Address, Transaction/block hash, Block Height, etc.', 'Block Height',
    'TX Amount', 'TX volume', 'From', 'To',
    'Time', 'View More', 'Home Page', 'End Page','amount_detail'],
  home: {
    cardleft: ['24H TX Amount', '24H TX volume', 'Block Reward', ' Remaining Reward'],
    cardright: ['Average value of transaction fuel fee (first 100 blocks)', 'Number of transactions per day','Fuel cost distribution map'],
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
    content: ['Transaction List', 'TxHash', 'Gas Fee','Balance','Trans List'],
    content2: ['Award:', 'Sign_node:', 'Transaction', 'Gas Fee ', 'Block Reward', 'Trans_time', 'Signature Node', 'Details']
  },
  chart: ['Daily UENC Transaction Index (USDT)','Daily Transaction Number','Daily Transaction Total','Daily Block Total','Average Transaction Fuel Fee (First 100 Blocks)'],
  address: {
    content: ['UENC address:', 'Ranking', 'Address', 'Amount', 'Percentage','Total','Item']
  },
  notfound:['Sorry, the data you want could not be found, please search again...'],
  wallet: ['Manage your digital assets', 'Fastoken is a digital asset management software that provides a safe, secure, easy-to-use, and powerful wallet application for ordinary users and miners. The UENC mainnet is currently online.', 'Fastoken provides functions such as transfer transactions, secure storage and fast payment. Transfer transactions are fast and safe and secure. At the current public beta phase, a transaction can be completed in 1 second, and the historical transaction records in the wallet account are clear at a glance. By adopting a decentralized design, the wallet provides convenient and fair mining functions for miners and users can freely choose stable nodes for broadcast transactions. '],
  ...enLocale
};

export default en;
