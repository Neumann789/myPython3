# -*- coding:utf8 -*-
# 练习if else的使用
#  Created by fanghuabao on 2017/9/25.


_username = 'fhb'
_passwd = 'fhb'

username = input('username:')
passwd = input('passwd:')

if _username == username and _passwd == passwd:
    print('welcom user {name} login ...'.format(name=username))

elif _username != username:
    print('username is wrong')
else:
    print('password is wrong!')

