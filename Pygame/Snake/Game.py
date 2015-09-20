from Constant import *
from Apple import Apple
from Snake import Snake


class Game(object):
    def __init__(self):
        """Initialize the game"""
        self.width = WIDTH
        self.height = HEIGHT
        self.display = pygame.display.set_mode((WIDTH, HEIGHT + PANEL_HEIGHT))
        pygame.display.set_icon(GAME_ICON)
        pygame.display.set_caption('Snake')
        super(Game, self).__init__()

    def message(self, msg, color, v_align='center', h_align='center', font=SMALL_FONT, off_set_x=0, off_set_y=0):
        """
        A simple message print function it you can place it on 9 place using
        the simple align system horizontal and vertical. And also off-set it by many px you want
        """
        mes_x = 0
        mes_y = 0
        screen_text = font.render(msg, True, color)
        text_width, text_height = font.size(msg)

        if v_align == 'center':
            mes_y = (self.height - text_height) / 2 + off_set_y
        elif v_align == 'top':
            mes_y = off_set_y
        elif v_align == 'bottom':
            mes_y = self.height - text_height + off_set_y

        if h_align == 'center':
            mes_x = (self.width - text_width) / 2 + off_set_x
        elif h_align == 'left':
            mes_x = off_set_x
        elif h_align == 'right':
            mes_x = self.width - text_width + off_set_x

        self.display.blit(screen_text, [mes_x, mes_y])

    @staticmethod
    def game_exit():
        """Exit the game"""
        pygame.quit()
        quit()

    def game_start(self):
        """A simple menu using only text"""
        menu_item = ["Start Normal Game", "2 Player Mode", "Exit"]
        choice = 0
        while True:
            self.display.fill(BLACK)
            self.message("Snake", RED, font=LARGE_FONT, off_set_y=-30)
            self.message(menu_item[0], WHITE, font=SMALL_FONT, off_set_y=10)
            self.message(menu_item[1], WHITE, font=SMALL_FONT, off_set_y=30)
            self.message(menu_item[2], WHITE, font=SMALL_FONT, off_set_y=50)
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
                self.message(menu_item[0], BLUE, font=SMALL_FONT, off_set_y=10)
            elif choice == 1:
                self.message(menu_item[1], BLUE, font=SMALL_FONT, off_set_y=30)
            elif choice == 2:
                self.message(menu_item[2], BLUE, font=SMALL_FONT, off_set_y=50)

            pygame.display.update()
            CLOCK.tick(10)

    def show_score(self, snake1, snake2, game_reset):
        """
        Show score on two player it also take a game_reset function to pass to game_over
        """
        self.display.fill(WHITE)
        self.message("SCORE", RED, v_align='top', font=LARGE_FONT, off_set_y=40)
        self.message("Snake 1", snake1.color, h_align='left', font=MEDIUM_FONT)
        self.message(str(snake1.score), snake1.color, h_align='left', font=MEDIUM_FONT, off_set_y=50)
        self.message("Snake 2", snake2.color, h_align='right', font=MEDIUM_FONT)
        self.message(str(snake2.score), snake2.color, h_align='right', font=MEDIUM_FONT, off_set_y=50)
        self.message("Press Enter to continue.", BLACK, v_align='bottom', font=MEDIUM_FONT)
        pygame.display.update()

        reset = False
        while not reset:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        reset = self.game_over(game_reset,
                                               snake1 if snake1.score > snake2.score else
                                               snake2 if snake2.score > snake1.score else "DRAW")
                if event.type == pygame.QUIT:
                    self.game_exit()

    def show_score(self, snake, game_reset):
        """Show score for one player"""
        self.display.fill(WHITE)
        self.message("SCORE", RED, v_align='top', font=LARGE_FONT, off_set_y=40)
        self.message(str(snake.score), snake.color, font=LARGE_FONT)
        self.message("Press Enter to continue.", BLACK, v_align='bottom', font=MEDIUM_FONT)
        pygame.display.update()

        reset = False
        while not reset:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        reset = self.game_over(game_reset)
                if event.type == pygame.QUIT:
                    self.game_exit()

    def game_over(self, game_reset, winner=None):
        """
        Show the Game Over screen, it take the game_reset function because we can't
        define game_reset as a function of Game it need to be inside the scope of game_loop
        so we can reset it's variable. And it also take winner as a optional parameter
        """
        while True:
            self.display.fill(WHITE)
            if winner is None:
                self.message("Game over", RED, font=LARGE_FONT, off_set_y=-30)
            elif winner == 'DRAW':
                self.message(winner, BLUE, font=LARGE_FONT, off_set_y=-30)
            else:
                self.message(winner.name + " WIN", winner.color, font=LARGE_FONT, off_set_y=-30)
            self.message("Press C to play again or Q to quit", BLACK, font=SMALL_FONT, off_set_y=50)
            self.message("Press M to Menu", BLACK, font=SMALL_FONT, off_set_y=70)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_exit()
                    elif event.key == pygame.K_c:
                        game_reset()
                        return True
                    elif event.key == pygame.K_m:
                        self.game_start()
                if event.type == pygame.QUIT:
                    self.game_exit()

    def game_loop(self):
        """The game loop for 1 player mode"""
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
                self.show_score(snake, game_reset)

            self.display.fill(WHITE)
            pygame.draw.rect(self.display, BLACK, [0, self.height, self.width, PANEL_HEIGHT])
            self.message("Score: " + str(snake.score), RED, h_align='left', v_align='bottom', off_set_y=20)
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
        """Game loop for 2 player mode"""
        snake_length = 6
        snake1 = Snake(snake_length, color=GREEN, game=self, name="Player 1")
        snake2 = Snake(snake_length, color=BLUE, game=self, img=SNAKE_HEAD_2, name="Player 2", offset_y=20)
        apple = Apple(APPLE_SIZE, game=self)

        def game_reset():
            nonlocal snake1, snake2, apple
            snake1 = Snake(snake_length, color=GREEN, game=self, name="Player 1")
            snake2 = Snake(snake_length, color=BLUE, game=self, img=SNAKE_HEAD_2, name="Player 2", offset_y=20)
            apple = Apple(APPLE_SIZE, game=self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake1.direction != 'RIGHT' and not snake1.turned:
                        snake1.turn('LEFT')
                    elif event.key == pygame.K_RIGHT and snake1.direction != 'LEFT' and not snake1.turned:
                        snake1.turn('RIGHT')
                    elif event.key == pygame.K_UP and snake1.direction != 'DOWN' and not snake1.turned:
                        snake1.turn('UP')
                    elif event.key == pygame.K_DOWN and snake1.direction != 'UP' and not snake1.turned:
                        snake1.turn('DOWN')
                    elif event.key == pygame.K_a and snake2.direction != 'RIGHT' and not snake2.turned:
                        snake2.turn('LEFT')
                    elif event.key == pygame.K_d and snake2.direction != 'LEFT' and not snake2.turned:
                        snake2.turn('RIGHT')
                    elif event.key == pygame.K_w and snake2.direction != 'DOWN' and not snake2.turned:
                        snake2.turn('UP')
                    elif event.key == pygame.K_s and snake2.direction != 'UP' and not snake2.turned:
                        snake2.turn('DOWN')

            self.display.fill(WHITE)

            pygame.draw.rect(self.display, BLACK, [0, self.height, self.width, PANEL_HEIGHT])
            self.message("Score: " + str(snake1.score), GREEN, h_align='left', v_align='bottom', off_set_y=20)
            self.message("Score: " + str(snake2.score), BLUE, h_align='right', v_align='bottom', off_set_y=20)

            apple.draw()
            snake1.draw()
            snake2.draw()

            snake1.go()
            snake2.go()

            if snake1.hit_wall() or snake1.hit_tail():
                snake1.die = True
            if snake2.hit_wall() or snake2.hit_tail():
                snake2.die = True

            if snake1.die and snake2.die:
                self.show_score(snake1, snake2, game_reset)

            pygame.display.update()

            if snake1.eat(apple) or snake2.eat(apple):
                apple = Apple(APPLE_SIZE, game=self)

            CLOCK.tick(FPS)
