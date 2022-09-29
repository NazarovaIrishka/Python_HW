# Умный бот.
from random import randint, choice

messages = ['Возьмите конфеты','Ваш ход']

def introduce_players():
    player1 = input('Как Вас зовут?  ')
    player2 = 'Фиксик'
    print(f'Меня зовут {player2}')
    return [player1, player2]

def get_rules(players):
    n = int(input('Сколько будет кофет?  '))
    m = int(input('Сколько максимально будем брать конфет за один ход?  '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу  '))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('Ничья.')
else:
    print( f'Победитель {winer}! Заберите все конфеты!')


