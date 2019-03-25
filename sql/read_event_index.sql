use read_event;
DROP INDEX index_all ON read_event;
ALTER TABLE `read_event` ADD INDEX index_all (`timeStamp`, `app`, `userLevel`, `userNewOld`, `ismonth`, `userFee`, `areaLevel`, `status`, `cate`);