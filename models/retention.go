package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"strconv"
)

type RetentionRequest struct {
	Weidu           string
	Types           string
	Limitfree       []string
	Fee             []string
	Status          []string
	ViewCount       []string
	Intime          []string
	Uptime          []string
	Classify1       []string
	Target          []string
	TimeRange       []string
}

func QueryRetention(req *RetentionRequest, response *Response) {
	sqls := make(chan SqlInfo, 100)
	go func() {
		if startTime, ok := utils.TimeStringToString(req.TimeRange[0]); nil == ok {
			if endTime, ok := utils.TimeStringToString(req.TimeRange[1]); nil == ok {
				switch req.Weidu {
				case "limitfree":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_limitfree WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, tf := range req.Limitfree {
						msql := SqlInfo{
							Introduction: retentionMapToString[tf],
							Sql: fmt.Sprintf("%s AND tfCate = %d", mmsql, retentionMapToNum[tf]),
						}
						sqls <- msql
					}
				case "fee":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_fee WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, tar := range req.Target {
							msql := SqlInfo{
								Introduction: retentionMapToString[fee] + "-" + retentionMapToString[tar],
								Sql: fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar]),
							}
							sqls <- msql
						}
					}
				case "status":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_status WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, status := range req.Status {
							for _, tar := range req.Target {
								msql := SqlInfo{
									Introduction: retentionMapToString[fee] + "-" + retentionMapToString[status] + "-" + retentionMapToString[tar],
									Sql:fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d AND statuCate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar], retentionMapToNum[status]),
								}
								sqls <- msql
							}
						}
					}
				case "viewCount":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_viewcount WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, viewcount := range req.ViewCount {
							for _, tar := range req.Target {
								msql := SqlInfo{
									Introduction: retentionMapToString[fee] + "-" + retentionMapToString[viewcount] + "-" + retentionMapToString[tar],
									Sql:fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d AND viewCate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar], retentionMapToNum[viewcount]),
								}
								sqls <- msql
							}
						}
					}
				case "intime":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_intime WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, intime := range req.Intime {
							for _, tar := range req.Target {
								msql := SqlInfo{
									Introduction: retentionMapToString[fee] + "-" + retentionMapToString[intime] + "-" + retentionMapToString[tar],
									Sql:fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d AND intimeCate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar], retentionMapToNum[intime]),
								}
								sqls <- msql
							}
						}
					}
				case "uptime":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_update WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, uptime := range req.Uptime {
							for _, tar := range req.Target {
								msql := SqlInfo{
									Introduction: retentionMapToString[fee] + "-" + retentionMapToString[uptime] + "-" + retentionMapToString[tar],
									Sql:fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d AND updateCate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar], retentionMapToNum[uptime]),
								}
								sqls <- msql
							}
						}
					}
				case "classify1":
					mmsql := "SELECT remain, last, retent, timeStamp FROM item_retent_classify1 WHERE timeStamp >= " +
						startTime + " AND timeStamp <= " + endTime
					for _, fee := range req.Fee {
						for _, classify1 := range req.Classify1 {
							for _, tar := range req.Target {
								msql := SqlInfo{
									Introduction: retentionMapToString[fee] + "-" + retentionMapToString[classify1] + "-" + retentionMapToString[tar],
									Sql:fmt.Sprintf("%s AND feeCate = %d AND typeCate = %d AND cate1Cate = %d", mmsql, retentionMapToNum[fee], retentionMapToNum[tar], retentionMapToNum[classify1]),
								}
								sqls <- msql
							}
						}
					}
				}
			}
		}
		close(sqls)
	}()
	
	if retentionDB, err := sql.Open("mysql", mysqlInfo+"item_retention?charset=utf8"); nil == err {
		timeDays := utils.TimeStringRangeToInt(req.TimeRange[0], req.TimeRange[1])
		for mmsql := range sqls {
			retent := map[int]float64{}
			last := map[int]int{}
			remain := map[int]int{}
			
			for _, tm := range timeDays {
				retent[tm] = 0.0
				remain[tm] = 0
				last[tm] = 0
			}
			
			if ress, err := retentionDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					remaint, lastt, retentt, timeStampt := 0, 0, 0.0, 0
					if err = ress.Scan(&remaint, &lastt, &retentt, &timeStampt); nil == err {
						retent[timeStampt] = retentt
						remain[timeStampt] = remaint
						last[timeStampt] = lastt
					}
				}
				
				line := Line{}
				line.Introduction = mmsql.Introduction
				switch req.Types {
				case "num":
					for _, t := range timeDays {
						line.X = append(line.X, strconv.Itoa(t))
						line.Y = append(line.Y, float64(remain[t]))
					}
					break
				case "rate":
					for _, t := range timeDays {
						line.X = append(line.X, strconv.Itoa(t))
						line.Y = append(line.Y, float64(retent[t]))
					}
				case "lastNum":
					for _, t := range timeDays {
						line.X = append(line.X, strconv.Itoa(t))
						line.Y = append(line.Y, float64(last[t]))
					}
				}
				
				response.Status = true
				response.Lines = append(response.Lines, line)
			}
		}
	} else {
		response.Status = false
		response.Rrror = "mysql连接失败"
	}
}