import pygame as pg
from abc import ABC, abstractmethod


class mapObject(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Wall(mapObject):
    def __init__(self, game, x, y, w, h):
        mapObject.__init__(self, game, x, y, w, h)
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)


class Grass(mapObject):
    def __init__(self, game, x, y, w, h):
        mapObject.__init__(self, game, x, y, w, h)
        self.groups = game.grasses
        pg.sprite.Sprite.__init__(self, self.groups)


class Road(mapObject):
    def __init__(self, game, x, y, w, h):
        mapObject.__init__(self, game, x, y, w, h)
        self.groups = game.roads
        pg.sprite.Sprite.__init__(self, self.groups)


class Indoor(mapObject):
    def __init__(self, game, x, y, w, h):
        mapObject.__init__(self, game, x, y, w, h)
        self.groups = game.indoors
        pg.sprite.Sprite.__init__(self, self.groups)


class Dirt(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        mapObject.__init__(self, game, x, y, w, h)
        self.groups = game.dirt
        pg.sprite.Sprite.__init__(self, self.groups)