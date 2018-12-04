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
var exhibitMapToNum = map[string]int{
	"freFee": 1, "chgFee": 2, "monFee": 3, "pubFee": 4, "tfFee": 5, "allFee": 6,
	"livStmRec": 1, "usrKnnRec": 2, "codBotRec": 3, "popRec": 4, "itemKnnRec": 5, "samCtgRec": 6, "subMdlRec": 7, "redMdlRec": 8, "cotSimRec": 9, "redSimRec": 10, "cat1SimCtgRec": 11, "nerIcfKnn": 13,
	"shfRecMdl": 1, "freGusMdl": 2, "bakArdMdl": 3, "foeArdMdl": 4, "shfGusMdl": 5, "chsStmMdl": 6, "foeArdMorMdl": 7, "monStmMdl": 8, "foeCtgMdl": 9, "foeAutMdl": 10, "chsFinStmMdl": 11, "chsGilStmMdl": 15, "freMonRecMdl": 12, "chsBoyStmMdl": 13, "chsRakStmMdl": 14, "redRecMdl": 16, "extRecMdl": 17, "chsBDMdl": 18, "chsHRMdl": 19, "freFRMdl": 20, "chsRRCMdl": 21, "chsRRBMdl": 22, "chsCRMdl": 23,
	"noCmpStau": 1, "cmpStau": 2,
	"bt0to10Sub": 1, "bt10to1bSub": 2, "bt1bto1kSub": 3, "bt1kto10kSub": 4, "bt10kto100kSub": 5, "bt100kto1000kSub": 6, "bt1000kto10000kSub": 7,
	"lesMonIn": 1, "bt1mto3mIn": 2, "bt3mto12mIn": 3, "bt12mto99mIn": 4,
	"lesMonUpd": 1, "bt1mto3mUpd": 2, "bt3mto12mUpd": 3, "bt12mto99mUpd": 4,
	"boyCfy1": 1, "girlCfy1": 2, "monCfy1": 3, "pshCfy1": 4, "othCfy1": 5,
}

var exhibitMapToString = map[string]string{
	"clkDsp": "点展比", "subClk": "订点比", "subDsp": "订展比", "redSub": "阅订比", "redDsp": "阅展比", "retent": "留存率", "rteDsp": "留展比",
	"shfRecMdl": "书架推荐", "freGusMdl": "免费猜你喜欢", "bakArdMdl": "章末页读本书的人还看过", "foeArdMdl": "封面页读本书的人还看过", "shfGusMdl": "书架猜你喜欢", "chsStmMdl": "精选瀑布流", "foeArdMorMdl": "封面页读本书的人还看过更多", "monStmMdl": "包月瀑布流", "foeCtgMdl": "封面页类别推荐", "foeAutMdl": "封面页作者推荐", "chsFinStmMdl": "精选完结瀑布流", "chsGilStmMdl": "精选女频瀑布流", "freMonRecMdl": "免费包月推荐", "chsBoyStmMdl": "精选男频瀑布流", "chsRakStmMdl": "精选排行瀑布流", "redRecMdl": "根据阅读推荐", "extRecMdl": "退出拦截推荐", "chsBDMdl": "精选-精品必读", "chsHRMdl": "精选-热门推荐", "freFRMdl": "免费-免费推荐", "chsRRCMdl": "精选-根据阅读分类推荐", "chsRRBMdl": "精选-根据阅读书籍推荐", "chsCRMdl": "精选-完结佳作",
	"chgFee": "付费", "freFee": "免费(互联网书)", "monFee": "包月", "pubFee": "公版", "tfFee": "限免", "allFee": "全免(付费书免费读)",
	"livStmRec": "实时流", "usrKnnRec": "用户协同", "codBotRec": "冷启动", "popRec": "流行度", "itemKnnRec": "物品协同", "samCtgRec": "同分类", "subMdlRec": "订阅模型", "redMdlRec": "阅读模型", "cotSimRec": "内容相似", "redSimRec": "阅读同分类", "cat1SimCtgRec": "1级同分类", "nerIcfKnn": "近期协同",
	"cmpStau": "完结", "noCmpStau": "连载",
	"bt0to10Sub": "[0,10)", "bt10to1bSub": "[10,100)", "bt1bto1kSub": "[100,1000)", "bt1kto10kSub": "[1000,10000)", "bt10kto100kSub": "[10000,100000)", "bt100kto1000kSub": "[100000,1000000)", "bt1000kto10000kSub": "[1000000,10000000)",
	"lesMonIn": "1月内入库", "bt1mto3mIn": "1到3月内入库", "bt3mto12mIn": "3到12月内入库", "bt12mto99mIn": "12到99月内入库",
	"lesMonUpd": "0到1月未更新", "bt1mto3mUpd": "1到3月未更新", "bt3mto12mUpd": "3到12月未更新", "bt12mto99mUdp": "12到99月未更新",
	"boyCfy1": "男频", "girlCfy1": "女频", "monCfy1": "包月", "pshCfy1": "出版", "othCfy1": "其他",
	"dspNum": "展现量", "clkNum": "点击量", "srbNum": "订阅量", "redNum": "阅读量", "rteNum": "留存量",
}

func init() {
	host := beego.AppConfig.String("mysql::host")
	port := beego.AppConfig.String("mysql::port")
	user := beego.AppConfig.String("mysql::user")
	passwd := beego.AppConfig.String("mysql::passwd")
	mysqlInfo = user + ":" + passwd + "@tcp(" + host + ":" + port + ")/"
}
