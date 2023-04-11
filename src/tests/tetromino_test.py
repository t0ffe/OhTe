import unittest
from index import Game


class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.tetris_game_instance = Game()

    def test_movement_left_and_right(self):
        self.starting_pos = self.tetris_game_instance.tetris.tetromino.blocks[0].position[0]
        self.tetris_game_instance.animation = True

        # Test if pos was decreased by one
        self.tetris_game_instance.tetris.tetromino.move("l")
        self.assertEqual(
            self.tetris_game_instance.tetris.tetromino.blocks[0].position[0], self.starting_pos - 1)

        # Test if pos goes back to starting pos
        self.tetris_game_instance.tetris.tetromino.move("r")
        self.assertEqual(
            self.tetris_game_instance.tetris.tetromino.blocks[0].position[0], self.starting_pos)
