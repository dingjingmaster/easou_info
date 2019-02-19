#!/bin/bash
source ~/.bash_profile
source ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
yesterday=`date -d "-2 day" +%Y%m%d`

exhibitYesterday="hdfs://10.26.26.145:8020/rs/stat/${yesterday}/recsubs/useritem2/"
infoYesterday="data/exhibit_info_yesterday.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${exhibitYesterday}/*" > ${infoYesterday}

cd ${workDir}
python update_exhibit.py "127.0.0.1" "root" "123456" "${yesterday}" "${infoYesterday}"
