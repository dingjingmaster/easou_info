package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"strconv"
)

type ExhibitRequest struct {
	Weidu     string
	Module    []string
	Fee       []string
	Strategy  []string
	Status    []string
	Sub       []string
	Intime    []string
	Uptime    []string
	Classify1 []string
	TimeRange []string
	Target    []string
}

func getSql(request *ExhibitRequest) ([]SqlInfo, error) {
	ret := []SqlInfo{}
	if startTime, err := utils.TimeStringToString(request.TimeRange[0]); nil == err {
		if stopTime, err := utils.TimeStringToString(request.TimeRange[1]); nil == err {
			switch request.Weidu {
			case "summary":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp," + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						sqlInfo := SqlInfo{}
						sqlInfo.Sql = msql + "typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
							" AND timeStamp>=" + startTime +
							" AND timeStamp<=" + stopTime
						sqlInfo.Introduction = exhibitMapToString[module] +
							"-" + exhibitMapToString[tg]
						ret = append(ret, sqlInfo)
					}
				}
			case "fee":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							sqlInfo := SqlInfo{}
							sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
								" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
								" AND  timeStamp>=" + startTime +
								" AND timeStamp<=" + stopTime
							sqlInfo.Introduction = exhibitMapToString[module] +
								"-" + exhibitMapToString[fee] +
								"-" + exhibitMapToString[tg]
							ret = append(ret, sqlInfo)
						}
					}
				}
			case "status":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, status := range request.Status {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND statusCate=" + strconv.Itoa(exhibitMapToNum[status]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[status] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			case "view":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, view := range request.Sub {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND viewCate=" + strconv.Itoa(exhibitMapToNum[view]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[view] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			case "intime":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, intime := range request.Intime {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND intimeCate=" + strconv.Itoa(exhibitMapToNum[intime]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[intime] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			case "uptime":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, uptime := range request.Uptime {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND updateCate=" + strconv.Itoa(exhibitMapToNum[uptime]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[uptime] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			case "classify1":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, classify1 := range request.Classify1 {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND classify1Cate=" + strconv.Itoa(exhibitMapToNum[classify1]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[classify1] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			case "strategy":
				for _, tg := range request.Target {
					msql := "SELECT timeStamp, " + tg + " FROM " + "item_exhibit_" + request.Weidu + " WHERE "
					for _, module := range request.Module {
						for _, fee := range request.Fee {
							for _, strategy := range request.Strategy {
								sqlInfo := SqlInfo{}
								sqlInfo.Sql = msql + "feeCate=" + strconv.Itoa(exhibitMapToNum[fee]) +
									" AND strategyCate=" + strconv.Itoa(exhibitMapToNum[strategy]) +
									" AND typeCate=" + strconv.Itoa(exhibitMapToNum[module]) +
									" AND timeStamp>=" + startTime +
									" AND timeStamp<=" + stopTime
								sqlInfo.Introduction = exhibitMapToString[module] +
									"-" + exhibitMapToString[fee] +
									"-" + exhibitMapToString[strategy] +
									"-" + exhibitMapToString[tg]
								ret = append(ret, sqlInfo)
							}
						}
					}
				}
			}
			return ret, nil
		} else {
			return []SqlInfo{}, err
		}
	} else {
		return []SqlInfo{}, err
	}
}

func QueryInfo(request *ExhibitRequest, response *Response) {
	if exhibit, err := sql.Open("mysql", mysqlInfo+"item_exhibit?charset=utf8"); nil == err {
		if sqls, err := getSql(request); nil == err {
			result := []Line{}
			timeRange := utils.TimeStringRangeToInt(request.TimeRange[0], request.TimeRange[1])
			for _, sqlInfo := range sqls {
				if ress, err := exhibit.Query(sqlInfo.Sql); nil == err {
					line := Line{}
					line.Introduction = sqlInfo.Introduction
					tmp := map[int]float64{}
					for ress.Next() {
						x := 0
						y  := 0.0
						if err = ress.Scan(&x, &y); nil == err {
							tmp[x] = y
						} else {
							// 错误
							fmt.Println(err)
						}
					}
					for _, itime1 := range timeRange {
						if y, ok := tmp[itime1]; ok {
							line.X = append(line.X, itime1)
							line.Y = append(line.Y, y)
						} else {
							line.X = append(line.X, itime1)
							line.Y = append(line.Y, 0)
						}
					}
					result = append(result, line)
				} else {
					// 错误
				}
			}
			response.Status = true
			response.Lines = result
		} else {
			response.Status = false
			response.Rrror = err.Error()
		}
	} else {
		response.Status = false
		response.Rrror = err.Error()
	}
}
