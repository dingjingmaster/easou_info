#!/usr/bin/env python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time

'''
    flag = 1 近一个月
    flag = 2 近一季度
    flag = 3 近一年
    flag = 4 一年以上
'''
def time_if_in(itemTime, timeStart, timeEnd):

    if int(itemTime) >= int(timeStart) and int(itemTime) <= int(timeEnd):
        return True

    return False

# 获取时间间断
def get_time(year, month, day):

    nowTime = time.time()

    # 一个月之后的时间戳
    lastMonth = nowTime - 86400 * 30
    last3Month = nowTime - 86400 * 30 * 3
    lastYear = nowTime - 86400 * 366

    inMonth = "l1m"
    in3Month = "bt1mt3m"
    inyear = "bt3mt1y"
    outYear = "gt1y"
    isZero = "notime"

    # 直接把 0 返回
    if int(year) == 0:
        return isZero

    itemTime = time.mktime(time.strptime(str(year) + "-" + str(month) + "-" + str(day), "%Y-%m-%d"))

    # 一个月之内
    if time_if_in(itemTime, lastMonth, nowTime):
        return inMonth

    # 判断是否在一月 到 三个月
    if time_if_in(itemTime, last3Month, lastMonth):
        return in3Month

    # 三月 到 一年
    if time_if_in(itemTime, lastYear, last3Month):
        return inyear

    return outYear

'''
    读取处理的数据
'''
def read_data(list, path):

    fRead = open(path, "r")

    for i in fRead.readlines():
        i = i.strip("\n")
        list.append(i)

    fRead.close()

    return fRead

'''
    获取 上一时间段数据 详情
    获取 这一时间段留下的数据 详情
    最后统一计算
'''
# appudid 字符串组合
def appudid_string(appudid, curChap, cate1, cate2, cate3, viewCount, status, freeFlag, intimeStamp, lastUpdateStamp, createTimeStamp, tf, outlist):
    outlist.append((appudid, curChap, cate1, cate2, cate3, viewCount, status, freeFlag, intimeStamp, lastUpdateStamp, createTimeStamp, tf))
    return outlist

# 计算留存率
def calcu_retention_rate(lastD, thisD, resList):

    for i in thisD.keys():
        if lastD.has_key(i) and thisD.has_key(i):
            res = float(float(thisD[i]) / float(lastD[i])) * 100
            resList.append((i, lastD[i], thisD[i], res))

    return resList

'''
    上一阶段的数据 和 这一阶段留下的数据
'''
def remain_data(lastlist, thislist, lastDict, remainDict):

    # 获取 lastday 的 udid 及其阅读章节数
    for i in lastlist:                                                                                                                          # 上次信息解析
        arr1 = i.split("\t")
        gid = arr1[0]
        itemInfoStr = arr1[1]
        itemArr = itemInfoStr.split("{]")

        cate1 = itemArr[0]
        cate2 = itemArr[1]
        cate3 = itemArr[2]
        viewCount = itemArr[3]
        status = itemArr[4]
        freeFlag = itemArr[5]
        intimeStamp = itemArr[6]
        lastUpdateStamp = itemArr[7]
        createTimeStamp = itemArr[8]
        tf = itemArr[9]
        cpid = itemArr[10]
        by = itemArr[11]
        fc = itemArr[12]

        # cate1, cate2, cate3, viewcount, status, freeflag, intimestamp, lastupdatestamp, createdatestamp, tf, cpid, by 
        itemInfo = (cate1, cate2, cate3, viewCount, status, freeFlag, intimeStamp, lastUpdateStamp, createTimeStamp, tf, cpid, by, fc)          # 物品信息

        udidNum = len(arr1) - 2
        lastDict[gid] = (itemInfo, udidNum)

    # 获取 thisday 留下来的 udid 针对每个 gid
    for i in thislist:
        arr1 = i.split("\t")
        gid = arr1[0]                                                                                                                           # 获取 gid
        itemInfoStr = arr1[1]
        itemArr = itemInfoStr.split("{]")

        cate1 = itemArr[0]
        cate2 = itemArr[1]
        cate3 = itemArr[2]
        viewCount = itemArr[3]
        status = itemArr[4]
        freeFlag = itemArr[5]
        intimeStamp = itemArr[6]
        lastUpdateStamp = itemArr[7]
        createTimeStamp = itemArr[8]
        tf = itemArr[9]
        cpid = itemArr[10]
        by = itemArr[11]
        fc = itemArr[12]

        itemInfo = (cate1, cate2, cate3, viewCount, status, freeFlag, intimeStamp, lastUpdateStamp, createTimeStamp, tf, cpid, by, fc)                    # 物品信息

        udidNum = len(arr1) - 2
        remainDict[gid] = (itemInfo, udidNum)


    return (lastDict, remainDict)

