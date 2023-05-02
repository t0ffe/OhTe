import pygame as pg
from settings import TILE_SIZE, FIELD_W, FIELD_H, INITIAL_POSITION_OFFSET, Vec
from tetromino import Tetromino


class Tetris:
    """
    Class representing the Tetris game.

    Attributes:
    -----------
    game: object
        The instance of the main game object.
    sprite_group: pygame.sprite.Group
        The sprite group containing all the Tetromino blocks.
    tetromino: Tetromino
        The current Tetromino object.
    array_of_gamefield: list of lists
        A 2D list representing the gamefield.
    faster_speed: bool
        A flag indicating whether the Tetromino is moving at a faster speed.

    Methods:
    --------
    check_full_lines()
        Checks for completed rows and clears them from the gamefield.
    blocks_to_array()
        Copies the blocks from the current Tetromino to the gamefield array.
    make_array()
        Initializes an empty gamefield array.
    game_over()
        Checks if the game is over by checking if any blocks have reached the top of the gamefield.
    tetromino_at_bottom()
        Checks if the current Tetromino has reached the bottom and updates the game state 
        accordingly.
    control(key)
        Controls the movement of the current Tetromino based on the user's key input.
    draw_grid()
        Draws the grid lines of the gamefield.
    update()
        Updates the game state by checking for completed rows, updating the current Tetromino, 
        and handling the game over condition.
    draw()
        Draws the gamefield grid and the current Tetromino blocks on the screen.
    """

    def __init__(self, game):
        """
        Initializes a Tetris object.

        Parameters:
        -----------
        game: object
            The instance of the main game object.
        """
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.array_of_gamefield = self.make_array()
        self.faster_speed = False

    def check_full_lines(self):
        """
        Checks for completed rows and clears them from the gamefield.
        """
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
        """
        Copies the blocks from the current Tetromino to the gamefield array.
        """
        for block in self.tetromino.blocks:
            block_x, block_y = int(block.position.x), int(block.position.y)
            self.array_of_gamefield[block_y][block_x] = block

    def make_array(self):
        """
        Initializes an empty gamefield array.

        Returns:
        list of lists
            A 2D list representing the gamefield.
        """
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def game_over(self):
        """
        Checks if the game is over by checking if any blocks have reached the top of the gamefield.

        Returns:
        bool
            True if the game is over, False otherwise.
        """
        if self.tetromino.blocks[0].position.y == INITIAL_POSITION_OFFSET[1]:
            pg.time.wait(400)
            return True
        return False

    def tetromino_at_bottom(self):
        """
        Check if the current Tetromino is at the bottom of the game field.
        If the Tetromino is at the bottom, it stops moving and is added to the game field.
        If the game is over (i.e. the Tetromino is at the top of the game field), restart the game.
        """
        if self.tetromino.at_bottom:
            self.faster_speed = False
            if self.game_over():
                self.__init__(self.game)
            else:
                self.blocks_to_array()
                self.tetromino = Tetromino(self)

    def control(self, key):
        """
        Move or rotate the current Tetromino based on the given input key.

        Parameters:
        key
            The key pressed by the user, mapped to one of the arrow keys or WASD.
        """
        if key in (pg.K_LEFT, pg.K_a):
            self.tetromino.move("l")
        elif key in (pg.K_RIGHT, pg.K_d):
            self.tetromino.move("r")
        elif key in (pg.K_UP, pg.K_w):
            self.tetromino.rotate(90)
        elif key in (pg.K_DOWN, pg.K_s):
            self.faster_speed = True

    def draw_grid(self):
        """
        Draws a grid of black rectangles on the game screen to represent the playing field.

        Each rectangle has a size of TILE_SIZE pixels and a black border of width 1 pixel.
        The grid covers an area of FIELD_W columns by FIELD_H rows, where FIELD_W and FIELD_H
        are constants defined in the settings module.

        This method is called once per frame by the Tetris game loop to draw the grid
        background before rendering the tetromino blocks and other sprites on top of it.
        """

        for width in range(FIELD_W):
            for height in range(FIELD_H):
                pg.draw.rect(self.game.screen, 'black', (width * TILE_SIZE,
                             height * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        """
        Updates the game state for a single frame.

        This method performs the following actions:
        - If the faster speed flag is set, triggers the fast animation, otherwise triggers the 
        normal animation.
        - Calls the `check_full_lines` method to check if there are any full lines in the game 
        field, and clear them.
        - Calls the `update` method of the current tetromino, which updates its position and state.
        - Calls the `tetromino_at_bottom` method to check if the current tetromino has reached 
        the bottom of the game field,and either starts a new tetromino or ends the game depending
        on whether the game is over or not.
        - Calls the `update` method of the sprite group, which updates the positions and states 
        of all sprites in the group.

        This method does not take any arguments, and does not return any values.
        """

        trigger = [self.game.animation,
                   self.game.fast_animation][self.faster_speed]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.tetromino_at_bottom()
        self.sprite_group.update()

    def draw(self):
        """
        Draw the game grid and all the sprites in the sprite group onto the game screen.

        The game grid is drawn by looping through each cell of the grid and drawing a black 
        rectangle with a white border.
        The sprite group is drawn using the `draw` method of the `pygame.sprite.Group` class.

        This method does not take any arguments and does not return anything.
        """
        self.draw_grid()
        self.sprite_group.draw(self.game.screen)
