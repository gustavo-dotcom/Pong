import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600                               #Tamanho da tela definido para 1000 pixels por 600 pixels
window = pygame.display.set_mode((WIDTH, HEIGHT))       #Criando uma janela vazia do pygame
run = True
while run:                                              #Loop principal do jogo onde vai acontecer todas as animações e eventos
    for i in pygame.event.get():                        #Armazena os eventos coletados pelo event.get() na variável i 
        if i.type == pygame.QUIT:                       #Verifica se o usuário precionou o botão de sair
            run = False