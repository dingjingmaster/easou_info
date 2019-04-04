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

readEventChapterPath="hdfs://10.26.26.145:8020/rs/dingjing/static/read_day/chapter/${datestr}/"
readEventUserPath="hdfs://10.26.26.145:8020/rs/dingjing/static/read_day/user/${datestr}/"
readEventBookPath="hdfs://10.26.26.145:8020/rs/dingjing/static/read_day/book/${datestr}/"
infoChapterToday="data/read_event_chapter.txt"
infoUserToday="data/read_event_user.txt"
infoBookToday="data/read_event_book.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${readEventChapterPath}/*" > ${infoChapterToday}
hadoop fs -cat "${readEventUserPath}/*" > ${infoUserToday}
hadoop fs -cat "${readEventBookPath}/*" > ${infoBookToday}

cd ${workDir}/
python inject.py "127.0.0.1" "root" "123456" "${nowTime}" "${infoChapterToday}" "${infoUserToday}" "${infoBookToday}"









