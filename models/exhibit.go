package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"strconv"
)

type ExhibitRequest struct {
	App          []string
	Module       []string
	AreaLevel    []string
	UserLevel    []string
	UserNewLevel []string
	UserFeeLevel []string
	ItemFeeLevel []string
	Strategy     []string
	Status       []string
	Sub          []string
	Intime       []string
	Target       []string
	TimeRange    []string
}

func QueryExhibit(req *ExhibitRequest, response *Response) {
	sqls := make(chan SqlInfo, 100)
	go func() {
		if startTime, ok := utils.TimeStringToString(req.TimeRange[0]); nil == ok {
			if endTime, ok := utils.TimeStringToString(req.TimeRange[1]); nil == ok {
				mmsql := "SELECT recNum, clkNum, subNum, redNum1, redNum2, timeStamp FROM item_exhibit WHERE timeStamp >= " +
					startTime + " AND timeStamp <= " + endTime
				for _, app := range req.App {
					mmsql1 := mmsql
					if app != "allApp" {
						mmsql1 = mmsql + " AND app = " + strconv.Itoa(exhibitMapToNum[app])
					}
					for _, module := range req.Module {
						mmsql2 := mmsql1
						if module != "allMdl" {
							mmsql2 = mmsql1 + " AND module = " + strconv.Itoa(exhibitMapToNum[module])
						}
						for _, areaLevel := range req.AreaLevel {
							mmsql3 := mmsql2
							if areaLevel != "allArea" {
								mmsql3 = mmsql2 + " AND areaLevel = " + strconv.Itoa(exhibitMapToNum[areaLevel])
							}
							for _, userLevel := range req.UserLevel {
								mmsql4 := mmsql3
								if userLevel != "allUsrLevel" {
									mmsql4 = mmsql3 + " AND userLevel = " + strconv.Itoa(exhibitMapToNum[userLevel])
								}
								for _, userNewOld := range req.UserNewLevel {
									mmsql5 := mmsql4
									if userNewOld != "allUsr" {
										mmsql5 = mmsql4 + " AND userNewOld = " + strconv.Itoa(exhibitMapToNum[userNewOld])
									}
									for _, userFee := range req.UserFeeLevel {
										mmsql6 := mmsql5
										if userFee != "allFeeUsr" {
											mmsql6 = mmsql5 + " AND userFee = " + strconv.Itoa(exhibitMapToNum[userFee])
										}
										for _, itemFee := range req.ItemFeeLevel {
											mmsql7 := mmsql6
											if itemFee != "allItmFee" {
												mmsql7 = mmsql6 + " AND itemFee = " + strconv.Itoa(exhibitMapToNum[itemFee])
											}
											for _, strategy := range req.Strategy {
												mmsql8 := mmsql7
												if strategy != "allRec" {
													mmsql8 = mmsql7 + " AND strategy = " + strconv.Itoa(exhibitMapToNum[strategy])
												}
												for _, status := range req.Status {
													mmsql9 := mmsql8
													if status != "allStu" {
														mmsql9 = mmsql8 + " AND status = " + strconv.Itoa(exhibitMapToNum[status])
													}
													for _, view := range req.Sub {
														mmsql10 := mmsql9
														if view != "allSub" {
															mmsql10 = mmsql9 + " AND view = " + strconv.Itoa(exhibitMapToNum[view])
														}
														for _, intime := range req.Intime {
															mmsql11 := mmsql10
															if intime != "allIn" {
																mmsql11 = mmsql10 + " AND intime = " + strconv.Itoa(exhibitMapToNum[intime])
															}
															msql := SqlInfo{}
															msql.Introduction = exhibitMapToString[app] + "-" + exhibitMapToString[module] + "-" +
																exhibitMapToString[areaLevel] + "-" + exhibitMapToString[userLevel] + "-" +
																exhibitMapToString[userNewOld] + "-" + exhibitMapToString[userFee] + "-" +
																exhibitMapToString[itemFee] + "-" + exhibitMapToString[strategy] + "-" +
																exhibitMapToString[status] + "-" + exhibitMapToString[view] + "-" +
																exhibitMapToString[intime]
															msql.Sql = mmsql11
															sqls <- msql
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			} else {
				fmt.Println("结束时间解析出错")
			}
		} else {
			fmt.Println("开始时间解析出错")
		}
		close(sqls)
	}()

	if exhibitDB, err := sql.Open("mysql", mysqlInfo+"item_exhibit?charset=utf8"); nil == err {
		timeDays := utils.TimeStringRangeToInt(req.TimeRange[0], req.TimeRange[1])
		for mmsql := range sqls {
			recNum := map[int]int{}  // 推荐量 日期和值的关系
			clkNum := map[int]int{}  // 点击量 日期和值的关系
			subNum := map[int]int{}  // 订阅量 日期和值的关系
			redNum1 := map[int]int{} // 阅读量1 日期和值的关系
			redNum2 := map[int]int{} // 阅读量2 日期和值的关系
			for _, tm := range timeDays {
				recNum[tm] = 0
				clkNum[tm] = 0
				subNum[tm] = 0
				redNum1[tm] = 0
				redNum2[tm] = 0
			}
			//fmt.Println(mmsql.Sql)
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					recNumTmp, clkNumTmp, subNumTmp, redNum1Tmp, redNum2Tmp, timeStampTmp := 0, 0, 0, 0, 0, 0
					if err = ress.Scan(&recNumTmp, &clkNumTmp, &subNumTmp, &redNum1Tmp, &redNum2Tmp, &timeStampTmp); nil == err {
						recNum[timeStampTmp] += recNumTmp
						clkNum[timeStampTmp] += clkNumTmp
						subNum[timeStampTmp] += subNumTmp
						redNum1[timeStampTmp] += redNum1Tmp
						redNum2[timeStampTmp] += redNum2Tmp
					} else {
						//
					}
				}
				for _, target := range req.Target {
					line := Line{}
					line.Introduction = mmsql.Introduction + "-" + exhibitMapToString[target]
					switch target {
					case "dspNum":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(recNum[t]))
						}
						break
					case "clkNum":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(clkNum[t]))
						}
						break
					case "srbNum":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(subNum[t]))
						}
						break
					case "redNum1":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum1[t]))
						}
						break
					case "redNum2":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum2[t]))
						}
						break
						// 比例
					case "clkDsp":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(clkNum[t]) / float64(recNum[t]))
						}
					case "subClk":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(subNum[t]) / float64(clkNum[t]))
						}
					case "subDsp":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(subNum[t]) / float64(recNum[t]))
						}
					case "redSub":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum1[t]) / float64(subNum[t]))
						}
					case "redDsp":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum1[t]) / float64(recNum[t]))
						}
					case "retent":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum2[t]) / float64(subNum[t]))
						}
					case "rteDsp":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum1[t]) / float64(recNum[t]))
						}
					}
					response.Status = true
					response.Lines = append(response.Lines, line)
				}
			} else {
				//response.Status = false
				//response.Rrror = "sql 出错"
			}
		}
	} else {
		response.Status = false
		response.Rrror = "MySQL数据库连接失败"
	}
}
