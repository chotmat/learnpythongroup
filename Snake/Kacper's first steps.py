import sys, random, pygame
pygame.init()

size = width, height = 800, 640

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

c_speed = 2

snake_x = 400
snake_y = 320

speed_x = -c_speed
speed_y = 0

done = False
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
    pygame.draw.rect(screen, GREEN, [snake_x, snake_y, 5, 5])
    pygame.draw.rect(screen, BLUE, [snake_x + 5, snake_y, 5, 5])
    snake_x += speed_x
    snake_y += speed_y
    
    
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()