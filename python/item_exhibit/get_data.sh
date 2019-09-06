#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTime=`date -d "-1 day" +%Y%m%d`
yesterday=`date -d "-2 day" +%Y%m%d`

HADOOP="hdfs://10.26.26.145:8020/"

exhibitToday="${HADOOP}/rs/stat/${nowTime}/recsubs/useritem/"
exhibitYesterday="${HADOOP}/rs/stat/${yesterday}/recsubs/useritem2/"
infoToday="data/exhibit_info_today.txt"
infoYesterday="data/exhibit_info_yesterday.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${exhibitToday}/*" > ${infoToday}
hadoop fs -cat "${exhibitYesterday}/*" > ${infoYesterday}

cd ${workDir}/
python inject_exhibit.py "127.0.0.1" "root" "123456" "${nowTime}" "${yesterday}" "${infoToday}" "${infoYesterday}"









