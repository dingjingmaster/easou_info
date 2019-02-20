#!/usr/bin/env bash
. ~/.bash_profile
. ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
year=`date -d "-0 day" +%Y`
itemInfoPath=`hadoop fs -ls "hdfs://10.26.26.145:8020/rs/iteminfo/${year}-*/item_*/*" | tail -n 1 | awk -F' ' '{print $8}'`
updateTime=`hadoop fs -ls "hdfs://10.26.26.145:8020/rs/iteminfo/${year}-*/item_*/*" | tail -n 1 | awk -F' ' '{print $6" "$7}'`
itemInfoLocal="data/item_info.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${itemInfoPath}" > "${itemInfoLocal}"

cd ${workDir}
python inject_item.py "127.0.0.1" "root" "123456" "${itemInfoLocal}" "${updateTime}"