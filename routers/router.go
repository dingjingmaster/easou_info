package routers

import (
	"easou_info/controllers"
	"github.com/astaxie/beego"
)

func init() {
	beego.Router("/", &controllers.IndexController{})
	beego.Router("/exhibit", &controllers.ExhibitSelectControl{})
	beego.Router("/read_event", &controllers.ReadEventSelectControl{})
	beego.Router("/retention", &controllers.RetentionSelectControl{})
	beego.Router("/search_item", &controllers.ItemInfoControl{})
}
