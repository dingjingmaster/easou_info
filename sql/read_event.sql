alter database read_event default character set utf8;

use read_event;

CREATE TABLE IF NOT EXISTS `read_event` (
  `id` VARCHAR(1024) NOT NULL             COMMENT '主键，包含所有信息的简写',
  `app` INT(12) DEFAULT 0 NOT NULL        COMMENT '1.宜搜 2.微卷 3.其它',
  `userLevel` INT(12) DEFAULT 0 NOT NULL  COMMENT '1.普通用户 2.特殊用户 3.其它',
  `userNewOld` INT(12) DEFAULT 0 NOT NULL COMMENT '1.新用户 2.老用户 3.其它',
  `ismonth` INT(12) DEFAULT 0 NOT NULL    COMMENT '1.包月 2.非包月 3.其它',
  `userFee` INT(12) DEFAULT 0 NOT NULL    COMMENT '1.纯免费 2.潜在付费 3.轻度付费 4.中度付费 5.重度付费 6.其它',
  `areaLevel` INT(12) DEFAULT 0 NOT NULL  COMMENT '1.一类地区 2.二类地区 3.三类地区 4.四类地区 5.其它',
  `status` INT(12) DEFAULT 0 NOT NULL     COMMENT '1.连载 2.完结 3.其它',
  `cate` INT(12) DEFAULT 0 NOT NULL       COMMENT '1.按章计费 2.包月 3.非包月 4.限免 5.一折书籍 6.免费CP书 7.免费互联网书 8.断更 9.普通 10.赠书 11.其它',
  `gidNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '书籍量',
  `usrNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '用户量',
  `chgNum` INT(12) DEFAULT 0 NOT NULL     COMMENT '付费章节量',
  `freNum` INT(12) DEFAULT 0 NOT NULL    COMMENT  '免费章节量',
  `tfNum` INT(12) DEFAULT 0 NOT NULL     COMMENT  '限免章节量',
  `sumNum` INT(12) DEFAULT 0 NOT NULL    COMMENT  '总章节量',
  `timeStamp` INT(12) DEFAULT 0 NOT NULL  COMMENT '时间戳',
  PRIMARY KEY (`id`)
);

alter table read_event default character set utf8;
