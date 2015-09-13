import pygame
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

WIDTH = 400
HEIGHT = 300
BLOCK_SIZE = 10
FPS = 24


gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

class Block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake(object):
    def __init__(self):
        self.blocks = [Block(WIDTH/2,HEIGHT/2)]
    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(gameDisplay, BLACK, [block.x, block.y, BLOCK_SIZE, BLOCK_SIZE])


def message(msg, color):
    screen_text = font.render(msg, True, color)
    text_width, text_height = font.size(msg)
    gameDisplay.blit(screen_text, [(WIDTH - text_width)/2, (HEIGHT - text_height)/2])

def gameExit():
    pygame.quit()
    quit()

def gameOver(gameReset):
    reset = False
    while not reset:
        gameDisplay.fill(WHITE)
        message("Game over, press C to play again or Q to quit", RED)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit()
                elif event.key == pygame.K_c:
                    gameReset()
                    reset = True
            if event.type == pygame.QUIT:
                gameExit()

def gameLoop():
    snake = Snake()
    speed_x = 0
    speed_y = 0

    randAppleX = round(random.randrange(0,WIDTH - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
    randAppleY = round(random.randrange(0,HEIGHT - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE

    def gameReset():
        nonlocal snake, speed_x, speed_y, randAppleX, randAppleY
        snake = Snake()
        speed_x = 0
        speed_y = 0
        randAppleX = round(random.randrange(0,WIDTH - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
        randAppleY = round(random.randrange(0,HEIGHT - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed_x = -BLOCK_SIZE
                    speed_y = 0
                elif event.key == pygame.K_RIGHT:
                    speed_x = BLOCK_SIZE
                    speed_y = 0
                elif event.key == pygame.K_UP:
                    speed_y = -BLOCK_SIZE
                    speed_x = 0
                elif event.key == pygame.K_DOWN:
                    speed_y = BLOCK_SIZE
                    speed_x = 0

        snake.blocks[0].x += speed_x
        snake.blocks[0].y += speed_y

        if (snake.blocks[0].x >= WIDTH or snake.blocks[0].x < 0 or snake.blocks[0].y >= HEIGHT or snake.blocks[0].y < 0):
            gameOver(gameReset)

        gameDisplay.fill(WHITE)
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, BLOCK_SIZE, BLOCK_SIZE])
        snake.draw()
        pygame.display.update()

        if snake.blocks[0].x == randAppleX and snake.blocks[0].y == randAppleY:
            randAppleX = round(random.randrange(0,WIDTH - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
            randAppleY = round(random.randrange(0,HEIGHT - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE

        clock.tick(FPS)

gameLoop()