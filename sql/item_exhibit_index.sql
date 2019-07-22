use item_exhibit;
-- DROP INDEX index_app ON item_exhibit;
-- DROP INDEX index_fee ON item_exhibit;
-- DROP INDEX index_all ON item_exhibit;
-- DROP INDEX index_time ON item_exhibit;
-- DROP INDEX index_module ON item_exhibit;
-- DROP INDEX index_strategy ON item_exhibit;


CREATE INDEX idx_app ON item_exhibit(app);
CREATE INDEX idx_fee ON item_exhibit(itemFee);
CREATE INDEX idx_module ON item_exhibit(module);
CREATE INDEX idx_time ON item_exhibit(timeStamp);
CREATE INDEX idx_strategy ON item_exhibit(strategy);
CREATE INDEX idx_all ON item_exhibit(`app`, `module`, `areaLevel`, `userLevel`, `userNewOld`, `userFee`, `itemFee`, `strategy`, `status`, `view`, `intime`);

