"""
@Author:张时贰
@Date:2022年05月18日
@CSDN:张时贰
@Blog:zhangshier.vip
"""
import os

def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(file)
            if (file.endswith(".md")):
                with open(cur_path, encoding="utf-8", mode='r+') as f:
                    t = f.read()
                    t = t.replace('https://cdn.jsdelivr.net/gh/GC-ZF/Typora-Img/',        # gitee中的图片链接仓库名前部分
                                  'https://fastly.jsdelivr.net/gh/GC-ZF/Typora-Img/')  # github中的图片链接仓库名前部分
                    # 读写偏移位置移到最开始处
                    f.seek(0, 0)
                    f.write(t)

                    # 设置文件结尾 EOF
                    f.truncate()

    return all_files
# 条用函数进行全部替换
contents = show_files("_posts", [])  # 参数一传入所有文章存在的目录
