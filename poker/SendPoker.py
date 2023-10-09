'''
Author: Ken Luo ken.luo.5227@gmail.com
Date: 2023-10-07 13:37:53
FilePath: /python/poker/SendPoker.py
'''
import Poker
import Player


poker = Poker.poker()
poker.shuffle()

players = [Player.player('老婆'), Player.player('儿子'), Player.player('女儿'), Player.player('我')]


for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)