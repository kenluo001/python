'''
Author: “kenluo001” “ken.luo.5227@gmail.com”
Date: 2023-10-01 09:58:10
LastEditors: “kenluo001” “ken.luo.5227@gmail.com”
LastEditTime: 2023-10-01 09:58:13
FilePath: /python/moduleTest6.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    """生成指定长度的验证码
    
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))