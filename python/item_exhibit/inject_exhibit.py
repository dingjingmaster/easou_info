#!/bin/env python
#-*- coding: UTF-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import MySQLdb
from function import get_path_time
from function import get_inject_sql
from function import get_update_sql


# inject mysql
def inject_mysql(exhibitPath, today, cursor, db):
    with open(exhibitPath, 'r') as fr:
        timeStamp = int(today)
        for line in fr.readlines():
            line = line.strip('\n')
            arr = line.split('\t')
            if len(arr) != 23:
                print('错误行: ' + line + '\n')
                continue
            msql = get_inject_sql(arr, timeStamp)
            try:
                cursor.execute(msql)
            except:
                pass
            msql = get_update_sql(arr, timeStamp)
            try:
                cursor.execute(msql)
            except:
                pass
    commit_sql(db)
    print('当天数据注入 MySQL 完成！！！')


if __name__ == '__main__':

    if len(sys.argv) != 6:
        print ('请输入数据库用户名和密码以及时间 例:"20180101"')
        exit(-1)
    ip = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]
    historyInjectPath = sys.argv[4]
    exhibitToday = sys.argv[5]

    injectList = []
    historyList = []
    db = MySQLdb.connect(ip, user, passwd, 'item_exhibit', unix_socket='/data/wapage/hhzk/mserver/mysql5713/mysql.sock')
    cursor = db.cursor()

    # 获取历史注入的文件
    if not os.path.isfile(historyInjectPath):
        open(historyInjectPath, 'w')
    with open(historyInjectPath, 'r') as fr:
        for line in fr.readlines():
            line = line.strip()
            historyList.append(line)
            print('已注入的数据：' + line)

    # 获取要注入的文件
    for path in os.listdir(exhibitToday):
        injectList.append(path)

    # 去除历史注入的文件
    for his in historyList:
        if his in injectList:
            injectList.remove(his)
            print(his + ' 文件已经被注入，跳过！')

    # 开始注入MySQL
    for line in injectList:
        time = get_path_time(line)
        if None is time:
            continue
        path = exhibitToday + '/' + line.strip() + '/' + 'part-00000'
        inject_mysql(path, time, cursor, db)
        historyList.append(line)
    db.close()

    # 保存历史记录
    with open(historyInjectPath, 'w') as fw:
        for line in historyList:
            fw.write(line.strip() + '\n')
    exit(0)

