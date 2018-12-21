#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
nowTime=`date -d "-1 day" +%Y%m%d`
yesterday=`date -d "-2 day" +%Y%m%d`

exhibitBaset="hdfs://10.26.26.145:8020/rs/stat/${nowTime}/recsubs/useritem/"
exhibitBasey="hdfs://10.26.26.145:8020/rs/stat/${yesterday}/recsubs/useritem2/"
infot="data/exhibit_infot.txt"
infoy="data/exhibit_infoy.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${exhibitBaset}/*" > ${infot}
hadoop fs -cat "${exhibitBasey}/*" > ${infoy}

cd ${workDir}/
python inject_exhibit.py "127.0.0.1" "root" "123456" "${nowTime}" "${infot}" "${infoy}"











