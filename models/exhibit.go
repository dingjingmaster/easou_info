package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"math"
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
				mmsql := "SELECT recNum, clkNum, subNum, redNum1, redNum2, timeStamp FROM item_exhibit WHERE "
				intro := ""
				for _, app := range req.App {
					mmsql1 := mmsql
					intro1 := intro
					if app != "allApp" {
						mmsql1 = mmsql + " app = " + strconv.Itoa(exhibitMapToNum[app]) + " AND "
						intro1 = intro + exhibitMapToString[app]
					}
					for _, module := range req.Module {
						mmsql2 := mmsql1
						intro2 := intro1
						if module != "allMdl" {
							mmsql2 = mmsql1 + "module = " + strconv.Itoa(exhibitMapToNum[module]) + " AND "
							intro2 = intro1 + exhibitMapToString[module]
						}
						for _, areaLevel := range req.AreaLevel {
							mmsql3 := mmsql2
							intro3 := intro2
							if areaLevel != "allArea" {
								mmsql3 = mmsql2 + "areaLevel = " + strconv.Itoa(exhibitMapToNum[areaLevel]) + " AND "
								intro3 = intro2 + exhibitMapToString[areaLevel]
							}
							for _, userLevel := range req.UserLevel {
								mmsql4 := mmsql3
								intro4 := intro3
								if userLevel != "allUsrLevel" {
									mmsql4 = mmsql3 + "userLevel = " + strconv.Itoa(exhibitMapToNum[userLevel]) + " AND "
									intro4 = intro3 + exhibitMapToString[userLevel]
								}
								for _, userNewOld := range req.UserNewLevel {
									mmsql5 := mmsql4
									intro5 := intro4
									if userNewOld != "allUsr" {
										mmsql5 = mmsql4 + "userNewOld = " + strconv.Itoa(exhibitMapToNum[userNewOld]) + " AND "
										intro5 = intro4 + exhibitMapToString[userNewOld]
									}
									for _, userFee := range req.UserFeeLevel {
										mmsql6 := mmsql5
										intro6 := intro5
										if userFee != "allFeeUsr" {
											mmsql6 = mmsql5 + "userFee = " + strconv.Itoa(exhibitMapToNum[userFee]) + " AND "
											intro6 = intro5 + exhibitMapToString[userFee]
										}
										for _, itemFee := range req.ItemFeeLevel {
											mmsql7 := mmsql6
											intro7 := intro6
											if itemFee != "allItmFee" {
												mmsql7 = mmsql6 + "itemFee = " + strconv.Itoa(exhibitMapToNum[itemFee]) + " AND "
												intro7 = intro6 + exhibitMapToString[itemFee]
											}
											for _, strategy := range req.Strategy {
												mmsql8 := mmsql7
												intro8 := intro7
												if strategy != "allRec" {
													mmsql8 = mmsql7 + "strategy = " + strconv.Itoa(exhibitMapToNum[strategy]) + " AND "
													intro8 = intro7 + exhibitMapToString[strategy]
												}
												for _, status := range req.Status {
													mmsql9 := mmsql8
													intro9 := intro8
													if status != "allStu" {
														mmsql9 = mmsql8 + "status = " + strconv.Itoa(exhibitMapToNum[status]) + " AND "
														intro9 = intro8 + exhibitMapToString[status]
													}
													for _, view := range req.Sub {
														mmsql10 := mmsql9
														intro10 := intro9
														if view != "allSub" {
															mmsql10 = mmsql9 + "view = " + strconv.Itoa(exhibitMapToNum[view]) + " AND "
															intro10 = intro9 + exhibitMapToString[view]
														}
														for _, intime := range req.Intime {
															mmsql11 := mmsql10
															intro11 := intro10
															if intime != "allIn" {
																mmsql11 = mmsql10 + "intime = " + strconv.Itoa(exhibitMapToNum[intime]) + " AND "
																intro11 = intro10 + exhibitMapToString[intime]
															}
															msql := SqlInfo{}
															msql.Introduction = intro11
															msql.Sql = mmsql11 + "timeStamp >= " + startTime + " AND timeStamp <= " + endTime
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
			redNum7 := map[int]int{}
			redNum30 := map[int]int{}
			redChap1 := map[int]int{}
			redChap7 := map[int]int{}
			redChap30 := map[int]int{}
			value1 := map[int]int{}
			value7 := map[int]int{}
			value30 := map[int]int{}
			for _, tm := range timeDays {
				recNum[tm] = 0
				clkNum[tm] = 0
				subNum[tm] = 0
				redNum1[tm] = 0
				redNum2[tm] = 0
				redNum7[tm] = 0
				redNum30[tm] = 0
				redChap1[tm] = 0
				redChap7[tm] = 0
				redChap30[tm] = 0
				value1[tm] = 0
				value7[tm] = 0
				value30[tm] = 0
			}
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				if ress.Next() {
					fmt.Println(mmsql.Sql)
					fmt.Println("请求完成！！！")
				}
				for ress.Next() {
					recNumTmp, clkNumTmp, subNumTmp, redNum1Tmp, redNum2Tmp, redNum7Tmp, redNum30Tmp, redChap1Tmp, redChap7Tmp,
					redChap30Tmp, value1Tmp, value7Tmp, value30Tmp, timeStampTmp := 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
					if err = ress.Scan(&recNumTmp, &clkNumTmp, &subNumTmp, &redNum1Tmp, &redNum2Tmp, &timeStampTmp); nil == err {
						recNum[timeStampTmp] += recNumTmp
						clkNum[timeStampTmp] += clkNumTmp
						subNum[timeStampTmp] += subNumTmp
						redNum1[timeStampTmp] += redNum1Tmp
						redNum2[timeStampTmp] += redNum2Tmp
						redNum7[timeStampTmp] += redNum7Tmp
						redNum30[timeStampTmp] += redNum30Tmp
						redChap1[timeStampTmp] += redChap1Tmp
						redChap7[timeStampTmp] += redChap7Tmp
						redChap30[timeStampTmp] += redChap30Tmp
						value1[timeStampTmp] += value1Tmp
						value7[timeStampTmp] += value7Tmp
						value30[timeStampTmp] += value30Tmp
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
					case "redNum7":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum7[t]))
						}
						break
					case "redNum30":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redNum30[t]))
						}
						break
					case "redChap1":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redChap1[t]))
						}
						break
					case "redChap7":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redChap7[t]))
						}
						break
					case "redChap30":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(redChap30[t]))
						}
						break
					case "value1":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(value1[t]))
						}
						break
					case "value7":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(value7[t]))
						}
						break
					case "value30":
						for _, t := range timeDays {
							line.X = append(line.X, strconv.Itoa(t))
							line.Y = append(line.Y, float64(value30[t]))
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
					case "redDsp7":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(redNum7[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "redDsp30":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(redNum30[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "redcDsp1":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(redChap1[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "redcDsp7":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(redChap7[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "redcDsp30":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(redChap30[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "valDsp1":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(value1[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "valDsp7":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(value7[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					case "valDsp30":
						for _, t := range timeDays {
							if redNum1[t] > 0 {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, math.Trunc(float64(value30[t])/float64(recNum[t])*100 * 1e3 + 0.5) * 1e-3)
							} else {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, 0)
							}
						}
						break
					}
					response.Status = true
					response.Lines = append(response.Lines, line)
				}
				ress.Close()
			} else {
				response.Status = false
				response.Error = "sql 出错"
			}
		}
	} else {
		response.Status = false
		response.Error = "MySQL数据库连接失败"
	}
}
