import pygame
import sys
import saper

sys.setrecursionlimit(10 ** 6)
# pygame i generalnie rysowanie


pygame.init()

x = 20
y = 20
box = 19
max_tps = 600
sizex = ((box+1) * x) + 1
sizey = ((box+1) * y) + 1
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
img9 = pygame.image.load('bomb.png')
images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, 0, img9]

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

    screen.fill((0, 0, 0))

    for j, j2 in zip(range(0, sizey, (box+1)), range(y)):
        pygame.draw.rect(screen, (255, 0, 255), (0, j, sizex, 1))
        for i, i2 in zip(range(0, sizex, (box+1)), range(x)):
            pygame.draw.rect(screen, (255, 0, 255), (i, j, 1, (box+1)))
            if i < mpos[0] < (i + (box+1)):
                if j < mpos[1] < (j + (box+1)):
                    pygame.draw.rect(screen, (0, 255, 0), (i + 1, j + 1, box, box))
                    if mclick[0] == 1 and (j2, i2) not in painted:
                        if saper.bmap[j2][i2] == 10:
                            play = False
                        saper.check(j2, i2)
            if (j2, i2) in painted:
                screen.blit(images[saper.bmap[j2][i2]], [i + 1, j + 1])
    pygame.draw.rect(screen, (255, 0, 255), (sizex - 1, 0, 1, sizey))
    pygame.draw.rect(screen, (255, 0, 255), (0, sizey - 1, sizex, 1))
    pygame.display.flip()
