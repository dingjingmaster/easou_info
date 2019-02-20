#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('缺少需要的输入参数')
        exit(-1)
    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    itemInfo = sys.argv[4]
    updateTime = sys.argv[5]

    db = MySQLdb.connect(ip, user, passwd, 'item_info', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock')
    cursor = db.cursor()

    db.close()