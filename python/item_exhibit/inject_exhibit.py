#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import datetime


def get_update_sql(arr, timeStamp):
    id = app_trans_to_word(arr[0]) + \
            '-' + module_trans_to_word(arr[1]) + \
            '-' + area_level_trans_to_word(arr[2]) + \
            '-' + user_level_trans_to_word(arr[3]) + \
            '-' + user_nd_trans_to_word(arr[4]) + \
            '-' + user_fee_trans_to_word(arr[5]) + \
            '-' + item_fee_trans_to_word(arr[6]) + \
            '-' + strategy_trans_to_word(arr[7]) + \
            '-' + status_trans_to_word(arr[8]) + \
            '-' + view_trans_to_word(arr[9]) + \
            '-' + intime_trans_to_word(arr[10]) + \
            '-' + str(timeStamp)
    sql = "UPDATE item_exhibit SET app = '%d', module = '%d', areaLevel = '%d', userLevel = '%d', \
          userNewOld = '%d', userFee = '%d', itemFee = '%d', strategy = '%d', status = '%d', view = '%d', \
          intime = '%d', recNum = '%d', clkNum = '%d', subNum = '%d', redNum1 = '%d', redNum2 = '%d', timeStamp = '%d' WHERE id = '%s';" %\
          (app_trans_to_num(arr[0]), \
            module_trans_to_num(arr[1]), area_level_trans_to_num(arr[2]), \
            user_level_trans_to_num(arr[3]), user_nd_trans_to_num(arr[4]), \
            user_fee_trans_to_num(arr[5]), item_fee_trans_to_num(arr[6]), \
            strategy_trans_to_num(arr[7]), status_trans_to_num(arr[8]), \
            view_trans_to_num(arr[9]), intime_trans_to_num(arr[10]), \
            int(arr[11]), int(arr[12]), int(arr[13]), int(arr[14]), int(arr[15]), int(timeStamp), id)

    return sql

# inject mysql
#def inject_mysql(exhibitPath, exhibitYesterdayPath,  cursor, time):
def inject_mysql(today, yesterday, exhibitToday, exhibitYesterday,  cursor):
    fr = open(exhibitToday, "r")
    timeStamp = int(today)
    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split("\t")
        if len(arr) != 16:
            print ('错误的行: ' + line + '\n')
            continue
        sql = get_inject_sql(arr, timeStamp)
        execute_sql(cursor, sql)
    fr.close()
    db.commit()

    fr = open(exhibitYesterday, "r")
    timeStamp = int(yesterday)
    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split("\t")
        if len(arr) != 16:
            print ('错误的行: ' + line + '\n')
            continue
        sql = get_inject_sql(arr, timeStamp)
        execute_sql(cursor, sql)
    fr.close()
    db.commit()

    fr = open(exhibitYesterday, "r")
    timeStamp = int(yesterday)
    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split("\t")
        if len(arr) != 16:
            print ('错误的行: ' + line + '\n')
            continue
        sql = get_update_sql(arr, timeStamp)
        execute_sql(cursor, sql)
    fr.close()
    try:
        db.commit()
    except Exception, e:
        db.rollback()
        print ('sql 事务执行错误：' + e)


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

