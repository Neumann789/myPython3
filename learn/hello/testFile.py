# -*- coding: UTF-8 -*-



def testfilewrite():
    f = open("data.txt", 'w')               # 'r' is the default procesing mode
    f.write('Hello\n')
    f.close()   # 关闭的时候才真正将内容输出到data.txt文件中

def testfileread():
    fr = open('data.txt')
    text = fr.read()
    print(text)

# testfilewrite()
testfileread()




