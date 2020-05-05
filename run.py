import pygame
import sys
import saper

sys.setrecursionlimit(10 ** 6)
# pygame i generalnie rysowanie


pygame.init()

x = 20
y = 20
box = 19
space = 0
max_tps = 600
sizex = ((box + space) * x) + space
sizey = ((box + space) * y) + space
screen = pygame.display.set_mode((sizex, sizey))

painted = []

img0 = pygame.image.load('0.png')
img1 = pygame.image.load('1.png')
img2 = pygame.image.load('2.png')
img3 = pygame.image.load('3.png')
img4 = pygame.image.load('4.png')
img5 = pygame.image.load('5.png')
img6 = pygame.image.load('6.png')
img7 = pygame.image.load('7.png')
img8 = pygame.image.load('8.png')
img9 = pygame.image.load('tile.png')
img10 = pygame.image.load('bomb.png')
images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]

# saper
n = 40
play = True

saper.map_gen(y, x, n)
saper.vars()
for i in saper.bmap:
    print(i)

while play:
    # eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    # myszka
    mpos = pygame.mouse.get_pos()

    mclick = pygame.mouse.get_pressed()

    screen.fill((195, 195, 195))

    for j, j2 in zip(range(0, sizey, (box + space)), range(y)):
        pygame.draw.rect(screen, (127, 127, 127), (0, j, sizex, space))
        for i, i2 in zip(range(0, sizex, (box + space)), range(x)):
            pygame.draw.rect(screen, (127, 127, 127), (i, j, space, (box + space)))
            if i < mpos[0] < (i + (box + space)):
                if j < mpos[1] < (j + (box + space)):
                    if mclick[0] == 1 and (j2, i2) not in painted:
                        if saper.bmap[j2][i2] == 10:
                            play = False
                        saper.check(j2, i2)
                    elif mclick[1] == 1 and (j2, i2) not in painted:
                        pass

                        #tu można zrobić flagi

            if (j2, i2) in painted:
                screen.blit(images[saper.bmap[j2][i2]], [i + space, j + space])
            else:
                screen.blit(images[9], [i + space, j + space])
    if not play:
        for bomb in saper.bombs_pos:
            screen.blit(images[10], [(bomb[1] + space) * box, (bomb[0] + space) * box])
    pygame.draw.rect(screen, (127, 127, 127), (sizex - space, 0, space, sizey))
    pygame.draw.rect(screen, (127, 127, 127), (0, sizey - space, sizex, space))
    pygame.display.flip()
