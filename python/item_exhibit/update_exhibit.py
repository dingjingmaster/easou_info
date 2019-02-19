#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
from function import delete_sdy
from function import get_inject_sql
from function import execute_sql
from function import commit_sql

def inject_mysql(dataTime, dataPath, cursor, db):
    timeStamp = int(dataTime)
    with open(dataPath, 'r') as fr:
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 16:
                print ('错误行: ' + line + '\n')
        sql = get_inject_sql(arr, timeStamp)
        execute_sql(cursor, sql)
    commit_sql(db)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print ("请输入手动更新的时间")
        exit(-1)

    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    dataTime = sys.argv[4]
    exhibitData = sys.argv[5]

    db = MySQLdb.connect(ip, user, passwd, 'item_exhibit', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock')
    cursor = db.cursor()
    delete_sdy(cursor, db, dataTime)
    inject_mysql(dataTime, exhibitData, cursor, db)
    db.close()