'''
    付费请概况留存率
'''
def fee_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        fee = 0, 1, 2, 10
    '''
    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum= i[1]

        key = ""
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if int(freeFlag) == 0 or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif int(by) == 1:
            freeFlag = "month"
        elif int(freeFlag) == 1:
            freeFlag = "charge"
        elif int(freeFlag) == 10:
            freeFlag = "pub"

        key = "fee" + "|" + str(freeFlag)
        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum= i[1]

        key = ""
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if int(freeFlag) == 0 or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif int(by) == 1:
            freeFlag = "month"
        elif int(freeFlag) == 1:
            freeFlag = "charge"
        elif int(freeFlag) == 10:
            freeFlag = "pub"

        key = "fee" + "|" + str(freeFlag)
        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList

'''
    计算 status 留存率
'''
def status_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        status = 2 或者 status = 1
        fee = 0, 1, 2, 10
    '''
    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        status = itemInfo[4]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"
        if status == "2":
            status = "accomplish"
        else:
            status = "publish"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        key = "status" + "|" + str(freeFlag) + "|" + str(status)
        if lastD.has_key(key):
            lastD[key] = int(lastD[key]) + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        status = itemInfo[4]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if status == "2":
            status = "accomplish"
        else:
            status = "publish"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        key = "status" + "|" + str(freeFlag) + "|" + str(status)
        if thisD.has_key(key):
            thisD[key] = int(thisD[key]) + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList


# 计算分类留存率
def category_rate(lastDayDict, thisDayRemain, outRateDayList):

    '''
        category cate1, cate2, cate3 每级分类下还有子分类
        fee = 0, 1, 2, 10
    '''
    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum= i[1]

        key = ""
        cate1 = itemInfo[0]
        cate2 = itemInfo[1]
        cate3 = itemInfo[2]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "0":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        # 一级分类
        key = "cate" + "|" + "1" + "|" + str(freeFlag) + "|" + cate1
        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

        # 二级分类
        key = "cate" + "|" + "2" + "|" + str(freeFlag) + "|" + cate2
        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

        # 三级分类
        key = "cate" + "|" + "3" + "|" + str(freeFlag) + "|" + cate3
        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        cate1 = itemInfo[0]
        cate2 = itemInfo[1]
        cate3 = itemInfo[2]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) != 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        # 一级分类
        key = "cate" + "|" + "1" + "|" + str(freeFlag) + "|" + cate1
        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

        # 二级分类
        key = "cate" + "|" + "2" + "|" + str(freeFlag) + "|" + cate2
        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

        # 三级分类
        key = "cate" + "|" + "3" + "|" + str(freeFlag) + "|" + cate3
        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateDayList)

    return outRateDayList

#
def viewcount_rate(lastDayDict, thisDayRemain, outRateDayList):

    '''
        viewCount 分段 0 - 100, 100 - 1000, 1000 - 10000, 大于10000
        fee = 0, 1, 2, 10
    '''
    # 上段时间参数
    lastD = {}
    thisD = {}

    b0to100 =       "bt0to1b"
    b100to1000 =    "bt1bto1k"
    b1000to10000 =  "bt1kto1w"
    b10000to100000 ="bt1wto10w"
    g100000 =       "gt10w"

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]
        key = ""

        viewCount = int(itemInfo[3])
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        # 0 - 100
        if viewCount >=0 and viewCount < 100:
            key = "view" + "|" + freeFlag + "|" + str(b0to100)
        elif viewCount >= 100 and viewCount < 1000:
            key = "view" + "|" + freeFlag + "|" + str(b100to1000)
        elif viewCount >= 1000 and viewCount < 10000:
            key = "view" + "|" + freeFlag + "|" + str(b1000to10000)
        elif viewCount >= 10000 and viewCount < 100000:
            key = "view" + "|" + freeFlag + "|" + str(b10000to100000)
        elif viewCount >= 100000:
            key = "view" + "|" + freeFlag + "|" + str(g100000)
        else:
            continue

        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        viewCount = int(itemInfo[3])
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "2":
            freeFlag = "month"
        elif freeFlag == "10":
            freeFlag = "pub"

        # 0 - 100
        if viewCount >=0 and viewCount < 100:
            key = "view" + "|" + freeFlag + "|" + str(b0to100)
        elif viewCount >= 100 and viewCount < 1000:
            key = "view" + "|" + freeFlag + "|" + str(b100to1000)
        elif viewCount >= 1000 and viewCount < 10000:
            key = "view" + "|" + freeFlag + "|" + str(b1000to10000)
        elif viewCount >= 10000 and viewCount < 100000:
            key = "view" + "|" + freeFlag + "|" + str(b10000to100000)
        elif viewCount >= 100000:
            key = "view" + "|" + freeFlag + "|" + str(g100000)
        else:
            continue

        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateDayList)

    return outRateDayList

