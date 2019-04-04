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
def inject_chapter_mysql(today, dataPath, cursor, db):
    with open(dataPath, 'r') as fr:
        timeStamp = int(today)
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 14:
                print('错误行: ' + line + '\n')
                continue
            msql = ''
            msql = get_inject_sql(arr, timeStamp)
            execute_sql(cursor, msql)
    commit_sql(db)
    print ('当天数据注入 MySQL 完成！！！')
    return


if __name__ == '__main__':

    if len(sys.argv) != 8:
        print ('请输入数据库用户名和密码以及时间 例:"20180101"')
        exit(-1)
    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    today = sys.argv[4]
    dataChapterPath = sys.argv[5]
    dataUserPath = sys.argv[6]
    dataBookPath = sys.argv[7]

    db = MySQLdb.connect(ip, user, passwd, 'read_event', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock')
    cursor = db.cursor()
    inject_chapter_mysql(today, dataChapterPath, cursor, db)
    db.close()

