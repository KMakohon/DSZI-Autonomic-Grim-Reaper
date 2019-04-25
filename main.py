import sys
from os import path
from reaper import *
from tilemap import *
from person import *
from map_objects import *

from random import randint


class Game:
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, 'images')
    map_folder = path.join(game_folder, 'maps')




    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.map = TiledMap(path.join(self.map_folder, 'Szi1v2.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img_R = pg.image.load(path.join(self.img_folder, PLAYER_IMG_R)).convert_alpha()
        self.person_img = pg.image.load(path.join(self.img_folder, PERSON_IMG)).convert_alpha()
        self.player_img_L = pg.image.load(path.join(self.img_folder, PLAYER_IMG_L)).convert_alpha()
        self.drawPeople = True
        self.dead_img = pg.image.load(path.join(self.img_folder, DEAD_IMG)).convert_alpha()
        self.reaper = pg.sprite.Group()
        self.people = pg.sprite.Group()
        self.grasses = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.roads = pg.sprite.Group()
        self.indoors = pg.sprite.Group()
        self.dirt = pg.sprite.Group()
        self.font = pg.font.SysFont("arial", 20)

        self.playing = True
        for i in range(40):
            Person(self, randint(1, 41), randint(1, 35))
        self.agent = Reaper(self, 2, 2)
        self.camera = Camera(self.map.width, self.map.height)

    def new(self):
        for grass in self.map.tmxdata.layers[3]:
            Grass(self, grass.x, grass.y, grass.width, grass.height)

        for road in self.map.tmxdata.layers[5]:
            Road(self, road.x, road.y, road.width, road.height)

        for indoor in self.map.tmxdata.layers[6]:
            Indoor(self, indoor.x, indoor.y, indoor.width, indoor.height)

        for dirt in self.map.tmxdata.layers[7]:
            Dirt(self, dirt.x, dirt.y, dirt.width, dirt.height)

        for walls in self.map.tmxdata.layers[4]: #wszystkie obiekty w warstwie "walls"
            Wall(self, walls.x, walls.y, walls.width, walls.height)


    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.reaper.update()
        if self.drawPeople:
            for sprite in self.people:
                sprite.update()
        self.camera.update(self.agent)

    def draw(self):
        text = "Zostalo " + str(len(self.people)) + " ludzi."
        text2 = "Kostucha wykonala juz " + str(self.agent.countsteps) + " kroki."
        text_render = self.font.render(text, 1, (250, 250, 250))
        text_render2 = self.font.render(text2, 1, (250, 250, 250))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.reaper:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.drawPeople:
            for sprite in self.people:
                sprite.draw(self.map_img)
            self.drawPeople = False
        self.screen.blit(text_render, (10, 10))
        self.screen.blit(text_render2, (10, 30))

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.agent.go_to(self, pg.mouse.get_pos())


g = Game()
while True:
    g.new()
    g.run()
