SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_address
-- ----------------------------
DROP TABLE IF EXISTS `t_address`;
CREATE TABLE `t_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(255) NOT NULL,
  `amount` double(20,0) NOT NULL,
  `transaction_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `index_address` (`address`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3782 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_avg_gas
-- ----------------------------
DROP TABLE IF EXISTS `t_avg_gas`;
CREATE TABLE `t_avg_gas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `avg_gas` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1622 DEFAULT CHARSET=utf8 COLLATE=utf8_bin ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_award
-- ----------------------------
DROP TABLE IF EXISTS `t_award`;
CREATE TABLE `t_award` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transaction_id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `amount` double(20,0) NOT NULL,
  `tx_hash` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `index_transaction_id` (`transaction_id`) USING BTREE,
  KEY `index_address` (`address`) USING BTREE,
  KEY `index_type` (`type`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14527 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_block
-- ----------------------------
DROP TABLE IF EXISTS `t_block`;
CREATE TABLE `t_block` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `height` int(11) NOT NULL,
  `hash` varchar(255) NOT NULL DEFAULT '',
  `prevHash` varchar(255) NOT NULL DEFAULT '',
  `time` bigint(20) NOT NULL,
  `merkleRoot` varchar(255) NOT NULL DEFAULT '',
  `extra` text NOT NULL,
  `comment` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `index_hash` (`hash`) USING BTREE,
  KEY `index_height` (`height`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1206 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_count_block
-- ----------------------------
DROP TABLE IF EXISTS `t_count_block`;
CREATE TABLE `t_count_block` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(255) NOT NULL DEFAULT '' COMMENT '统计日期',
  `count` int(11) NOT NULL COMMENT '统计当天区块数量',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `count_block_date_index` (`date`) USING BTREE COMMENT '每天的记录只存储一条'
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_count_transaction
-- ----------------------------
DROP TABLE IF EXISTS `t_count_transaction`;
CREATE TABLE `t_count_transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` bigint(20) NOT NULL COMMENT '统计日期',
  `countResulte` int(11) NOT NULL COMMENT '统计当天交易笔数',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `date_index` (`date`) USING BTREE COMMENT '每天的统计记录只能存储一条'
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_count_transaction_amount
-- ----------------------------
DROP TABLE IF EXISTS `t_count_transaction_amount`;
CREATE TABLE `t_count_transaction_amount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(255) NOT NULL DEFAULT '' COMMENT '统计日期',
  `count` double(20,6) NOT NULL COMMENT '统计结果',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `count_transaction_amoun_indext` (`date`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_gas
-- ----------------------------
DROP TABLE IF EXISTS `t_gas`;
CREATE TABLE `t_gas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gas` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3677 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_transaction
-- ----------------------------
DROP TABLE IF EXISTS `t_transaction`;
CREATE TABLE `t_transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `block_id` int(11) NOT NULL,
  `transaction_hash` varchar(255) NOT NULL DEFAULT '',
  `type` varchar(255) NOT NULL DEFAULT '',
  `from_address` mediumtext NOT NULL,
  `to_address` mediumtext NOT NULL,
  `amount` double(20,0) NOT NULL,
  `fee` double(20,0) NOT NULL,
  `time` bigint(20) NOT NULL,
  `extra` text NOT NULL,
  `comment` text NOT NULL,
  `amount_detail` mediumtext,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `f_block_id` (`block_id`) USING BTREE,
  KEY `index_transaction_hash` (`transaction_hash`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1198 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for t_tx_detail
-- ----------------------------
DROP TABLE IF EXISTS `t_tx_detail`;
CREATE TABLE `t_tx_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tx_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `amount` double(20,0) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tx_detail_address` (`address`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=7360 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_usdt
-- ----------------------------
DROP TABLE IF EXISTS `t_usdt`;
CREATE TABLE `t_usdt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `usdt` double(20,6) NOT NULL,
  `rmb` double(20,6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1402 DEFAULT CHARSET=utf8 COLLATE=utf8_bin ROW_FORMAT=DYNAMIC;
