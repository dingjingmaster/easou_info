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


def get_summary_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, typeCate, timeStamp):
    sql = "INSERT INTO item_exhibit_summary(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, typeCate, timeStamp)

    return sql

def get_fee_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_fee(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, typeCate, timeStamp)

    return sql


def get_strategy_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, strategyCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_strategy(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, strategyCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, strategyCate, typeCate, timeStamp)

    return sql

def get_status_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, statusCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_status(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, statusCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, statusCate, typeCate, timeStamp)

    return sql

def get_view_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, viewCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_view(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, viewCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, viewCate, typeCate, timeStamp)

    return sql

def get_intime_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, intimeCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_intime(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, intimeCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, intimeCate, typeCate, timeStamp)

    return sql

def get_update_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, updateCate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_update(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, updateCate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, updateCate, typeCate, timeStamp)

    return sql

def get_classify1_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, classify1Cate, typeCate, timeStamp):

    sql = "INSERT INTO item_exhibit_classify1(dzid,\
            dspNum, clkNum, srbNum, redNum, rteNum,\
            clkDsp, subClk, subDsp, redSub, redDsp, retent, rteDsp,\
            feeCate, classify1Cate, typeCate, timeStamp)\
            VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f','%d', '%d', '%d', '%d');" %\
            (dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, classify1Cate, typeCate, timeStamp)

    return sql



# 将中文字符转为英文字符
def trans_to_word(mstr):
    res = ""

    # 推荐模块
    if mstr == '书架推荐':
        res = 'shfRecMdl'
    elif mstr == '书架-猜你喜欢':
        res = 'shfGusMdl'
    elif mstr == '免费-猜你喜欢':
        res = 'freGusMdl'
    elif mstr == '免费-包月推荐':
        res = 'freMonRecMdl'
    elif mstr == '章末页-读本书的人还看过':
        res = 'bakArdMdl'
    elif mstr == '封面页-读本书的人还看过':
        res = 'foeArdMdl'
    elif mstr == '封面页-读本书的人还看过更多':
        res = 'foeArdMorMdl'
    elif mstr == '封面页-类别推荐':
        res = 'foeCtgMdl'
    elif mstr == '封面页-作者推荐':
        res = 'foeAutMdl'
    elif mstr == '精选-瀑布流':
        res = 'chsStmMdl'
    elif mstr == '包月瀑布流':
        res = 'monStmMdl'
    elif mstr == '精选-完结瀑布流':
        res = 'chsFinStmMdl'
    elif mstr == '精选-女频瀑布流':
        res = 'chsGilStmMdl'
    elif mstr == '精选-男频瀑布流':
        res = 'chsBoyStmMdl'
    elif mstr == '精选-排行瀑布流':
        res = 'chsRakStmMdl'
    elif mstr == '根据阅读推荐':
        res = 'redRecMdl'
    elif mstr == '退出拦截推荐':
        res = 'extRecMdl'
    elif mstr == '精选-精品必读':
        res = 'chsBDMdl'
    elif mstr == '精选-热门推荐':
        res = 'chsHRMdl'
    elif mstr == '免费-免费推荐':
        res = 'freFRMdl'
    elif mstr == '精选-根据阅读分类推荐':
        res = 'chsRRCMdl'
    elif mstr == '精选-根据阅读书籍推荐':
        res = 'chsRRBMdl'
    elif mstr == '精选-完结佳作':
        res = 'chsCRMdl'

    # 书籍付费情况
    elif mstr == '付费':
        res = 'chgFee'
    elif mstr == '免费':
        res = 'freFee'
    elif mstr == '包月':
        res = 'monFee'
    elif mstr == '公版':
        res = 'pubFee'
    elif mstr == '限免':
        res = 'tfFee'
    elif mstr == '全免':
        res = 'allFee'

    # 推荐策略
    elif mstr == '实时流':
        res = 'livStmRec'
    elif mstr == '用户协同':
        res = 'usrKnnRec'
    elif mstr == '冷启动':
        res = 'codBotRec'
    elif mstr == '流行度':
        res = 'popRec'
    elif mstr == '物品协同':
        res = 'itmKnnRec'
    elif mstr == '同分类':
        res = 'samCtgRec'
    elif mstr == '订阅模型':
        res = 'subMdlRec'
    elif mstr == '阅读模型':
        res = 'redMdlRec'
    elif mstr == '内容相似':
        res = 'cotSimRec'
    elif mstr == '阅读同分类':
        res = 'redSimRec'
    elif mstr == '一级同分类':
        res = 'cat1SimCtgRec'
    elif mstr == '近期协同':
        res = 'nerIcfKnn'

    # 状态
    elif mstr == '完结':
        res = 'cmpStau'
    elif mstr == '连载':
        res = 'noCmpStau'

    # 订阅量级别
    elif mstr == '[0,10)':
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

    # 入库时间划分
    elif mstr == '1月内入库':
        res = 'lesMonIn'
    elif mstr == '1~3月内入库':
        res = 'bt1mto3mIn'
    elif mstr == '3~12月内入库':
        res = 'bt3mto12mIn'
    elif mstr == '12~99月内入库':
        res = 'bt12mto99mIn'

    # 更新时间划分
    elif mstr == '0~1月未更新':
        res = 'lesMonUpd'
    elif mstr == '1~3月未更新':
        res = 'bt1mto3mUpd'
    elif mstr == '3~12月未更新':
        res = 'bt3mto12mUpd'
    elif mstr == '12~99月未更新':
        res = 'bt12mto99mUdp'

    # 一级分类
    elif mstr == '男频':
        res = 'boyCfy1'
    elif mstr == '女频':
        res = 'girlCfy1'
    elif mstr == '包月':
        res = 'monCfy1'
    elif mstr == '出版':
        res = 'pshCfy1'
    elif mstr == '其他':
        res = 'othCfy1'

    return res

