import random as ra
import pygame as pg
from settings import (
    INITIAL_POSITION_OFFSET, TILE_SIZE,
    TETROMINOES, TETROMINOE_SHAPES,
    DIRECTIONS, Vec, FIELD_W, FIELD_H,
    RANDOM_COLORS
)


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = Vec(position) + INITIAL_POSITION_OFFSET
        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()

    def set_position(self):
        self.rect.topleft = self.position * TILE_SIZE

    def update(self):
        self.set_position()

    def collision(self, position):
        block_x, block_y = int(position.x), int(position.y)
        if 0 <= block_x < FIELD_W and block_y < FIELD_H and (
                block_y < 0 or not self.tetromino.tetris.array_of_gamefield[block_y][block_x]):
            return False
        return True


class Tetromino:
    def __init__(self, tetris):
        self.shape_num = ra.randint(0, 6)
        self.tetris = tetris
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(ra.choice(RANDOM_COLORS))
        self.shape = TETROMINOES[self.shape_num]
        self.blocks = [Block(self, position)
                       for position in TETROMINOE_SHAPES[self.shape_num]]
        self.at_bottom = False

    def collision(self, block_pos):
        return any(map(Block.collision, self.blocks, block_pos))

    def move(self, direction):
        move_dir = DIRECTIONS[direction]
        blocks_future_pos = [block.position +
                             move_dir for block in self.blocks]
        collision = self.collision(blocks_future_pos)

        if not collision:
            for block in self.blocks:
                block.position += move_dir
        elif direction == "d":
            self.at_bottom = True

    def update(self):
        self.move("d")
