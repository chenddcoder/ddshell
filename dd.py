# -*- coding:utf-8 -*-
#（1）启动后读取配置文件，加载命令并展示
#（2）:e可编辑配置文件，编辑完后:qw退出（实际上用了vi工具）
#（3）配置文件格式tag=value形式，例如（查看cpu使用率=ps aux)
import sys
import os
import utils
mainconf="conf/main.conf"
mainmenu={}
def menu(file):
    utils.mkdir(os.path.dirname(file))
    menuId=0
    menuDem={}
    with open(file,"r+") as ff:
        for l in ff.readlines():
            kv=l.split("=")
            menuDem[str(menuId)]=kv
            menuId=menuId+1
    return menuDem
mainmenu=menu(mainconf)
def showmenu():
    os.system("clear")
    for k in mainmenu.keys():
        print(k+":"+mainmenu[k][0])
showmenu()
while True:
    a=input("请选择：")
    if a=="e":
        os.system("vi "+mainconf)
    elif a=="m":
        # print("列出所有菜单")
        showmenu()
    else:
        if a in mainmenu.keys():
            os.system(mainmenu[a][1])
        else:
            print("无此选项")
            showmenu()




