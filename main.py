import sys
from os import path
from reaper import *
from tilemap import *
from person import *
from wall import *

from random import randint


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
        self.drawPeople = True

    def new(self):
        self.reaper = pg.sprite.Group()
        self.people = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        Person(self, 3, 6)
        Person(self, 10, 8)
        Person(self, 4, 2,1,1,1,1,1)

        for i in range(100):
           Person(self, randint(1,41), randint(1,35))

        self.agent = Reaper(self, 41, 35)
        self.camera = Camera(self.map.width, self.map.height)
        for walls in self.map.tmxdata.layers[3]: #wszystkie obiekty w warstwie "walls"
               Wall(self, walls.x, walls.y, walls.width, walls.height)



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
        self.reaper.update()
        if self.drawPeople == True:
            for sprite in self.people:
                sprite.update()
        self.camera.update(self.agent)

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.reaper:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.drawPeople == True:
            for sprite in self.people:
                    sprite.draw(self.map_img)
                    self.drawPeople = False
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
