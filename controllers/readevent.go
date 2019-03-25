package controllers

import (
	"easou_info/models"
	"fmt"
	"github.com/astaxie/beego"
	"github.com/json-iterator/go"
)

type ReadEventSelectControl struct {
	beego.Controller
}

/**
 *	post 请求
 * 		1. 解析请求参数
 *		2. 数据查找
 *		3. json 打包
 *		4. 返回数据
 */
func (ts *ReadEventSelectControl) Post() {
	request := models.ReadEventRequest{}
	response := models.Response{}
	var json = jsoniter.ConfigCompatibleWithStandardLibrary
	if err := json.Unmarshal(ts.Ctx.Input.RequestBody, &request); nil == err {
		models.QueryReadEvent(&request, &response)
	} else {
		// 错误处理
		response.Status = false
		response.Rrror = "请求的 json 解析失败..."
	}
	if respString, err := json.Marshal(response); nil == err {
		ts.Ctx.WriteString(string(respString))
	} else {
		fmt.Printf("\n错误: %s \n %s\n", err, respString)
	}
}
