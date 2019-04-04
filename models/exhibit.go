package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"math"
	"strconv"
	"sync"
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
				intro := ""
				for _, app := range req.App {
					mmsql1 := mmsql
					intro1 := intro
					if app != "allApp" {
						mmsql1 = mmsql + " AND app = " + strconv.Itoa(exhibitMapToNum[app])
						intro1 = intro + exhibitMapToString[app]
					}
					for _, module := range req.Module {
						mmsql2 := mmsql1
						intro2 := intro1
						if module != "allMdl" {
							mmsql2 = mmsql1 + " AND module = " + strconv.Itoa(exhibitMapToNum[module])
							intro2 = intro1 + exhibitMapToString[module]
						}
						for _, areaLevel := range req.AreaLevel {
							mmsql3 := mmsql2
							intro3 := intro2
							if areaLevel != "allArea" {
								mmsql3 = mmsql2 + " AND areaLevel = " + strconv.Itoa(exhibitMapToNum[areaLevel])
								intro3 = intro2 + exhibitMapToString[areaLevel]
							}
							for _, userLevel := range req.UserLevel {
								mmsql4 := mmsql3
								intro4 := intro3
								if userLevel != "allUsrLevel" {
									mmsql4 = mmsql3 + " AND userLevel = " + strconv.Itoa(exhibitMapToNum[userLevel])
									intro4 = intro3 + exhibitMapToString[userLevel]
								}
								for _, userNewOld := range req.UserNewLevel {
									mmsql5 := mmsql4
									intro5 := intro4
									if userNewOld != "allUsr" {
										mmsql5 = mmsql4 + " AND userNewOld = " + strconv.Itoa(exhibitMapToNum[userNewOld])
										intro5 = intro4 + exhibitMapToString[userNewOld]
									}
									for _, userFee := range req.UserFeeLevel {
										mmsql6 := mmsql5
										intro6 := intro5
										if userFee != "allFeeUsr" {
											mmsql6 = mmsql5 + " AND userFee = " + strconv.Itoa(exhibitMapToNum[userFee])
											intro6 = intro5 + exhibitMapToString[userFee]
										}
										for _, itemFee := range req.ItemFeeLevel {
											mmsql7 := mmsql6
											intro7 := intro6
											if itemFee != "allItmFee" {
												mmsql7 = mmsql6 + " AND itemFee = " + strconv.Itoa(exhibitMapToNum[itemFee])
												intro7 = intro6 + exhibitMapToString[itemFee]
											}
											for _, strategy := range req.Strategy {
												mmsql8 := mmsql7
												intro8 := intro7
												if strategy != "allRec" {
													mmsql8 = mmsql7 + " AND strategy = " + strconv.Itoa(exhibitMapToNum[strategy])
													intro8 = intro7 + exhibitMapToString[strategy]
												}
												for _, status := range req.Status {
													mmsql9 := mmsql8
													intro9 := intro8
													if status != "allStu" {
														mmsql9 = mmsql8 + " AND status = " + strconv.Itoa(exhibitMapToNum[status])
														intro9 = intro8 + exhibitMapToString[status]
													}
													for _, view := range req.Sub {
														mmsql10 := mmsql9
														intro10 := intro9
														if view != "allSub" {
															mmsql10 = mmsql9 + " AND view = " + strconv.Itoa(exhibitMapToNum[view])
															intro10 = intro9 + exhibitMapToString[view]
														}
														for _, intime := range req.Intime {
															mmsql11 := mmsql10
															intro11 := intro10
															if intime != "allIn" {
																mmsql11 = mmsql10 + " AND intime = " + strconv.Itoa(exhibitMapToNum[intime])
																intro11 = intro10 + exhibitMapToString[intime]
															}
															msql := SqlInfo{}
															msql.Introduction = intro11
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
		// sqls 多线程查询
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
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					recNumTmp, clkNumTmp, subNumTmp, redNum1Tmp, redNum2Tmp, timeStampTmp := 0, 0, 0, 0, 0, 0
					if err = ress.Scan(&recNumTmp, &clkNumTmp, &subNumTmp, &redNum1Tmp, &redNum2Tmp, &timeStampTmp); nil == err {
						recNum[timeStampTmp] += recNumTmp
						clkNum[timeStampTmp] += clkNumTmp
						subNum[timeStampTmp] += subNumTmp
						redNum1[timeStampTmp] += redNum1Tmp
						redNum2[timeStampTmp] += redNum2Tmp
					}
				}
				ta := sync.WaitGroup{}
				for _, target := range req.Target {
					ta.Add(1)
					go func() {
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
								if recNum[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(clkNum[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "subClk":
							for _, t := range timeDays {
								if clkNum[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(subNum[t])/float64(clkNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "subDsp":
							for _, t := range timeDays {
								if recNum[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(subNum[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "redSub1":
							for _, t := range timeDays {
								if redNum1[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(redNum1[t])/float64(subNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "redDsp1":
							for _, t := range timeDays {
								if redNum1[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(redNum1[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "redSub2":
							for _, t := range timeDays {
								if subNum[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(redNum2[t])/float64(subNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						case "redDsp2":
							for _, t := range timeDays {
								if redNum1[t] > 0 {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, math.Trunc(float64(redNum2[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
								} else {
									line.X = append(line.X, strconv.Itoa(t))
									line.Y = append(line.Y, 0)
								}
							}
							break
						}
						response.Status = true
						response.Lines = append(response.Lines, line)
						ta.Done()
					}()
					ta.Wait()
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
