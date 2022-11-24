"""
@Author:张时贰
@Date:2022年11月22日
@CSDN:张时贰
@Blog:zhangshier.vip
"""
import urllib

import requests

music_name = "浪漫主义"
url = "https://music.163.com/api/cloudsearch/pc?s=" + f"{music_name}" + "&type=1&offset=0&limit=1"
get_data = requests.get ( url )

result = get_data.json ()
print ( result )  # 打印json数据，其实就是用第一个链接获取json查找id 你可以直接访问url看看是啥，就是一个列表字典
print ( "id= ", result[ 'result' ][ 'songs' ][ 0 ][ 'id' ] )
with open ('vip.py') as f:
    f.re
id=result[ 'result' ][ 'songs' ][ 0 ][ 'id' ]
murl = "http://music.163.com/song/media/outer/url?id=" + f'{id}' + ".mp3"
print(murl)
music_file=requests.get(murl).text
# print(music_file)
# with open ( music_name+".mp3", "wb" ) as f:
#     f.write ( music_file )
