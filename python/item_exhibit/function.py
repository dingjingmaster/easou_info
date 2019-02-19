#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import datetime

###
# 将 app————汉字转英文
def app_trans_to_word(mstr):
    res = ''
    if mstr == '宜搜小说':
        res = 'easouApp'
    elif mstr == '微卷':
        res = 'weijuanApp'
    elif mstr == '其它':
        res = 'othApp'
    return res

###
# 将模块————汉字转英文
def module_trans_to_word(mstr):
    res = ''
    if mstr == '书架推荐':
        res = 'shfRecMdl'
    elif mstr == '书架-猜你喜欢':
        res = 'shfGusMdl'
    elif mstr == '免费-免费推荐':
        res = 'freRecMdl'
    elif mstr == '免费-猜你喜欢':
        res = 'freGusMdl'
    elif mstr == '包月瀑布流':
        res = 'monStmMdl'
    elif mstr == '封面页-类别推荐':
        res = 'foeCateRecMdl'
    elif mstr == '封面页-读本书的人还看过':
        res = 'foeRedRedMdl'
    elif mstr == '封面页-读本书的人还看过更多':
        res = 'foeRedMorMdl'
    elif mstr == '搜索结果页-热搜TOP榜':
        res = 'sehResTopMdl'
    elif mstr == '搜索结果页-猜你喜欢':
        res = 'sehResGusMdl'
    elif mstr == '章末页-读本书的人还看过':
        res = 'bakRedRedMdl'
    elif mstr == '精选-女频瀑布流':
        res = 'chsGilStmMdl'
    elif mstr == '精选-完结佳作':
        res = 'chsCmpMdl'
    elif mstr == '精选-完结瀑布流':
        res = 'chsCmpStmMdl'
    elif mstr == '精选-排行瀑布流':
        res = 'chsRakStmMdl'
    elif mstr == '精选-根据阅读书籍推荐':
        res = 'chsRedRecMdl'
    elif mstr == '精选-根据阅读分类推荐':
        res = 'chsRedCatRecMdl'
    elif mstr == '精选-瀑布流':
        res = 'chsStmMdl'
    elif mstr == '精选-热门推荐':
        res = 'chsHotRecMdl'
    elif mstr == '精选-男频瀑布流':
        res = 'chsBoyStmMdl'
    elif mstr == '精选-精品必读':
        res = 'chsChsRedMdl'
    elif mstr == '退出拦截推荐':
        res = 'extBlkMdl'
    elif mstr == '免费-包月推荐':
        res = 'freByRecMdl'
    elif mstr == '七日限免':
        res = 'fre7TfMdl'
    elif mstr == '封面页-作者推荐':
        res = 'foeAutRecMdl'
    return res

###
# 地区级别————汉字转英文
def area_level_trans_to_word(mstr):
    res = ''
    if mstr == '一类地区':
        res = 'oneArea'
    elif mstr == '二类地区':
        res = 'twoArea'
    elif mstr == '三类地区':
        res = 'trdArea'
    elif mstr == '其它':
        res = 'othArea'
    elif mstr == '四类地区':
        res = 'fthArea'
    return res

###
# 用户级别————汉字转英文
def user_level_trans_to_word(mstr):
    res = ''
    if mstr == '普通用户':
        res = 'regUsrLevel'
    elif mstr == '特殊用户':
        res = 'sphUsrLevel'
    elif mstr == '其它':
        res = 'othUsrLevel'
    return res

###
# 新旧用户————汉字转英文
def user_nd_trans_to_word(mstr):
    res = ''
    if mstr == '新用户':
        res = 'newUsr'
    elif mstr == '老用户':
        res = 'oldUsr'
    elif mstr == '其它':
        res = 'othUsr'
    return res

###
# 用户付费类型————汉字转英文
def user_fee_trans_to_word(mstr):
    res = ''
    if mstr == '纯免费':
        res = 'freFeeUsr'
    elif mstr == '潜在付费':
        res = 'mybChgFeeUsr'
    elif mstr == '轻度付费':
        res = 'lgtChgFeeUsr'
    elif mstr == '中度付费':
        res = 'mdlChgFeeUsr'
    elif mstr == '重度付费':
        res = 'hghChgFeeUsr'
    elif mstr == '其它':
        res = 'othFeeUsr'
    return res

