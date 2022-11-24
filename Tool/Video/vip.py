import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
# 创建一个窗口
root=tk.Tk()
# 设置窗口大小
root.geometry("755x500+200+150")
#设置标题
root.title('羊羊羊影视vip')
def show():
    #判断是哦那个接口
    num=bianliang.get()
    word=lianjie.get()
    print('输入的内容是', word)
    if num==1:
        print('选择的是第一个接口')
        link = 'https://jiexi.pengdouw.com/jiexi1/?url=' + word
        # html_data = requests.get(url=link).text
        # video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(link)
    elif num==2:
        print('选择的是第二个接口')
        link = 'https://jiexi.pengdouw.com/jiexi2/?url=' + word
        # html_data = requests.get(url=link).text
        # video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(link)
    elif num == 3:
        print('选择的是第三个接口')
        link = 'https://jiexi.pengdouw.com/jiexi3/?url='+ word
        # html_data = requests.get(url=link).text
        # video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(link)
#设置读取一张图
# img=tk.PhotoImage('2.png')
img_open=Image.open('2.png')
img=ImageTk.PhotoImage(img_open)
# 把标签label放到窗口，pack是布局
tk.Label(root,image=img).pack(fill='both')
#设置标签框pady=10与上边距离是10，side=tk.LEFT靠左
choose_frame=tk.LabelFrame(root)
choose_frame.pack(pady=10,fill='both')
tk.Label(choose_frame,text='选择接口:',font=('楷体',20)).pack(side=tk.LEFT)
#设置输入内容
lianjie=tk.StringVar()
#设置可变变量
bianliang=tk.IntVar()
#设置默认为1
bianliang.set(1)
#设置选择  接口间距5，padx=5
tk.Radiobutton(choose_frame,text='接口1',font=('楷体',15),variable=bianliang,value=1).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(choose_frame,text='接口2',font=('楷体',15),variable=bianliang,value=2).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(choose_frame,text='接口3',font=('楷体',15),variable=bianliang,value=3).pack(side=tk.LEFT,padx=5)
#设置输入窗口 宽度width=100relief='flot'平滑
input_chuangk=tk.LabelFrame(root)
input_chuangk.pack(pady=10,fill='both')
tk.Label(input_chuangk,text='播放地址:',font=('楷体',20)).pack(side=tk.LEFT)
tk.Entry(input_chuangk,width=100,textvariable=lianjie,relief='flat',font=('楷体',20)).pack(side=tk.LEFT)
#设置点击解析按钮
tk.Button(root,text='Go点击在线解析播放',relief='flat',command=show,bg='#57d705',font=('楷体',20)).pack(pady=10,fill='both')
#让窗口持续展现
root.mainloop()