def get_fee_number(mstr):
    res = 0;
    if mstr == "免费":
        res = 1
    elif mstr == "付费":
        res = 2
    elif mstr == "包月":
        res = 3
    elif mstr == "公版":
        res = 4
    elif mstr == "限免":
        res = 5
    elif mstr == "全免":
        res = 6

    return res;

def get_strategy_number(mstr):
    res = 0

    # 推荐策略
    if mstr == '实时流':
        res = 1
    elif mstr == '用户协同':
        res = 2
    elif mstr == '冷启动':
        res = 3
    elif mstr == '流行度':
        res = 4
    elif mstr == '物品协同':
        res = 5
    elif mstr == '同分类':
        res = 6
    elif mstr == '订阅模型':
        res = 7
    elif mstr == '阅读模型':
        res = 8
    elif mstr == '内容相似':
        res = 9
    elif mstr == '阅读同分类':
        res = 10
    elif mstr == '一级同分类':
        res = 11
    elif mstr == '0':
        res = 12
    elif mstr == '近期协同':
        res = 13

    return res

def get_module_number(mstr):

    res = 0

    # 推荐模块
    if mstr == '书架推荐':
        res = 1
    elif mstr == '免费-猜你喜欢':
        res = 2
    elif mstr == '章末页-读本书的人还看过':
        res = 3
    elif mstr == '封面页-读本书的人还看过':
        res = 4
    elif mstr == '书架-猜你喜欢':
        res = 5
    elif mstr == '精选-瀑布流':
        res = 6
    elif mstr == '封面页-读本书的人还看过更多':
        res = 7
    elif mstr == '包月瀑布流':
        res = 8
    elif mstr == '封面页-类别推荐':
        res = 9
    elif mstr == '封面页-作者推荐':
        res = 10
    elif mstr == '精选-完结瀑布流':
        res = 11
    elif mstr == '精选-女频瀑布流':
        res = 15
    elif mstr == '免费-包月推荐':
        res = 12
    elif mstr == '精选-男频瀑布流':
        res = 13
    elif mstr == '精选-排行瀑布流':
        res = 14
    elif mstr == '根据阅读推荐':
        res = 16
    elif mstr == '退出拦截推荐':
        res = 17
    elif mstr == '精选-精品必读':
        res = 18
    elif mstr == '精选-热门推荐':
        res = 19
    elif mstr == '免费-免费推荐':
        res = 20
    elif mstr == '精选-根据阅读分类推荐':
        res = 21
    elif mstr == '精选-根据阅读书籍推荐':
        res = 22
    elif mstr == '精选-完结佳作':
        res = 23

    return res

def get_status_number(mstr):
    res = 0

    if mstr == '连载':
        res = 1
    elif mstr == '完结':
        res = 2

    return res

def get_view_number(mstr):

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

    return res

def get_intime_number(mstr):

    res = 0
    if mstr == '1月内入库':
        res = 1
    elif mstr == '1~3月内入库':
        res = 2
    elif mstr == '3~12月内入库':
        res = 3
    elif mstr == '12~99月内入库':
        res = 4

    return res

def get_update_number(mstr):

    res = 0
    if mstr == '0~1月未更新':
        res = 1
    elif mstr == '1~3月未更新':
        res = 2
    elif mstr == '3~12月未更新':
        res = 3
    elif mstr == '12~99月未更新':
        res = 4

    return res

def get_classify1_number(mstr):

    res = 0
    if mstr == '男频':
        res = 1
    elif mstr == '女频':
        res = 2
    elif mstr == '包月':
        res = 3
    elif mstr == '出版':
        res = 4
    elif mstr == '其他':
        res = 5

    return res

