use read_event;
DROP INDEX index_all ON read_event_c;
ALTER TABLE `read_event_c` ADD INDEX index_all (`timeStamp`, `app`, `userLevel`, `userNewOld`, `ismonth`, `userFee`, `areaLevel`, `status`, `cate`);
