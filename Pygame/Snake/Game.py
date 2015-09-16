from Constant import *
from Apple import Apple
from Snake import Snake


class Game(object):
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake')
        super(Game, self).__init__()

    def message(self, msg, color, font=SMALL_FONT, off_set_y=0):
        screen_text = font.render(msg, True, color)
        text_width, text_height = font.size(msg)
        self.display.blit(screen_text, [(self.width - text_width)/2, (self.height - text_height)/2 + off_set_y])

    @staticmethod
    def game_exit():
        pygame.quit()
        quit()

    # Work in progress gonna refactor it to be more simple
    def game_start(self):
        menu_item = ["Start Game", "Exit"]
        choice = 0
        while True:
            self.message("Snake", RED, font=LARGE_FONT, off_set_y=-30)
            self.message(menu_item[0], WHITE, font=SMALL_FONT, off_set_y=10)
            self.message(menu_item[1], WHITE, font=SMALL_FONT, off_set_y=30)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if choice == len(menu_item) - 1:
                            choice = 0
                        else:
                            choice += 1
                    elif event.key == pygame.K_UP:
                        if choice == 0:
                            choice = len(menu_item) - 1
                        else:
                            choice -= 1
                    elif event.key == pygame.K_RETURN:
                        if menu_item[choice] == menu_item[0]:
                            self.game_loop()
                        elif menu_item[choice] == menu_item[1]:
                            self.game_exit()
                if event.type == pygame.QUIT:
                    self.game_exit()
            if menu_item[choice] == menu_item[0]:
                self.message(menu_item[0], BLUE, font=SMALL_FONT, off_set_y=10)
            elif menu_item[choice] == menu_item[1]:
                self.message(menu_item[1], BLUE, font=SMALL_FONT, off_set_y=30)
            pygame.display.update()
            CLOCK.tick(10)

    def game_over(self, game_reset):
        reset = False
        while not reset:
            self.display.fill(WHITE)
            self.message("Game over", RED, font=LARGE_FONT, off_set_y=-30)
            self.message("Press C to play again or Q to quit", BLACK, font=SMALL_FONT, off_set_y=50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_exit()
                    elif event.key == pygame.K_c:
                        game_reset()
                        reset = True
                if event.type == pygame.QUIT:
                    self.game_exit()

    def game_loop(self):
        started = False
        turned = False
        snake_length = 6
        snake = Snake(snake_length, color=GREEN, game=self)
        apple = Apple(APPLE_SIZE, game=self)

        def game_reset():
            nonlocal snake, apple, started, turned
            snake = Snake(snake_length, color=GREEN, game=self)
            apple = Apple(APPLE_SIZE, game=self)
            started = False
            turned = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake.direction != 'RIGHT' and not turned:
                        started = True
                        turned = True
                        snake.turn('LEFT')
                    elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT' and not turned:
                        started = True
                        turned = True
                        snake.turn('RIGHT')
                    elif event.key == pygame.K_UP and snake.direction != 'DOWN' and not turned:
                        started = True
                        turned = True
                        snake.turn('UP')
                    elif event.key == pygame.K_DOWN and snake.direction != 'UP' and not turned:
                        started = True
                        turned = True
                        snake.turn('DOWN')

            if snake.hit_wall() or snake.hit_tail():
                self.game_over(game_reset)

            self.display.fill(WHITE)
            apple.draw()
            snake.draw()

            if started:
                snake.go()
                turned = False

            pygame.display.update()

            if snake.eat(apple):
                apple = Apple(APPLE_SIZE, game=self)

            CLOCK.tick(FPS)
