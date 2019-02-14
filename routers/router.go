package routers

import (
	"easou_info/controllers"
	"github.com/astaxie/beego"
)

func init() {
	beego.Router("/", &controllers.IndexController{})
	beego.Router("/exhibit", &controllers.ExhibitSelectControl{})
	beego.Router("/retention", &controllers.RetentionSelectControl{})
}
