'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-30 23:42:30
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-09-30 23:42:42
FilePath: /python/python base/tupleandlist.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a), sys.getsizeof(b))    # 900120 800056

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))