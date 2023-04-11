import pygame as pg

Vec = pg.math.Vector2

TILE_SIZE = 20
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FPS = 60
GAME_TIME = 300
FIELD_COLOR = (55, 55, 55)

INITIAL_POSITION_OFFSET = Vec(FIELD_W // 2, 0)
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
