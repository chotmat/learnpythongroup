import sys, random, pygame
pygame.init()

size = width, height = 800, 640

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
# Constant speed of the snake
c_speed = 10
FPS =1
#Starting point and lenght
snake_x = 400
snake_y = 320
snake_l = 3
#Starting speed
speed_x = -c_speed
speed_y = 0

done = False
#Position of our snake's cubes
snake = [snake_x, snake_y, snake_x+10, snake_y, snake_x+20,snake_y]
#Array for temporary data used to turn snake
t_snake = [0, 0, 0, 0]
#Is there an apple on the field?
key_dis = False
apple_v = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and key_dis == False:
            if event.key == pygame.K_LEFT:
                if speed_y != 0:
                    speed_x = -c_speed
                    speed_y = 0
                    key_dis = True
            elif event.key == pygame.K_RIGHT:
                if speed_y != 0:
                    speed_x = c_speed
                    speed_y = 0
                    key_dis = True
            elif event.key == pygame.K_UP:
                if speed_x != 0:
                    speed_x = 0
                    speed_y = -c_speed
                    key_dis = True
            elif event.key == pygame.K_DOWN:
                if speed_x != 0:
                    speed_x = 0
                    speed_y = c_speed
                    key_dis = True

    screen.fill(BLACK)
    #All this mess just to make him turn
    snake[0] = snake_x
    snake[1] = snake_y
    for i in range((snake_l - 1) * 2):
        t_snake[i] = snake[i]
    #Let's show our snake    
    for x,y in zip(snake[0::2], snake[1::2]):                 
        pygame.draw.rect(screen, BLUE, [x, y, 10, 10])
    #Adding some speed to change position    
    snake_x += speed_x
    snake_y += speed_y
    #All this mess vol.2
    for i in range((snake_l - 1) * 2):
        snake[i+2] = t_snake[i]
    #No apple? Let's random one
    if apple_v == False:
        apple_x = random.randrange(0, 800, 10)
        apple_y = random.randrange(0, 640, 10)
        apple_v = True
    #And draw    
    pygame.draw.rect(screen, GREEN, [apple_x, apple_y, 10, 10])
    #Collect apples, set apple_v to False so we will get new one
    #And add some lenght to our snake
    if snake_x == apple_x and snake_y == apple_y:
        apple_v = False
        t_snake.append(0)
        t_snake.append(0)
        snake.append(snake[snake_l * 2 - 2])
        snake.append(snake[snake_l * 2 - 1])
        snake_l += 1
    if key_dis == True:
        key_dis = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()