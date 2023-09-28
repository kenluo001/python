'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-09-16 17:01:48
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-09-28 20:10:47
FilePath: /python/python base/for.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# for 

for i in range(1,10):
    print(i)

sum = 0
for x in range(101):
    sum += x
print(sum)

print('------------------------------------')

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    print()