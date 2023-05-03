"""
@Author:张时贰
@Date:2022年08月08日
@CSDN:张时贰
@Blog:zhsher.cn
@Private:私有部署方案
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
init_path='/xxxxx/bin/db.json.1'
backup_path='/xxxxx/bin/backup/'
init_path='"'+init_path+'"'
backup_path='"'+backup_path+f"/{now_time.year}年{now_time.month}月{now_time.day}日.json"+'"'
commond = 'cp '+init_path+" "+backup_path
code = os.system ( commond )
if code == 0:
    print ( data + " 备份成功" )
else:
    print ( data + " 备份失败，请检查python文件中init_path和backup_path是否正确或备份路径是否有读写权限" )
print ()