# 计算入库时间留存率
def intime_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        入库时间 按月统计, 没有时间另计 notime
        fee = 0, 1, 2, 10
    '''
    year = 0
    month = 0
    day = 0

    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        timeStr = ""
        intime = itemInfo[6]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        year = 0
        month = 0
        day = 0
        if intime != "0" and intime != "":
            year = int(time.strftime("%Y", time.localtime(float(intime))))
            month = int(time.strftime("%m", time.localtime(float(intime))))
            day = int(time.strftime("%d", time.localtime(float(intime))))

        timeStr = get_time(year, month, day)
        key = "intime" + "|" + freeFlag + "|" + str(timeStr)

        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]
        key = ""

        timeStr = ""
        intime = itemInfo[6]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        year = 0
        month = 0
        day = 0
        if intime != "0" and intime != "":
            year = int(time.strftime("%Y", time.localtime(float(intime))))
            month = int(time.strftime("%m", time.localtime(float(intime))))
            day = int(time.strftime("%d", time.localtime(float(intime))))

        timeStr = get_time(year, month, day)
        key = "intime" + "|" + freeFlag + "|" + str(timeStr)

        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList

# 计算最后更新时间留存率
def lastUpdate_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        最后更新时间 一个月、一个季度、近一年、其它
        fee = 0, 1, 2, 10
    '''
    year = 0
    month = 0
    day = 0

    timeStr = ""

    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        timeStr = ""
        lastUpdate = itemInfo[7]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        year = 0
        month = 0
        day = 0
        if lastUpdate != "0" and lastUpdate != "":
            year = int(time.strftime("%Y", time.localtime(float(lastUpdate))))
            month = int(time.strftime("%m", time.localtime(float(lastUpdate))))
            day = int(time.strftime("%d", time.localtime(float(lastUpdate))))

        timeStr = get_time(year, month, day)
        key = "updatetime" + "|" + freeFlag + "|" + str(timeStr)

        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]

        key = ""
        timeStr = ""
        lastUpdate = itemInfo[7]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "free"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "allFee"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "limitfree"
        elif by == "1":
            freeFlag = "month"
        elif freeFlag == "1":
            freeFlag = "charge"
        elif freeFlag == "10":
            freeFlag = "pub"

        year = 0
        month = 0
        day = 0
        if lastUpdate != "0" and lastUpdate != "":
            year = int(time.strftime("%Y", time.localtime(float(lastUpdate))))
            month = int(time.strftime("%m", time.localtime(float(lastUpdate))))
            day = int(time.strftime("%d", time.localtime(float(lastUpdate))))

        timeStr = get_time(year, month, day)
        key = "updatetime" + "|" + freeFlag + "|" + str(timeStr)

        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList

