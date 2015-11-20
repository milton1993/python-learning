__author__ = 'milton'
#coding=utf-8

# try:
#     f = open('/home/milton/todo', 'r')
#     content = f.read()
#     print(content)
# finally:
#     f.close()

# try...finally比较麻烦，使用with语句可以自动调用close()方法
with open('/home/milton/todo', 'r') as f:
    # print f.read()

    for line in f.readlines():
        print(line.strip())

#读取二进制文件
with open('/home/milton/software/eclipse/icon.xpm', 'rb') as f:
    print f.read()

#读取非ASCII编码德文件
# with open('/home/milton/downloads/aaa.txt', 'rb') as f:
#     # print f.read()
#     print f.read().decode('gb2312')
#
# #使用codecs自动转换编码
# import codecs
# with codecs.open('/home/milton/downloads/aaa.txt', 'r', 'gb2312') as f:
#     print f.read()
#
# with codecs.open('/home/milton/downloads/aaa.txt', 'w', 'gb2312') as f:
#     f.write('abc')

for line in open('/home/milton/todo', 'r'):
    print line