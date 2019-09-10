#!/bin/bash
source ~/.bash_profile
source ~/.bashrc

HADOOP="hdfs://10.26.24.69:8020/"

workDir=$(cd $(dirname $0); pwd)
nowTime=`date -d "-1 day" +%Y%m%d`
yesterday=`date -d "-2 day" +%Y%m%d`

infoTodayPath="${workDir}/data/"
tmpFile="${workDir}/.${nowTime}.txt"
exhibitToday="${HADOOP}/rs/stat/${nowTime}/recsubs/*"

cd ${workDir} && rm -fr data && mkdir data
rm -fr "${workDir}/.${yesterday}.txt"
hadoop fs -get ${exhibitToday} data/

cd ${workDir}/
python inject_exhibit.py "10.26.24.87" "root" "123456" "${tmpFile}" "${infoTodayPath}"









