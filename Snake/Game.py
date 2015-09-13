import sys, random, pygame
pygame.init()

size = width, height = 800, 640

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

c_speed = 10
FPS =1

snake_x = 400
snake_y = 320
snake_l = 3

speed_x = -c_speed
speed_y = 0

done = False
snake = [snake_x, snake_y, snake_x+10, snake_y, snake_x+20,snake_y] 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if speed_y != 0:
                    speed_x = -c_speed
                    speed_y = 0
            elif event.key == pygame.K_RIGHT:
                if speed_y != 0:
                    speed_x = c_speed
                    speed_y = 0
            elif event.key == pygame.K_UP:
                if speed_x != 0:
                    speed_x = 0
                    speed_y = -c_speed
            elif event.key == pygame.K_DOWN:
                if speed_x != 0:
                    speed_x = 0
                    speed_y = c_speed
    screen.fill(BLACK)
    snake[0] = snake_x
    snake[1] = snake_y
    a = snake[0]
    b = snake[1]
    c = snake[2]
    d = snake[3]
    for x,y in zip(snake[0::2], snake[1::2]):                      
        pygame.draw.rect(screen, BLUE, [x, y, 10, 10])
    snake_x += speed_x
    snake_y += speed_y
    snake[2] = a
    snake[3] = b
    snake[4] = c
    snake[5] = d
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()