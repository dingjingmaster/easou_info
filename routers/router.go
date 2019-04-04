package routers

import (
	"easou_info/controllers"
	"github.com/astaxie/beego"
)

func init() {
	beego.Router("/", &controllers.IndexController{})
	beego.Router("/exhibit", &controllers.ExhibitSelectControl{})
	beego.Router("/read_event_c", &controllers.ReadEventCSelectControl{})
	beego.Router("/read_event_u", &controllers.ReadEventUSelectControl{})
	beego.Router("/read_event_b", &controllers.ReadEventBSelectControl{})
	beego.Router("/retention", &controllers.RetentionSelectControl{})
	beego.Router("/search_item", &controllers.ItemInfoControl{})
}
