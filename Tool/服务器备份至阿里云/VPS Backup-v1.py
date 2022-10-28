from aligo import Aligo
import time 
import datetime
import gzip
import os
import zipfile

# 备份目录路径数组
backup_dir_list = [
    '/www/lskypro/storage/app/uploads',
    '/www/shinie.top'
]
# 压缩包路径
compress_dir = '/www/aligo/backup/'
# 压缩包文件名数组
compress_name_list = [
    'lskypro.zip',
    'shinie.top.zip'
]
# 阿里云盘上传路径
upload_dir = 'AList/服务器数据备份/'
# 压缩包保存多少天
day=7

t=time.strftime("%Y-%m-%d",time.localtime())
t_be=(datetime.datetime.now() - datetime.timedelta(days = day)).strftime("%Y-%m-%d")

if __name__ == '__main__':
    ali = Aligo(email=('1982989137@qq.com', 'haivhisaofwu1920u90du90w'))
    # 遍历备份目录
    for i in range(0,len(backup_dir_list)):
        remote_folder = ali.get_folder_by_path(upload_dir)
        # 将旧文件移入回收站
        expire_file=ali.get_folder_by_path(upload_dir+t_be+"-"+compress_name_list[i])
        if expire_file:
            ali.move_file_to_trash(expire_file.file_id)
        # 删除本地旧文件
        old_zip_file=backup_dir_list[i]+t_be+"-"+compress_name_list[i]
        if os.path.exists(old_zip_file):
            os.remove(old_zip_file)
        # 压缩
        zip_file=compress_dir+t+"-"+compress_name_list[i]
        zip = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
        for root,dirs,files in os.walk(backup_dir_list[i]):    #遍历统计
            for each in files:
                if os.path.exists(root+"/"+each):
                    zip.write(root+"/"+each)
        zip.close()
        # 同步文件夹（以本地文件为主）
        ali.sync_folder(local_folder=compress_dir, remote_folder=remote_folder.file_id,flag=True,follow_delete=True)
