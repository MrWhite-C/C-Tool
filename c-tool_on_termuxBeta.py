#Modules
import time
import os
import random
import linecache
from datetime import datetime

#functions
def download_environment(packetname,name,common):
    open("./config/environment/"+packetname+"/D",'a+')
    open("./config/environment/"+packetname+"/D",'a+').close
    read_environment=open("./config/environment/"+packetname+"/D","r+")
    read_result=read_environment.read()
    if read_result == '':
        os.system("clear")
        print("补全环境中")
        print("下载"+name)
        time.sleep(2)
        os.system(common)
        read_environment=open("./config/environment/"+packetname+"/D",'w+')
        read_environment.write("yes")
        read_environment.close

def sleep(S):
    time.sleep(S)


def mkdir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)

def gu():
    print(TRed+"To be built")
    sleep(0.7)
    print("\n\n\n\n\n")
    main_menu()

def error_enter():
    print(BYellow+"您输入序号的有误"+reset_colors)
    main_menu()

def copy_os():
    OSname=input(BGreen+"请为文件取个名"+reset_colors)
    os.system("cd && cd ../.. && echo \"即将开始备份\" && tar -cvzf "+OSname+".tar.gz files/ && mv "+OSname+".tar.gz /sdcard/C-Tool/OS")
    print(TGreen+"""
    如果成功那么在/sdcard/C-Tool/OS会有一个叫"""+OSname+""".tar.gz的东东
    或者它在      /storage/emulated/0/C-Tool/OS下
    /sdcard/ = /storage/emulated/0/
    建议用MT管理器查看(安卓应用)\n\n""")
    main_menu()

def return_os():
    print(TSkyblue+"""
    输入文件目录加文件名称(要加后缀)
    如:/storage/emulated/0/C-Tool/OS/示例文件.tar.gz\n\n
    如果不行就手动mv加上tar -xvzf解压
    具体去搜百度或者以后更新
    """)
    files=input(TRed+"请按上面提示输入")
    os.system("cd && cd ../.. && tar -xvzf "+files)
    print(TGreen+"还原系统成功")

def add_saying(mess):
    saying_list.append(mess)

def a_s(mess):
    add_saying(mess)

def message(mess,times1,times2):
    R=random.randint(0,times1)
    if R <= times2:
        print(mess)

def set_random_saying():
    os.system("clear")
    print(TRed+"""
    使用方法：输入随机句子再回车即可
    千万不要直接什么都不输入就回车，如果你这样做了请按最后一排说的做
    输入 a 回主菜单
    暂时不支持自动修改
    可以去此程序的目录下的/config/sayings/sayings手动修改\n\n\n\n\n
    """+reset_colors)
    add_=input(TGreen+"请输入你的句子"+reset_colors)
    if add_ == 'a':
        main_menu()
    else:
        write_saying=open("./config/sayings/sayings","a+")
        write_saying.write("\n"+add_)
        write_saying.close()
        set_random_saying()
    
def print_saying():
    if saying_list == []:
        print(TRed+"在设置里设置随机句子\n")
    else:
        print(TYellow+random.choice(saying_list)+'\n')

#Make Settings
mkdir("./config/")
mkdir("./config/colors/")
mkdir("./config/sayings/")
mkdir("/sdcard/C-Tool")
mkdir("/sdcard/C-Tool/OS")
mkdir("./config/environment/psutil")
saying=open("./config/sayings/sayings",'a+')
saying.close


#Download Environment
download_environment("psutil","psutil","pip install psutil")

#Modules need to download
import psutil



#Shell Scripts
installjava="pkg in proot -y && pkg in git -y && cd && git clone https://github.com/Egrak/Termux-java.git && mv Termux-java/javainstaller.sh . && rm -rf Termux-java && bash javainstaller.sh"
downloadall="apt upgrade && apt update && apt-get install vim -y && apt-get install vim -y && apt-get install vim -y &&"
download_annie="pkg in wget && cd && wget https://github.com/iawia002/annie/releases/download/0.10.3/annie_0.10.3_Linux_ARM64.tar.gz && tar -xvzf annie_0.10.3_Linux_ARM64.tar.gz && chmod +x annie && mv annie ../usr/bin && rm annie_0.10.3_Linux_ARM64.tar.gz"

#

#--------
#Colors
#--------
reset_colors="\033[0m"
#--------
#Text colors
#--------
TBlack = "\033[90m"
TRed = "\033[91m"
TGreen = "\033[92m"
TYellow = "\033[93m"
TBlue = "\033[94m"
TPurple = "\033[95m"
TSkyblue = "\033[96m"
TWhite = "\033[97m"
#--------
#Background colors
#--------
BBlack = "\033[0;37;40m"
BRed = "\033[0;37;41m"
BGreen = "\033[0;37;42m"
BYellow = "\033[0;37;43m"
BBlue = "\033[0;37;44m"
BPurple = "\033[0;37;45m"
BSkyblue = "\033[0;37;46m"
BWhite = "\033[0;37;47m"


