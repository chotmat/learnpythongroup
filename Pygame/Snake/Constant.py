import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (136, 170, 0)
BLUE = (0, 0, 255)

WIDTH = 600
HEIGHT = 400
PANEL_HEIGHT = 20
BLOCK_SIZE = 15
APPLE_SIZE = 16
SPEED = 10
FPS = 24

GAME_NAME = "Snake"

pygame.font.init()
LARGE_FONT = pygame.font.Font('font/Action_Man.ttf', 80)
MEDIUM_FONT = pygame.font.Font('font/Action_Man.ttf', 40)
SMALL_FONT = pygame.font.Font('font/Action_Man.ttf', 20)

SNAKE_HEAD_1 = pygame.image.load('img/snake_head.png')
SNAKE_HEAD_2 = pygame.image.load('img/snake_head_2.png')
APPLE_IMG = pygame.image.load('img/Apple.png')

CLOCK = pygame.time.Clock()
