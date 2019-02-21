#!/bin/env python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb

#
def item_filter (arr):
    if len(arr) < 91:
        return False
    if '' == arr[2] or '' == arr[8]:
        return False
    if 'i_' != arr[0][:2]:
        return False
    if '-' == arr[0][2]:
        return False
    return True

def update_gid_sql (arr, tim):
    gid = arr[0]
    name = ''
    author = ''
    normName = ''
    normAuthor = ''
    normSeries = ''
    rank = 0.0
    tag1 = ''
    tag2 = ''
    viewCount = 0
    status = 0
    feeFlag = ''
    ncp = ''
    intimeStamp = 0
    chapterUptime = 0
    makeLevel = ''
    by = ''
    tf = ''
    rnd = 0
    rtd = 0.0
    rnw = 0
    rtw = 0.0

    for i in range(1, len(arr)):
        if arr[i] == 'name':
            name = arr[i + 1]
        elif arr[i] == 'author':
            author = arr[i + 1]
        elif arr[i] == 'norm_name':
            normName = arr[i + 1]
        elif arr[i] == 'norm_author':
            normAuthor = arr[i + 1]
        elif arr[i] == 'norm_series':
            normSeries = arr[i + 1]
        elif arr[i] == 'rank':
            try:
                rank = double(arr[i + 1])
            except Exception, e:
                rank = 0.0
        elif arr[i] == 'tag1':
            tag1 = arr[i + 1]
        elif arr[i] == 'tag2':
            tag2 = arr[i + 1]
        elif arr[i] == 'view_count':
            try:
                viewCount = int(arr[i + 1])
            except Exception, e:
                viewCount = 0
        elif arr[i] == 'status':
            try:
                status = int(arr[i + 1])
            except Exception, e:
                status = 0
        elif arr[i] == 'fee_flag':
            feeFlag = arr[i + 1]
        elif arr[i] == 'ncp':
            ncp = arr[i + 1]
        elif arr[i] == 'intime_stamp':
            try:
                intimeStamp = int(arr[i + 1])
            except Exception, e:
                intimeStamp = 0
        elif arr[i] == 'chapter_uptime':
            try:
                chapterUptime = int(arr[i + 1])
            except Exception, e:
                chapterUptime = 0
        elif arr[i] == 'mask_level':
            makeLevel = arr[i + 1]
        elif arr[i] == 'by':
            by = arr[i + 1]
        elif arr[i] == 'tf':
            tf = arr[i + 1]
        elif arr[i] == 'rn_d':
            try:
                rnd = int(arr[i + 1])
            except Exception, e:
                rnd = 0
        elif arr[i] == 'rt_d':
            try:
                rtd = double(arr[i + 1])
            except Exception, e:
                rtd = 0
        elif arr[i] == 'rn_w':
            try:
                rnw = int(arr[i + 1])
            except Exception, e:
                rnw = 0
        elif arr[i] == 'rt_w':
            try:
                rtw = double(arr[i + 1])
            except Exception, e:
                rtw = 0
    msql = "INSERT INTO item_info (gid, name, author," \
          "norm_name, norm_author, norm_series, rank, tag1, tag2," \
          "view_count, status, fee_flag, ncp, intime_stame, chapter_uptime, " \
          "mask_level, by, tf, rn_d, rt_d, rn_w, rt_w, update_time) VALUES " \
          "('%s', '%s', '%s', '%s', '%s', '%s'," \
          "'%f', '%s', '%s', '%d', '%d'," \
          "'%s', '%s', '%d', '%d', '%s', '%s', '%s'," \
          "'%d', '%f', '%d', '%f', '%s');" % \
          (gid, name, author, normName, normAuthor, normSeries, rank, tag1, tag2,
           viewCount, status, feeFlag, ncp, intimeStamp, chapterUptime,
           makeLevel, by, tf, rnd, rtd, rnw, rtw, tim)
    return msql

