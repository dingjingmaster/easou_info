package main

import (
	"github.com/astaxie/beego"
	_ "iyuedu_service/routers"
)

func main() {

	/* 配置 */
	beego.BConfig.RouterCaseSensitive = true  // 是否开启区分大小写
	beego.BConfig.ServerName = "easou_info"   // 服务器名称
	beego.BConfig.RecoverPanic = true         // 是否异常恢复
	beego.BConfig.CopyRequestBody = true      // 是否允许在HTTP请求时，返回原始请求体数据字节
	beego.BConfig.EnableErrorsShow = true     // 是否显示系统错误信息
	beego.BConfig.WebConfig.AutoRender = true // 是否模板自动渲染
	beego.BConfig.WebConfig.EnableDocs = true // 否开启文档内置功能
	//beego.BConfig.WebConfig.FlashName = "easou_info"   // Flash数据设置时Cookie的名称
	beego.BConfig.WebConfig.DirectoryIndex = false // 是否开启静态目录的列表显示

	// 静态文件是否压缩
	beego.BConfig.WebConfig.StaticExtensionsToGzip = []string{".css", ".js"} // 允许哪些后缀名的静态文件进行gzip压缩，默认支持 .css 和 .js

	// http 配置
	beego.BConfig.Listen.Graceful = false  // 是否开启热升级
	beego.BConfig.Listen.ServerTimeOut = 0 // 设置 HTTP 的超时时间，默认是 0，不超时。
	beego.BConfig.Listen.EnableHTTP = true // 是否启用HTTP监听
	beego.BConfig.Listen.HTTPAddr = ""     // 应用监听地址，默认为空，监听所有的网卡 IP。

	// https 配置
	beego.BConfig.Listen.EnableHTTPS = false // 是否启用 https
	beego.BConfig.Listen.HTTPSAddr = ""      // beego.BConfig.Listen.HTTPSAddr = ""
	//beego.BConfig.Listen.HTTPSPort = 10443              // 应用监听端口，默认为 10443
	//beego.BConfig.Listen.HTTPSCertFile = "conf/ssl.crt" // https
	//beego.BConfig.Listen.HTTPSKeyFile = "conf/ssl.key"  // https

	// session 配置
	//beego.BConfig.WebConfig.Session.SessionOn = true                       // session 是否开启
	//beego.BConfig.WebConfig.Session.SessionProvider = "file"               // session 的引擎，默认是 memory
	//beego.BConfig.WebConfig.Session.SessionProviderConfig = "tmp_session/" // session 缓存目录
	//beego.BConfig.WebConfig.Session.SessionName = "ENJOYREADID"            // 存在客户端的 cookie 名称
	//beego.BConfig.WebConfig.Session.SessionGCMaxLifetime = 3600            // session 过期时间
	//beego.BConfig.WebConfig.Session.SessionCookieLifeTime = 3600           // session 默认存在客户端的 cookie 的时间
	//beego.BConfig.WebConfig.Session.SessionAutoSetCookie = true            // 是否开启SetCookie

	// 日志
	//beego.SetLogger("file",
	//	`{
	//				"filename":"logs/log.log",
	//				"level":4,
	//				"separate":["emergency", "alert", "critical", "error", "warning", "notice", "info", "debug"]
	//				}`)

	/* 开始运行 */
	beego.Run()
}
