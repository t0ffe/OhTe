```mermaid

classDiagram
    class Tetromino{
        shape
        blocks
    }
    class Tetris{
        tetromino
    }
    class Block{
        position
    }
    class Game{
        tetris
        clock
    }

    Game --|> Tetris
    Tetris --|> Tetromino
    Tetromino --|> Block

```
