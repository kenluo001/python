'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-10-01 09:52:15
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-10-01 09:52:18
FilePath: /python/mathDemo3.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，那么该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，1和2分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6
# 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
print(add(c=50, a=100, b=200))    # 350