import Poker
import Player


poker = Poker.poker()
poker.shuffle()

players = [Player.player('东邪'), Player.player('西毒'), Player.player('南帝'), Player.player('北丐')]


for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)