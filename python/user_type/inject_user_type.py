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


def get_summary_sql(utid, freNum, nchNum, chaNum, monNum, allNum, frePro, nchPro, chaPro, monPro, timeStamp):
    utid = 'summary' + '-' + str(timeStamp)
    sql = "INSERT INTO utype_summary(utid,\
            freNum, nchNum, chaNum, monNum, allNum,\
            frePro, nchPro, chaPro, monPro,\
            timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%d');" %\
            (utid, freNum, nchNum, chaNum, monNum, allNum, frePro, nchPro, chaPro, monPro, timeStamp)
    return sql

# inject mysql
def inject_mysql(mdict, cursor, times):
    sql = ""
    utid = ""
    freNum = 0
    nchNum = 0
    chaNum = 0
    monNum = 0
    allNum = 0
    frePro = 0.0
    nchPro = 0.0
    chaPro = 0.0
    monPro = 0.0
    timeStamp = int(times)

    freNum = mdict['freNum']
    nchNum = mdict['nchNum']
    chaNum = mdict['chaNum']
    monNum = mdict['monNum']
    allNum = mdict['allNum']

    frePro = float(mdict['freNum']) / mdict['allNum']
    nchPro = float(mdict['nchNum']) / mdict['allNum']
    chaPro = float(mdict['chaNum']) / mdict['allNum']
    monPro = float(mdict['monNum']) / mdict['allNum']

    sql = get_summary_sql(utid, freNum, nchNum, chaNum, monNum, allNum, frePro, nchPro, chaPro, monPro, timeStamp)
    execute_sql(cursor, sql)
    return

def get_user_type(path):
    mdict = {}
    mdict['freNum'] = 0
    mdict['nchNum'] = 0
    mdict['chaNum'] = 0
    mdict['monNum'] = 0
    mdict['allNum'] = 0

    fr = open(path, 'r')
    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split('\t')
        if len(line) < 2:
            continue
        uid, type = arr

        mdict['allNum'] += 1
        if 1 == int(type):
            mdict['freNum'] += 1
        elif 2 == int(type):
            mdict['nchNum'] += 1
        elif 3 == int(type):
            mdict['chaNum'] += 1
        elif 4 == int(type):
            mdict['monNum'] += 1
            fr.close()
    return mdict


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print '请输入数据库用户名和密码以及notime(例:"20180101")'
        exit(-1)
    user = sys.argv[1]
    passwd = sys.argv[2]
    time = sys.argv[3]
    userTypePath = sys.argv[4]

    retdict = {}
    
    db = MySQLdb.connect('localhost', user, passwd, 'user_type', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock');
    cursor = db.cursor()                                                                # 获取操作游标

    '''
    免费        用户量       占比
    准付费      用户量       占比
    付费        用户量       占比
    包月        用户量       占比
    时间戳
    '''
    # 获取用户类别数据
    retdict = get_user_type(userTypePath)
    inject_mysql(retdict, cursor, time)

    db.close()                                                                          # 关闭数据库

