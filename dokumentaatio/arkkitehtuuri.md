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
    class Text{
        UI
    }
    class settings{
        resolution
        shapes
        colors
        positions
    }

    Game --|> Tetris
    Tetris --|> Tetromino
    Tetromino --|> Block
    Game --|> Text
    Text  --|> settings
    Tetris --|> settings
    Tetromino --|> settings
    Block --|> settings

```
