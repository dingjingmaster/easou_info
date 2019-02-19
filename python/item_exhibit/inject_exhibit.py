#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
from function import get_inject_sql
from function import get_update_sql
from function import execute_sql
from function import commit_sql

# inject mysql
def inject_mysql(today, yesterday, exhibitToday, exhibitYesterday,  cursor, db):
    with open(exhibitToday, 'r') as fr:
        timeStamp = int(today)
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 16:
                print('错误行: ' + line + '\n')
                continue
            sql = get_inject_sql(arr, timeStamp)
            execute_sql(cursor, sql)
    commit_sql(db)
    print ('当天数据注入 MySQL 完成！！！')

    with open(exhibitYesterday, 'r') as fr:
        timeStamp = int(yesterday)
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 16:
                print ('错误行: ' + line + '\n')
                continue
            sql = get_inject_sql(arr, timeStamp)
            execute_sql(cursor, sql)
    commit_sql(db)
    print ('昨天数据注入 MySQL 完成！！！')

    with open(exhibitYesterday, 'r') as fr:
        timeStamp = int(yesterday)
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 16:
                print ('错误行: ' + line + '\n')
                continue
            sql = get_update_sql(arr, timeStamp)
            execute_sql(cursor, sql)
    commit_sql(db)
    print ('昨天数据更细 MySQL 完成！！！')
    return


if __name__ == '__main__':

    if len(sys.argv) != 8:
        print ('请输入数据库用户名和密码以及时间 例:"20180101"')
        exit(-1)
    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    today = sys.argv[4]
    yesterday = sys.argv[5]
    exhibitToday = sys.argv[6]
    exhibitYesterday = sys.argv[7]

    #db = MySQLdb.connect(ip, user, passwd, 'item_exhibit');
    db = MySQLdb.connect(ip, user, passwd, 'item_exhibit', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock');
    cursor = db.cursor()
    inject_mysql(today, yesterday, exhibitToday, exhibitYesterday,  cursor)
    db.close()

