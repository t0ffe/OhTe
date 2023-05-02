import random as ra
import pygame as pg
from settings import (
    INITIAL_POSITION_OFFSET, TILE_SIZE,
    TETROMINOES, TETROMINOE_SHAPES,
    DIRECTIONS, Vec, FIELD_W, FIELD_H,
    COLORS
)


class Block(pg.sprite.Sprite):
    """A class representing a block of a tetromino.

    Attributes:
        tetromino (Tetromino): The Tetromino object that the block belongs to.
        position (Vec): The position of the block on the game field.
        image (pygame.Surface): The image of the block.
        rect (pygame.Rect): The rectangle that encloses the block.
        cleared (bool): A flag indicating if the block has been cleared or not.

    Methods:
        is_cleared(): Deletes the block if it is cleared.
        rotate(pivot_point, direction): Rotates the block around a pivot point in a given direction.
        set_position(): Sets the position of the block on the game field.
        update(): Calls the is_cleared() and set_position() methods of the Block object.
        collision(position): Returns True if the block collides with a block at a given position, False otherwise.
    """

    def __init__(self, tetromino, position):
        """Initializes a Block object with the given tetromino and position."""
        self.tetromino = tetromino
        self.position = Vec(position) + INITIAL_POSITION_OFFSET
        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()
        self.cleared = False

    def is_cleared(self):
        """Deletes the block if it is cleared."""
        if self.cleared:
            self.kill()

    def rotate(self, pivot_point, direction):
        """Rotates the block around a pivot point in a given direction.

        Args:
            pivot_point (Vec): The point around which the block will be rotated.
            
            direction (str): The direction of rotation.

        Returns:
            Vec: The rotated position of the block.
        """
        position_corrected = self.position - pivot_point
        rotated = position_corrected.rotate(direction)
        return rotated + pivot_point

    def set_position(self):
        """Sets the position of the block on the game field."""
        self.rect.topleft = self.position * TILE_SIZE

    def update(self):
        """Calls the is_cleared() and set_position() methods of the Block object."""
        self.is_cleared()
        self.set_position()

    def collision(self, position):
        """Returns True if the block collides at a given position, False otherwise.

        Args:
            position (Vec): The position to check for collision.

        Returns:
            bool: True if the block collides with a block at the given position, False otherwise.
        """
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
        """
        Rotates the tetromino clockwise or counterclockwise depending on the specified direction.

        Args:
            direction (str): The direction and amount of the rotation.
        """
        pivot_point = self.blocks[0].position
        blok_positions = [block.rotate(pivot_point, direction)
                          for block in self.blocks]
        if not self.collision(blok_positions):
            for i, block in enumerate(self.blocks):
                block.position = blok_positions[i]

    def collision(self, block_pos):
        """
        Check if the current Tetromino object collides with any other blocks in the game field.

        Args:
            block_pos (list): A list of the positions of the blocks in the Tetromino object.

        Returns:
            bool: True if the Tetromino object collides with any other blocks in the game field,
                  False otherwise.

        The method takes a list of the positions of the blocks in the Tetromino object, and checks
        if any of these positions overlap with the positions of any other blocks in the game field.
        If there is a collision, the method returns True, indicating that the Tetromino cannot move
        in the requested direction. Otherwise, the method returns False, indicating that the Tetromino
        can move in the requested direction.
        """
        return any(map(Block.collision, self.blocks, block_pos))

    def move(self, direction):
        """
        Moves the tetromino in the specified direction.

        Args:
            direction (str): The direction to move the tetromino in. Valid values are 'l' (left), 'r' (right), 'd' (down).
        """
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
