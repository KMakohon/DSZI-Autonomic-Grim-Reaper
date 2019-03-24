import pygame as pg
from settings import TILESIZE
from random import randint, normalvariate
from math import floor


class Person(pg.sprite.Sprite):
    def __init__(self, game, x, y, *rest):

        self.groups = game.people
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.person_img
        self.rect = self.image.get_rect()
        self.rect.y = y * TILESIZE
        self.rect.x = x * TILESIZE
        if (len(rest) == 5):
            self.age = rest[0]
            self.disease = rest[1]
            self.good = rest[2]
            self.lawful = rest[3]
            self.money = rest[4]
        else:
            self.age = randint(0, 50) + randint(0, 25) + randint(0, 25)
            self.disease = randint(0, 10)
            self.good = randint(0, 100)
            self.lawful = randint(0, 100)
            self.money = floor(normalvariate(1000, 500))