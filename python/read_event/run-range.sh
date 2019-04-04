#!/bin/bash
. ~/.bashrc
. ~/.bash_profile

workDir=$(cd $(dirname $0); pwd)
days=40

cd ${workDir}
for (( i=1; i<${days}; i++ )) {
    today=`date -d "-$i day" +%Y%m%d`
    nowTime=`date -d "-$i day" +%Y-%m-%d`
    sh ./inject.sh "${today}" "${nowTime}"
}



