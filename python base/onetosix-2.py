'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-28 20:25:55
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-09-28 20:26:09
FilePath: /python/python base/onetosix-2.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import random

counters = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')