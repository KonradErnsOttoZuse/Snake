import os
import pygame

WIDTH = 1280
HEIGHT = 960

#видео-режим
displayMode = (WIDTH, HEIGHT)

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (127,127,255)

snakeBlock = 10
snakeSpeed = 10


# текстуры змейки
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Assets')
snakeHeadUp = pygame.image.load(os.path.join(img_folder, 'head_up.png'))
snakeHeadDown = pygame.image.load(os.path.join(img_folder, 'head_down.png'))
snakeHeadRight = pygame.image.load(os.path.join(img_folder, 'head_right.png'))
snakeHeadLeft = pygame.image.load(os.path.join(img_folder, 'head_left.png'))
snakeTailUp = pygame.image.load(os.path.join(img_folder, 'tail_up.png'))
snakeTailDown = pygame.image.load(os.path.join(img_folder, 'tail_down.png'))
snakeTailLeft = pygame.image.load(os.path.join(img_folder, 'tail_left.png'))
snakeTailRight = pygame.image.load(os.path.join(img_folder, 'tail_right.png'))
snakeBend1 = pygame.image.load(os.path.join(img_folder, 'bend1.png'))
snakeBend2 = pygame.image.load(os.path.join(img_folder, 'bend2.png'))
snakeBend3 = pygame.image.load(os.path.join(img_folder, 'bend3.png'))
snakeBend4 = pygame.image.load(os.path.join(img_folder, 'bend4.png'))
snakeBodyHoriz = pygame.image.load(os.path.join(img_folder, 'body_horiz.png'))
snakeBodyVert = pygame.image.load(os.path.join(img_folder, 'body_vert.png'))

