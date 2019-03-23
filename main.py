import sys
from os import path
from sprites import *
from tilemap import *


class Game:
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, 'images')
    map_folder = path.join(game_folder, 'maps')

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.map = TiledMap(path.join(self.map_folder, 'Szi1v2.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img_R = pg.image.load(path.join(self.img_folder, PLAYER_IMG_R)).convert_alpha()
        self.person_img = pg.image.load(path.join(self.img_folder, PERSON_IMG)).convert_alpha()
        self.player_img_L = pg.image.load(path.join(self.img_folder, PLAYER_IMG_L)).convert_alpha()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.person = Person(self, 5, 5)
        self.player = Player(self, 1, 1)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


g = Game()
while True:
    g.new()
    g.run()
