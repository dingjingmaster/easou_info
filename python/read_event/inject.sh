#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTime=""
datestr=""

if [ $# -gt 1 ]
then
nowTime="$1"
datestr="$2"
else
nowTime=`date -d "-1 day" +%Y%m%d`
datestr=`date -d "-1 day" +%Y-%m-%d`
fi
#nowTime="20190320"
#datestr="2019-03-20"

readEventPath="hdfs://10.26.26.145:8020/rs/dingjing/static/read_day/${datestr}/"
infoToday="data/read_event.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${readEventPath}/*" > ${infoToday}

cd ${workDir}/
python inject.py "127.0.0.1" "root" "123456" "${nowTime}" "${infoToday}"









