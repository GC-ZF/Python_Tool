import shutil
from aligo import Aligo
import time
import datetime
import os
import zipfile


class VPSBackup:
    def __init__(self, Aligo):
        '''
        初始化 阿里云登录用户
        :param Aligo: 阿里云盘
        '''
        self.ali = Aligo
        self.remote_folder = ali.get_folder_by_path ( upload_dir )
        self.upload ()
        self.delete ()

    def compress(self):
        '''
        将需要备份的目录依次压缩并保持至 tmp 下
        '''
        # 压缩
        for i in range ( 0, len ( compress_name_list ) ):
            zip_file = compress_dir + '/' + t + "-" + compress_name_list[ i ]
            zip = zipfile.ZipFile ( zip_file, 'w', zipfile.ZIP_DEFLATED )
            for root, dirs, files in os.walk ( backup_dir_list[ i ] ):  # 遍历统计
                for each in files:
                    if os.path.exists ( root + "/" + each ):
                        zip.write ( root + "/" + each )
            zip.close ()

    def getFile(self):
        '''
        获取阿里云盘指定目录下所有备份文件
        :return: zip_file_list 列表
        '''
        zip_file_list = [ ]
        list = ali.get_file_list ( self.remote_folder.file_id )  # 获取网盘根目录文件列表
        # 遍历文件列表
        for file in list:
            tmp = {'file_id': file.file_id, 'file_name': file.name}
            zip_file_list.append ( tmp )
        return zip_file_list

    def upload(self):
        '''
        将 tmp 下的压缩包上传
        '''
        self.compress ()  # 压缩
        file_list = os.listdir ( compress_dir )  # 压缩文件夹中的文件列表
        # 拼接相对路径
        print ( file_list )
        for i in range ( 0, len ( file_list ) ):
            file_list[ i ] = os.path.join ( compress_dir, file_list[ i ] )
        # 批量上传压缩后的文件列表
        ali.upload_files ( file_list, parent_file_id=self.remote_folder.file_id )

    def delete(self):
        '''
        删除阿里云盘中过期的压缩包 以及 本地 tmp 临时压缩包
        '''
        zip_file_list = self.getFile ()
        for i in zip_file_list:
            if (i[ 'file_name' ][ 0:10 ] < t_be):
                ali.move_file_to_trash ( i[ 'file_id' ] )
        shutil.rmtree ( compress_dir )  # 删掉 tmp 临时文件夹


if __name__ == '__main__':
    '''
    依次填写
        ali：登录阿里云盘
        backup_dir_list：需要备份的文件夹路径
        compress_name_list：压缩包命名
        upload_dir：阿里云盘上传路径
        day：压缩包保留天数
    '''
    # 登录信息存放在 < 用户家目录 >/.aligo/< name >.json中
    # ali = Aligo () # 方式一，扫码登录
    # ali = Aligo ( refresh_token='<refresh_token>' ) # 方式二，从 网页控制台->应用 获取 token
    ali = Aligo ( email=('1310446718@qq.com', 'haivhisaofwu1920u90du90w') )  # 方式三，发送邮箱，邮箱+随机定义一个字符

    # 备份目录路径数组
    backup_dir_list = [
        'D:\Git repo\新建文件夹\_posts\C++笔记',
        'D:\Git repo\新建文件夹\_posts\笔记'
    ]

    # 压缩包文件名数组与 backup_dir_list 一一对应
    compress_name_list = [
        '测试.zip',
        '测试2.zip'
    ]
    # 阿里云盘上传路径
    upload_dir = 'Alist/Backup'
    # 压缩包保存多少天
    day = 7

    # 临时压缩包路径
    try:
        os.mkdir ( 'tmp' )
    except FileExistsError as e:
        e = str ( e )
        print ( "error:" + e )
        print ( '文件夹重名，请将现有tmp文件夹移除或按任意键继续' )
        os.system ( 'pause' )
    compress_dir = 'tmp'

    t = time.strftime ( "%Y-%m-%d", time.localtime () )
    t_be = (datetime.datetime.now () - datetime.timedelta ( days=day - 1 )).strftime ( "%Y-%m-%d" )

    back = VPSBackup ( ali )
