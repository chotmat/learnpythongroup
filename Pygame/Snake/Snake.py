from Constant import *


class Block(object):
    def __init__(self, x, y, size, game, img=None, color=GREEN):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.img = img
        self.game = game

    def draw(self):
        if self.img is None:
            pygame.draw.ellipse(self.game.display, self.color, [self.x, self.y, self.size, self.size])
        else:
            self.game.display.blit(self.img, [self.x, self.y])


class Snake(object):
    def __init__(self, length, game, color):
        self.length = length
        self.color = color
        self.game = game
        head = pygame.transform.rotate(SNAKE_HEAD, 270)
        self.blocks = [Block(game.width / 2, game.height / 2, color, game, img=head)]
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 'RIGHT'
        for i in range(1, length - 1):
            self.blocks.append(Block(game.width / 2 - i * SPEED, game.height / 2, size=BLOCK_SIZE, game=game))

    def draw(self):
        for block in self.blocks:
            block.draw()

    def turn(self, direction):
        self.direction = direction
        if direction == 'LEFT':
            self.speed_x = -SPEED
            self.speed_y = 0
            self.blocks[0].img = pygame.transform.rotate(SNAKE_HEAD, 90)
        elif direction == 'UP':
            self.speed_y = -SPEED
            self.speed_x = 0
            self.blocks[0].img = SNAKE_HEAD
        elif direction == 'RIGHT':
            self.speed_x = SPEED
            self.speed_y = 0
            self.blocks[0].img = pygame.transform.rotate(SNAKE_HEAD, 270)
        elif direction == 'DOWN':
            self.speed_y = SPEED
            self.speed_x = 0
            self.blocks[0].img = pygame.transform.rotate(SNAKE_HEAD, 180)

    def go(self):
        for i in reversed(range(1, len(self.blocks))):
            self.blocks[i].x = self.blocks[i - 1].x
            self.blocks[i].y = self.blocks[i - 1].y
        self.blocks[0].x += self.speed_x
        self.blocks[0].y += self.speed_y

    def eat(self, apple):
        if ((apple.x <= self.blocks[0].x <= apple.x + BLOCK_SIZE and
                apple.y <= self.blocks[0].y <= apple.y + BLOCK_SIZE) or
            (apple.x <= self.blocks[0].x + BLOCK_SIZE <= apple.x + BLOCK_SIZE and
                apple.y <= self.blocks[0].y + BLOCK_SIZE <= apple.y + BLOCK_SIZE)):
            self.blocks.append(Block(self.blocks[-1].x, self.blocks[-1].y, size=BLOCK_SIZE, game=self.game))
            return True
        else:
            return False

    def hit_wall(self):
        if (self.blocks[0].x >= self.game.width or
                self.blocks[0].x < 0 or
                self.blocks[0].y >= self.game.height or
                self.blocks[0].y < 0):
            return True
        else:
            return False

    def hit_tail(self):
        for block in self.blocks[1:]:
            if self.blocks[0].x == block.x and self.blocks[0].y == block.y:
                return True
        else:
            return False
