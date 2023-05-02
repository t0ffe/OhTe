import pygame as pg
from settings import TILE_SIZE, FIELD_W, FIELD_H, INITIAL_POSITION_OFFSET, Vec
from tetromino import Tetromino


class Tetris:
    def __init__(self, game):
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.array_of_gamefield = self.make_array()
        self.faster_speed = False

    def check_full_lines(self):
        row = FIELD_H - 1
        for value_y in range(FIELD_H - 1, -1, -1):
            for value_x in range(FIELD_W):
                self.array_of_gamefield[row][value_x] = self.array_of_gamefield[value_y][value_x]

                if self.array_of_gamefield[value_y][value_x]:
                    self.array_of_gamefield[row][value_x].position = Vec(
                        value_x, value_y)

            if sum(map(bool, self.array_of_gamefield[value_y])) < FIELD_W:
                row -= 1
            else:
                for value_x in range(FIELD_W):
                    self.array_of_gamefield[row][value_x].cleared = True
                    self.array_of_gamefield[row][value_x] = 0

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
            self.faster_speed = False
            if self.game_over():
                self.__init__(self.game)
            else:
                self.blocks_to_array()
                self.tetromino = Tetromino(self)

    def control(self, key):
        if key in (pg.K_LEFT, pg.K_a):
            self.tetromino.move("l")
        elif key in (pg.K_RIGHT, pg.K_d):
            self.tetromino.move("r")
        elif key in (pg.K_UP, pg.K_w):
            self.tetromino.rotate(90)
        elif key in (pg.K_DOWN, pg.K_s):
            self.faster_speed = True

    def draw_grid(self):
        for width in range(FIELD_W):
            for height in range(FIELD_H):
                pg.draw.rect(self.game.screen, 'black', (width * TILE_SIZE,
                             height * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.game.animation,
                   self.game.fast_animation][self.faster_speed]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.tetromino_at_bottom()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.game.screen)
