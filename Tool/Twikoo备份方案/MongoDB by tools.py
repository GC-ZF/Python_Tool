"""
@Author:张时贰
@Date:2022年08月08日
@CSDN:张时贰
@Blog:zhsher.cn
@Funtion:初版方案，适用MongoDB部署，在服务器中备份
"""
import os
from datetime import datetime
import sys


class Logger ( object ):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open ( fileN, "a" )

    def write(self, message):
        self.terminal.write ( message )
        self.log.write ( message )

    def flush(self):
        pass


sys.stdout = Logger ( "backuplog.txt" )  # 输出日志
print ( "--------------------------------------------------------------\n" )
now_time = datetime.now ()  # 当前时间
now_time_day = now_time.day  # 日
data = f"{now_time.year}年{now_time.month}月{now_time.day}日"
delete_day = [ 15, 30 ]  # 每月15、30号清空备份
if now_time_day in delete_day:
    os.system ( 'rm *.json -f' )  # 删除所有json
    print ( data + " 清空备份文件" )
    # os.system ( 'rm backuplog.txt.txt -f' )     # 删除日志
MONGODB_URI = 'mongodb+srv://1310446718:zf632852@cluster0.i7omd.mongodb.net/myFirstDatabase'
commond = 'mongoexport --uri ' + f'{MONGODB_URI}' + ' --collection comment --forceTableScan --type json --out ' + f"{now_time.year}年{now_time.month}月{now_time.day}日.json"
code = os.system ( commond )
if code == 0:
    print ( data + " 备份成功" )
else:
    print ( data + " 备份失败，请检查python文件中MONGODB_URI值是否正确" )
print ()
