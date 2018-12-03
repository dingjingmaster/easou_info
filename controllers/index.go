package controllers

import (
	"github.com/astaxie/beego"
)

type IndexController struct {
	beego.Controller
}

func (ts *IndexController) Get() {
	ts.TplName = "index.html"
}
