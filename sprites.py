from settings import TILESIZE, PLAYER_SPEED, pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img_R
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0

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


class Person(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.person_img
        self.rect = self.image.get_rect()
        self.rect.y = y * TILESIZE
        self.rect.x = x * TILESIZE
