'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-30 23:45:50
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-09-30 23:52:31
FilePath: /python/python base/string.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
s1 = 'hello, world!'
s2 = "你好，世界！"
print(s1, s2)
# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello, 
world!
'''
print(s3, end='')

s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)

# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = 'hello' + ' ' + 'world'
print(s1)    # hello world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2     # s1 = s1 + s2
print(s1)    # hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # hello world!!!hello world!!!

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)      # False True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = '骆昊'
print(ord('罗'), ord('尧'))               # 39558 26122
s4 = '王大锤'
print(ord('王'), ord('大'), ord('锤'))    # 29579 22823 38180
print(s3 > s4, s3 <= s4)      # True False

s1 = 'hello world'
s2 = 'hello world'
s3 = s2
# 比较字符串的内容
print(s1 == s2, s2 == s3)    # True True
# 比较字符串的内存地址
print(s1 is s2, s2 is s3)    # False True

s1 = 'hello, world'
print('wo' in s1)    # True
s2 = 'goodbye'
print(s2 in s1)      # False

s = 'hello, world'
print(len(s))                   # 12
print(len('goodbye, world'))    # 14

s = 'abc123456'
N = len(s)

# 获取第一个字符
print(s[0], s[-N])    # a a

# 获取最后一个字符
print(s[N-1], s[-1])  # 6 6

# 获取索引为2或-7的字符
print(s[2], s[-7])    # c c

# 获取索引为5和-4的字符
print(s[5], s[-4])    # 3 3

s1 = 'hello'
for index in range(len(s1)):
    print(s1[index])

s1 = 'hello'
for ch in s1:
    print(ch)

s1 = 'hello, world!'

# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())   # Hello, world!
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())        # Hello, World!
# 使用upper方法获得字符串大写后的字符串
print(s1.upper())        # HELLO, WORLD!

s2 = 'GOODBYE'
# 使用lower方法获得字符串小写后的字符串
print(s2.lower())        # goodbye

s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('shit'))      # -1
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8
# 找不到引发异常
# print(s.index('shit'))     # ValueError: substring not found

s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12