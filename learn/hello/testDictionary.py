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

Y = {'d': 1, 'b': 2, 'c': 3}
print(Y)
print(Y.keys())
print(list(Y.keys()))
YY = list(Y.keys())
YY.sort()
print(YY)

for key in YY:
    print(key, '=>', Y[key])


D = {'d': 4, 'r': 7}
print('f' in D)
print(not'f' in D)


