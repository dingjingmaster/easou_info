use item_exhibit;
DROP INDEX index_all ON item_exhibit;
ALTER TABLE `item_exhibit` ADD INDEX index_all ( `app`, `module`, `areaLevel`, `userLevel`, `userFee`, `itemFee`, `strategy`, `status`, `view`, `intime`);