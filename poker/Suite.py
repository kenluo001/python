from enum import Enum

class suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
# for suite1 in suite:
#     print(f'{suite1}: {suite1.value}')

# class Suite(Enum):
#     """花色(枚举)"""
#     SPADE = 0
#     HEART = 1
#     CLUB = 2
#     DIAMOND = 3

# print(Suite.SPADE.value)
