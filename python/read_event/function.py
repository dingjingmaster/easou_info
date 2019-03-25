#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import datetime

###
# app
def app_trans_to_word(mstr):
    res = ''
    if mstr == '宜搜小说':
        res = 'easouApp'
    elif mstr == '微卷':
        res = 'weijuanApp'
    elif mstr == '其它':
        res = 'othApp'
    return res

def app_trans_to_num(mstr):
    res = 0
    if mstr == '宜搜小说':
        res = 1
    elif mstr == '微卷':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 用户级别
def user_level_trans_to_word(mstr):
    res = ''
    if mstr == '普通用户':
        res = 'regUsrLevel'
    elif mstr == '特殊用户':
        res = 'sphUsrLevel'
    elif mstr == '其它':
        res = 'othUsrLevel'
    return res

def user_level_trans_to_num(mstr):
    res = 0
    if mstr == '普通用户':
        res = 1
    elif mstr == '特殊用户':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 新旧用户
def user_new_old_trans_to_word(mstr):
    res = ''
    if mstr == '新用户':
        res = 'newUsrNew'
    elif mstr == '老用户':
        res = 'oldUsrNew'
    elif mstr == '其它':
        res = 'othUsrNew'
    return res

def user_new_old_trans_to_num(mstr):
    res = 0
    if mstr == '新用户':
        res = 1
    elif mstr == '老用户':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 包月用户
def user_month_trans_to_word(mstr):
    res = ''
    if mstr == '包月':
        res = 'monUsrMon'
    elif mstr == '非包月':
        res = 'unMonUsrMon'
    elif mstr == '其它':
        res = 'othUsrMon'
    return res

def user_month_trans_to_num(mstr):
    res = 0
    if mstr == '包月':
        res = 1
    elif mstr == '非包月':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 用户付费程度
def user_fee_trans_to_word(mstr):
    res = ''
    if mstr == '纯免费':
        res = 'freUsrFee'
    elif mstr == '潜在付费':
        res = 'mybChgUsrFee'
    elif mstr == '轻度付费':
        res = 'lgtChgUsrFee'
    elif mstr == '中度付费':
        res = 'mdlChgUsrFee'
    elif mstr == '重度付费':
        res = 'hghChgUsrFee'
    elif mstr == '其它':
        res = 'othUsrFee'
    return res

def user_fee_trans_to_num(mstr):
    res = 0
    if mstr == '纯免费':
        res = 1
    elif mstr == '潜在付费':
        res = 2
    elif mstr == '轻度付费':
        res = 3
    elif mstr == '中度付费':
        res = 4
    elif mstr == '重度付费':
        res = 5
    elif mstr == '其它':
        res = 6
    return res

###
# 用户地区级别
def user_area_trans_word(mstr):
    res = ''
    if mstr == '一类地区':
        res = 'oneArea'
    elif mstr == '二类地区':
        res = 'twoArea'
    elif mstr == '三类地区':
        res = 'trdArea'
    elif mstr == '四类地区':
        res = 'fthArea'
    elif mstr == '其它':
        res = 'othArea'
    return res

def user_area_trans_num(mstr):
    res = 0
    if mstr == '一类地区':
        res = 1
    elif mstr == '二类地区':
        res = 2
    elif mstr == '三类地区':
        res = 3
    elif mstr == '四类地区':
        res = 4
    elif mstr == '其它':
        res = 5
    return res

###
# 书籍状态级别
def status_trans_word(mstr):
    res = ''
    if mstr == '完结':
        res = 'cmpBookStu'
    elif mstr == '连载':
        res = 'noCmpBookStu'
    elif mstr == '其它':
        res = 'othBookStu'
    return res

def status_trans_num(mstr):
    res = ''
    if mstr == '完结':
        res = 1
    elif mstr == '连载':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 书籍类别
def category_trans_word(mstr):
    res = ''
    if mstr == '按章计费':
        res = 'tchgItmCate'
    elif mstr == '包月':
        res = 'monItmCate'
    elif mstr == '非包月':
        res = 'unMonItmCate'
    elif mstr == '限免':
        res = 'tfItmCate'
    elif mstr == '一折书籍':
        res = 'yzItmCate'
    elif mstr == '免费CP书':
        res = 'mcpItmCate'
    elif mstr == '免费互联网书':
        res = 'tfreItmCate'
    elif mstr == '断更':
        res = 'brkItmCate'
    elif mstr == '普通':
        res = 'genItmCate'
    elif mstr == '赠书':
        res = 'gveItmCate'
    elif mstr == '其它':
        res = 'othItmCate'
    return res

def category_trans_num(mstr):
    res = 0
    if mstr == '按章计费':
        res = 1
    elif mstr == '包月':
        res = 2
    elif mstr == '非包月':
        res = 3
    elif mstr == '限免':
        res = 4
    elif mstr == '一折书籍':
        res = 5
    elif mstr == '免费CP书':
        res = 6
    elif mstr == '免费互联网书':
        res = 7
    elif mstr == '断更':
        res = 8
    elif mstr == '普通':
        res = 9
    elif mstr == '赠书':
        res = 10
    elif mstr == '其它':
        res = 11
    return res

