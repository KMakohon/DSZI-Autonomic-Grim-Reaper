from settings import TILESIZE, PLAYER_SPEED, PLAYER_HIT_RECT
from collisions import *
from math import floor
from time import sleep


vec = pg.math.Vector2


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

        walls = pg.sprite.spritecollide(self, self.game.walls, False, grass_collide )
        if walls:
            return 1000000
        grasses = pg.sprite.spritecollide(self, self.game.grasses, False, grass_collide)
        if grasses:
            return 10
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
        self.pos = vec(x, y) * TILESIZE
        self.countsteps = 0
        self.target = vec(0, 0)
        self.direction = 1

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

    def go(self, howtogo):
        for i in range (len(howtogo)-1, -1, -1):
            print("x: ", howtogo[i].x, ", y: ", howtogo[i].x)
            self.pos.x = howtogo[i].x * TILESIZE + 32
            self.pos.y = howtogo[i].y * TILESIZE + 32




            if (howtogo[i].direction == 1):
                self.image = self.game.player_img_R
                print("R")
            if (howtogo[i].direction == 3):
                self.image = self.game.player_img_L
                print("L")
            if (howtogo[i].direction == 2):
                print("D")
                self.image = self.game.player_img_D
            if (howtogo[i].direction == 4):
                print("U")
                self.image = self.game.player_img_U

            self.direction = howtogo[i].direction
            self.countsteps = howtogo[i].cost
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.hit_rect.centerx = self.pos.x
            self.hit_rect.centery = self.pos.y
            #collide_with_walls(self, self.game.walls, 'x')
            #collide_with_walls(self, self.game.walls, 'y')
            self.rect.center = self.hit_rect.center

            self.game.update()
            self.game.draw()
            sleep(0.5)

    def go_to(self, game, newpos):
        self.target = vec(newpos[0], newpos[1])
        self.pos.y = floor(self.pos.y)
        self.pos.x = floor(self.pos.x)
        self.target.x = self.target.x - game.camera.x
        self.target.y = self.target.y - game.camera.y
        self.target.x = (self.target.x - self.target.x % 16) + 16
        self.target.y = (self.target.y - self.target.y % 16) + 16
        oldposx = 0
        oldposy = 0
        while(True):
            if(oldposx == self.pos.x and oldposy == self.pos.y):
                break
            oldposx = self.pos.x
            oldposy = self.pos.y
            if self.target.x == self.pos.x and self.target.y == self.pos.y:
                break
            if self.target.x > self.pos.x:
                self.pos.x += 1
                if self.target.x - self.pos.x > 16 and (self.image == self.game.player_img_L):
                    self.image = self.game.player_img_R
                    self.countsteps += 1
                #prawo
            if self.target.x < self.pos.x:
                self.pos.x -= 1
                if self.pos.x - self.target.x > 16 and self.image == self.game.player_img_R:
                        self.image = self.game.player_img_L
                        self.countsteps += 1
                #lewo
            if self.target.y > self.pos.y:
                self.pos.y += 1
                #dol
            if self.target.y < self.pos.y:
                self.pos.y -= 1
                #gora
            hits = pg.sprite.spritecollide(self, self.game.people, True, collide_hit_rect)
            if hits:
                for sprite in hits:
                    sprite.banish()
            grasses = pg.sprite.spritecollide(self, self.game.grasses, False, grass_collide)

            if grasses:
                print("Trawa")
            roads = pg.sprite.spritecollide(self,self.game.roads, False, grass_collide)

            if roads:
                print("Droga")

            indoors = pg.sprite.spritecollide(self, self.game.indoors, False, grass_collide)
            if indoors:
                print("Wnetrze")

            dirt = pg.sprite.spritecollide(self, self.game.dirt, False, grass_collide)
            if dirt:
                print("Ziemia")

            self.countsteps += 1
            game.update()
            game.draw()
        self.countsteps -= 1

