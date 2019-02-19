use item_exhibit;
DROP INDEX index_all ON item_exhibit;
ALTER TABLE `item_exhibit` ADD INDEX index_all (`timeStamp`);