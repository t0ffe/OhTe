import sys
import pygame as pg
from settings import GAME_TIME, FAST_GAME_TIME, FIELD_COLOR, FPS, WIN_RES, FIELD_RES
from tetris import Tetris
from user_interface import Text


class Game:
    """The `Game` class represents the game engine for OhTe-tris. 

    Attributes:
    - `screen`: Pygame window to render the game.
    - `clock`: Pygame clock to limit the game's FPS.
    - `user_event`: Pygame user event to be used for regular game animation.
    - `fast_user_event`: Pygame user event to be used for fast game animation.
    - `animation`: Boolean flag to indicate if the regular game animation should be triggered.
    - `fast_animation`: Boolean flag to indicate if the fast game animation should be triggered.
    - `tetris`: The instance of the `Tetris` class representing the game mechanics.

    Usage:
    - Instantiate the `Game` class to start the game engine, and call the `run()` 
    method to start the main game loop.
    """

    def __init__(self):
        pg.init()
        pg.display.set_caption('OhTe-tris')
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.animation = False
        self.fast_animation = False
        self.timer()
        self.tetris = Tetris(self)
        self.user_interface = Text(self)

    def timer(self):
        pg.time.set_timer(self.user_event, GAME_TIME)
        pg.time.set_timer(self.fast_user_event, FAST_GAME_TIME)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=(33, 33, 33))
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.user_interface.draw()
        pg.display.flip()

    def check_events(self):
        self.animation = False
        self.fast_animation = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
            if event.type == self.user_event:
                self.animation = True
            if event.type == self.fast_user_event:
                self.fast_animation = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