###
# 物品付费类型————汉字转英文
def item_fee_trans_to_word(mstr):
    res = ''
    if mstr == '付费':
        res = 'chgItmFee'
    elif mstr == '免费':
        res = 'freItmFee'
    elif mstr == '包月':
        res = 'monItmFee'
    elif mstr == '限免':
        res = 'tfItmFee'
    elif mstr == '其它':
        res = 'othItmFee'
    elif mstr == '互联网':
        res = 'allFreItmFee'
    return res

###
# 推荐策略————汉字转英文
def strategy_trans_to_word(mstr):
    res = ''
    if mstr == '一级同分类':
        res = 'cat1Rec'
    elif mstr == '二级同分类':
        res = 'cat2Rec'
    elif mstr == '内容相似':
        res = 'cotSimRec'
    elif mstr == '同作者':
        res = 'simAthRec'
    elif mstr == '同分类':
        res = 'catRec'
    elif mstr == '实时流':
        res = 'livStmRec'
    elif mstr == '流行度':
        res = 'popRec'
    elif mstr == '物品协同':
        res = 'icfKnnRec'
    elif mstr == '用户协同':
        res = 'ucfKnnRec'
    elif mstr == '近期协同':
        res = 'nerIcfKnnRec'
    elif mstr == '冷启动':
        res = 'codRec'
    elif mstr == '订阅模型':
        res = 'subMdlRec'
    elif mstr == '阅读模型':
        res = 'redMdlRec'
    elif mstr == '其它':
        res = 'othRec'
    return res

###
# 连载/完结状态————汉字转英文
def status_trans_to_word(mstr):
    res = ''
    if mstr == '完结':
        res = 'cmpStu'
    elif mstr == '连载':
        res = 'noCmpStu'
    elif mstr == '其它':
        res = 'othStu'
    return res

###
# 订阅级别————汉字转英文
def view_trans_to_word(mstr):
    res = ''
    if mstr == '[0,10)':
        res = 'bt0to10Sub'
    elif mstr == '[10,100)':
        res = 'bt10to1bSub'
    elif mstr == '[100,1000)':
        res = 'bt1bto1kSub'
    elif mstr == '[1000,10000)':
        res = 'bt1kto10kSub'
    elif mstr == '[10000,100000)':
        res = 'bt10kto100kSub'
    elif mstr == '[100000,1000000)':
        res = 'bt100kto1000kSub'
    elif mstr == '[1000000,10000000)':
        res = 'bt1000kto10000kSub'
    elif mstr == '其它':
        res = 'othSub'
    return res

###
# 入库时间————汉字转英文
def intime_trans_to_word(mstr):
    res = ''
    if mstr == '1月内入库':
        res = 'lesMonIn'
    elif mstr == '1~3月内入库':
        res = 'bt1mto3mIn'
    elif mstr == '3~12月内入库':
        res = 'bt3mto12mIn'
    elif mstr == '12~99月内入库':
        res = 'bt12mto99mIn'
    elif mstr == '其它':
        res = 'othIn'
    return res

###
# 将 app————汉字转英文
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
# 将模块————汉字转数字
def module_trans_to_num(mstr):
    res = 0
    if mstr == '书架推荐':
        res = 1
    elif mstr == '书架-猜你喜欢':
        res = 2
    elif mstr == '免费-免费推荐':
        res = 3
    elif mstr == '免费-猜你喜欢':
        res = 4
    elif mstr == '包月瀑布流':
        res = 5
    elif mstr == '封面页-类别推荐':
        res = 6
    elif mstr == '封面页-读本书的人还看过':
        res = 7
    elif mstr == '封面页-读本书的人还看过更多':
        res = 8
    elif mstr == '搜索结果页-热搜TOP榜':
        res = 9
    elif mstr == '搜索结果页-猜你喜欢':
        res = 10
    elif mstr == '章末页-读本书的人还看过':
        res = 11
    elif mstr == '精选-女频瀑布流':
        res = 12
    elif mstr == '精选-完结佳作':
        res = 13
    elif mstr == '精选-完结瀑布流':
        res = 14
    elif mstr == '精选-排行瀑布流':
        res = 15
    elif mstr == '精选-根据阅读书籍推荐':
        res = 16
    elif mstr == '精选-根据阅读分类推荐':
        res = 17
    elif mstr == '精选-瀑布流':
        res = 18
    elif mstr == '精选-热门推荐':
        res = 19
    elif mstr == '精选-男频瀑布流':
        res = 20
    elif mstr == '精选-精品必读':
        res = 21
    elif mstr == '退出拦截推荐':
        res = 22
    elif mstr == '免费-包月推荐':
        res = 23
    elif mstr == '七日限免':
        res = 24
    elif mstr == '封面页-作者推荐':
        res = 25
    return res