# inject mysql
def inject_mysql(txtpath, cursor, times, type):

    fr = open(txtpath, "r")
    sql = ""
    dzid = ""
    shwNum = 0
    clkNum = 0
    subNum = 0
    redNum = 0
    remNum = 0
    clkShwRat = 0.0
    subClkRat = 0.0
    subShwRat = 0.0
    redSubRat = 0.0
    redShwRat = 0.0
    remRat = 0.0
    remShwRat = 0.0

    # 组装好 key
    timeStamp = int(times)

    for line in fr.readlines():
        line = line.strip('\n')
        arr = line.split("\t")
        moduleName = arr[0]
        feeStr = ""
        paraStr = ""

        # 获取数据 -- 总计
        if len(arr) == 13:
            shwNum = int(arr[1])
            clkNum = int(arr[2])
            subNum = int(arr[3])
            redNum = int(arr[4])
            remNum = int(arr[5])
            clkShwRat = float(arr[6][:-1])
            subClkRat = float(arr[7][:-1])
            subShwRat = float(arr[8][:-1])
            redSubRat = float(arr[9][:-1])
            redShwRat = float(arr[10][:-1])
            remRat = float(arr[11][:-1])
            remShwRat = float(arr[12][:-1])
        elif len(arr) == 14:
            feeStr = arr[1]
            shwNum = int(arr[2])
            clkNum = int(arr[3])
            subNum = int(arr[4])
            redNum = int(arr[5])
            remNum = int(arr[6])
            clkShwRat = float(arr[7][:-1])
            subClkRat = float(arr[8][:-1])
            subShwRat = float(arr[9][:-1])
            redSubRat = float(arr[10][:-1])
            redShwRat = float(arr[11][:-1])
            remRat = float(arr[12][:-1])
            remShwRat = float(arr[13][:-1])
        elif len(arr) == 15:
            feeStr = arr[1]
            paraStr = arr[2]
            shwNum = int(arr[3])
            clkNum = int(arr[4])
            subNum = int(arr[5])
            redNum = int(arr[6])
            remNum = int(arr[7])
            clkShwRat = float(arr[8][:-1])
            subClkRat = float(arr[9][:-1])
            subShwRat = float(arr[10][:-1])
            redSubRat = float(arr[11][:-1])
            redShwRat = float(arr[12][:-1])
            remRat = float(arr[13][:-1])
            remShwRat = float(arr[14][:-1])
        else:
            print 'error';

        if type == "summary":
            typeCate = get_module_number(moduleName)
            dzid = trans_to_word(moduleName) + '-' + str(times)
            sql = get_summary_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, typeCate, timeStamp)
        elif type == "fee":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + str(times)
            sql = get_fee_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, typeCate, timeStamp)
        elif type == "strategy":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            strategyCate = get_strategy_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_strategy_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, strategyCate, typeCate, timeStamp)
        elif type == "status":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            statusCate = get_status_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_status_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, statusCate, typeCate, timeStamp)
        elif type == "view":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            viewCate = get_view_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_view_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, viewCate, typeCate, timeStamp)
        elif type == "intime":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            intimeCate = get_intime_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_intime_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, intimeCate, typeCate, timeStamp)
        elif type == "update":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            updateCate = get_update_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_update_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, updateCate, typeCate, timeStamp)
        elif type == "classify1":
            typeCate = get_module_number(moduleName)
            feeCate = get_fee_number(feeStr)
            classify1Cate = get_classify1_number(paraStr)
            dzid = trans_to_word(moduleName) + '-' + trans_to_word(feeStr) + '-' + trans_to_word(paraStr) + '-' + str(times)
            sql = get_classify1_sql(dzid, shwNum, clkNum, subNum, redNum, remNum, clkShwRat, subClkRat, subShwRat, redSubRat, redShwRat, remRat, remShwRat, feeCate, classify1Cate, typeCate, timeStamp)
        execute_sql(cursor, sql)
    fr.close()

    return


if __name__ == '__main__':

    if len(sys.argv) != 13:
        print '请输入数据库用户名和密码以及notime(例:"20180101")'
        exit(-1)
    user = sys.argv[1]
    passwd = sys.argv[2]
    time = sys.argv[3]
    summaryPath = sys.argv[4]
    feePath = sys.argv[5]
    strategyPath = sys.argv[6]
    statusPath = sys.argv[7]
    viewPath = sys.argv[8]
    intimePath = sys.argv[9]
    updatePath = sys.argv[10]
    classify1Path = sys.argv[11]
    classify2Path = sys.argv[12]

    #db = MySQLdb.connect('localhost', user, passwd, 'item_exhibit');
    db = MySQLdb.connect('localhost', user, passwd, 'item_exhibit', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock');
    cursor = db.cursor()                                                                # 获取操作游标

    # 用户+物品维度
    inject_mysql(summaryPath, cursor, time, "summary")
    inject_mysql(feePath, cursor, time, "fee")
    inject_mysql(strategyPath, cursor, time, "strategy")
    inject_mysql(statusPath, cursor, time, "status")
    inject_mysql(viewPath, cursor, time, "view")
    inject_mysql(intimePath, cursor, time, "intime")
    inject_mysql(updatePath, cursor, time, "update")
    inject_mysql(classify1Path, cursor, time, "classify1")
    #inject_mysql(classify2Path, cursor, time, "classify2")

    # 用户维度

    # 用户维度
    db.close()                                                                          # 关闭数据库

