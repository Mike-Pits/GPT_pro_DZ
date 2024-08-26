'''
Попробуйте написать простую карточную игру. Играют два игрока - player_1 и player_2. У каждого из них по 6 карт.

player_1 = [6, 10, 7, 8, 9, 6]
player_2 = [10, 7, 9, 6, 10, 7]
Необходимо, используя операторы for, if и elif, сыграть одну партию. Игроки ходят по очереди, и тот, у кого достоинство карты больше, забирает себе карту противника. Сыгранные карты больше не используются. Достоинства карт в списке берутся по порядку, например:

первый ход: (6, 10);
второй ход: (10, 7).
Побеждает тот, у кого по окончании игры на руках меньшая сумма достоинств карт.

Кто победил, player_1 или player_2?
'''

player_1 = [6, 10, 7, 8, 9, 6]
player_2 = [10, 7, 9, 6, 10, 7]

player_1_gain = 0
player_2_gain = 0

for n in range(len(player_1)):
  if player_1[n] > player_2[n]:
    player_1_gain += player_2[n]
  else:
    player_2_gain += player_1[n]

if player_1_gain > player_2_gain:
  print(f'The winner is Player_1 with the score {player_1_gain}')
else:
  print(f'The winner is Player_2 with the score {player_2_gain}')