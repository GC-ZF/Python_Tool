"""
@Author:张时贰
@Date:2022年12月16日
@CSDN:张时贰
@Blog:zhsher.cn
"""
import os
import pyautogui
import pyperclip
import asyncio
import json
import time
import aiohttp


def send_msg(msg_num, frequency):
    i = 0
    while i < msg_num:
        time.sleep ( frequency )
        foo = send_list[ i ]
        pyperclip.copy ( foo )  # 剪切板
        pyautogui.hotkey ( 'ctrl', 'v' )  # 组合按键
        pyautogui.press ( "enter" )
        i = i + 1


# request无法异步，换用aiohttp库做异步请求
async def requests_get(link):
    async with aiohttp.ClientSession () as session:
        async with session.get ( link ) as resp:
            text = await resp.text ()
            # print(text)
            try:
                text = json.loads ( text )[ 'text' ]
                send_list.append ( text )
                return text
            except Exception as e:
                e = str ( e )
                print ( f'请求状态码{resp.status}，错误：{e}' )


def run(number):
    base_url = 'https://api.oddfar.com/yl/q.php?c=1009&encode=json'
    # 创建协程容器（获取事件循环）
    loop = asyncio.get_event_loop ()
    # 指定协程添加任务
    tasks = [ asyncio.ensure_future ( requests_get ( base_url ) ) for i in range ( number ) ]
    # 运行任务（将所有的事件对象传入事件循环）
    loop.run_until_complete ( asyncio.wait ( tasks ) )


if __name__ == '__main__':
    print ( '@Author:张时贰\n脏话为在线抓取，需要联网\n李云龙太菜就不要玩了！！！' )
    number = int ( input ( '发送数量：' ) )
    frequency = int ( input ( '发送频率，单位s：' ) )
    send_list = [ ]
    run ( number )
    msg_num = len ( send_list )
    print ( f'共抓取到{msg_num}条消息（可能会由于网络环境抓取不够）' )
    send_msg ( msg_num, frequency )
    os.system ( 'pause' )

# pyinstaller -F -c ../auto_send.py
