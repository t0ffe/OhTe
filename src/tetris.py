import pygame as pg
from settings import TILE_SIZE, FIELD_W, FIELD_H
from tetromino import Tetromino


class Tetris:
    def __init__(self, game):
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def control(self, key):
        if key == pg.K_a:
            self.tetromino.move("l")
        elif key == pg.K_d:
            self.tetromino.move("r")

    def draw_grid(self):
        for width in range(FIELD_W):
            for height in range(FIELD_H):
                pg.draw.rect(self.game.screen, 'black', (width * TILE_SIZE,
                             height * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.game.animation:
            self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.game.screen)
