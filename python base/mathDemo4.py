'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-10-01 09:52:46
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-10-01 09:52:49
FilePath: /python/mathDemo4.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# 用星号表达式来表示args可以接收0个或任意多个参数
def add(*args):
    total = 0
    # 可变参数可以放在for循环中取出每个参数的值
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))