package models

import (
	"database/sql"
	"easou_info/utils"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"strconv"
	"sync"
)

type ReadEventCRequest struct {
	App            []string
	UserLevel      []string
	UserNewLevel   []string
	UserMonthLevel []string
	UserFeeLevel   []string
	UserAreaLevel  []string
	ItemStatus     []string
	ItemCategory   []string
	Target         []string
	TimeRange      []string
}
type ReadEventURequest struct {
	App            []string
	UserLevel      []string
	UserNewLevel   []string
	UserMonthLevel []string
	UserFeeLevel   []string
	UserAreaLevel  []string
	Target         []string
	TimeRange      []string
}
type ReadEventBRequest struct {
	App            []string
	ItemStatus     []string
	ItemCategory   []string
	Target         []string
	TimeRange      []string
}
func QueryReadEventC(req *ReadEventCRequest, response *Response) {
	sqls := make(chan SqlInfo, 100)
	go func() {
		if startTime, ok := utils.TimeStringToString(req.TimeRange[0]); nil == ok {
			if endTime, ok := utils.TimeStringToString(req.TimeRange[1]); nil == ok {
				mmsql := "SELECT gidNum, usrNum, chgNum, freNum, tfNum, sumNum, timeStamp FROM read_event_c WHERE timeStamp >= " +
					startTime + " AND timeStamp <= " + endTime
				intro := ""
				for _, app := range req.App {
					mmsql1 := mmsql
					intro1 := intro
					if app != "allApp" {
						mmsql1 = mmsql + " AND app = " + strconv.Itoa(readeventMapToNum[app])
						intro1 = intro + readeventMapToString[app]
					}
					for _, module := range req.UserLevel {
						mmsql2 := mmsql1
						intro2 := intro1
						if module != "allUsrLevel" {
							mmsql2 = mmsql1 + " AND userLevel = " + strconv.Itoa(readeventMapToNum[module])
							intro2 = intro1 + readeventMapToString[module]
						}
						for _, areaLevel := range req.UserNewLevel {
							mmsql3 := mmsql2
							intro3 := intro2
							if areaLevel != "allUsrNew" {
								mmsql3 = mmsql2 + " AND userNewOld = " + strconv.Itoa(readeventMapToNum[areaLevel])
								intro3 = intro2 + readeventMapToString[areaLevel]
							}
							for _, userLevel := range req.UserMonthLevel {
								mmsql4 := mmsql3
								intro4 := intro3
								if userLevel != "allUsrMon" {
									mmsql4 = mmsql3 + " AND ismonth = " + strconv.Itoa(readeventMapToNum[userLevel])
									intro4 = intro3 + readeventMapToString[userLevel]
								}
								for _, userNewOld := range req.UserFeeLevel {
									mmsql5 := mmsql4
									intro5 := intro4
									if userNewOld != "allUsrFee" {
										mmsql5 = mmsql4 + " AND userFee = " + strconv.Itoa(readeventMapToNum[userNewOld])
										intro5 = intro4 + readeventMapToString[userNewOld]
									}
									for _, userFee := range req.UserAreaLevel {
										mmsql6 := mmsql5
										intro6 := intro5
										if userFee != "allArea" {
											mmsql6 = mmsql5 + " AND areaLevel = " + strconv.Itoa(readeventMapToNum[userFee])
											intro6 = intro5 + readeventMapToString[userFee]
										}
										for _, itemFee := range req.ItemStatus {
											mmsql7 := mmsql6
											intro7 := intro6
											if itemFee != "allBookStu" {
												mmsql7 = mmsql6 + " AND status = " + strconv.Itoa(readeventMapToNum[itemFee])
												intro7 = intro6 + readeventMapToString[itemFee]
											}
											for _, strategy := range req.ItemCategory {
												mmsql8 := mmsql7
												intro8 := intro7
												if strategy != "allItmCate" {
													mmsql8 = mmsql7 + " AND cate = " + strconv.Itoa(readeventMapToNum[strategy])
													intro8 = intro7 + readeventMapToString[strategy]
												}
												msql := SqlInfo{}
												msql.Introduction = intro8
												msql.Sql = mmsql8
												sqls <- msql
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

	if exhibitDB, err := sql.Open("mysql", mysqlInfo+"read_event?charset=utf8"); nil == err {
		timeDays := utils.TimeStringRangeToInt(req.TimeRange[0], req.TimeRange[1])
		// sqls 多线程查询
		for mmsql := range sqls {
			gidNum := map[int]int{}
			usrNum := map[int]int{}
			chgNum := map[int]int{}
			freNum := map[int]int{}
			tfNum := map[int]int{}
			sumNum := map[int]int{}
			for _, tm := range timeDays {
				gidNum[tm] = 0
				usrNum[tm] = 0
				chgNum[tm] = 0
				freNum[tm] = 0
				tfNum[tm] = 0
				sumNum[tm] = 0
			}
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					gidNumTmp, usrNumTmp, chgNumTmp, freNumTmp, tfNumTmp, sumNumTmp, timeStampTmp := 0, 0, 0, 0, 0, 0, 0
					if err = ress.Scan(&gidNumTmp, &usrNumTmp, &chgNumTmp, &freNumTmp, &tfNumTmp, &sumNumTmp, &timeStampTmp); nil == err {
						gidNum[timeStampTmp] += gidNumTmp
						usrNum[timeStampTmp] += usrNumTmp
						chgNum[timeStampTmp] += chgNumTmp
						freNum[timeStampTmp] += freNumTmp
						tfNum[timeStampTmp] += tfNumTmp
						sumNum[timeStampTmp] += sumNumTmp
					}
				}

				ta := sync.WaitGroup{}
				for _, target := range req.Target {
					ta.Add(1)
					go func() {
						line := Line{}
						line.Introduction = mmsql.Introduction + "-" + readeventMapToString[target]
						switch target {
						case "itmTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(gidNum[t]))
							}
							break
						case "usrTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(usrNum[t]))
							}
							break
						case "chgTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(chgNum[t]))
							}
							break
						case "freTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(freNum[t]))
							}
							break
						case "tfTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(tfNum[t]))
							}
							break
						case "sumTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(sumNum[t]))
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

func QueryReadEventU(req *ReadEventURequest, response *Response) {
	sqls := make(chan SqlInfo, 100)
	go func() {
		if startTime, ok := utils.TimeStringToString(req.TimeRange[0]); nil == ok {
			if endTime, ok := utils.TimeStringToString(req.TimeRange[1]); nil == ok {
				mmsql := "SELECT usrNum timeStamp FROM read_event_u WHERE timeStamp >= " +
					startTime + " AND timeStamp <= " + endTime
				intro := ""
				for _, app := range req.App {
					mmsql1 := mmsql
					intro1 := intro
					if app != "allApp" {
						mmsql1 = mmsql + " AND app = " + strconv.Itoa(readeventMapToNum[app])
						intro1 = intro + readeventMapToString[app]
					}
					for _, module := range req.UserLevel {
						mmsql2 := mmsql1
						intro2 := intro1
						if module != "allUsrLevel" {
							mmsql2 = mmsql1 + " AND userLevel = " + strconv.Itoa(readeventMapToNum[module])
							intro2 = intro1 + readeventMapToString[module]
						}
						for _, areaLevel := range req.UserNewLevel {
							mmsql3 := mmsql2
							intro3 := intro2
							if areaLevel != "allUsrNew" {
								mmsql3 = mmsql2 + " AND userNewOld = " + strconv.Itoa(readeventMapToNum[areaLevel])
								intro3 = intro2 + readeventMapToString[areaLevel]
							}
							for _, userLevel := range req.UserMonthLevel {
								mmsql4 := mmsql3
								intro4 := intro3
								if userLevel != "allUsrMon" {
									mmsql4 = mmsql3 + " AND ismonth = " + strconv.Itoa(readeventMapToNum[userLevel])
									intro4 = intro3 + readeventMapToString[userLevel]
								}
								for _, userNewOld := range req.UserFeeLevel {
									mmsql5 := mmsql4
									intro5 := intro4
									if userNewOld != "allUsrFee" {
										mmsql5 = mmsql4 + " AND userFee = " + strconv.Itoa(readeventMapToNum[userNewOld])
										intro5 = intro4 + readeventMapToString[userNewOld]
									}
									for _, userFee := range req.UserAreaLevel {
										mmsql6 := mmsql5
										intro6 := intro5
										if userFee != "allArea" {
											mmsql6 = mmsql5 + " AND areaLevel = " + strconv.Itoa(readeventMapToNum[userFee])
											intro6 = intro5 + readeventMapToString[userFee]
											msql := SqlInfo{}
											msql.Introduction = intro6
											msql.Sql = mmsql6
											sqls <- msql
											
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
	
	if exhibitDB, err := sql.Open("mysql", mysqlInfo+"read_event?charset=utf8"); nil == err {
		timeDays := utils.TimeStringRangeToInt(req.TimeRange[0], req.TimeRange[1])
		// sqls 多线程查询
		for mmsql := range sqls {
			usrNum := map[int]int{}
			
			for _, tm := range timeDays {
				usrNum[tm] = 0
				
			}
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					usrNumTmp, timeStampTmp := 0, 0
					if err = ress.Scan(&usrNumTmp, &timeStampTmp); nil == err {
						usrNum[timeStampTmp] += usrNumTmp
					}
				}
				
				ta := sync.WaitGroup{}
				for _, target := range req.Target {
					ta.Add(1)
					go func() {
						line := Line{}
						line.Introduction = mmsql.Introduction + "-" + readeventMapToString[target]
						switch target {
						case "usrTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(usrNum[t]))
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

func QueryReadEventB(req *ReadEventBRequest, response *Response) {
	sqls := make(chan SqlInfo, 100)
	go func() {
		if startTime, ok := utils.TimeStringToString(req.TimeRange[0]); nil == ok {
			if endTime, ok := utils.TimeStringToString(req.TimeRange[1]); nil == ok {
				mmsql := "SELECT gidNum, timeStamp FROM read_event_b WHERE timeStamp >= " +
					startTime + " AND timeStamp <= " + endTime
				intro := ""
				for _, app := range req.App {
					mmsql1 := mmsql
					intro1 := intro
					if app != "allApp" {
						mmsql1 = mmsql + " AND app = " + strconv.Itoa(readeventMapToNum[app])
						intro1 = intro + readeventMapToString[app]
					}
					for _, itemFee := range req.ItemStatus {
						mmsql2 := mmsql1
						intro2 := intro1
						if itemFee != "allBookStu" {
							mmsql2 = mmsql2 + " AND status = " + strconv.Itoa(readeventMapToNum[itemFee])
							intro2 = intro2 + readeventMapToString[itemFee]
						}
						for _, strategy := range req.ItemCategory {
							mmsql3 := mmsql2
							intro3 := intro2
							if strategy != "allItmCate" {
								mmsql3 = mmsql3 + " AND cate = " + strconv.Itoa(readeventMapToNum[strategy])
								intro3 = intro3 + readeventMapToString[strategy]
							}
							msql := SqlInfo{}
							msql.Introduction = intro3
							msql.Sql = mmsql3
							sqls <- msql
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
	
	if exhibitDB, err := sql.Open("mysql", mysqlInfo+"read_event?charset=utf8"); nil == err {
		timeDays := utils.TimeStringRangeToInt(req.TimeRange[0], req.TimeRange[1])
		// sqls 多线程查询
		for mmsql := range sqls {
			gidNum := map[int]int{}
			for _, tm := range timeDays {
				gidNum[tm] = 0
			}
			if ress, err := exhibitDB.Query(mmsql.Sql); nil == err {
				for ress.Next() {
					gidNumTmp, usrNumTmp, chgNumTmp, freNumTmp, tfNumTmp, sumNumTmp, timeStampTmp := 0, 0, 0, 0, 0, 0, 0
					if err = ress.Scan(&gidNumTmp, &usrNumTmp, &chgNumTmp, &freNumTmp, &tfNumTmp, &sumNumTmp, &timeStampTmp); nil == err {
						gidNum[timeStampTmp] += gidNumTmp
					}
				}
				
				ta := sync.WaitGroup{}
				for _, target := range req.Target {
					ta.Add(1)
					go func() {
						line := Line{}
						line.Introduction = mmsql.Introduction + "-" + readeventMapToString[target]
						switch target {
						case "itmTag":
							for _, t := range timeDays {
								line.X = append(line.X, strconv.Itoa(t))
								line.Y = append(line.Y, float64(gidNum[t]))
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