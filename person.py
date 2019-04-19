import pygame as pg
from settings import TILESIZE
from collisions import collide_with_walls
from settings import PLAYER_HIT_RECT
from random import randint, normalvariate
from math import floor


vec = pg.math.Vector2

class Person(pg.sprite.Sprite):
    def __init__(self, game, x, y, *rest):

        self.groups = game.people
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.person_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.y = y * TILESIZE
        self.rect.x = x * TILESIZE
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        collide_with_walls(self, self.game.walls, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, "y")
        self.rect.center = self.hit_rect.center
        self.vel = vec(0, 0)

    def update(self):
        self.rect.center = self.pos
        self.pos += self.vel
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        for i in range(1,4):
            collide_with_walls(self, self.game.walls, 'x', 2)
            self.hit_rect.centery = self.pos.y
            collide_with_walls(self, self.game.walls, 'y', 2)
            self.rect.center = self.hit_rect.center

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if (len(rest) == 6):
            self.age = rest[0]
            self.disease = rest[1]
            self.good = rest[2]
            self.lawful = rest[3]
            self.money = rest[4]
            self.gender = rest[5]
        else:
            self.age = randint(0, 50) + randint(0, 25) + randint(0, 25)
            self.disease = randint(0, 10)
            self.good = randint(0, 100)
            self.lawful = randint(0, 100)
            self.money = floor(normalvariate(1000, 500))
            self. gender = randint(0, 1)

