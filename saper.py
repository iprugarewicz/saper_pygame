import random
import sys
import run

sys.setrecursionlimit(10 ** 6)

bombs = []
bombs_pos = []
bmap = []
checked = []


def map_gen(x, y, n):
    global bombs
    global bmap
    global bombs_pos
    bombs = []
    bombs_pos = []
    bmap = []
    if n >= (x - 1) * (y - 1):
        print("dane nie maja sensu ")
    else:
        for i in range(x):
            row = []
            for j in range(y):
                bombs.append([i, j])
                row.append(0)
            bmap.append(row)
        for i in range(n):
            bomb = random.choice(bombs)
            bombs = bombs[:bombs.index(bomb)] + bombs[bombs.index(bomb) + 1:]
            bmap[(bomb[0])][(bomb[1])] = 10
            bombs_pos.append((bomb[0], bomb[1]))

        print("done")
    return (0)


def vars():
    for x in range(len(bmap)):

        for y in range(len(bmap[x])):

            if bmap[x][y] == 0:
                bomb_amount = 0
                up = False
                down = False
                left = False
                right = False

                if x != 0:  up = True
                if x != len(bmap) - 1: down = True
                if y != 0: left = True
                if y != len(bmap[1]) - 1: right = True

                if up == True and bmap[x - 1][y] == 10:
                    bomb_amount += 1

                if up == True and right == True and bmap[x - 1][y + 1] == 10:
                    bomb_amount += 1

                if right == True and bmap[x][y + 1] == 10:
                    bomb_amount += 1

                if right == True and down == True and 10 == bmap[x + 1][y + 1]:
                    bomb_amount += 1

                if down == True and bmap[x + 1][y] == 10:
                    bomb_amount += 1

                if down == True and left == True and bmap[x + 1][y - 1] == 10:
                    bomb_amount += 1

                if left == True and bmap[x][y - 1] == 10:
                    bomb_amount += 1

                if up == True and left == True and bmap[x - 1][y - 1] == 10:
                    bomb_amount += 1

                if bomb_amount != 0:
                    bmap[x][y] = bomb_amount

    return bmap


def check(x, y):
    if (x, y) in run.painted:
        return (0)
    run.painted.append((x, y))

    if bmap[x][y] != 0:
        return 0
    up = False
    down = False
    left = False
    right = False

    if x != 0:  up = True
    if x != len(bmap) - 1: down = True
    if y != 0: left = True
    if y != len(bmap[1]) - 1: right = True

    if up == True and bmap[x - 1][y] != 10:
        check(x - 1, y)

    if up == True and right == True and bmap[x - 1][y + 1] != 10:
        check(x - 1, y + 1)

    if right == True and bmap[x][y + 1] != 10:
        check(x , y + 1)

    if right == True and down == True and bmap[x + 1][y + 1] != 10:
        check(x + 1, y + 1)

    if down == True and bmap[x + 1][y] != 10:
        check(x + 1, y)
    if down == True and left == True and bmap[x + 1][y - 1] != 10:
        check(x + 1, y - 1)
    if left == True and bmap[x][y - 1] != 10:
        check(x, y - 1)
    if up == True and left == True and bmap[x - 1][y - 1] != 10:
        check(x - 1, y - 1)
    return 0


