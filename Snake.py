import pygame
from pygame.locals import *
from sys import exit
from random import randint

# cores
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (20, 255, 20)

# inicializa o pygame
pygame.init()

# dimensões da tela
width = 1280
height = 720

# posicao inicial da cobra
x_cobra = int(width/2) 
y_cobra = int(height/2)

velocidade = 20
x_controle = velocidade
y_controle = 0

# posicao da comida
x_maca = randint(2, 63) * 20
y_maca = randint(5, 35) * 20

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
gameOver = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, green, (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, gameOver
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(width/2) 
    y_cobra = int(height/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(2, 63) * 20
    y_maca = randint(5, 35) * 20
    gameOver = False

while True:
    relogio.tick(30)
    tela.fill(white)
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, black)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
    cobra = pygame.draw.rect(tela, green, (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, red, (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(2, 63) * 20
        y_maca = randint(5, 35) * 20
        pontos += 1
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, black)
        ret_texto = texto_formatado.get_rect()

        gameOver = True
        while gameOver:
            tela.fill(white)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (width//2, height//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    
    if x_cobra > width:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = width
    if y_cobra < 0:
        y_cobra = height
    if y_cobra > height:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (550,30))

    
    pygame.display.update()