'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-30 23:58:30
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-10-01 00:00:44
FilePath: /python/python base/dictionaryDemo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)


# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)    # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)    # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print(len(person))    # 4
for key in person:
    print(key)

person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
# 检查name和tel两个键在不在person字典中
print('name' in person, 'tel' in person)    # True False
# 通过age修将person字典中对应的值修改为25
if 'age' in person:
    person['age'] = 25
# 通过索引操作向person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print('name' in person, 'tel' in person)    # True True
# 检查person字典中键值对的数量
print(len(person))    # 6
# 对字典的键进行循环并通索引运算获取键对应的值
for key in person:
    print(f'{key}: {person[key]}')