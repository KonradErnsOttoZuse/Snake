import sys
import time
import random
import pygame
from Settings import *

pygame.init()
screen = pygame.display.set_mode(displayMode)
pygame.display.update()
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):  # Создадим функцию, которая будет показывать нам сообщения на игровом экране.
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 10, HEIGHT / 3])

def gameLoop():
    gameOverFlag = False
    gameCloseFlag = False
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    xDelta = 0
    yDelta = 0
    foodx = round(random.randrange(0, WIDTH - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snakeBlock) / 10.0) * 10.0
    while not gameOverFlag:
        while gameCloseFlag == True:
            screen.fill(WHITE)
            message("Вы проиграли! Нажмите Q для выхода или R для повторной игры", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOverFlag = True
                        gameCloseFlag = False
                    if event.key == pygame.K_r:
                        return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverFlag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xDelta = -snakeBlock
                    yDelta = 0
                if event.key == pygame.K_RIGHT:
                    xDelta = snakeBlock
                    yDelta = 0
                if event.key == pygame.K_UP:
                    xDelta = 0
                    yDelta = -snakeBlock
                if event.key == pygame.K_DOWN:
                    xDelta = 0
                    yDelta = snakeBlock

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            gameCloseFlag = True

        x1 += xDelta
        y1 += yDelta
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snakeBlock, snakeBlock])
        pygame.draw.rect(screen, WHITE, [x1, y1, snakeBlock, snakeBlock])
        pygame.display.update()
        clock.tick(snakeSpeed)
    return False
# message("Вы проиграли :(", RED)
# pygame.display.update()
# time.sleep(3)

while True:
    if not gameLoop():
        print("Прерываем цикл игры")
        break
    print("Новый раунд")

pygame.quit()
quit()