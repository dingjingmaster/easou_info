package models

import "github.com/astaxie/beego"

type SqlInfo struct {
	Sql          string
	Introduction string
}

type Line struct {
	Introduction string
	X            []string
	Y            []float64
}

type Response struct {
	Status          bool                    // 成功或失败
	Error           string                  // 失败说明
	Lines           []Line                  // 返回 n 条线
	Data            []map[string]string     // 返回 json 字符串
}

var mysqlInfo = ""

/* exhibit 相关全局变量 */
var exhibitMapToNum = map[string]int{
	"easouApp": 1, "weijuanApp": 2, "othApp": 3,
	"shfRecMdl": 1, "shfGusMdl": 2, "freRecMdl": 3, "freGusMdl": 4, "monStmMdl": 5, "foeCateRecMdl": 6, "foeRedRedMdl": 7, "foeRedMorMdl": 8, "sehResTopMdl": 9, "sehResGusMdl": 10, "bakRedRedMdl": 11, "chsGilStmMdl": 12, "chsCmpMdl": 13, "chsCmpStmMdl": 14, "chsRakStmMdl": 15, "chsRedRecMdl": 16, "chsRedCatRecMdl": 17, "chsStmMdl": 18, "chsHotRecMdl": 19, "chsBoyStmMdl": 20, "chsChsRedMdl": 21, "extBlkMdl": 22, "freByRecMdl": 23, "fre7TfMdl": 24, "foeAutRecMdl": 25,
	"oneArea": 1, "twoArea": 2, "trdArea": 3, "othArea": 4, "fthArea": 5,
	"regUsrLevel": 1, "sphUsrLevel": 2, "othUsrLevel": 3,
	"newUsr": 1, "oldUsr": 2, "othUsr": 3,
	"freFeeUsr": 1, "mybChgFeeUsr": 2, "lgtChgFeeUsr": 3, "mdlChgFeeUsr": 4, "hghChgFeeUsr": 5, "othFeeUsr": 6,
	"freItmFee": 1, "chgItmFee": 2, "monItmFee": 3, "tfItmFee": 4, "othItmFee": 5, "allFreItmFee": 6,
	"cat1Rec": 1, "cat2Rec": 2, "cotSimRec": 3, "simAthRec": 4, "catRec": 5, "livStmRec": 6, "popRec": 7, "icfKnnRec": 8, "ucfKnnRec": 9, "nerIcfKnnRec": 10, "codRec": 11, "subMdlRec": 12, "redMdlRec": 13, "othRec": 14,
	"noCmpStu": 1, "cmpStu": 2, "othStu": 3,
	"bt0to10Sub": 1, "bt10to1bSub": 2, "bt1bto1kSub": 3, "bt1kto10kSub": 4, "bt10kto100kSub": 5, "bt100kto1000kSub": 6, "bt1000kto10000kSub": 7, "othSub": 8,
	"lesMonIn": 1, "bt1mto3mIn": 2, "bt3mto12mIn": 3, "bt12mto99mIn": 4, "othIn": 5,
}
var exhibitMapToString = map[string]string{
	"allApp": "全部app叠加", "easouApp": "宜搜小说", "weijuanApp": "微卷", "othApp": "其它app",
	"allMdl": "全模块叠加", "shfRecMdl": "书架推荐", "shfGusMdl": "书架 猜你喜欢", "freRecMdl": "免费 免费推荐", "freGusMdl": "免费猜你喜欢", "monStmMdl": "包月瀑布流", "foeCateRecMdl": "封面页类别推荐", "foeRedRedMdl": "封面页读本书的人还看过", "foeRedMorMdl": "封面页读本书的人还看过更多", "sehResTopMdl": "搜索结果页 热搜TOP榜", "sehResGusMdl": "搜索结果页 猜你喜欢", "bakRedRedMdl": "章末页 读本书的人还看过", "chsGilStmMdl": "精选 女频瀑布流", "chsCmpMdl": "精选 完结佳作", "chsCmpStmMdl": "精选 完结瀑布流", "chsRakStmMdl": "精选 排行瀑布流", "chsRedRecMdl": "精选 根据阅读书籍推荐", "chsRedCatRecMdl": "精选 根据阅读分类推荐", "chsStmMdl": "精选 瀑布流", "chsHotRecMdl": "精选 热门推荐", "chsBoyStmMdl": "精选 男频瀑布流", "chsChsRedMdl": "精选 精品必读", "extBlkMdl": "退出拦截推荐", "freByRecMdl": "免费包月推荐", "fre7TfMdl": "七日限免", "foeAutRecMdl": "封面页-作者推荐",
	"allArea": "全区域叠加", "oneArea": "一类地区", "twoArea": "二类地区", "trdArea": "三类地区", "othArea": "其它地区", "fthArea": "四类地区",
	"allUsrLevel": "全用户级别叠加", "regUsrLevel": "普通用户", "sphUsrLevel": "特殊用户", "othUsrLevel": "其它用户级别",
	"allUsr": "全新旧用户叠加", "newUsr": "新用户", "oldUsr": "老用户", "othUsr": "其它新/老用户",
	"allFeeUsr": "全付费类型用户叠加", "freFeeUsr": "纯免费用户", "mybChgFeeUsr": "潜在付费用户", "lgtChgFeeUsr": "轻度付费用户", "mdlChgFeeUsr": "中度付费用户", "hghChgFeeUsr": "重度付费用户", "othFeeUsr": "其它付费类型用户",
	"allItemFee": "全付费类型物品叠加", "freItmFee": "免费物品", "chgItmFee": "付费物品", "monItmFee": "包月物品", "tfItmFee": "限免物品", "othItmFee": "其它付费类型物品", "allFreItmFee":"互联网",
	"allRec": "全策略叠加", "cat1Rec": "一级同分类", "cat2Rec": "二级同分类", "cotSimRec": "内容相似", "simAthRec": "同作者", "catRec": "同分类", "livStmRec": "实时流", "popRec": "流行度", "icfKnnRec": "物品协同", "ucfKnnRec": "用户协同", "nerIcfKnnRec": "近期协同", "codRec": "冷启动", "subMdlRec": "订阅模型", "redMdlRec": "阅读模型", "othRec": "其它策略",
	"allStu": "全书籍状态叠加", "noCmpStu": "连载", "cmpStu": "完结", "othStu": "其它状态",
	"allSub": "全订阅级别叠加", "bt0to10Sub": "0~10订阅", "bt10to1bSub": "10~100订阅", "bt1bto1kSub": "100~1千订阅", "bt1kto10kSub": "1千~1万订阅", "bt10kto100kSub": "1万~10万订阅", "bt100kto1000kSub": "10万~1百万订阅", "bt1000kto10000kSub": "1百万~1千万订阅", "othSub": "其它订阅级别",
	"allIn": "全入库时间叠加", "lesMonIn": "1月内入库", "bt1mto3mIn": "1~3月内入库", "bt3mto12mIn": "3~12月内入库", "bt12mto99mIn": "12~99月内入库", "othIn": "其它入库时间",
	"dspNum": "推荐量", "clkNum": "点击量", "srbNum": "订阅量", "redNum1": "阅读量1", "redNum2": "阅读量2", "redNum7": "周阅读量", "redNum30": "月阅读量", "redChap1": "天阅读章节量", "redChap7": "周阅读章节量", "redChap30": "月阅读章节两", "value1": "天收益", "value7": "周收益", "value30": "月收益",
	"clkDsp": "点展比", "subClk": "订点比", "subDsp": "订展比", "redSub1": "阅订比1", "redDsp1": "阅展比1", "redSub2": "阅订比2", "redDsp2": "阅展比2", "redDsp7": "周阅读展现比", "redDsp30": "月阅读展现比", "redcDsp1": "天阅读章节展现比", "redcDsp7": "周阅读展现比", "redcDsp30": "月阅读章节展现比", "valDsp1": "天价值展现比", "valDsp7": "周价值展现比", "valDsp30": "月价值展现比",
}

