'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-30 23:54:43
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-09-30 23:57:19
FilePath: /python/python base/setDemo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# 创建集合的字面量语法(重复元素不会出现在集合中)
set1 = {1, 2, 3, 3, 3, 2}
print(set1)         # {1, 2, 3}
print(len(set1))    # 3

# 创建集合的构造器语法(后面会讲到什么是构造器)
set2 = set('hello')
print(set2)         # {'h', 'l', 'o', 'e'}

# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)         # {1, 2, 3}

# 创建集合的生成式语法(将列表生成式的[]换成{})
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)         # {3, 5, 6, 9, 10, 12, 15, 18}

# 集合元素的循环遍历
for elem in set4:
    print(elem)

set1 = {11, 12, 13, 14, 15}
print(10 in set1)        # False 
print(15 in set1)        # True
set2 = {'Python', 'Java', 'Go', 'Swift'}
print('Ruby' in set2)    # False
print('Java' in set2)    # True

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
# 方法一: 使用 & 运算符
print(set1 & set2)                # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2))    # {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1 | set2)         # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用union方法
print(set1.union(set2))    # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
# 方法一: 使用 - 运算符
print(set1 - set2)              # {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2))    # {1, 3, 5, 7}

# 对称差
# 方法一: 使用 ^ 运算符
print(set1 ^ set2)                        # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2))    # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2))      # {1, 3, 5, 7, 8, 10}


# 创建一个空集合
set1 = set()

# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})
print(set1)    # {33, 1, 100, 55, 1000, 10}

# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
print(set1)    # {1, 10, 33, 55, 1000}

# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 10 in set1:
    set1.remove(10)
print(set1)    # {33, 1, 55, 1000}

# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())

# clear方法可以清空整个集合
set1.clear()

print(set1)    # set()