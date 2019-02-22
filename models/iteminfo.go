package models

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"time"
)

type ItemInfoRequest struct {
	ReqType                     string                      // gid name author
	Value                       []string                    // 要查询的值
}

func If (c bool, a string, b string) string {
	if c {
		return a
	}
	return b
}

func FeeFlag (tp string) string {
	switch tp {
	case "1":
		return "付费"
	case "10":
		return "公版"
	case "0":
		return "免费"
	}
	return "未知类型"
}

func QueryItemInfo(req *ItemInfoRequest, response *Response) {
	sqls := make(chan string, 10)
	ssql := "SELECT `gid`, `name`, `author`, `norm_name`, `norm_author`, `norm_series`, " +
		"`rank`, `tag1`, `tag2`, `view_count`, `status`, `fee_flag`, `ncp`, " +
		"`intime_stamp`, `chapter_uptime`, `mask_level`, `by`, `tf`, `rn_d`, `rt_d`, " +
		"`rn_w`, `rt_w`, `update_time` "
	go func() {
		for _, g := range req.Value {
			msql := fmt.Sprintf("%s FROM `item_info` WHERE `%s` = '%s';", ssql, req.ReqType, g)
			sqls <- msql
		}
		close(sqls)
	}()
	
	if itemDB, err := sql.Open("mysql", mysqlInfo+"item_info?charset=utf8"); nil == err {
		for mmsql := range sqls {
			var maskLevel, by, tf, updateTime, gid, name, author, normName, normAuthor, normSeries, tag1, tag2,  feeFlag, ncp =
			 	"", "", "", "", "", "", "", "", "", "", "", "", "", ""
			var rank, rtd, rtw = 0.0, 0.0, 0.0
			var viewCount, status, intimeStamp, chapterUptime, rnd, rnw = 0, 0, 0, 0, 0, 0
			if ress, err := itemDB.Query(mmsql); nil == err {
				for ress.Next() {
					if err = ress.Scan(&gid, &name, &author, &normName, &normAuthor, &normSeries, &rank, &tag1, &tag2,
						&viewCount, &status, &feeFlag, &ncp, &intimeStamp, &chapterUptime, &maskLevel, &by, &tf,
						&rnd, &rtd, &rnw, &rtw, &updateTime); nil == err {
						obj := map[string]string {
							"gid": gid,
							"name": name,
							"author": author,
							"norm_name": normName,
							"norm_author": normAuthor,
							"norm_series": normSeries,
							"rank": fmt.Sprintf("%.3f", rank),
							"tag1": tag1,
							"tag2": tag2,
							"view_count": fmt.Sprintf("%d", viewCount),
							"status": fmt.Sprintf("%s", If(status == 2, "完结", "连载")),
							"fee_flag": FeeFlag(feeFlag),
							"ncp": ncp,
							"intime_stamp": fmt.Sprintf("%s", time.Unix(int64(intimeStamp), 0).Format("2006-01-02 03:04:05")),
							"chapter_uptime": fmt.Sprintf("%s", time.Unix(int64(chapterUptime), 0).Format("2006-01-02 03:04:05")),
							"mask_level": maskLevel,
							"by": by,
							"tf": tf,
							"rn_d": fmt.Sprintf("%d", rnd),
							"rt_d": fmt.Sprintf("%.3f", rtd),
							"rn_w": fmt.Sprintf("%d", rnw),
							"rt_w": fmt.Sprintf("%.3f", rtw),
							"update_time": updateTime,
						}
						response.Status = true
						response.Data = append(response.Data, obj)
					}
				}
			}
		}
	}
}