def insert_gid_sql (arr, tim):
    gid = arr[0]
    name = ''
    author = ''
    normName = ''
    normAuthor = ''
    normSeries = ''
    rank = 0.0
    tag1 = ''
    tag2 = ''
    viewCount = 0
    status = 0
    feeFlag = ''
    ncp = ''
    intimeStamp = 0
    chapterUptime = 0
    makeLevel = ''
    by = ''
    tf = ''
    rnd = 0
    rtd = 0.0
    rnw = 0
    rtw = 0.0

    for i in range(1, len(arr)):
        if arr[i] == 'name':
            name = arr[i + 1]
        elif arr[i] == 'author':
            author = arr[i + 1]
        elif arr[i] == 'norm_name':
            normName = arr[i + 1]
        elif arr[i] == 'norm_author':
            normAuthor = arr[i + 1]
        elif arr[i] == 'norm_series':
            normSeries = arr[i + 1]
        elif arr[i] == 'rank':
            try:
                rank = double(arr[i + 1])
            except Exception, e:
                rank = 0.0
        elif arr[i] == 'tag1':
            tag1 = arr[i + 1]
        elif arr[i] == 'tag2':
            tag2 = arr[i + 1]
        elif arr[i] == 'view_count':
            try:
                viewCount = int(arr[i + 1])
            except Exception, e:
                viewCount = 0
        elif arr[i] == 'status':
            try:
                status = int(arr[i + 1])
            except Exception, e:
                status = 0
        elif arr[i] == 'fee_flag':
            feeFlag = arr[i + 1]
        elif arr[i] == 'ncp':
            ncp = arr[i + 1]
        elif arr[i] == 'intime_stamp':
            try:
                intimeStamp = int(arr[i + 1])
            except Exception, e:
                intimeStamp = 0
        elif arr[i] == 'chapter_uptime':
            try:
                chapterUptime = int(arr[i + 1])
            except Exception, e:
                chapterUptime = 0
        elif arr[i] == 'mask_level':
            makeLevel = arr[i + 1]
        elif arr[i] == 'by':
            by = arr[i + 1]
        elif arr[i] == 'tf':
            tf = arr[i + 1]
        elif arr[i] == 'rn_d':
            try:
                rnd = int(arr[i + 1])
            except Exception, e:
                rnd = 0
        elif arr[i] == 'rt_d':
            try:
                rtd = double(arr[i + 1])
            except Exception, e:
                rtd = 0
        elif arr[i] == 'rn_w':
            try:
                rnw = int(arr[i + 1])
            except Exception, e:
                rnw = 0
        elif arr[i] == 'rt_w':
            try:
                rtw = double(arr[i + 1])
            except Exception, e:
                rtw = 0

    msql = "UPDATE item_info SET name = '%s', author = '%s'," \
           "norm_name = '%s', norm_author = '%s', norm_series = '%s', rank = '%f', tag1 = '%s', tag2 = '%s'," \
           "view_count = '%d', status = '%d', fee_flag = '%s', ncp = '%s', intime_stame = '%d', chapter_uptime = '%d', " \
           "mask_level = '%s', by = '%s', tf = '%s', rn_d = '%d', rt_d = '%f', rn_w = '%d', rt_w = '%f', update_time = '%s' WHERE gid = %s;" % \
           (name, author, normName, normAuthor, normSeries, rank, tag1, tag2,
            viewCount, status, feeFlag, ncp, intimeStamp, chapterUptime,
            makeLevel, by, tf, rnd, rtd, rnw, rtw, tim, gid)
    return msql

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('缺少需要的输入参数')
        exit(-1)
    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    itemInfo = sys.argv[4]
    updateTime = sys.argv[5]

    db = MySQLdb.connect(ip, user, passwd, 'item_info', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock')
    cursor = db.cursor()
    with open(itemInfo, 'r') as fr:
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if not item_filter(arr):
                continue
            msql1 = insert_gid_sql(arr, updateTime)
            msql2 = update_gid_sql(arr, updateTime)
            try:
                cursor.execute(msql1)
                cursor.execute(msql2)
                db.commit()
            except Exception, e:
                pass
    db.close()