# Задача с конфетами. Человек против человека.
import random

messages = ['Возьмите конфеты', 'Ваш ход']


def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print('Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]


player1 = input('Имя первого игровка:  ')
player2 = input('Имя второго игровка:  ')
players = [player1, player2]

n = int(input('Сколько у вас конфет?  '))
m = int(input('Сколько максимально будем брать конфет за один ход? '))

winer = play_game(n, m, players, messages)
if not winer:
    print('Ничья.')
else: print(f'Победитель {winer}! Забери все конфеты!')