#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTime=`date -d "-2 day" +%Y%m%d`

exhibitBase="hdfs://10.26.26.145:8020/rs/stat/${nowTime}/recsubs/useritem2/"
info="data/exhibit_info.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${exhibitBase}/*" > ${info}

cd ${workDir}/
python inject_exhibit.py "127.0.0.1" "root" "123456" "${nowTime}" "${info}"











