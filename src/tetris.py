import pygame as pg
from settings import TILE_SIZE, FIELD_W, FIELD_H, INITIAL_POSITION_OFFSET
from tetromino import Tetromino


class Tetris:
    def __init__(self, game):
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.array_of_gamefield = self.make_array()

    def blocks_to_array(self):
        for block in self.tetromino.blocks:
            block_x, block_y = int(block.position.x), int(block.position.y)
            self.array_of_gamefield[block_y][block_x] = block

    def make_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def game_over(self):
        if self.tetromino.blocks[0].position.y == INITIAL_POSITION_OFFSET[1]:
            pg.time.wait(400)
            return True
        return False

    def tetromino_at_bottom(self):
        if self.tetromino.at_bottom:
            if self.game_over():
                self.__init__(self.game)
            else:
                self.blocks_to_array()
                self.tetromino = Tetromino(self)

    def control(self, key):
        if key == pg.K_LEFT:
            self.tetromino.move("l")
        elif key == pg.K_RIGHT:
            self.tetromino.move("r")

    def draw_grid(self):
        for width in range(FIELD_W):
            for height in range(FIELD_H):
                pg.draw.rect(self.game.screen, 'black', (width * TILE_SIZE,
                             height * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.game.animation:
            self.tetromino.update()
            self.tetromino_at_bottom()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.game.screen)
