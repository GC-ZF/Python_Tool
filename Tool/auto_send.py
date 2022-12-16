"""
@Author:张时贰
@Date:2022年12月16日
@CSDN:张时贰
@Blog:zhangshier.vip
"""
import os

import pyautogui
import time
import pyperclip
import requests


def send_msg(number, frequency):
    i = 0
    dirty = [ ]
    print ( '脏话灌水中' )
    while i < number:
        dirty.append ( get_words () )
        i = i + 1
        print ( f'已灌入{i}条' )
    print ( '灌水完毕', dirty )
    i = 0
    while i < number:
        time.sleep ( frequency )
        foo = dirty[ i ]
        pyperclip.copy ( foo )  # 剪切板
        pyautogui.hotkey ( 'ctrl', 'v' )  # 组合按键
        pyautogui.press ( "enter" )
        i = i + 1


def get_words():
    url = "https://api.oddfar.com/yl/q.php?c=1009&encode=json"
    get_data = requests.get ( url )
    if get_data.status_code == 200:
        words = get_data.json ()[ 'text' ]
        return words
    else:
        get_words ()


if __name__ == '__main__':
    print ( '@Author:张时贰\n脏话为在线请求，不要使用vpn工具\n李云龙太菜就不要玩了！！！' )
    number = int ( input ( '发送数量：' ) )
    frequency = int ( input ( '发送频率，单位s：' ) )
    send_msg ( number, frequency )
    os.system ( 'pause' )

# pyinstaller -F -c ../auto_send.py
