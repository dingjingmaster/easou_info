use item_exhibit;
-- DROP INDEX index_app ON item_exhibit;
-- DROP INDEX index_fee ON item_exhibit;
-- DROP INDEX index_all ON item_exhibit;
-- DROP INDEX index_time ON item_exhibit;
-- DROP INDEX index_area ON item_exhibit;
-- DROP INDEX index_user ON item_exhibit;
-- DROP INDEX index_module ON item_exhibit;
-- DROP INDEX index_strategy ON item_exhibit;


-- ALTER TABLE `item_exhibit` ADD INDEX index_app (`app`);
-- ALTER TABLE `item_exhibit` ADD INDEX index_fee (`itemFee`);
-- ALTER TABLE `item_exhibit` ADD INDEX index_area (`areaLevel`);
-- ALTER TABLE `item_exhibit` ADD INDEX index_user (`userLevel`);

ALTER TABLE `item_exhibit` ADD INDEX index_module (`module`);


-- ALTER TABLE `item_exhibit` ADD INDEX index_time (`timeStamp`);
CREATE INDEX idx_time ON item_exhibit(timeStamp);

ALTER TABLE `item_exhibit` ADD INDEX index_strategy (`strategy`);
ALTER TABLE `item_exhibit` ADD INDEX index_all (`timeStamp`, `app`, `module`, `areaLevel`, `userLevel`, `userNewOld`, `userFee`, `itemFee`, `strategy`, `status`, `view`, `intime`);

