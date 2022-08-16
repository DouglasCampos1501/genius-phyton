import pygame
import time
from random import randrange


#definir as cores do jogo
white = (255, 255, 255)
grey = (100, 100, 100)
black = (0, 0, 0)
red = (255, 100, 100)
redDark = (200, 0, 0)
yellow = (255, 255, 150)
yellowDark = (255, 255, 0)
green = (100, 255, 100)
greenDark = (0, 200, 0)
blue = (150, 150, 255)
blueDark = (0, 0, 255)


window = pygame.display.set_mode((600, 600))
window.fill(white)

#Upando textos em cima da imagem
pygame.font.init()
fontGame = pygame.font.SysFont("Comic Sans MS", 35)

def start(window):
    pygame.draw.rect(window, greenDark, (100, 100, 200, 200))
    pygame.draw.rect(window, redDark, (300, 100, 200, 200))
    pygame.draw.rect(window, yellowDark, (100, 300, 200, 200))
    pygame.draw.rect(window, blueDark, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()

def buttonGreen(window):
    pygame.draw.rect(window, green, (100, 100, 200, 200))
    pygame.draw.rect(window, redDark, (300, 100, 200, 200))
    pygame.draw.rect(window, yellowDark, (100, 300, 200, 200))
    pygame.draw.rect(window, blueDark, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()

def buttonRed(window):
    pygame.draw.rect(window, greenDark, (100, 100, 200, 200))
    pygame.draw.rect(window, red, (300, 100, 200, 200))
    pygame.draw.rect(window, yellowDark, (100, 300, 200, 200))
    pygame.draw.rect(window, blueDark, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()

def buttonYellow(window):
    pygame.draw.rect(window, greenDark, (100, 100, 200, 200))
    pygame.draw.rect(window, redDark, (300, 100, 200, 200))
    pygame.draw.rect(window, yellow, (100, 300, 200, 200))
    pygame.draw.rect(window, blueDark, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()

def buttonBlue(window):
    pygame.draw.rect(window, greenDark, (100, 100, 200, 200))
    pygame.draw.rect(window, redDark, (300, 100, 200, 200))
    pygame.draw.rect(window, yellowDark, (100, 300, 200, 200))
    pygame.draw.rect(window, blue, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()

def buttonCenter(window):
    pygame.draw.rect(window, greenDark, (100, 100, 200, 200))
    pygame.draw.rect(window, redDark, (300, 100, 200, 200))
    pygame.draw.rect(window, yellowDark, (100, 300, 200, 200))
    pygame.draw.rect(window, blueDark, (300, 300, 200, 200))
    pygame.draw.rect(window, black, (100, 300, 400, 10))
    pygame.draw.rect(window, black, (300, 100, 10, 400))
    pygame.draw.circle(window, white, (300, 300), 300, 100)
    pygame.draw.circle(window, black, (300, 300), 90)
    pygame.draw.circle(window, black, (300, 300), 210, 10)
    pygame.draw.circle(window, grey, (300, 300), 80)
    text = fontGame.render("PAFT", 1, white)
    window.blit(text, (260, 275))
    pygame.display.update()


clickActive = 0
gameSequence = []
colorRepet = 0
result = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Pegar a posição do mouse
    mouse = pygame.mouse.get_pos()
    #Testando a posição so mouse
    #print(mouse)

    #Pegar o click do mouse
    click = pygame.mouse.get_pressed()

    #Repetir as cores
    if colorRepet == 1:
        start(window)
        time.sleep(1)
        for i in range(len(gameSequence)):
            pygame.draw.rect(window, white, (0, 0, 500, 50))
            text = fontGame.render(str(i + 1) + ' - ' + str(len(gameSequence)), 1, black)
            window.blit(text, (10, 10))
            pygame.display.update()
            if gameSequence[i] == 0:
                buttonGreen(window)
            if gameSequence[i] == 1:
                buttonRed(window)
            if gameSequence[i] == 2:
                buttonYellow(window)
            if gameSequence[i] == 3:
                buttonBlue(window)
            time.sleep(1)
            start(window)
            time.sleep(0.5)
        colorRepet = 0

    if result == gameSequence and gameSequence != []:
        colorRepet = 1
        gameSequence.append(randrange(4))
        result = []
    if len(result) > 0 and len(gameSequence) > 0 and result[len(result) - 1] != gameSequence[len(result) - 1] and \
        gameSequence != []:
        pygame.draw.rect(window, white, (0, 0, 500, 50))
        text = fontGame.render("Vc conseguiu atingir " + str(len(gameSequence) -1) + " pontos", 1, red)
        window.blit(text, (10, 10))
        pygame.display.update()
        time.sleep(4)
        gameSequence = []
        result = []

    #Ativando o botão verde
    if (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= \
        8100 and 100 <= mouse[0] <= 300 and 100 <= mouse[1] <= 300:
        buttonGreen(window)
        if click[0] == 0 and clickActive == 1:
            result.append(0)

    #Ativando o botão vermelho
    elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= \
        8100 and 300 <= mouse[0] <= 500 and 100 <= mouse[1] <= 300:
        buttonRed(window)
        if click[0] == 0 and clickActive == 1:
            result.append(1)

    #Ativando o botão amarelo
    elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= \
        8100 and 100 <= mouse[0] <= 300 and 300 <= mouse[1] <= 500:
        buttonYellow(window)
        if click[0] == 0 and clickActive == 1:
            result.append(2)

    #Ativando o botão azul
    elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= \
        8100 and 300 <= mouse[0] <= 500 and 300 <= mouse[1] <= 500:
        buttonBlue(window)
        if click[0] == 0 and clickActive == 1:
            result.append(3)

    #Ativando o botão central
    elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 6400:
        buttonCenter(window)
        if click[0] == 0 and clickActive == 1:
            colorRepet = 1
            gameSequence.append(randrange(4))
            result = []

    #Iniciando game
    else:
        start(window)

    pygame.draw.rect(window, white, (0, 0, 500, 50))
    text = fontGame.render(str(len(gameSequence)), 1, black)
    window.blit(text, (10, 10))
    clickActive = click[0]
    pygame.display.update()
