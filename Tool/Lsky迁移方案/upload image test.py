"""
@Author:张时贰
@Date:2022年10月21日
@CSDN:张时贰
@Blog:zhangshier.vip
@Function:上传单张图片测试
@request请求：https://blog.csdn.net/m0_37737957/article/details/123843265
"""
import os

import requests

token = 'Bearer 335|aatlbU9CTHKKbemsTXxB7F2uSd2PXL3m7By5uD7i'  # token Bearer+空格+token
url = 'https://7bu.top/api/v1/upload'  # 图床地址 域名/api/v1/upload'
path = 'test/background.png'  # 图片路径

headers = {
    # "Content-Type": "multipart/form-data", # 文档声明中必须有改字段，但是程序无法运行，详见github.com/lsky-org/lsky-pro/issues/403
    "Authorization": token,
    "Accept": "application/json",
}

if __name__ == "__main__":
    files = {
        "file": ('file.png', open ( path, 'rb' ).read (), 'image/png')  # 加个read方法，之后使用os不会造成资源占用
    }
    json = {
        # "album_id": 188  # 相册ID Int
        # 如果你不是图床的搭建者，以下值请忽略
        # "strategy_id":      # 存储策略 Int
        # 以下参数为企业版
        # "permission": 0     # 权限 Int 1=公开，0=私有 默认0
        # "expired_at":       # 过期时间 String 'yyyy-MM-dd HH:mm:ss'
    }
    r = requests.post ( url, data=json, files=files, headers=headers )
    r.encoding = "utf-8"
    print ( r.json () )
    os.remove ( path )