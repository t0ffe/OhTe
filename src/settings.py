import pygame as pg

Vec = pg.math.Vector2

TILE_SIZE = 20
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.5, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * \
    FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

FPS = 60
GAME_TIME = 200
FAST_GAME_TIME = 5

POINT_PER_LINE = {0: 0, 1: 80, 2: 200, 3: 600, 4: 2400}

FIELD_COLOR = (55, 55, 55)
COLORS = ["cyan", "blue", "orange", "yellow", "green", "purple", "red"]

INITIAL_POSITION_OFFSET = Vec(FIELD_W // 2 - 1, 0)
NEXT_POSITION_OFFSET = Vec(FIELD_W * 1.2, FIELD_H * 0.17)

DIRECTIONS = {"l": Vec(-1, 0), "r": Vec(1, 0), "d": Vec(0, 1)}

TETROMINOES = ["I", "J", "L", "O", "S", "T", "Z"]

TETROMINOE_SHAPES = [
    [(0, 0), (0, 1), (0, -1), (0, -2)],
    [(0, 0), (-1, 0), (0, -1), (0, -2)],
    [(0, 0), (1, 0), (0, -1), (0, -2)],
    [(0, 0), (0, -1), (1, 0), (1, -1)],
    [(0, 0), (-1, 0), (0, -1), (1, -1)],
    [(0, 0), (-1, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (0, -1), (-1, -1)]
]
