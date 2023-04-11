import random as ra
import pygame as pg
from settings import (
    INITIAL_POSITION_OFFSET, TILE_SIZE,
    TETROMINOES, TETROMINOE_SHAPES,
    DIRECTIONS, Vec
)


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = Vec(position) + INITIAL_POSITION_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('white')
        self.rect = self.image.get_rect()

    def set_position(self):
        self.rect.topleft = self.position * TILE_SIZE

    def update(self):
        self.set_position()


class Tetromino:
    def __init__(self, tetris):
        self.shape_num = ra.randint(0, 6)
        self.tetris = tetris
        self.shape = TETROMINOES[self.shape_num]
        self.blocks = [Block(self, position)
                       for position in TETROMINOE_SHAPES[self.shape_num]]

    def move(self, direction):
        for block in self.blocks:
            block.position += DIRECTIONS[direction]

    def update(self):
        self.move("d")
