package main

import (
	_ "easou_info/routers"
	"github.com/astaxie/beego"
)

func main() {

	/* 配置 */
	if ok, _ := beego.AppConfig.Bool("service::debug"); ok {
		beego.AppPath = "E:/GO/src/easou_info/"
		beego.SetStaticPath("/", "E:/easou-web/dist/")
	} else {
		beego.AppPath = "/data/release/web/"
		beego.SetStaticPath("/", "/data/release/web/dist/")
	}

	beego.BConfig.RouterCaseSensitive = true  // 是否开启区分大小写
	beego.BConfig.ServerName = "easou_info"   // 服务器名称
	beego.BConfig.RecoverPanic = true         // 是否异常恢复
	beego.BConfig.CopyRequestBody = true      // 是否允许在HTTP请求时，返回原始请求体数据字节
	beego.BConfig.EnableErrorsShow = true     // 是否显示系统错误信息
	beego.BConfig.WebConfig.EnableDocs = true // 否开启文档内置功能
	//beego.BConfig.WebConfig.FlashName = "easou_info"   // Flash数据设置时Cookie的名称
	beego.BConfig.WebConfig.DirectoryIndex = false // 是否开启静态目录的列表显示

	// 静态文件是否压缩
	beego.BConfig.WebConfig.StaticExtensionsToGzip = []string{".css", ".js"} // 允许哪些后缀名的静态文件进行gzip压缩，默认支持 .css 和 .js

	// http 配置
	beego.BConfig.Listen.Graceful = false  // 是否开启热升级
	beego.BConfig.Listen.ServerTimeOut = 0 // 设置 HTTP 的超时时间，默认是 0，不超时。
	beego.BConfig.Listen.EnableHTTP = true // 是否启用HTTP监听

	/* 开始运行 */
	beego.Run()
}