/* retention 相关全局变量 */
var retentionMapToNum = map[string]int {
	"freFee" : 1, "chgFee" : 2, "monFee" : 3, "pubFee" : 4, "tfFee" : 5, "allFee":6,
	"rteDay" : 1, "rteWeek" : 2, "rteWk7" : 3,
	"valDay" : 1, "valWeek" : 2, "valWk7" : 3,
	"limfe1" : 1, "limfe2" : 2, "limfe3" : 3, "limfe4" : 4,
	"unfinish" : 1, "finish" : 2,
	"bt0to1b" : 1, "bt1bto1k" : 2, "bt1kto1w" : 3, "bt1wto10w" : 4, "gt10w" : 5,
	"lesMonIn" : 1, "bt1mto3mIn" : 2, "bt3mto12mIn" : 3, "gt1yIn" : 4,
	"lesMonUpd" : 1, "bt1mto3mUpd" : 2, "bt3mto12mUpd" : 3, "gt1yUpd" : 4,
	"boyCfy1" : 1, "girlCfy1" : 2, "pshCfy1" : 3, "othCfy1" : 4,
}
var retentionMapToString = map[string]string{
	"freFee" : "免费(互联网书)", "chgFee" : "付费", "monFee" : "包月", "pubFee":"公版", "tfFee":"限免", "allFee":"全免(付费书免费读)",
	"rteDay" : "天留存", "rteWeek":"周留存", "rteWk7":"七日留存",
	"valDay" : "天阅读量", "valWeek":"周阅读量", "valWk7":"七日阅读量",
	"limfe1" : "第一批限免", "limfe2" : "第二批限免", "limfe3" : "第三批限免", "limfe4" : "第四批限免",
	"finish" : "完结", "unfinish" : "连载",
	"bt0to1b" : "1到1百", "bt1bto1k" : "1百到1千", "bt1kto1w" : "1千到1万", "bt1wto10w" : "1万到10万", "gt10w" : "大于10万",
	"lesMonIn" : "少于1月入库", "bt1mto3mIn" : "1月到3月入库", "bt3mto12mIn" : "3月到12月入库", "gt1yIn" : "大于1年入库",
	"lesMonUpd" : "少于1月更新", "bt1mto3mUpd" : "1月到3月更新", "bt3mto12mUpd" : "3月到12月更新", "gt1yUpd" : "大于1年更新",
	"boyCfy1" : "男频", "girlCfy1" : "女频", "pshCfy1" : "出版", "othCfy1" : "其它",
}