#saying

saying_list=[]


#Read Settings
menu_color=open("./config/colors/main_menu_color.config",'w+').read()
open("./config/colors/main_menu_color.config",'w+').close

#Load sayings

write_saying=open("./config/sayings/sayings","a+")
load_saying=open("./config/sayings/sayings","r+")
saying_lines=len(load_saying.readlines())
for a in range(saying_lines):
    a_s(linecache.getline('./config/sayings/sayings', a+1))


#Auto Set Settings
if menu_color == '':
    menu_color=TSkyblue









#Texts
time_now=datetime.now().strftime(BRed+"%Y-%m-%d %H:%M:%S"+reset_colors+menu_color)

version=BRed+"BetaV0.14.9"+reset_colors

logo=TRed+"""
   ______   ______            __"""+TYellow+"""
  / ____/  /_  __/___  ____  / /"""+TGreen+"""
 / /  ______/ / / __ \/ __ \/ /"""+TBlue+"""
/ /__/_____/ / / /_/ / /_/ / /"""+TSkyblue+"""
\____/    /_/  \____/\____/_/"""+version

logo1=TRed+"""
    _/_/_/      _/_/_/_/_/                     _/"""+TYellow+"""
  _/                _/      _/_/      _/_/    _/"""+TGreen+"""
 _/    _/_/_/_/_/  _/    _/    _/  _/    _/  _/"""+TBlue+"""
_/                _/    _/    _/  _/    _/  _/"""+TSkyblue+"""
 _/_/_/          _/      _/_/      _/_/    _/"""+version

RS="""Only my railgun
Hi,Bilibili
You will reach that you can see
想打的话就握紧你的拳头，不想打的话就别挡路啊，别用这种半吊子的态度来践踏别人的决心
我们会到达目光到达的尽头
一个人，不会因为所在位置的不同，灵魂就因此而受到玷污。
就算是我，也能成为你的力量。
你知道么？樱花飘落的速度，是每秒五厘米。
如果存在皆大欢喜，人人期待的幸福世界的话，那里就没有我的容身之所。
当面对两难的抉择时，不妨丢一枚硬币吧，并非是要靠那二分之一的机运来帮你做出抉择，而是因为，当硬币被抛上空中，开始旋转的那一瞬间你会突然明白，自己想要的，不要被所谓的极限所禁锢。
别在这种地方畏畏缩缩的，别对自己说谎，再努力一次吧。
讨厌毫无力量的自己，但是，无论如何都无法割舍这份憧憬。
再努力一次吧，不要躲在这里，真诚地面对自己再试一次。
接下来就是我个人打架时间了，抱歉，我要出手了。
你以为我是谁？这是我埋下的因，我要亲手解决这一切。
明明不希望他去做危险的事，依然能拍着他的背送他离开，这样才是好女人。
究竟是要有多可悲，把别人的好扭曲成这样
我又不是输送带上的布娃娃。一旦知道前进只会掉下悬崖，什么信念理念的，当然能干脆地改变。
极限不存在，也毫无意义。
你指间跃动的电光，是我此生不变的信仰
如果真爱有颜色，那一定是蓝色
喜欢那一份遥不可及
明知道不努力就会堕入深渊，但是还是自甘堕落"""

main_menu_texts=menu_color+"""
|时间:"""+time_now+"""
|CPU逻辑个数:"""+str(psutil.cpu_count())+"""
|CPU物理个数:"""+str(psutil.cpu_count(logical=False))+"""
|上次更新时间:2020.12.5


 ____________________________
|___________主菜单___________|
|[1] 超多工具                |
|[2] 编程环境下载 内含java   |
|[3] 关于作者                |
|[4] 原创的强大Termux工具    |
|[5] 设置                    |
|[a] 退出C-tool              |
 ----------------------------


"""

tool_menu_texts=menu_color+"""

 ____________________________
|___________工具单___________|
|[1] 实用的工具              |
|[2] hack工具                |
 ----------------------------
 
 
 
"""


useful_tools_texts=menu_color+"""

 _______________________________________
|_______________实用工具________________|
|[1] annie[下载各个网站资源如bilibili]  |
 ---------------------------------------



"""

setting_saying_texts=menu_color+"""

 _______________________________________
|_______________设置句子________________|
|[1] 添加随机句子                       |
|[2] 删除随即句子配置                   |
|[3] 加载作者设置好的随机句子           |
 ---------------------------------------


"""