# 计算创建时间留存率
def createtime_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        创建时间 一个月、一个季度、近一年、其它
        fee = 0, 1, 2, 10
    '''
    year = 0
    month = 0
    day = 0

    timeStr = ""

    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum= i[1]
        key = ""
        timeStr = ""
        createtime  = itemInfo[8]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "免费书"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "全免"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "限免书"
        elif by == "1":
            freeFlag = "包月书"
        elif freeFlag == "1":
            freeFlag = "付费书"
        elif freeFlag == "10":
            freeFlag = "公版书"

        year = 0
        month = 0
        day = 0
        if createtime != "0" and createtime != "":
            year = int(time.strftime("%Y", time.localtime(float(createtime))))
            month = int(time.strftime("%m", time.localtime(float(createtime))))
            day = int(time.strftime("%d", time.localtime(float(createtime))))

        timeStr = get_time(year, month, day)
        key = "createtime" + "|" + freeFlag + "|" + str(timeStr)

        if lastD.has_key(key):
            lastD[key] = lastD[key] + int(udidNum)
        else:
            lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, udidList = i
        itemInfo, udidNum= i[1]
        key = ""
        timeStr = ""
        createtime = itemInfo[8]
        freeFlag = itemInfo[5]
        tf = itemInfo[9]
        by = itemInfo[11]
        fc = itemInfo[12]
        if tf == "":
            tf = "0"
        if by == "":
            by = "0"

        if freeFlag == "0" or freeFlag == "":
            freeFlag = "免费书"
        elif int(fc) > 0 and int(freeFlag) > 0:
            freeFlag = "全免"
        elif int(tf) > 0 and int(freeFlag) > 0:
            freeFlag = "限免书"
        elif by == "1":
            freeFlag = "包月书"
        elif freeFlag == "1":
            freeFlag = "付费书"
        elif freeFlag == "10":
            freeFlag = "公版书"

        year = 0
        month = 0
        day = 0
        if createtime != "0" and createtime != "":
            year = int(time.strftime("%Y", time.localtime(float(createtime))))
            month = int(time.strftime("%m", time.localtime(float(createtime))))
            day = int(time.strftime("%d", time.localtime(float(createtime))))

        timeStr = get_time(year, month, day)
        key = "createtime" + "|" + freeFlag + "|" + str(timeStr)

        if thisD.has_key(key):
            thisD[key] = thisD[key] + int(udidNum)
        else:
            thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList


# 计算包月限免书的留存率(仅按天计算)
def monthly_limit_free_rate(lastDayDict, thisDayRemain, outRateList):

    '''
        包月限免 第一批 第二批 第三批 第四批
        fee = 0, 1, 2, 10 (免费书、付费、包月、公版)
    '''

    # 上段时间参数
    lastD = {}
    thisD = {}

    # 上段时间整理
    for i in lastDayDict.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]
        key = ""
        flag = ""                                                                                             # 是否是包月书
        tf = itemInfo[9]                                                                                         # 包月限免
        freeFlag = itemInfo[5]
        if tf == "":
            tf = "0"

        freeFlag = ""

        #
        if tf == "1":
            key = "tf" + "|" + freeFlag + "|" + "1"
            flag = "ok"
        elif tf == "2":
            key = "tf" + "|" + freeFlag + "|" + "2"
            flag = "ok"
        elif tf == "3":
            key = "tf" + "|" + freeFlag + "|" + "3"
            flag = "ok"
        elif tf == "4":
            key = "tf" + "|" + freeFlag + "|" + "4"
            flag = "ok"

        if flag == "ok":
            if lastD.has_key(key):
                lastD[key] = lastD[key] + int(udidNum)
            else:
                lastD[key] = int(udidNum)

    # 这段时间整理
    for i in thisDayRemain.items():
        gid, allInfo = i
        itemInfo, udidNum = i[1]
        key = ""
        flag = ""
        tf = itemInfo[9]
        freeFlag = itemInfo[5]
        if tf == "":
            tf = "0"

        freeFlag = ""
        #
        if tf == "1":
            key = "tf" + "|" + freeFlag + "|" + "1"
            flag = "ok"
        elif tf == "2":
            key = "tf" + "|" + freeFlag + "|" + "2"
            flag = "ok"
        elif tf == "3":
            key = "tf" + "|" + freeFlag + "|" + "3"
            flag = "ok"
        elif tf == "4":
            key = "tf" + "|" + freeFlag + "|" + "4"
            flag = "ok"

        if flag == "ok":
            if thisD.has_key(key):
                thisD[key] = thisD[key] + int(udidNum)
            else:
                thisD[key] = int(udidNum)

    # 计算留存率
    calcu_retention_rate(lastD, thisD, outRateList)

    return outRateList


'''
    输出 最后结果
