from Constant import *
import random


class Apple(object):
    def __init__(self, size, game):
        """"""
        self.size = size
        self.x = random.randrange(0, game.width - size, size)
        self.y = random.randrange(0, game.height - size, size)
        self.game = game
        self.img = APPLE_IMG

    def draw(self):
        self.game.display.blit(self.img, [self.x, self.y])