/* 阅读事件相关查询 */
var readeventMapToNum = map[string]int {
	"easouApp": 1, "weijuanApp": 2, "othApp": 3,
	"regUsrLevel": 1, "sphUsrLevel": 2, "othUsrLevel": 3,
	"newUsrNew": 1, "oldUsrNew": 2, "othUsrNew": 3,
	"monUsrMon": 1, "unMonUsrMon": 2, "othUsrMon": 3,
	"freUsrFee": 1, "mybChgUsrFee": 2, "lgtChgUsrFee": 3, "mdlChgUsrFee": 4, "hghChgUsrFee": 5, "othUsrFee": 6,
	"oneArea": 1, "twoArea": 2, "trdArea": 3, "fthArea": 4, "othArea": 5,
	"cmpBookStu": 1, "noCmpBookStu": 2, "othBookStu": 3,
	"tchgItmCate": 1, "monItmCate": 2, "unMonItmCate": 3, "tfItmCate": 4, "yzItmCate": 5, "mcpItmCate": 6, "tfreItmCate": 7, "brkItmCate": 8, "genItmCate": 9, "gveItmCate": 10, "othItmCate": 11,
}
var readeventMapToString = map[string]string {
	"allApp": "全部app", "easouApp": "宜搜小说", "weijuanApp": "微卷", "othApp": "其它",
	"allUsrLevel": "全部用户级别", "regUsrLevel": "普通用户", "sphUsrLevel": "特殊用户", "othUsrLevel": "其它用户级别",
	"allUsrNew": "全部新旧用户", "newUsrNew": "新用户", "oldUsrNew": "老用户", "othUsrNew": "其他用户",
	"allUsrMon": "全部包月非包月用户", "monUsrMon": "包月用户", "unMonUsrMon": "非包月用户", "othUsrMon": "其它包月非包月用户",
	"allUsrFee": "全部付费级别", "freUsrFee": "纯免费", "mybChgUsrFee": "潜在付费", "lgtChgUsrFee": "轻度付费", "mdlChgUsrFee": "中度付费", "hghChgUsrFee": "重度付费", "othUsrFee": "其它付费",
	"allArea": "全部地区", "oneArea": "一类地区", "twoArea": "二类地区", "trdArea": "三类地区", "fthArea": "四类地区", "othArea": "其它地区",
	"allBookStu": "全部状态", "cmpBookStu": "完结", "noCmpBookStu": "连载", "othBookStu": "其它状态",
	"allItmCate": "全部书籍类型", "tchgItmCate": "按章计费", "monItmCate": "包月", "unMonItmCate": "非包月", "tfItmCate": "限免", "yzItmCate": "一折书籍", "mcpItmCate": "免费CP书", "tfreItmCate": "免费互联网书", "brkItmCate": "断更", "genItmCate": "普通", "gveItmCate": "赠书", "othItmCate": "其它书籍类型",
	"itmTag": "书籍量", "usrTag": "用户量", "chgTag": "付费章节量", "freTag": "免费章节量", "tfTag": "限免章节量", "sumTag": "总章节量",
}

func init() {
	host := beego.AppConfig.String("mysql::host") 
	port := beego.AppConfig.String("mysql::port")
	user := beego.AppConfig.String("mysql::user")
	passwd := beego.AppConfig.String("mysql::passwd")
	mysqlInfo = user + ":" + passwd + "@tcp(" + host + ":" + port + ")/"
}
