"""
@Author:张时贰
@Date:2022年10月21日
@CSDN:张时贰
@Blog:zhangshier.vip
@Function:查看相册ID
"""
import json

import requests

token = 'Bearer 335|aatlbU9CTHKKbemsTXxB7F2uSd2PXL3m7By5uD7i'  # token，Bearer+空格+token
url = 'https://7bu.top/api/v1/albums'  # 图床地址 域名/api/v1/albums

headers = {
    "Content-Type": "multipart/form-data",
    "Authorization": token,
    "Accept": "application/json",
}

if __name__ == "__main__":
    r = requests.get ( url, headers=headers )
    r.encoding = "utf-8"
    getJson = r.json ()[ 'data' ][ 'data' ]
    photoID = [ ]
    for i in getJson:
        tmp = {'id': i[ 'id' ],
               'name': i[ 'name' ]}
        photoID.append ( tmp )
    # print ( json.dumps(photoID,indent=4, ensure_ascii=False) )
    for i in photoID:
        print ( i )