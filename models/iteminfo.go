package models

import (
	_ "github.com/go-sql-driver/mysql"
)

type ItemInfoRequest struct {
	reqType                     string                      // gid name author
	value                       []string                    // 要查询的值
}

func QueryItemInfo(req *ItemInfoRequest, response *Response) {
	response.Status = true
	response.Data = []map[string]string{{"gid": "i_11111"}, {"gid": "i_22222", "name": "那么"}}
}