'''
def print_format(outBuf, title, outList):

    #outBuf = outBuf + '<tr align="center"><th align="center">分类</th><th align="center">上一时间段用户数</th><th align="center">剩下用户数</th><th align="center">留存率</th>'
    outBuf = ""
    for i in outList:
        res1 = i[0]
        res2 = i[1]
        res3 = i[2]
        res4 = float(i[3])
        outBuf = outBuf + str(res1) + "\t" + str(res2) + "\t" + str(res3) + "\t" + str(res4) + "\n"
    return outBuf

'''
    分好的标签内进行排序
'''
def list_sort(outList):

    filter = {}
    dictList = {}

    if len(outList) == 0:
        return outList

    # 先遍历一遍，找到 第一分类的数量
    for i in outList:
        key = i[0]
        arr = key.split("-")
        c = arr[0].strip()
        filter[c] = 0

    for i in filter.keys():
        value = []
        for j in outList:
            if i in j[0]:
                value.append((j[0], j[1], j[2], j[3]))
        dictList[i] = value

    del outList[:]

    # 排序 并输出 到 outList
    for i in filter:
        lis = dictList[i]
        lis.sort(key = lambda x: x[3], reverse = True)

        for j in lis:
            outList.append(j)
    return outList

# 字符串输出结果 flag = 1 表示是清除文件后写入
def trans_to_string(inList, outPath, title, flag = 0):

    fS = ""
    fV = ""
    fC = ""
    fI = ""
    fU = ""
    fM = ""
    outBuf = ""
    outList0 = []
    outList1 = []
    outList2 = []
    outList3 = []
    title = ""

    if len(inList) <= 0:
        print "输入链表为空"
        return

    temp = inList[0]
    key = temp[0]
    arr = key.split("|")

    if flag == 0:
        fW = open(outPath, "a")
    else:
        fW = open(outPath, "w")

    # 如果非分类
    if len(arr) == 2:
        #title = "总体付费情况结果统计" + title
        for i in inList:
            arr = i[0].split("|")
            outList0.append((arr[0] + "-" + arr[1], i[1], i[2], i[3]))
    elif len(arr) == 3:
        for i in inList:
            arr = i[0].split("|")
            if arr[0] == "status" and fS == "":
                title = "连载/完结 留存率结果统计" + title
                fS = "ok"
            elif arr[0] == "view" and fV == "":
                title = "订阅量分段 留存率结果统计" + title
                fV = "ok"
            elif arr[0] == "intime"and fI == "":
                title = "入库时间 留存率结果统计" + title
                fI = "ok"
            elif arr[0] == "updatetime" and fU == "":
                title = "最后更新时间 留存率结果统计" + title
                fU = "ok"
            elif arr[0] == "createtime" and fC == "":
                title = "创建时间 留存率结果统计" + title
                fC = "ok"
            elif arr[0] == "tf" and fM == "":
                title = "限免书籍 留存率结果统计" + title
                fM = "ok"
            outList1.append((arr[0] + "-" + arr[1] + "-" + arr[2], i[1], i[2], i[3]))
    else:
        title = "分类结果统计" + title
        for i in inList:
            arr = i[0].split("|")
            cate = arr[1]
            if cate == "1":
                if arr[3] != "男频" and arr[3] != "女频" and arr[3] != "出版" and arr[3] != "其他":
                    continue
                outList1.append(("cate1" + "-" + arr[2] + "-" + arr[3], i[1], i[2], i[3]))
            elif cate == "2":
                continue
                #outList2.append((arr[2] + " - " + arr[3], i[1], i[2], i[3]))
            elif cate == "3":
                continue
                #outList3.append((arr[2] + " - " + arr[3], i[1], i[2], i[3]))

    if len(outList0) != 0:
        outList0.sort(key = lambda x: x[3], reverse = True)
    outList1 = list_sort(outList1)
    outList2 = list_sort(outList2)
    outList3 = list_sort(outList3)

    # 输出
    if len(outList0) != 0 and len(outList1) == 0:
        outBuf = print_format(outBuf, "", outList0)
    elif len(outList0) == 0 and len(outList3) != 0:
        outBuf = print_format(outBuf, "" + "cat1", outList1)
        outBuf = print_format(outBuf, "" + "cat2", outList2)
        outBuf = print_format(outBuf, "" + "cat3", outList3)
    else:
        outBuf = print_format(outBuf, "", outList1)
    fW.write(outBuf)
    fW.close()

    return
