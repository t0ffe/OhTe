import pygame.freetype as ft
from settings import TILE_SIZE, WIN_H, WIN_W


class Text:
    """The `Text` class represents the user interface for the game. 

    Attributes:
    - `game`: Pygame game to render the UI into.
    - `font`: font used to render the elements
    """

    def __init__(self, game):
        self.game = game
        self.font = ft.SysFont(ft.get_default_font(), WIN_W)

    def draw(self):
        """
        Draws the text to the right side of the playing field
        """
        self.font.render_to(self.game.screen, (WIN_W * 0.75, WIN_H * 0.01),
                            text='NEXT', fgcolor='white',
                            size=TILE_SIZE)
        self.font.render_to(self.game.screen, (WIN_W * 0.70, WIN_H * 0.7),
                            text='SCORE', fgcolor='white',
                            size=TILE_SIZE)
        self.font.render_to(self.game.screen, (WIN_W * 0.70, WIN_H * 0.8),
                            text=f'{self.game.tetris.score}', fgcolor='white',
                            size=TILE_SIZE * 1.5)
