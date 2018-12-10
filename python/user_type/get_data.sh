#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTimeStr=`date -d "-1 day" +%Y-%m-%d`
nowTime=`date -d "-1 day" +%Y%m%d`

###################     参数定义      ###########################
userType="hdfs://10.26.26.145:8020/rs/dingjing/user_type/thisday_utype/${nowTimeStr}"
localUserType="data/user_type.txt"

###################     开始执行      ###########################
# 拉取数据
cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${userType}/*" > ${localUserType}

# 留存率结果统计
cd ${workDir}/
python inject_user_type.py "root" "123456" "${nowTime}" "${localUserType}"













