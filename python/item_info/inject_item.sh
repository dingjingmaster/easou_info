#!/usr/bin/env bash
. ~/.bash_profile
. ~/.bashrc
workDir=$(cd $(dirname $0); pwd)
itemInfoPath="hdfs://10.26.26.145:8020/rs/iteminfo/current"
itemInfoLocal="data/item_info.txt"

cd ${workDir} && rm -fr data && mkdir data
hadoop fs -cat "${itemInfoPath}" > "${itemInfoLocal}"

cd ${workDir}
