-- 书籍信息查询表
alter database item_info default character set utf8;
use item_info;

CREATE TABLE IF NOT EXISTS `item_info` (
  `gid`                 VARCHAR(32) NOT NULL                            COMMENT '主键 书籍ID',
  `name`                VARCHAR(256) NOT NULL                           COMMENT '书名',
  `author`              VARCHAR(256) NOT NULL                           COMMENT '作者名',
  `norm_name`           VARCHAR(256) NOT NULL                           COMMENT '归一书名',
  `norm_author`         VARCHAR(256) NOT NULL                           COMMENT '归一作者名',
  `norm_series`         VARCHAR(256) NOT NULL                           COMMENT '归一系列名',
  `rank`                DOUBLE NOT NULL                                 COMMENT '书籍质量 打分',
  `tag1`                VARCHAR(256) NOT NULL                           COMMENT '标签1',
  `tag2`                VARCHAR(256) NOT NULL                           COMMENT '标签2',
  `view_count`          INT(255) NOT NULL                               COMMENT '历史累计订阅量',
  `status`              INT(4) NOT NULL                                 COMMENT '书籍状态',
  `fee_flag`            VARCHAR(128) NOT NULL                           COMMENT '付费标记',
  `ncp`                 VARCHAR(128) NOT NULL                           COMMENT '归一化 cp id',
  `intime_stamp`        INT(15) NOT NULL                                COMMENT '入库时间',
  `chapter_uptime`      INT(15) NOT NULL                                COMMENT '最新章节更新时间',
  `mask_level`          VARCHAR(128) NOT NULL                           COMMENT '是否屏蔽',
  `by`                  VARCHAR(128) NOT NULL                           COMMENT '是否包月',
  `tf`                  VARCHAR(128) NOT NULL                           COMMENT '是否限免',
  `rn_d`                INT(10) NOT NULL                                COMMENT '天阅读量',
  `rt_d`                DOUBLE NOT NULL                                 COMMENT '天留存率',
  `rn_w`                INT(10) NOT NULL                                COMMENT '周阅读量',
  `rt_w`                DOUBLE NOT NULL                                 COMMENT '周留存率',
  `update_time`         VARCHAR(20) NOT NULL                            COMMENT '啥时候更新的 我自己加的',
  PRIMARY KEY (`gid`)
);

CREATE TABLE IF NOT EXISTS `item_option` (
  `key`                 VARCHAR(1024) NOT NULL                          COMMENT '键',
  `value`               VARCHAR(1024) NOT NULL                          COMMENT '值',
  PRIMARY KEY (`key`)
);

alter table `item_info` default character set utf8;
alter table `item_option` default character set utf8;