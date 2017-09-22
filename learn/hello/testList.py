# -*- coding: UTF-8 -*-


print('序列操作')

L = [123, 'SPAM', '2222']

print(len(L))
print(L)
L.append('NI')
print(L[-1])

print("列表嵌套")
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(M)
print(M[1])

print("列表解析")
print("从嵌套列表中提取第二列")
col2 = [row[1] for row in M]
print(col2)

print("从嵌套列表中提取第二列,并对此列的没每一个元素值加10")
col2 = [row[1]+10 for row in M]
print(col2)

print("从嵌套列表中提取第三列")
col3 = [row[2] for row in M]
print(col3)

print("从嵌套列表中提取第三列中，元素为偶数的集合")
col3 = [row[2] for row in M if row[2] % 2 == 0]
print(col3)








