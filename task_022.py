# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# from random import randint

# a = int(input('Введите количество конфет'))
# hod = 0
# wins = {0: 'Игрок', 1: 'Бот'}
# while a > 0:
#    if a <= 28:
#        print(f'Выиграл {wins[hod]}')
#        break
#    if hod % 2 == 0:
#        print('Ход Игрока')
#        d = int(input('Введите количество конфет, которое хотите взять'))
#        a -= d
#        print(f'Осталось конфет: {a}')
#    else:
#        print('Ход Бота')
#        d = a % 29
#        a -= d
#        print(f'Осталось конфет: {a}')
#    hod = (hod + 1) % 2

# def kto_viigral(doska):
#     pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# for x in pobeda:
#    if doska[x[0]] == doska[x[1]] == doska[x[2]]:
#  return doska[x[0]]
# return False

# def igra(doska):
# count = 0
# win = False
# while not win:
# draw_board(doska)
# if count % 2 == 0:
# stavim_hod("X")
# else:
# stavim_hod("O")
# count += 1
# if count > 4:
# m = kto_viigral(doska)
# if m:
# print (m, "Победил!")
# win = True
# break
#      if count == 9:
#        print ("Победила дружба!")
# break
# draw_board(doska)

# igra(doska)





from random import randint as rnd
dificult = None
can_take = None
gm_pl = None
players = ''

print('Игра в конфетки!')
print('Выбор варианта игры\n1: против ПК\n2: Вдвоем')

gm_pl = int(input('Номер варианта? : '))
while True and (gm_pl > 2 or gm_pl < 1):
    gm_pl = int(input('неверный ввод исправьте: '))

players = [input(f"Введите ник {i+1}-го игрока : ") for i in range(gm_pl)]

if gm_pl==1:
    players.append("PC")
    dificult = input('Выберите сложность:\n"новичек" "профи"\nВаш выбор: ')
    print(f'Если решка то первым ходит - {players[gm_pl-1]}, \n'
          f'Если орел то PC\n')
else:
    print(f'Если решка то первым ходит - {players[gm_pl - 2]}, \n'
          f'Если орел то {players[gm_pl - 1]}')


candy= int(input(f'Введите сколько конфет хотите разыграть?: \nВаш выбор= '))
if candy <= 7:
    print('У вас нечего делить:)\nКонец Игры!')
    quit()
elif 7 < candy < 30:
    can_take = rnd(4, candy//3)
else:
    can_take = candy * 2//100 + rnd(5, 11)


print(f'Правила игры:\nСложность !!! {dificult} !!!\nЗа один ход можно забрать не более чем {can_take} конфет.\n'
      'Все конфеты оппонента достаются сделавшему последний ход.')


def coin():
    if rnd(1, 100) % 2 == 0:
        print(f'\n<<<Орел>>>\n')
        return 1
    else:
        print(f"\n<<<Решка>>>\n")
        return 0


start = coin()


while candy > 0:
    for player in players:
        print(f'Игрок {player} ваш выбор\n'
              f' <<  {candy}  >> конфет осталось')
        if player == 'PC':
            if dificult != 'профи':
                chose = rnd(1, candy % can_take)
            else:
                if candy / can_take >= 1 and candy % can_take >= 2:
                    chose = candy % can_take - 1
                elif candy / can_take >= 1 and 0 <= candy % can_take < 2:
                    chose = can_take - rnd(1, can_take-1)
                else:
                    if candy % can_take > 0:
                        chose = rnd(1, candy % can_take + 1)
                    else:
                        chose = candy
            print(f'  PC choice  <<  {chose}  >>  ')
        else:
            chose = int(input(f'Сколько конфет берете? : '))
        if 1 <= chose <= can_take:
            pass
        else:
            while True and (chose < 1 or chose > can_take):
                chose = int(input('!!!вы вышли за рамки правил,\n'
                                  'так сколько забираете? : '))
        candy -= chose
        if candy == 0 and candy >= 0:
            print(f'    <<<  Winner - {player}  >>>')