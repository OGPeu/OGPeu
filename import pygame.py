import pygame
import time
import random

# Inicializa o pygame
pygame.init()

# Definir as cores
branco = (0, 0, 0)
preto = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (4, 255, 4)

# Definir o tamanho da tela
largura = 600
altura = 400

# Definir o tamanho do bloco da cobrinha e a velocidade
tamanho_bloco = 10
velocidade = 10

# Criar a tela do jogo
tela = pygame.display.set_mode((largura, altura))

# Definir o relógio do jogo
relogio = pygame.time.Clock()

# Definir as fontes
fonte = pygame.font.SysFont("bahnschrift", 25)

def pontuacao(score):
    valor = fonte.render("Pontuação: " + str(score), True, preto)
    tela.blit(valor, [0, 0])

def nossa_cobrinha(tamanho_bloco, lista_cobrinha):
    for bloco in lista_cobrinha:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    fim_de_jogo = False
    game_over = False

    x = largura / 2
    y = altura / 2

    x_mudanca = 0
    y_mudanca = 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not fim_de_jogo:

        while game_over:
            tela.fill(branco)
            mensagem("Você perdeu! Pressione C para jogar novamente ou Q para sair", vermelho)
            pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_de_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True
        x += x_mudanca
        y += y_mudanca
        tela.fill(branco)

        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca_cobrinha = []
        cabeca_cobrinha.append(x)
        cabeca_cobrinha.append(y)
        lista_cobrinha.append(cabeca_cobrinha)
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]

        for bloco in lista_cobrinha[:-1]:
            if bloco == cabeca_cobrinha:
                game_over = True

        nossa_cobrinha(tamanho_bloco, lista_cobrinha)
        pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobrinha += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()