###
# 地区级别————汉字转数字
def area_level_trans_to_num(mstr):
    res = 0
    if mstr == '一类地区':
        res = 1
    elif mstr == '二类地区':
        res = 2
    elif mstr == '三类地区':
        res = 3
    elif mstr == '其它':
        res = 4
    elif mstr == '四类地区':
        res = 5
    return res

###
# 用户级别————汉字转数字
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
# 新旧用户————汉字转数字
def user_nd_trans_to_num(mstr):
    res = 0
    if mstr == '新用户':
        res = 1
    elif mstr == '老用户':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 用户付费类型————汉字转数字
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
# 物品付费类型————汉字转数字
def item_fee_trans_to_num(mstr):
    res = 0
    if mstr == '免费':
        res = 1
    elif mstr == '付费':
        res = 2
    elif mstr == '包月':
        res = 3
    elif mstr == '限免':
        res = 4
    elif mstr == '其它':
        res = 5
    elif mstr == '互联网':
        res = 6
    return res

###
# 推荐策略————汉字转数字
def strategy_trans_to_num(mstr):
    res = 0
    if mstr == '一级同分类':
        res = 1
    elif mstr == '二级同分类':
        res = 2
    elif mstr == '内容相似':
        res = 3
    elif mstr == '同作者':
        res = 4
    elif mstr == '同分类':
        res = 5
    elif mstr == '实时流':
        res = 6
    elif mstr == '流行度':
        res = 7
    elif mstr == '物品协同':
        res = 8
    elif mstr == '用户协同':
        res = 9
    elif mstr == '近期协同':
        res = 10
    elif mstr == '冷启动':
        res = 11
    elif mstr == '订阅模型':
        res = 12
    elif mstr == '阅读模型':
        res = 13
    elif mstr == '其它':
        res = 14
    return res

###
# 连载/完结状态————汉字转数字
def status_trans_to_num(mstr):
    res = 0
    if mstr == '连载':
        res = 1
    elif mstr == '完结':
        res = 2
    elif mstr == '其它':
        res = 3
    return res

###
# 订阅级别————汉字转数字
def view_trans_to_num(mstr):
    res = 0
    if mstr == '[0,10)':
        res = 1
    elif mstr == '[10,100)':
        res = 2
    elif mstr == '[100,1000)':
        res = 3
    elif mstr == '[1000,10000)':
        res = 4
    elif mstr == '[10000,100000)':
        res = 5
    elif mstr == '[100000,1000000)':
        res = 6
    elif mstr == '[1000000,10000000)':
        res = 7
    elif mstr == '其它':
        res = 8
    return res

###
# 入库时间————汉字转数字
def intime_trans_to_num(mstr):
    res = 0
    if mstr == '1月内入库':
        res = 1
    elif mstr == '1~3月内入库':
        res = 2
    elif mstr == '3~12月内入库':
        res = 3
    elif mstr == '12~99月内入库':
        res = 4
    elif mstr == '其它':
        res = 5
    return res

def get_inject_sql(arr, timeStamp):
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
    sql = "INSERT INTO item_exhibit(id, app, \
              module, areaLevel, userLevel, userNewOld, userFee, itemFee, \
              strategy, status, view, intime, \
              recNum, clkNum, subNum, redNum1, redNum2, timeStamp)\
              VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d');" % \
          (id,  app_trans_to_num(arr[0]), \
           module_trans_to_num(arr[1]), area_level_trans_to_num(arr[2]), \
           user_level_trans_to_num(arr[3]), user_nd_trans_to_num(arr[4]), \
           user_fee_trans_to_num(arr[5]), item_fee_trans_to_num(arr[6]), \
           strategy_trans_to_num(arr[7]), status_trans_to_num(arr[8]), \
           view_trans_to_num(arr[9]), intime_trans_to_num(arr[10]), \
           int(arr[11]), int(arr[12]), int(arr[13]), int(arr[14]), int(arr[15]), int(timeStamp))
    return sql

def execute_sql(cursor, sql):
    try:
        cursor.execute(sql)
    except:
        print "sql:" + sql + "\t 执行错误"
    return

def commit_sql(cursor):
    try:
        db.commit()
    except Exception, e:
        db.rollback()
        print ('sql 事务执行失败! 错误: ' + e)
    return

def delete_sdy(db, tim):
    msql = 'DELETE FROM item_exhibit WHERE timeStamp = ' + tim + ';'
    execute_sql(db, msql)
