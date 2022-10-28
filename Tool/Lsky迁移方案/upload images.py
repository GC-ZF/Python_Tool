"""
@Author:张时贰
@Date:2022年10月21日
@CSDN:张时贰
@Blog:zhangshier.vip
@Function:批量上传图片
"""
import os
import time

import requests


def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir ( path )
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join ( path, file )
        # 判断是否是文件夹
        if os.path.isdir ( cur_path ):
            show_files ( cur_path, all_files )
        else:
            all_files.append ( file )
            if file.endswith ( ('.jpeg', '.jpg', '.png', '.gif', '.tif', '.bmp', '.ico', '.psd', '.webp') ):
                end = (os.path.splitext ( file )[ -1 ])
                end = end.replace ( '.', '' )  # 获取后缀
                files = {
                    "file": (file, open ( cur_path, 'rb' ).read (), 'image/' + end)  # 加个read方法，之后使用os不会造成资源占用
                }
                r = requests.post ( url, data=json, files=files, headers=headers )
                r.encoding = "utf-8"
                print ( r.json () )
                # 去不图床仪表盘显示每分钟是200张请求，一次性上传多张图片，会出现上传失败
                # 解决办法：每成功上传一张就删除一张（如果代码中断可以反复运行上传剩余图片直至所有图片上传完成），额外加一个sleep，超出频率就歇一会
                while not r.json ()[ 'status' ]:
                    print ( '小歇一下叭' )
                    time.sleep ( 60 )
                    print ( '开个开干' )
                    r = requests.post ( url, data=json, files=files, headers=headers )
                    r.encoding = "utf-8"
                    print ( r.json () )
                print ( '删除 ' + cur_path )
                os.remove ( cur_path )

    return all_files


if __name__ == "__main__":
    '''
        必填：
            token：兰空的 token
            url：域名/api/v1/upload
            path：图片文件夹
        选填 json 参考注释
        请将本地文件夹备份，path=备份路径，原因详见35~36
    '''
    token = 'Bearer 335|aatlbU9CTHKKbemsTXxB7F2uSd2PXL3m7By5uD7i'  # token Bearer+空格+token
    url = 'https://7bu.top/api/v1/upload'  # 图床地址 域名/api/v1/upload
    path = 'test'  # 图片文件夹路径，图片可以嵌套多个文件夹
    json = {
        # "album_id": 188  # 相册ID Int
        # 如果你不是图床的搭建者，以下值请忽略
        # "strategy_id":      # 存储策略 Int
        # 以下参数为企业版
        # "permission": 0     # 权限 Int 1=公开，0=私有 默认0
        # "expired_at":       # 过期时间 String 'yyyy-MM-dd HH:mm:ss'
    }
    headers = {
        # "Content-Type": "multipart/form-data", # 文档声明中必须有改字段，但是程序无法运行，详见github.com/lsky-org/lsky-pro/issues/403
        "Authorization": token,
        "Accept": "application/json"
    }

    contents = show_files ( path, [ ] )  # 参数一传入所有文章存在的目录
