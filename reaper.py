from __future__ import division
from settings import TILESIZE, TIMESLEEP, PLAYER_HIT_RECT, PEOPLE_TYPE
from Dtree.Dtree import *
from collisions import *
from time import sleep
import aStar

vec = pg.math.Vector2
estimator = BuildTree()


class ScoutReaper(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = pg.sprite.Group()
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img_R
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)

    def whereAmI(self):
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos[0]
        self.hit_rect.centery = self.pos[1]
        grasses = pg.sprite.spritecollide(self, self.game.grasses, False, grass_collide)
        if grasses:
            return 6
        roads = pg.sprite.spritecollide(self, self.game.roads, False, grass_collide)
        if roads:
            return 2
        indoors = pg.sprite.spritecollide(self, self.game.indoors, False, grass_collide)
        if indoors:
            return 1
        dirt = pg.sprite.spritecollide(self, self.game.dirt, False, grass_collide)
        if dirt:
            return 3
        return 100000000


class Reaper(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.reaper
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img_R
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x+0.5, y+0.5) * TILESIZE
        self.countsteps = 0
        self.direction = 1
        self.rect.center = self.pos

    def distanceTo(self, person):
        pom = aStar.Astar(self.game, self.pos.x, self.pos.y, person.pos.x, person.pos.y, 1)
        return pom[0].cost

    def go(self, howtogo):
        if isinstance(howtogo, int):
            print("Bledny cel drogi")
            return -1

        for i in range(len(howtogo)-1, -1, -1):
            self.pos.x = howtogo[i].x * TILESIZE + 32
            self.pos.y = howtogo[i].y * TILESIZE + 32

            if self.direction != howtogo[i].direction:
                self.direction = howtogo[i].direction
                if self.direction == 1:
                    self.image = self.game.player_img_R
                elif self.direction == 3:
                    self.image = self.game.player_img_L
                elif howtogo[i].direction == 2:
                    self.image = self.game.player_img_D
                else:
                    self.image = self.game.player_img_U

            self.countsteps = howtogo[i].cost
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.hit_rect.centerx = self.pos.x
            self.hit_rect.centery = self.pos.y
            self.rect.center = self.hit_rect.center

            hits = pg.sprite.spritecollide(self, self.game.people, True, collide_hit_rect)
            if hits:
                for sprite in hits:
                    print("Typ obiektu przewidziany przez siec: ", sprite.predictedtype)
                    if sprite.predictedtype in PEOPLE_TYPE:
                        if PredictDead(sprite,estimator) == 1:
                            sprite.banish()
                    sprite.show()
            self.game.update()
            self.game.draw()
            sleep(TIMESLEEP)
