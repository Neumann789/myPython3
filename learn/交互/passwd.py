# -*- coding:utf8 -*-
# 练习input 输入不显示
#  Created by fanghuabao on 2017/9/25.

import getpass

username = input("username:")
# passwd = input("passwd:")
# getpass在编辑工具中运行不好使，在命令行使用是可以的
passwd = getpass.getpass("passwd:")

print(username, passwd)
