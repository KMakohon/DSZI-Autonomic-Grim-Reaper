import pygame as pg
from settings import TILESIZE


class Person(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.people
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.person_img
        self.rect = self.image.get_rect()
        self.rect.y = y * TILESIZE
        self.rect.x = x * TILESIZE
