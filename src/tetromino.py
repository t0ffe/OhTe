import random as ra
import pygame as pg
from settings import (
    INITIAL_POSITION_OFFSET, TILE_SIZE,
    TETROMINOES, TETROMINOE_SHAPES,
    DIRECTIONS, Vec, FIELD_W, FIELD_H,
    COLORS
)


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = Vec(position) + INITIAL_POSITION_OFFSET
        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()
        self.cleared = False

    def is_cleared(self):
        if self.cleared:
            self.kill()

    def rotate(self, pivot_point, direction):
        position_corrected = self.position - pivot_point
        rotated = position_corrected.rotate(direction)
        return rotated + pivot_point

    def set_position(self):
        self.rect.topleft = self.position * TILE_SIZE

    def update(self):
        self.is_cleared()
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
        self.image.fill(COLORS[self.shape_num])
        self.shape = TETROMINOES[self.shape_num]
        self.blocks = [Block(self, position)
                       for position in TETROMINOE_SHAPES[self.shape_num]]
        self.at_bottom = False

    def rotate(self, direction):
        pivot_point = self.blocks[0].position
        blok_positions = [block.rotate(pivot_point, direction) for block in self.blocks]
        if not self.collision(blok_positions):
            for i, block in enumerate(self.blocks):
                block.position = blok_positions[i]


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
