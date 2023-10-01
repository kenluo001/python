'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-10-01 09:50:14
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-10-01 09:50:18
FilePath: /python/mathDemo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# 定义函数：def是定义函数的关键字、fac是函数名，num是参数（自变量）
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    # 返回num的阶乘（因变量）
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))