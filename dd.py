# -*- coding:utf-8 -*-
# （1）启动后读取配置文件，加载命令并展示
# （2）:e可编辑配置文件，编辑完后:qw退出（实际上用了vi工具）
# （3）配置文件格式tag=value形式，例如（查看cpu使用率=ps aux)
import os
import utils

path = "conf"  # 全局路径，初始路径
menu = utils.showmenu(path)
while True:
    a = raw_input("请选择：")
    if a == "e":
        os.system("vi " + utils.menuconf(path))
    elif a == "m":
        print("列出所有菜单")
        menu = utils.showmenu(path)
    elif a == "q":
        if path == "conf":
            break
        path = utils.predir(path)
        menu = utils.showmenu(path)
    elif a.isdigit():
        num = int(a)  # 菜单编号
        if num < len(menu):
            v = menu[num][1]  # 取菜单值,>表示进入子菜单
            if v.startswith(">"):
                sub = v[1:]
                path = utils.subdir(path, sub)
                menu = utils.showmenu(path)
            else:
                os.system(v)
        else:
            print("无此选项")
            menu = utils.showmenu(path)
    else:
        print("无效操作")
