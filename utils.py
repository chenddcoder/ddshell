# -*- coding:utf-8 -*-
# 引入模块
import os


# 创建文件夹
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path+' 目录已存在')
        return False


# 读取配置文件，返回List<map>
def config(path):
    mkdir(os.path.dirname(path))
    # 数组返回
    menuDem = []
    if not os.path.exists(path):
        return menuDem
    with open(path, "r+") as ff:
        for l in ff.readlines():
            l = l.strip()
            kv = l.split("=", 2)
            menuDem.append(kv)
    return menuDem


# 返回拼接目录
def subdir(path, sub):
    return path + "/" + sub


# 返回上级目录
def predir(path):
    return path.rsplit("/", 2)[0]


def showmenu(path):
    menu = config(menuconf(path))
    showmenuV(menu, path)
    return menu


def showmenuV(m, path):
    os.system("clear")
    print("===============" + path + "================")
    print("e:编辑")
    for i in range(len(m)):
        print(str(i) + ":" + m[i][0])
    print("q:退出")


def menuconf(path):
    path = path.strip()
    return path + "/menu.conf"
