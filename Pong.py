import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600                                                                           #Tamanho da tela definido para 1000 pixels por 600 pixels
window = pygame.display.set_mode((WIDTH, HEIGHT))                                                   #Criando uma janela vazia do pygame
pygame.display.set_caption("Pong")                                                                  #Atribuindo o nome da janela para Pong

BLUE = (0, 0, 255)                                                                                  #Variáveis da cor azul

radius = 15                                                                                         #Raio da bola
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius                                                #Posição x e y da bola

run = True
while run:                                                                                          #Loop principal do jogo onde vai acontecer todas as animações e eventos
    for i in pygame.event.get():                                                                    #Armazena os eventos coletados pelo event.get() na variável i 
        if i.type == pygame.QUIT:                                                                   #Verifica se o usuário precionou o botão de sair
            run = False
    pygame.draw.circle(window, BLUE, (ball_x, ball_y), radius)                                      #Desenha a bola na janela
    pygame.draw.rect(window, RED, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))      #Variáveis da raquete esquerda
    pygame.draw.rect(window, RED, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))    #Variáveis da raquete direita
    pygame.display.update()