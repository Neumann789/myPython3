'''
Created on 2017年9月19日

@author: fanghuabao
'''


var1 = "Hello World"
var2 = "Runoob"

print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])
print("已更新字符串:",var1[:6]+'Runoob')

if("H" in var1):
    print("H 在变量var1中")
else:
    print("H 不在变量var1中")
 
print(r"\n")      
print(R"\n")
print("\n")
print("end")

msg = '''
我是一个好人，你们是吗哈哈哈

Hello world！

'''

print("msg==>>",msg)
print('测试ord函数,查看字符在ASCII表中对应的数字')
print(ord('0'))
print(ord('a'))
print(ord('A'))
print(ord('\n'))


print("模糊匹配 有问题")
import re
match = re.match('Hell[\t]*(.*)world', 'hello python world')
strMatch = match.groups()
#print(strMatch)



