import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (136, 170, 0)
BLUE = (0, 0, 255)

WIDTH = 400
HEIGHT = 300
BLOCK_SIZE = 15
APPLE_SIZE = 16
SPEED = 10
FPS = 24

GAME_NAME = "Snake"

PATH = os.path.dirname(os.path.abspath(__file__))

pygame.font.init()
largeFont = pygame.font.Font(PATH + '/Action_Man.ttf', 80)
smallFont = pygame.font.Font(PATH + '/Action_Man.ttf', 20)

snake_head = pygame.image.load(PATH + '/snake_head.png')
apple_img = pygame.image.load(PATH + '/Apple.png')

clock = pygame.time.Clock()