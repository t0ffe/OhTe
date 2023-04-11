import unittest
import pygame as pg
from index import Game
from tetris import Tetris


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.tetris_game_instance = Game()

    def test_initialization(self):
        self.assertIsInstance(self.tetris_game_instance, Game)
        self.assertIsInstance(self.tetris_game_instance.screen, pg.Surface)
        self.assertIsInstance(self.tetris_game_instance.clock, pg.time.Clock)
        self.assertIsInstance(self.tetris_game_instance.tetris, Tetris)
        # assert grid size
