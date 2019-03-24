from settings import TILESIZE, PLAYER_SPEED, pg, PLAYER_HIT_RECT
from collisions import *

vec = pg.math.Vector2


class Reaper(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.reaper
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img_R
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE


    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.vel = vec(0, -PLAYER_SPEED)
        if keys[pg.K_DOWN]:
            self.vel = vec(0, PLAYER_SPEED)
        if keys[pg.K_RIGHT]:
            self.vel = vec(PLAYER_SPEED, 0)
            if (self.image == self.game.player_img_L):
                self.image = self.game.player_img_R
        if keys[pg.K_LEFT]:
            self.vel = vec(-PLAYER_SPEED, 0)
            if (self.image == self.game.player_img_R):
                self.image = self.game.player_img_L

    def update(self):
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center