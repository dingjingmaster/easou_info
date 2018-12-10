#!/usr/bin/env python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from retention_result import read_data
from retention_result import remain_data
from retention_result import fee_rate
from retention_result import status_rate
from retention_result import category_rate
from retention_result import viewcount_rate
from retention_result import createtime_rate
from retention_result import intime_rate
from retention_result import lastUpdate_rate
from retention_result import monthly_limit_free_rate
from retention_result import trans_to_string


if __name__ == '__main__':

    if len(sys.argv) != 5:
        exit(1)

    lastDayPath = sys.argv[1]
    thisDayPath = sys.argv[2]
    lastWeekPath = sys.argv[3]
    thisWeekPath = sys.argv[4]

    lastDayList = []
    lastDayDict = {}
    thisDayList = []
    thisDayRemain = {}

    lastWeekList = []
    lastWeekDict = {}
    thisWeekList = []
    thisWeekRemain = {}

    # 结果输出
    outFeeRateDayList = []
    outStatusRateDayList = []
    outCategoryRateDayList = []
    outViewcountRateDayList = []
    outIntimeRateDayList = []
    outLastupdateRateDayList = []
    outMonthlyLimitFreeDayList = []

    outFeeRateWeekList = []
    outStatusRateWeekList = []
    outCategoryRateWeekList = []
    outViewcountRateWeekList = []
    outIntimeRateWeekList = []
    outLastupdateRateWeekList = []

    # 输出路径
    outpath_day = "./result_day.txt"
    outpath_week = "./result_week.txt"

    '''
        按天统计
        1. 获取数据存入链表
        2. 计算得到 昨天数据 + 今天留下的数据 保存在字典中
        3. 按需求统计结果
    '''
    read_data(lastDayList, lastDayPath)
    read_data(thisDayList, thisDayPath)
    remain_data(lastDayList, thisDayList, lastDayDict, thisDayRemain)
    del lastDayList
    del thisDayList

    read_data(lastWeekList, lastWeekPath)
    read_data(thisWeekList, thisWeekPath)
    remain_data(lastWeekList, thisWeekList, lastWeekDict, thisWeekRemain)
    del lastWeekList
    del thisWeekList

    # 按天计算 包月限免 留存率
    monthly_limit_free_rate(lastDayDict, thisDayRemain, outMonthlyLimitFreeDayList)

    # 计算 付费情况留存率
    fee_rate(lastDayDict, thisDayRemain, outFeeRateDayList)
    fee_rate(lastWeekDict, thisWeekRemain, outFeeRateWeekList)

    # 计算 status 留存率
    status_rate(lastDayDict, thisDayRemain, outStatusRateDayList)
    status_rate(lastWeekDict, thisWeekRemain, outStatusRateWeekList)

    # 计算 categroy 留存率
    category_rate(lastDayDict, thisDayRemain, outCategoryRateDayList)
    category_rate(lastWeekDict, thisWeekRemain, outCategoryRateWeekList)

    # 计算 viewcount 留存率
    viewcount_rate(lastDayDict, thisDayRemain, outViewcountRateDayList)
    viewcount_rate(lastWeekDict, thisWeekRemain, outViewcountRateWeekList)

    # 计算 intime 留存率
    intime_rate(lastDayDict, thisDayRemain, outIntimeRateDayList)
    intime_rate(lastWeekDict, thisWeekRemain, outIntimeRateWeekList)

    # 计算 last update time 留存率
    lastUpdate_rate(lastDayDict, thisDayRemain, outLastupdateRateDayList)
    lastUpdate_rate(lastWeekDict, thisWeekRemain, outLastupdateRateWeekList)

    # 输出 flag = 1 表示清除文件后写入
    trans_to_string(outMonthlyLimitFreeDayList, outpath_day, "(仅有天)", 1)

    trans_to_string(outFeeRateDayList, outpath_day, "(天)")
    trans_to_string(outFeeRateWeekList, outpath_week, "(周)", 1)

    trans_to_string(outStatusRateDayList, outpath_day, "(天)")
    trans_to_string(outStatusRateWeekList, outpath_week, "(周)")

    trans_to_string(outViewcountRateDayList, outpath_day, "(天)")
    trans_to_string(outViewcountRateWeekList, outpath_week, "(周)")

    trans_to_string(outIntimeRateDayList, outpath_day, "(天)")
    trans_to_string(outIntimeRateWeekList, outpath_week, "(周)")

    trans_to_string(outLastupdateRateDayList, outpath_day, "(天)")
    trans_to_string(outLastupdateRateWeekList, outpath_week, "(周)")

    trans_to_string(outCategoryRateDayList, outpath_day, "(天)")
    trans_to_string(outCategoryRateWeekList, outpath_week, "(周)")

    exit(0)