setting_menu_texts=menu_color+"""

 _______________________________________
|_______________设置菜单________________|
|[1] 随机句子设置                       |
 ---------------------------------------
"""

tool_madebyself_texts=menu_color+"""

 _______________________________________
|_______________原创工具________________|
|[1] 系统备份(不要开chroot)             |
|[2] 系统还原(与[1]合用不要开chroot)    |
 ---------------------------------------
 
"""

program_enviroment_texts=menu_color+"""

 _______________________________________
|_______________编程环境________________|
|[1] Java8                              |
 ---------------------------------------


"""


#The First Menus

def main_menu():
    time_now=datetime.now().strftime(BRed+"%Y-%m-%d %H:%M:%S"+reset_colors+menu_color)
    print("\n\n\n"+random.choice([logo,logo1])+reset_colors+"\n")
    print_saying()
    print(main_menu_texts)
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        tool_menu()
    elif choose == '2':
        program_enviroment()
    elif choose == '3':
        about_maker()
    elif choose == '4':
        tool_madebyself()
    elif choose == '5':
        setting_menu()
    elif choose == 'a':
        exit()
    else:
        error_enter()
#The Second Menus
def tool_menu():
    print("\n\n\n")
    print(tool_menu_texts)
    print(menu_color+"[a] 退出C-tool\n\n\n")
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        useful_tools()
    elif choose == '2':
        hack_tools()
    elif choose == 'a':
        exit()
    else:
        error_enter()

def program_enviroment():
    print("\n\n")
    print(program_enviroment_texts)
    print(menu_color+"[a] 退出C-tool\n\n\n")
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        os.system(installjava)
        print("使用Java前请执行termux-chroot")
    elif choose == 'a':
        exit()
    else:
        error_enter()

def about_maker():
    print(TGreen+"""
    作者的群:207172541
    链接:https://jq.qq.com/?_wv=1027&k=kaLCVJTz
    在这里你可以提交BUG 提出建议交流与讨论""")

def setting_menu():
    print("\n\n\n")
    print(setting_menu_texts)
    print(menu_color+"[a] 退出C-tool\n\n\n")
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        setting_saying()
    elif choose == 'a':
        exit()
    else:
        error_enter()


def tool_madebyself():
    print("\n\n\n")
    print(tool_madebyself_texts)
    print(menu_color+"[a] 退出C-tool\n\n\n")
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        copy_os()
    elif choose =='2':
        return_os()
    elif choose == 'a':
        exit()
    else:
        error_enter()
#The Third menus


def useful_tools():
    print("\n\n\n"+useful_tools_texts)
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        os.system(download_annie)
        print(TGreen+"\n\n现在您可用annie来使用它了，具体教程可以上百度查"+reset_colors)
    elif choose =='2':
        gu()
    elif choose == 'a':
        exit()
    else:
        error_enter()

def setting_saying():
    print("\n\n\n\n"+setting_saying_texts)
    print(menu_color+"[a] 退出C-tool\n\n\n")
    choose=input(TGreen+"C-Tool User => "+reset_colors)
    if choose == '1':
        set_random_saying()
    elif choose == '2':
        os.system("rm -rf ./config/sayings/sayings")
        print(TRed+"重启C-Tool来更新配置\n\n"+reset_colors)
    elif choose == '3':
        write_saying.write(RS)
        print(TRed+"重启C-Tool来更新配置\n\n"+reset_colors)
    elif choose == 'a':
        exit()
    else:
        error_enter()











main_menu()
#Example

#Text Color

#print("\033[90m%s\033[0m"%"黑色")
#print("\033[91m%s\033[0m"%"红色")
#print("\033[92m%s\033[0m"%"绿色")
#print("\033[93m%s\033[0m"%"黄色")
#print("\033[94m%s\033[0m"%"蓝色")
#print("\033[95m%s\033[0m"%"紫红色")
#print("\033[96m%s\033[0m"%"青蓝色")
#print("\033[97m%s\033[0m"%"白色")

#Background Color

#print("\033[0;37;40m%s\033[0m"%"黑底")
#print("\033[0;37;41m%s\033[0m"%"红底")
#print("\033[0;37;42m%s\033[0m"%"绿底")
#print("\033[0;37;43m%s\033[0m"%"黄底")
#print("\033[0;37;44m%s\033[0m"%"蓝底")
#print("\033[0;37;45m%s\033[0m"%"紫红底")
#print("\033[0;37;46m%s\033[0m"%"青蓝底")
#print("\033[0;30;47m%s\033[0m"%"白底黑字")
