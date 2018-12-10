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

    if len(sys.argv) != 3:
        exit(1)

    lastWeekPath = sys.argv[1]
    thisWeekPath = sys.argv[2]


    lastWeekList = []
    lastWeekDict = {}
    thisWeekList = []
    thisWeekRemain = {}

    # 结果输出
    outFeeRateWeekList = []
    outStatusRateWeekList = []
    outCategoryRateWeekList = []
    outViewcountRateWeekList = []
    outIntimeRateWeekList = []
    outLastupdateRateWeekList = []

    # 输出路径
    outpath_week7 = "./result_week7.txt"

    '''
        按天统计
        1. 获取数据存入链表
        2. 计算得到 昨天数据 + 今天留下的数据 保存在字典中
        3. 按需求统计结果
    '''
    read_data(lastWeekList, lastWeekPath)
    read_data(thisWeekList, thisWeekPath)
    remain_data(lastWeekList, thisWeekList, lastWeekDict, thisWeekRemain)
    del lastWeekList
    del thisWeekList

    fee_rate(lastWeekDict, thisWeekRemain, outFeeRateWeekList)                                                                  # 计算 付费情况留存率
    status_rate(lastWeekDict, thisWeekRemain, outStatusRateWeekList)                                                            # 计算 status 留存率
    category_rate(lastWeekDict, thisWeekRemain, outCategoryRateWeekList)                                                        # 计算 categroy 留存率
    viewcount_rate(lastWeekDict, thisWeekRemain, outViewcountRateWeekList)                                                      # 计算 viewcount 留存率
    intime_rate(lastWeekDict, thisWeekRemain, outIntimeRateWeekList)                                                            # 计算 intime 留存率
    lastUpdate_rate(lastWeekDict, thisWeekRemain, outLastupdateRateWeekList)                                                    # 计算 last update time 留存率

    # 输出 flag = 1 表示清除文件后写入
    trans_to_string(outFeeRateWeekList, outpath_week7, "(周)", 1)
    trans_to_string(outStatusRateWeekList, outpath_week7, "(周)")
    trans_to_string(outViewcountRateWeekList, outpath_week7, "(周)")
    trans_to_string(outIntimeRateWeekList, outpath_week7, "(周)")
    trans_to_string(outLastupdateRateWeekList, outpath_week7, "(周)")
    trans_to_string(outCategoryRateWeekList, outpath_week7, "(周)")


    exit(0)

