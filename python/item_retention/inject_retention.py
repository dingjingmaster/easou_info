#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import datetime

def execute_sql(cursor, sql):

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sql:" + sql + "\t 执行错误"
        db.rollback()
    return;


def get_limitfree_sql(irid, last, remain, retent, tfCate, timeStamp):
    sql = "INSERT INTO item_retent_limitfree(irid,\
            last, remain, retent,\
            tfCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d');" % \
            (irid, last, remain, retent, int(tfCate), timeStamp)

    return sql

'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    typeCate = 1天 2周 3七日
    timeStamp = 时间戳
'''
def get_fee_sql(irid, last, remain, retent, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_fee(irid,\
            last, remain, retent,\
            feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, feeCate, typeCate, timeStamp)

    return sql

'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    feeCate = 1免费 2付费 3包月 4公版 5限免 6 全免
    typeCate = 1天 2周 3七日
    timeStamp = 时间戳
'''
def get_status_sql(irid, last, remain, retent, statuCate, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_status(irid,\
            last, remain, retent,\
            statuCate, feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, statuCate, feeCate, typeCate, timeStamp)

    return sql


'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    feeCate = 1免费 2付费 3包月 4公版 5限免 6 全免
    typeCate = 1天 2周 3七日
    viewCate = 1小于100 2介于100与1000 3介于1000与10000 4介于10000与100000 5大于100000
    timeStamp = 时间戳
'''
def get_viewCount_sql(irid, last, remain, retent, viewCate, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_viewcount(irid,\
            last, remain, retent,\
            viewCate, feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, viewCate, feeCate, typeCate, timeStamp)

    return sql


'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    feeCate = 1免费 2付费 3包月 4公版 5限免 6 全免
    typeCate = 1天 2周 3七日
    intimeCate = 1小于1月 2介于1月与3月 3介于3月与1年 4大于1年
    timeStamp = 时间戳
'''
def get_intime_sql(irid, last, remain, retent, intimeCate, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_intime(irid,\
            last, remain, retent,\
            intimeCate, feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, intimeCate, feeCate, typeCate, timeStamp)

    return sql


'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    feeCate = 1免费 2付费 3包月 4公版 5限免 6 全免
    typeCate = 1天 2周 3七日 
    updateCate = 1小于1月 2介于1月与3月 3介于3月与1年 4大于1年
    timeStamp = 时间戳
'''
def get_update_sql(irid, last, remain, retent, updateCate, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_update(irid,\
            last, remain, retent,\
            updateCate, feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, updateCate, feeCate, typeCate, timeStamp)

    return sql


'''
    irid = 状态 + 付费分类 + 时间戳
    last = 0
    remain = 0
    retent = 0.0
    feeCate = 1免费 2付费 3包月 4公版 5限免 6全免
    typeCate = 1天 2周 3七日
    classify1Cate = 1男频 2女频 3出版 4其它
    timeStamp = 时间戳
'''
def get_classify1_sql(irid, last, remain, retent, cate1Cate, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_retent_classify1(irid,\
            last, remain, retent,\
            cate1Cate, feeCate, typeCate,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%f', '%d', '%d', '%d', '%d');" % \
            (irid, last, remain, retent, cate1Cate, feeCate, typeCate, timeStamp)

    return sql

# 获取分类情况
def get_cate_status(mstr):

    flag = ""
    if mstr == "男频":
        flag = "boy"
    elif mstr == "女频":
        flag = "girl"
    elif mstr == "出版":
        flag = "pub"
    elif mstr == "其他" or mstr == "其它":
        flag = "other"

    return flag

# 获取连载/完结情况
def get_statu_status(mstr):

    flag = 0
    if mstr == "publish":
        flag = 1
    elif mstr == "accomplish":
        flag = 2
    return flag

# 获取订阅级别情况
def get_view_status(mstr):

    flag = 0
    if mstr == "bt0to1b":
        flag = 1
    elif mstr == "bt1bto1k":
        flag = 2
    elif mstr == "bt1kto1w":
        flag = 3
    elif mstr == "bt1wto10w":
        flag = 4
    elif mstr == "gt10w":
        flag = 5

    return flag


# 获取时间级别情况
def get_time_status(mstr):

    flag = 0
    if mstr == "l1m":
        flag = 1
    elif mstr == "bt1mt3m":
        flag = 2
    elif mstr == "bt3mt1y":
        flag = 3
    elif mstr == "gt1y":
        flag = 4

    return flag

# 获取一级分类级别情况
def get_cate1_status(mstr):

    flag = 0
    if mstr == "男频":
        flag = 1
    elif mstr == "女频":
        flag = 2
    elif mstr == "出版":
        flag = 3
    elif mstr == "其他" or mstr == "其它":
        flag = 4

    return flag

# 获取付费情况
def get_fee_status(mstr):

    flag = 0
    if mstr == "free":
        flag = 1
    elif mstr == "charge":
        flag = 2
    elif mstr == "month":
        flag = 3
    elif mstr == "pub":
        flag = 4
    elif mstr == "limitfree":
        flag = 5
    elif mstr == "allFee":
        flag = 6

    return flag


# inject mysql
def inject_mysql(txtpath, cursor, times, type):

    fr = open(txtpath, "r")
    sql = ""
    irid = ""
    last = 0
    remain = 0
    reten = 0.0
    feeCate = 0
    typeCate = 0
    
    # 公共元素
    timeStamp = int(times)
    if type == "day":
        typeCate = 1
    elif type == "week":
        typeCate = 2
    elif type == "week7":
        typeCate = 3

    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split("\t")
        id = arr[0].split("-")

        last = int(arr[1])
        remain = int(arr[2])
        retent = float(arr[3])

        # 天限免 ok
        if len(id) == 3 and id[0] == "tf":
            irid = type + "-" + "tf" + id[2] + "-" + str(times)
            sql = get_limitfree_sql(irid, last, remain, retent, id[2], timeStamp)
        # 总体付费情况 ok
        elif len(id) == 2 and id[0] == "fee":
            irid = type + "-" + id[1] + "-" + str(times)
            feeCate = get_fee_status(id[1])
            sql = get_fee_sql(irid, last, remain, retent, feeCate, typeCate, timeStamp)
        # 状态(连载/完结)付费情况 ok
        elif len(id) == 3 and id[0] == "status":
            irid = type + "-" + id[1] + "-" + id[2] + "-" + str(times)
            statuCate = get_statu_status(id[2])
            feeCate = get_fee_status(id[1])
            sql = get_status_sql(irid, last, remain, retent, statuCate, feeCate, typeCate, timeStamp)
        # 订阅量情况 ok
        elif len(id) == 3 and id[0] == "view":
            irid = type + "-" + id[1] + "-" + id[2] + "-" + str(times)
            viewCate = get_view_status(id[2])
            feeCate = get_fee_status(id[1])
            sql = get_viewCount_sql(irid, last, remain, retent, viewCate, feeCate, typeCate, timeStamp)
        # 入库时间
        elif len(id) == 3 and id[0] == "intime":
            irid = type + "-" + id[1] + "-" + id[2] + "-" + str(times)
            intimeCate = get_time_status(id[2])
            feeCate = get_fee_status(id[1])
            sql = get_intime_sql(irid, last, remain, retent, intimeCate, feeCate, typeCate, timeStamp)
        # 最后更新时间
        elif len(id) == 3 and id[0] == "updatetime":
            irid = type + "-" + id[1] + "-" + id[2] + "-" + str(times)
            updateCate = get_time_status(id[2])
            feeCate = get_fee_status(id[1])
            sql = get_update_sql(irid, last, remain, retent, updateCate, feeCate, typeCate, timeStamp)
        # 一级分类
        elif len(id) == 3 and id[0] == "cate1":
            irid = type + "-" + id[1] + "-" + get_cate_status(id[2]) + "-" + str(times)
            cate1Cate = get_cate1_status(id[2])
            feeCate = get_fee_status(id[1])
            sql = get_classify1_sql(irid, last, remain, retent, cate1Cate, feeCate, typeCate, timeStamp)
        
        execute_sql(cursor, sql)
    fr.close()


if __name__ == '__main__':

    if len(sys.argv) != 7:
        print '请输入数据库用户名和密码以及notime(例:"20180101")'
        exit(-1)
    user = sys.argv[1]
    passwd = sys.argv[2]
    time = sys.argv[3]
    day = sys.argv[4]
    week = sys.argv[5]
    week7 = sys.argv[6]

    db = MySQLdb.connect('localhost', user, passwd, 'item_retention', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock');
    cursor = db.cursor()                                                                # 获取操作游标
    inject_mysql(day, cursor, time, "day")
    inject_mysql(week, cursor, time, "week")
    inject_mysql(week7, cursor, time, "week7")

    db.close()                                                                          # 关闭数据库

    pass
