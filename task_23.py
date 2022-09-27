# Создайте программу для игры в ""Крестики-нолики"".




# from turtle import *


# p1 = Turtle()
# p1.shape('triangle')
# p1.color('green')
# p1.penup()
# p1.goto(-30, 90)


# p2 = Turtle()
# p2.shape('triangle')
# p2.color('blue')
# p2.penup()
# p2.goto(-30, 0)



# def squad_f(f, x, y):
#     f.penup()
#     f.goto(x + 30, y)
#     f.pendown()
#     f.goto(x + 30, y + 30)
#     f.goto(x, y + 30)
#     f.goto(x, y)


# def game_place():
#     gp = Turtle()
#     gp.speed(0)
#     gp.color('red')
#     gp.begin_fill()
#     for x in range(0, 61, 30):
#         for y in range(0, 61, 30):
#             squad_f(gp, x, y)
#     gp.penup()
#     gp.goto(0, 0)
#     gp.pendown()
#     gp.goto(90, 0)
#     gp.hideturtle()


# game_place()


# def get_area1(x, y):
#     begin_fill()
#     p1.pendown()
#     p1.goto(x, y)
#     p1.filling()
#     p2.end_fill()


# p1.ondrag(goto, btn=1, add=())


# def get_area2(x, y):
#     p2.begin_fill()
#     p2.pendown()
#     p2.goto(x, y)
#     p2.filling()
#     p2.end_fill()

# p2.ondrag(goto, btn=2, add=())


# done(


maps=[1, 2, 3, 
      4, 5, 6, 
      7, 8, 9]
victories=[[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8]]
def print_maps():
    print(maps[0], end= '')
    print(maps[1], end='')
    print(maps[2])

    print(maps[3], end='')
    print(maps[4], end='')
    print(maps[5])

    print(maps[6], end='')
    print(maps[7], end='')
    print(maps[8])

def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ''

    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] =='X' and maps[i[2]] == 'X':
           win = 'X'
        if maps[i[0]] =='O' and maps[i[1]] =='O'and maps[i[2]] == 'O':
           win= 'O'
    return win

game_over = False
player1 = True

while game_over == False:
    print_maps()
    
    if player1 == True:
       symbol = 'X'
       step = int(input('Игрок 1, ваш ход: '))
    else:
       symbol = 'O'
       step = int(input('Игрок 2, ваш ход: '))

    step_maps(step, symbol)
    win = get_result()
    if win  != '':
        game_over = True
    else:
        game_over = False
    player1 = not(player1) 
print_maps()
print('Победил', win)           
