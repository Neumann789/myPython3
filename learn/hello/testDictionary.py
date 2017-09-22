# 练习字典
# -*- coding: UTF-8 -*-

print("创建字典方式一")
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quantity'] += 1
print(D)

print('创建字典方式二')
A = {}
A['name'] = 'Bob'
A['job'] = 'dev'
A['age'] = 40
print(A)
print(A['name'])

print('字典重访嵌套')
M = {
    'name': {'first': 'Bob', 'last': 'smith'},
    'job': ['dev', 'mgr'],
    'age': 40.5
}
print(M)
print(M['name'])
