import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (10, 10, 255)

width = 640
height = 480

x_cobra = int(width/2)
y_cobra = int(height/2)
              
vel = 10
x_control = vel
y_control = 0

xc = randint(40, 600)
yc = randint(50, 430)

pontos = 0
font = pygame.font.SysFont('arial', 40, bold=True)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

listC = []
comprimentoIni = 5
gameOver= False

def upCobra(listC):
    for XeY in listC:
        pygame.draw.rect(screen, green, (XeY[0], XeY[1], 20, 20))

def reset():
    global pontos, comprimentoIni, x_cobra, y_cobra, listC, listCab, xc, yc, gameOver
    pontos = 0
    comprimentoIni = 5
    x_cobra = int(width/2)
    y_cobra = int(height/2)
    listC = []
    listCab = []
    xc = randint(40, 600)
    yc = randint(50, 430)
    gameOver = False

while True:
    clock.tick(30)
    screen.fill((255, 255, 255))
    mens = f'Pontos: {pontos}'
    txtF = font.render(mens, True, black)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == vel:
                    pass
                else:
                    x_control = -vel
                    y_control = 0
            if event.key == K_d:
                if x_control == -vel:
                    pass
                else:
                    x_control = vel
                    y_control = 0
            if event.key == K_w:
                if y_control == vel:
                    pass
                else:
                    y_control = -vel
                    x_control = 0
            if event.key == K_s:
                if y_control == -vel:
                    pass
                else:
                    y_control = vel
                    x_control = 0
            
        x_cobra += x_control
        y_cobra += y_control

        cobra = pygame.draw.rect(screen, (green), (x_cobra, y_cobra, 20, 20))
        com = pygame.draw.rect(screen, red, (xc, yc, 20, 20))

        if cobra.collidedict(com):
            xc = randint(40, 600)
            yc = randint(50, 430)
            pontos += 1
            comprimentoIni += 1

        listCab = []
        listCab.append(x_cobra)
        listCab.append(y_cobra)

        listC.append(listCab)

        if listC.count(listCab) > 1:
            fonte = pygame.font.SysFont('arial', 20, True, False)
            mens = 'Game over! Precione R para jogar novamente'
            textF = fonte.render(mens, True, white)
            retTxt = textF.get_rect()
            gameOver = True
            while gameOver:
                screen.fill(white)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reset()
                retTxt.center = (width/2, height/2)
                screen.blit(txtF, retTxt)
                pygame.display.update()

        if x_cobra > width:
            x_cobra = 0
        if x_cobra < 0:
            x_cobra = width
        if y_cobra < 0:
            y_cobra = height
        if y_cobra > height:
            y_cobra = 0
        
        if len(listC) > comprimentoIni:
            del listC[0]

        upCobra(listC)

        screen.blit(txtF, (450, 40))

        pygame.display.update()
