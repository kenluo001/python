'''
Author: Ken Luo ken.luo.5227@gmail.com
Date: 2023-10-07 13:36:38
FilePath: /python/poker/Player.py
'''

class player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()