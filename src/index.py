import sys
import pygame as pg
from settings import FIELD_RES, GAME_TIME, FIELD_COLOR, FPS
from tetris import Tetris


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('OhTe-tris')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.user_event = pg.USEREVENT + 0
        self.animation = False
        self.timer()
        self.tetris = Tetris(self)

    def timer(self):
        pg.time.set_timer(self.user_event, GAME_TIME)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pg.display.flip()

    def check_events(self):
        self.animation = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
            elif event.type == self.user_event:
                self.animation = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
