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
    def __init__(self, x, y, color=BLACK):
        self.x = x
        self.y = y
        self.color = color

class Snake(object):
    def __init__(self, length):
        self.length = length
        self.blocks = [Block(WIDTH/2, HEIGHT/2, RED)]
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 'RIGHT'
        for i in range(1,length-1):
            self.blocks.append(Block(WIDTH/2 - i*BLOCK_SIZE,HEIGHT/2))
        

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(gameDisplay, block.color, [block.x, block.y, BLOCK_SIZE, BLOCK_SIZE])

    def turn(self, direction):
        self.direction = direction
        if direction == 'LEFT':
            self.speed_x = -10
            self.speed_y = 0
        elif direction == 'UP':
            self.speed_y = -10
            self.speed_x = 0
        elif direction == 'RIGHT':
            self.speed_x = 10
            self.speed_y = 0
        elif direction == 'DOWN':
            self.speed_y = 10
            self.speed_x = 0

    def go(self):
        for i in reversed(range(1, len(self.blocks))):
            self.blocks[i].x = self.blocks[i - 1].x
            self.blocks[i].y = self.blocks[i - 1].y
        self.blocks[0].x += self.speed_x
        self.blocks[0].y += self.speed_y 

    def eat(self, apple):
        if (self.blocks[0].x == apple.x and self.blocks[0].y == apple.y):
            self.blocks.append(Block(self.blocks[-1].x, self.blocks[-1].y))
            return True
        else:
            return False

    def hit_wall(self):
        if (self.blocks[0].x >= WIDTH or
            self.blocks[0].x < 0 or 
            self.blocks[0].y >= HEIGHT or 
            self.blocks[0].y < 0):
                return True
        else:
            return False

    def hit_tail(self):
        for block in self.blocks[1:]:
            if self.blocks[0].x == block.x and self.blocks[0].y == block.y:
                print("WTF")
                return True
        else:
            return False

class Apple(object):
    def __init__(self):
        self.x = round(random.randrange(0,WIDTH - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
        self.y = round(random.randrange(0,HEIGHT - BLOCK_SIZE)/BLOCK_SIZE)*BLOCK_SIZE
        self.size = BLOCK_SIZE
    def draw(self):
        pygame.draw.rect(gameDisplay, RED, [self.x, self.y, self.size, self.size])

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
    started = False
    snake = Snake(8)
    apple = Apple()

    def gameReset():
        nonlocal snake, apple, started
        snake = Snake(8)
        apple = Apple()
        started = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    started = True
                    snake.turn('LEFT')
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    started = True
                    snake.turn('RIGHT')
                elif event.key == pygame.K_UP and snake.direction != 'DOWN':
                    started = True
                    snake.turn('UP')
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    started = True
                    snake.turn('DOWN')

        if snake.hit_wall() or snake.hit_tail():
            gameOver(gameReset)

        gameDisplay.fill(WHITE)
        apple.draw()
        snake.draw()

        if started:
            snake.go()

        pygame.display.update()

        if snake.eat(apple):
            apple = Apple()

        clock.tick(FPS)

gameLoop()