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
	Status bool   // 成功或失败
	Rrror  string // 失败说明
	Lines  []Line // 返回 n 条线
}

var mysqlInfo = ""

/* exhibit 相关全局变量 */
var exhibitMapToNum = map[string]int{
	"shfRecMdl": 1, "shfGusMdl": 2, "freRecMdl": 3, "freGusMdl": 4, "monStmMdl": 5, "foeCateRecMdl": 6, "foeRedRedMdl": 7, "foeRedMorMdl": 8, "sehResTopMdl": 9, "sehResGusMdl": 10, "bakRedRedMdl": 11, "chsGilStmMdl": 12, "chsCmpMdl": 13, "chsCmpStmMdl": 14, "chsRakStmMdl": 15, "chsRedRecMdl": 16, "chsRedCatRecMdl": 17, "chsStmMdl": 18, "chsHotRecMdl": 19, "chsBoyStmMdl": 20, "chsChsRedMdl": 21,  "extBlkMdl": 22,
	"oneArea": 1, "twoArea": 2, "trdArea": 3, "othArea": 4,
	"regUsrLevel": 1, "sphUsrLevel": 2, "othUsrLevel": 3,
	"newUsr": 1, "oldUsr": 2, "othUsr": 3,
	"freFeeUsr": 1, "mybChgFeeUsr": 2, "lgtChgFeeUsr": 3, "mdlChgFeeUsr": 4, "hghChgFeeUsr": 5, "othFeeUsr": 6,
	"freItmFee": 1, "chgItmFee": 2, "monItmFee": 3, "tfItmFee": 4, "othItmFee": 5,
	"cat1Rec": 1, "cat2Rec": 2, "cotSimRec": 3, "simAthRec": 4, "catRec": 5, "livStmRec": 6, "popRec": 7, "icfKnnRec": 8, "ucfKnnRec": 9, "nerIcfKnnRec": 10, "othRec": 11,
	"noCmpStu": 1, "cmpStu": 2, "othStu": 3,
	"bt0to10Sub": 1, "bt10to1bSub": 2, "bt1bto1kSub": 3, "bt1kto10kSub": 4, "bt10kto100kSub": 5, "bt100kto1000kSub": 6, "bt1000kto10000kSub": 7, "othSub": 8,
	"lesMonIn": 1, "bt1mto3mIn": 2, "bt3mto12mIn": 3, "bt12mto99mIn": 4, "othIn": 5,
}

var exhibitMapToString = map[string]string{
	"allMdl": "全模块叠加", "shfRecMdl": "书架推荐", "shfGusMdl": "书架-猜你喜欢", "freRecMdl": "免费-免费推荐", "freGusMdl": "免费-猜你喜欢", "monStmMdl": "包月瀑布流", "foeCateRecMdl": "封面页-类别推荐", "foeRedRedMdl": "封面页-读本书的人还看过", "foeRedMorMdl": "封面页-读本书的人还看过更多", "sehResTopMdl": "搜索结果页-热搜TOP榜", "sehResGusMdl": "搜索结果页-猜你喜欢", "bakRedRedMdl": "章末页-读本书的人还看过", "chsGilStmMdl": "精选-女频瀑布流", "chsCmpMdl": "精选-完结佳作", "chsCmpStmMdl": "精选-完结瀑布流", "chsRakStmMdl": "精选-排行瀑布流", "chsRedRecMdl": "精选-根据阅读书籍推荐", "chsRedCatRecMdl": "精选-根据阅读分类推荐", "chsStmMdl": "精选-瀑布流", "chsHotRecMdl": "精选-热门推荐", "chsBoyStmMdl": "精选-男频瀑布流", "chsChsRedMdl": "精选-精品必读",  "extBlkMdl": "退出拦截推荐",
	"allArea": "全区域叠加", "oneArea": "一类地区", "twoArea": "二类地区", "trdArea": "三类地区", "othArea": "其它地区",
	"allUsrLevel": "全用户级别叠加", "regUsrLevel": "普通用户", "sphUsrLevel": "特殊用户", "othUsrLevel": "其它用户级别",
	"allUsr": "全新旧用户叠加", "newUsr": "新用户", "oldUsr": "老用户", "othUsr": "其它新/老用户",
	"allFeeUsr": "全付费类型用户叠加", "freFeeUsr": "纯免费用户", "mybChgFeeUsr": "潜在付费用户", "lgtChgFeeUsr": "轻度付费用户", "mdlChgFeeUsr": "中度付费用户", "hghChgFeeUsr": "重度付费用户", "othFeeUsr": "其它付费类型用户",
	"allItemFee": "全付费类型物品叠加", "freItmFee": "付费物品", "chgItmFee": "免费物品", "monItmFee": "包月物品", "tfItmFee": "限免物品", "othItmFee": "其它付费类型物品",
	"allRec": "全策略叠加", "cat1Rec": "一级同分类", "cat2Rec": "二级同分类", "cotSimRec": "内容相似", "simAthRec": "同作者", "catRec": "同分类", "livStmRec": "实时流", "popRec": "流行度", "icfKnnRec": "物品协同", "ucfKnnRec": "用户协同", "nerIcfKnnRec": "近期协同", "othRec": "其它策略",
	"allStu": "全书籍状态叠加", "noCmpStu": "连载", "cmpStu": "完结", "othStu": "其它状态",
	"allSub": "全订阅级别叠加", "bt0to10Sub": "0~10订阅", "bt10to1bSub": "10~100订阅", "bt1bto1kSub": "100~1千订阅", "bt1kto10kSub": "1千~1万订阅", "bt10kto100kSub": "1万~10万订阅", "bt100kto1000kSub": "10万~1百万订阅", "bt1000kto10000kSub": "1百万~1千万订阅", "othSub": "其它订阅级别",
	"allIn": "全入库时间叠加", "lesMonIn": "1月内入库", "bt1mto3mIn": "1~3月内入库", "bt3mto12mIn": "3~12月内入库", "bt12mto99mIn": "12~99月内入库", "othIn": "其它入库时间",
	"dspNum": "推荐量", "clkNum": "点击量", "srbNum": "订阅量", "redNum": "阅读量1", "rteNum": "阅读量2",
	"clkDsp": "点展比", "subClk": "订点比", "subDsp": "订展比", "redSub": "阅订比1", "redDsp": "阅展比1", "retent": "阅订比2", "rteDsp": "阅展比",
}

func init() {
	host := beego.AppConfig.String("mysql::host")
	port := beego.AppConfig.String("mysql::port")
	user := beego.AppConfig.String("mysql::user")
	passwd := beego.AppConfig.String("mysql::passwd")
	mysqlInfo = user + ":" + passwd + "@tcp(" + host + ":" + port + ")/"
}
