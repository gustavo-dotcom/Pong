import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600                                                                           #Tamanho da tela definido para 1000 pixels por 600 pixels
window = pygame.display.set_mode((WIDTH, HEIGHT))                                                   #Criando uma janela vazia do pygame
pygame.display.set_caption("Pong")                                                                  #Atribuindo o nome da janela para Pong

BLUE = (0, 0, 255)                                                                                  #Variáveis da cor azul
RED = (255, 0, 0)                                                                                   #Variáveis da cor vermelha
BLACK = (0, 0, 0)

radius = 15                                                                                         #Raio da bola
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius                                                #Posição x e y da bola
ball_vel_x, ball_vel_y = 0.7, 0.7                                                                       #Velocidade da bola na posição x e y

paddle_width, paddle_height = 20, 120                                                               #Largura e altura das raquetes
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2                                         #Posição y das raquetes esquerda e direita
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)                #Posição x das raquetes esquerda e direita
left_paddle_vel = right_paddle_vel = 0

run = True
while run:                                                                                          #Loop principal do jogo onde vai acontecer todas as animações e eventos
    window.fill(BLACK)                                                                              #Preenche o fundo com a cor preta para que os objetos na janela tenham sua posição atualizada e "apaga" a posição antiga
    for i in pygame.event.get():                                                                    #Armazena os eventos coletados pelo event.get() na variável i 
        if i.type == pygame.QUIT:                                                                   #Verifica se o usuário precionou o botão de sair
            run = False
        elif i.type == pygame.KEYDOWN:                                                              #Movimento das raquetes direita e esquerda pelo uso das setas cima/baixo e w/s
            if i.type == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.type == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.type == pygame.K_w:
                left_paddle_vel = -0.9
            if i.type == pygame.K_s:
                left_paddle_vel = 0.9                    

    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:                                           #Verificando se a bola encosta nas bordas de cima ou baixo e se sim inverte a direção
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:                                                                    #Verifica se a bola encosta na borda direita e se sim define a posição da bola para a inical e inverte a direção
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius                    
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:                                                                        #Verifica se a bola encosta na borda esquerda e se sim define a posição para a inicial e redefine a direção para a inicial também
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.7, 0.7

    ball_x += ball_vel_x                                                                            #Movimento da bola em x
    ball_y += ball_vel_y                                                                            #Movimento da bola em y

    pygame.draw.circle(window, BLUE, (ball_x, ball_y), radius)                                      #Desenha a bola na janela
    pygame.draw.rect(window, RED, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))      #Variáveis da raquete esquerda
    pygame.draw.rect(window, RED, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))    #Variáveis da raquete direita
    pygame.display.update()