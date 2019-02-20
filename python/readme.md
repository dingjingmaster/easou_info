####pip install mysql-python 安装MySQL模块

# item_exhibit
- 数据由儒安生成(当天日期目录下放的一定是由当天数据生成的，只是生成时期不同而已)
- 生成目录：hdfs://10.26.26.145:8020/rs/stat/时间/recsubs/useritem2/
    
    useritem:  生成的数据缺少次日留存量, 次日生成今天的。比如: 20190102 生成 20190101 的数据
    
    useritem2: 生成的是完整数据,次日生成昨天的。比如：20190103 生成 20190101 的数据
- mysql 表名 item_exhibit
 1. get_data.sh   ----------------> 获取昨天订展比数据并注入 mysql 同时更新 前天的次日留存量数据
 2. update_exhibit.sh ------------> 获取前天的完整数据，直接更新前天数据