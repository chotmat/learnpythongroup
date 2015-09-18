from Constant import *
from Apple import Apple
from Snake import Snake


class Game(object):
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.display = pygame.display.set_mode((WIDTH, HEIGHT + PANEL_HEIGHT))
        pygame.display.set_caption('Snake')
        super(Game, self).__init__()

    def message_center(self, msg, color, font=SMALL_FONT, off_set_y=0):
        screen_text = font.render(msg, True, color)
        text_width, text_height = font.size(msg)
        self.display.blit(screen_text, [(self.width - text_width) / 2,
                                        (self.height - text_height) / 2 + off_set_y])

    def message_left(self, msg, color, font=SMALL_FONT, off_set_y=0):
        screen_text = font.render(msg, True, color)
        self.display.blit(screen_text, [0, off_set_y])

    def message_right(self, msg, color, font=SMALL_FONT, off_set_y=0):
        screen_text = font.render(msg, True, color)
        text_width, text_height = font.size(msg)
        self.display.blit(screen_text, [self.width - text_width, off_set_y])

    @staticmethod
    def game_exit():
        pygame.quit()
        quit()

    # Work in progress gonna refactor it to be more simple
    def game_start(self):
        menu_item = ["Start Normal Game", "2 Player Mode", "Exit"]
        choice = 0
        while True:
            self.display.fill(BLACK)
            self.message_center("Snake", RED, font=LARGE_FONT, off_set_y=-30)
            self.message_center(menu_item[0], WHITE, font=SMALL_FONT, off_set_y=10)
            self.message_center(menu_item[1], WHITE, font=SMALL_FONT, off_set_y=30)
            self.message_center(menu_item[2], WHITE, font=SMALL_FONT, off_set_y=50)
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
                        if choice == 0:
                            self.game_loop()
                        elif choice == 1:
                            self.game_loop_2p()
                        elif choice == 2:
                            self.game_exit()
                if event.type == pygame.QUIT:
                    self.game_exit()

            if choice == 0:
                self.message_center(menu_item[0], BLUE, font=SMALL_FONT, off_set_y=10)
            elif choice == 1:
                self.message_center(menu_item[1], BLUE, font=SMALL_FONT, off_set_y=30)
            elif choice == 2:
                self.message_center(menu_item[2], BLUE, font=SMALL_FONT, off_set_y=50)

            pygame.display.update()
            CLOCK.tick(10)

    def game_over(self, game_reset):
        reset = False
        while not reset:
            self.display.fill(WHITE)
            self.message_center("Game over", RED, font=LARGE_FONT, off_set_y=-30)
            self.message_center("Press C to play again or Q to quit", BLACK, font=SMALL_FONT, off_set_y=50)
            self.message_center("Press M to Menu", BLACK, font=SMALL_FONT, off_set_y=70)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_exit()
                    elif event.key == pygame.K_c:
                        game_reset()
                        reset = True
                    elif event.key == pygame.K_m:
                        self.game_start()
                if event.type == pygame.QUIT:
                    self.game_exit()

    def game_loop(self):

        snake_length = 6
        snake = Snake(snake_length, color=GREEN, game=self)
        apple = Apple(APPLE_SIZE, game=self)

        def game_reset():
            nonlocal snake, apple
            snake = Snake(snake_length, color=GREEN, game=self)
            apple = Apple(APPLE_SIZE, game=self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake.direction != 'RIGHT' and not snake.turned:
                        snake.started = True
                        snake.turned = True
                        snake.turn('LEFT')
                    elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT' and not snake.turned:
                        snake.started = True
                        snake.turned = True
                        snake.turn('RIGHT')
                    elif event.key == pygame.K_UP and snake.direction != 'DOWN' and not snake.turned:
                        snake.started = True
                        snake.turned = True
                        snake.turn('UP')
                    elif event.key == pygame.K_DOWN and snake.direction != 'UP' and not snake.turned:
                        snake.started = True
                        snake.turned = True
                        snake.turn('DOWN')

            if snake.hit_wall() or snake.hit_tail():
                self.game_over(game_reset)

            self.display.fill(WHITE)
            pygame.draw.rect(self.display, BLACK, [0, self.height, self.width, PANEL_HEIGHT])
            self.message_left("Score: " + str(snake.score), RED, off_set_y=self.height)
            apple.draw()
            snake.draw()

            if snake.started:
                snake.go()
                snake.turned = False

            pygame.display.update()

            if snake.eat(apple):
                apple = Apple(APPLE_SIZE, game=self)

            CLOCK.tick(FPS)

    def game_loop_2p(self):
        snake_length = 6
        snake1 = Snake(snake_length, color=GREEN, game=self)
        snake2 = Snake(snake_length, color=BLUE, game=self)
        apple = Apple(APPLE_SIZE, game=self)

        def game_reset():
            nonlocal snake1, snake2, apple
            snake1 = Snake(snake_length, color=GREEN, game=self)
            snake2 = Snake(snake_length, color=BLUE, game=self)
            apple = Apple(APPLE_SIZE, game=self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake1.direction != 'RIGHT' and not snake1.turned:
                        snake1.started = True
                        snake1.turned = True
                        snake1.turn('LEFT')
                    elif event.key == pygame.K_RIGHT and snake1.direction != 'LEFT' and not snake1.turned:
                        snake1.started = True
                        snake1.turned = True
                        snake1.turn('RIGHT')
                    elif event.key == pygame.K_UP and snake1.direction != 'DOWN' and not snake1.turned:
                        snake1.started = True
                        snake1.turned = True
                        snake1.turn('UP')
                    elif event.key == pygame.K_DOWN and snake1.direction != 'UP' and not snake1.turned:
                        snake1.started = True
                        snake1.turned = True
                        snake1.turn('DOWN')
                    elif event.key == pygame.K_a and snake2.direction != 'RIGHT' and not snake2.turned:
                        snake2.started = True
                        snake2.turned = True
                        snake2.turn('LEFT')
                    elif event.key == pygame.K_d and snake2.direction != 'LEFT' and not snake2.turned:
                        snake2.started = True
                        snake2.turned = True
                        snake2.turn('RIGHT')
                    elif event.key == pygame.K_w and snake2.direction != 'DOWN' and not snake2.turned:
                        snake2.started = True
                        snake2.turned = True
                        snake2.turn('UP')
                    elif event.key == pygame.K_s and snake2.direction != 'UP' and not snake2.turned:
                        snake2.started = True
                        snake2.turned = True
                        snake2.turn('DOWN')

            self.display.fill(WHITE)
            pygame.draw.rect(self.display, BLACK, [0, self.height, self.width, PANEL_HEIGHT])
            self.message_left("Score: " + str(snake1.score), RED, off_set_y=self.height)
            self.message_right("Score: " + str(snake2.score), RED, off_set_y=self.height)
            apple.draw()
            snake1.draw()
            snake2.draw()

            if snake1.started:
                snake1.go()

                if snake1.hit_wall() or snake1.hit_tail():
                    self.game_over(game_reset)

                snake1.turned = False

            if snake2.started:
                snake2.go()

                if snake2.hit_wall() or snake2.hit_tail():
                    self.game_over(game_reset)

                snake2.turned = False

            pygame.display.update()

            if snake1.eat(apple) or snake2.eat(apple):
                apple = Apple(APPLE_SIZE, game=self)

            CLOCK.tick(FPS)
