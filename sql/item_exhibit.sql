alter database item_exhibit default character set utf8;

use item_exhibit;

CREATE TABLE IF NOT EXISTS `item_exhibit` (
  `id` VARCHAR(320) NOT NULL              COMMENT '主键，包含所有信息的简写',
  `app` INT(12) DEFAULT 0 NOT NULL        COMMENT '1.宜搜 2.微卷 3.其它',
  `module` INT(12) DEFAULT 0 NOT NULL     COMMENT '1.书架推荐 2.书架-猜你喜欢 3.免费-免费推荐 4.免费-猜你喜欢 5.包月瀑布流 6.封面页-类别推荐 7.封面页-读本书的人还看过 8.封面页-读本书的人还看过更多 9.搜索结果页-热搜TOP榜 10.搜索结果页-猜你喜欢 11.章末页-读本书的人还看过 12.精选-女频瀑布流 13.精选-完结佳作 14.精选-完结瀑布流 15.精选-排行瀑布流 16.精选-根据阅读书籍推荐 17.精选-根据阅读分类推荐 18.精选-瀑布流 19.精选-热门推荐 20.精选-男频瀑布流 21.精选-精品必读 22.退出拦截推荐',
  `areaLevel` INT(12) DEFAULT 0 NOT NULL  COMMENT '1.一类地区 2.二类地区 3.三类地区 4.其它',
  `userLevel` INT(12) DEFAULT 0 NOT NULL  COMMENT '1.普通用户 2.特殊用户 3.其它',
  `userNewOld` INT(12) DEFAULT 0 NOT NULL COMMENT '1.新用户 2.老用户 3.其它',
  `userFee` INT(12) DEFAULT 0 NOT NULL    COMMENT '1.纯免费 2.潜在付费 3.轻度付费 4.中度付费 5.重度付费 6.其它',
  `itemFee` INT(12) DEFAULT 0 NOT NULL    COMMENT '1.免费 2.付费 3.包月 4.限免 5.其它',
  `strategy` INT(12) DEFAULT 0 NOT NULL   COMMENT '1.一级同分类 2.二级同分类 3.内容相似 4.同作者 5.同分类 6.实时流 7.流行度 8.物品协同 9.用户协同 10.近期协同 11.其它',
  `status` INT(12) DEFAULT 0 NOT NULL     COMMENT '1.连载 2.完结 3.其它',
  `view` INT(12) DEFAULT 0 NOT NULL       COMMENT '1.[0,10) 2.[10, 100) 3.[100,1000) 4.[1000,10000) 5.[10000,100000) 6.[100000,1000000) 7.[1000000,10000000) 8.其它',
  `intime` INT(12) DEFAULT 0 NOT NULL     COMMENT '1.1月内入库 2.1~3月内入库 3.3~12月内入库 4.12~99月内入库 5.其它',
  `recNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '推荐量',
  `clkNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '点击量',
  `subNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '订阅量',
  `redNum1` INT(12) DEFAULT 0 NOT NULL    COMMENT '订阅后次日阅读量',
  `redNum7` INT(12) DEFAULT 0 NOT NULL    COMMENT '',
  `redNum30` INT(12) DEFAULT 0 NOT NULL   COMMENT '',
  `redChap1` INT(12) DEFAULT 0 NOT NULL   COMMENT '',
  `redChap7` INT(12) DEFAULT 0 NOT NULL   COMMENT '',
  `redChap30` INT(12) DEFAULT 0 NOT NULL  COMMENT '',
  `value1` INT(12) DEFAULT 0 NOT NULL     COMMENT '',
  `value7` INT(12) DEFAULT 0 NOT NULL     COMMENT '',
  `value30` INT(12) DEFAULT 0 NOT NULL    COMMENT '',
  `timeStamp` INT(12) DEFAULT 0 NOT NULL  COMMENT '时间戳',
  PRIMARY KEY (`id`)
);

-- 删除了旧的
--alter table `item_exhibit` drop column `redNum2`;

-- 增加新的列
--alter table `item_exhibit` add column `redNum7` INT(12) default 0;
--alter table `item_exhibit` add column `redNum30` INT(12) default 0;
--alter table `item_exhibit` add column `redChap1` INT(12) default 0;
--alter table `item_exhibit` add column `redChap7` INT(12) default 0;
--alter table `item_exhibit` add column `redChap30` INT(12) default 0;
--alter table `item_exhibit` add column `value1` INT(12) default 0;
--alter table `item_exhibit` add column `value7` INT(12) default 0;
--alter table `item_exhibit` add column `value30` INT(12) default 0;

alter table item_exhibit default character set utf8;
