import unittest
import pygame as pg
from index import Game
from tetris import Tetris

class TestIndex(unittest.TestCase):
    def setUp(self):
        self.tetris_game_instance = Game()
        print(self.tetris_game_instance)
        print(self.tetris_game_instance.screen)
        print(self.tetris_game_instance.clock)
        print(self.tetris_game_instance.tetris)

    def test_initialization(self):
        assert isinstance(self.tetris_game_instance, Game)
        assert isinstance(self.tetris_game_instance.screen , pg.Surface)
        assert isinstance(self.tetris_game_instance.clock , pg.time.Clock)
        assert isinstance(self.tetris_game_instance.tetris, Tetris)
        # assert grid size