def get_inject_sql(arr, timeStamp):
    id = app_trans_to_word(arr[0]) + \
         '-' + user_level_trans_to_word(arr[1]) + \
         '-' + user_area_trans_word(arr[2]) + \
         '-' + user_month_trans_to_word(arr[3]) + \
         '-' + user_fee_trans_to_word(arr[4]) + \
         '-' + user_new_old_trans_to_word(arr[5]) + \
         '-' + status_trans_word(arr[6]) + \
         '-' + category_trans_word(arr[7]) + \
         '-' + str(timeStamp)
    sql = "INSERT INTO item_exhibit(id, app, \
              userLevel, userNewOld, ismonth, userFee, areaLevel, \
              status, cate, \
              gidNum, usrNum, chgNum, freNum, tfNum, sumNum, timeStamp)\
              VALUES('%s', '%d', \
                '%d', '%d', '%d', '%d', '%d', \
                '%d', '%d', \
                '%d', '%d', '%d', '%d', '%d', '%d', '%d');" % \
          (id,  app_trans_to_num(arr[0]), user_level_trans_to_num(arr[1]), \
           user_area_trans_num(arr[2]), user_month_trans_to_num(arr[3]), \
           user_fee_trans_to_num(arr[4]), user_new_old_trans_to_num(arr[5]), \
           status_trans_num(arr[6]), category_trans_num(arr[7]), \
           int(arr[8]), int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]), int(timeStamp))
    return sql

def get_update_sql(arr, timeStamp):
    sql = ''
    id = app_trans_to_word(arr[0]) + \
         '-' + user_level_trans_to_word(arr[1]) + \
         '-' + user_area_trans_word(arr[2]) + \
         '-' + user_month_trans_to_word(arr[3]) + \
         '-' + user_fee_trans_to_word(arr[4]) + \
         '-' + user_new_old_trans_to_word(arr[5]) + \
         '-' + status_trans_word(arr[6]) + \
         '-' + category_trans_word(arr[7]) + \
         '-' + str(timeStamp)
    # sql = "UPDATE read_event SET app, \
    #           userLevel, userNewOld, ismonth, userFee, areaLevel, \
    #           status, cate, \
    #           gidNum, usrNum, chgNum, freNum, tfNum, sumNum, timeStamp)\
    #           VALUES('%s', '%d', \
    #             '%d', '%d', '%d', '%d', '%d', \
    #             '%d', '%d', \
    #             '%d', '%d', '%d', '%d', '%d', '%d', '%d');" % \
    #       (id,  app_trans_to_num(arr[0]), user_level_trans_to_num(arr[1]), \
    #        user_area_trans_num(arr[2]), user_month_trans_to_num(arr[3]), \
    #        user_fee_trans_to_num(arr[4]), user_new_old_trans_to_num(arr[5]), \
    #        status_trans_num(arr[6]), category_trans_num(arr[7]), \
    #        int(arr[8]), int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]), int(timeStamp))
    # sql = "UPDATE item_exhibit SET app = '%d', module = '%d', areaLevel = '%d', userLevel = '%d', \
    #       userNewOld = '%d', userFee = '%d', itemFee = '%d', strategy = '%d', status = '%d', view = '%d', \
    #       intime = '%d', recNum = '%d', clkNum = '%d', subNum = '%d', redNum1 = '%d', redNum2 = '%d', timeStamp = '%d' WHERE id = '%s';" % \
    #       (app_trans_to_num(arr[0]), \
    #        module_trans_to_num(arr[1]), area_level_trans_to_num(arr[2]), \
    #        user_level_trans_to_num(arr[3]), user_nd_trans_to_num(arr[4]), \
    #        user_fee_trans_to_num(arr[5]), item_fee_trans_to_num(arr[6]), \
    #        strategy_trans_to_num(arr[7]), status_trans_to_num(arr[8]), \
    #        view_trans_to_num(arr[9]), intime_trans_to_num(arr[10]), \
    #        int(arr[11]), int(arr[12]), int(arr[13]), int(arr[14]), int(arr[15]), int(timeStamp), id)
    return sql

def execute_sql(cursor, sql):
    try:
        cursor.execute(sql)
    except:
        pass
        #print "sql:" + sql + "\t 执行错误"
    return

def commit_sql(db):
    try:
        db.commit()
    except Exception, e:
        db.rollback()
        print ('sql 事务执行失败! 错误: ' + e)
    return

def delete_sdy(cursor, db, tim):
    msql = 'DELETE FROM read_event WHERE timeStamp = ' + tim + ';'
    execute_sql(cursor, msql)
    commit_sql(db)
