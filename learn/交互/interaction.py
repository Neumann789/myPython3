# -*- coding:utf8 -*-
# 交互
#  Created by fanghuabao on 2017/9/24.

# username = input("username:")
# password = input("password:")
# print('username,password', username, password)

name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")

# 使用字符串拼接的方式 会在内存中开辟多块空间 性能不好 建议不要使用
info = '''
---------------- info '''+name+'''----------------
Name:'''+name+'''
Age:'''+str(age)+'''
Salary:'''+salary+'''
'''

info2 = '''
---------------- info %s----------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

info3 = '''
---------------- info {_name}----------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

info4 = '''
---------------- info {0}----------------
Name:{1}
Age:{2}
Job:{3}
Salary:{4}
'''.format(name, name, age, job, salary)


# print(info)
print(info4)

