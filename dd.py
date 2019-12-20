# -*- coding:utf-8 -*-
# （1）启动后读取配置文件，加载命令并展示
# （2）:e可编辑配置文件，编辑完后:qw退出（实际上用了vi工具）
# （3）配置文件格式tag=value形式，例如（查看cpu使用率=ps aux)
import sys
import os
import utils

mainconf = "conf/menu.conf"
mainmenu = {}


def menu(file):
    utils.mkdir(os.path.dirname(file))
    menuId = 0
    menuDem = {}
    with open(file, "r+") as ff:
        for l in ff.readlines():
            kv = l.split("=")
            menuDem[str(menuId)] = kv
            menuId = menuId + 1
    return menuDem


mainmenu = menu(mainconf)


def showmenu(m):
    os.system("clear")
    for k in m.keys():
        print(k + ":" + m[k][0])


showmenu(mainmenu)
while True:
    a = raw_input("请选择：")
    if a == "e":
        os.system("vi " + mainconf)
    elif a == "m":
        # print("列出所有菜单")
        showmenu()
    else:
        if a in mainmenu.keys():
            v = mainmenu[a][1]#取菜单值,>表示进入子菜单
            if v.startswith(">"):
                print("进入子目录"+a[1:])
            else:
                os.system(v)
        else:
            print("无此选项")
            showmenu()
