#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTime=`date -d "-2 day" +%Y%m%d`
thisDay=`date -d "-2 day" +%Y-%m-%d`
lastDay=`date -d "-3 day" +%Y-%m-%d`

###################     参数定义      ###########################
#hadLogBase="hdfs://10.26.24.165:9090/rs/appsinfo/data/user_retention_rate"
hadLogBase="hdfs://10.26.26.145:8020/rs/appsinfo/data/user_retention_rate"


# 天数据
thisDayLog="data/day_${thisDay}"
lastDayLog="data/day_${lastDay}"

# 周数据
thisWeekLog="data/week_${thisDay}"
lastWeekLog="data/week_${lastDay}"

# 7日留存数据
thisWeek7Log="data/week7_${thisDay}"
lastWeek7Log="data/week7_${lastDay}"

###################     开始执行      ###########################
# 拉取数据
cd ${workDir} && rm -fr data && rm -fr ./*.txt && mkdir data
hadoop fs -cat "${hadLogBase}/${thisDay}/day/last/*" > ${lastDayLog}
hadoop fs -cat "${hadLogBase}/${thisDay}/day/remain/*" > ${thisDayLog}
hadoop fs -cat "${hadLogBase}/${thisDay}/week/last/*" > ${lastWeekLog}
hadoop fs -cat "${hadLogBase}/${thisDay}/week/remain/*" > ${thisWeekLog}
hadoop fs -cat "${hadLogBase}/${thisDay}/week/last_1_7/*" > ${lastWeek7Log}
hadoop fs -cat "${hadLogBase}/${thisDay}/week/remain_1_7/*" > ${thisWeek7Log}

# 留存率结果统计
cd ${workDir}/
python get_data/res_main_all.py ${lastDayLog} ${thisDayLog} ${lastWeekLog} ${thisWeekLog} 
python get_data/res_main_week7.py ${lastWeek7Log} ${thisWeek7Log} 
python inject_retention.py "root" "123456" "${nowTime}" "result_day.txt" "result_week.txt" "result_week7.txt"













