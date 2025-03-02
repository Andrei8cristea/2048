Cristea Andrei - 2048 Game Project

This project is a Python implementation of the classic 2048 game. It includes both a console (text-based) version and a graphical interface using Pygame.
Overview

    Game Mechanics:
        The game board is a 4x4 matrix initially filled with zeros.
        New tiles (values 2, 4, or 8) are added at random empty positions. The odds for each value are 60% for 2, 30% for 4, and 10% for 8.
        Players make moves using the WASD keys (or arrow keys):
            Left (A or LEFT): Moves all non-zero tiles to the left, merging adjacent equal values.
            Right (D or RIGHT): Moves all tiles to the right, merging where possible.
            Up (W or UP): Transposes the board, applies a left move, then transposes back.
            Down (S or DOWN): Transposes the board, applies a right move, then transposes back.
        After every valid move, a new tile is added to the board.
        The game ends when there are no valid moves (i.e. no zeros and no adjacent equal tiles).

    Scoring:
    The score is calculated as the sum of all numbers on the board.

Features

    Tile Addition:
    Automatically adds a new tile (with value 2, 4, or 8) at a random empty position after each move.

    Movement & Merging:
    Implements functions to shift the board left, right, up, or down. When two adjacent tiles have the same value, they merge to form a tile with double the value.

    Graphical Interface:
    Uses Pygame to display the board with colored tiles and rendered text.
        The window is 800x800 pixels.
        Each tile is drawn with a color according to its value.
        A "Game Over" screen is displayed when no moves remain, along with a "Play Again" button.

    Console Mode:
    (Commented out in the code) A text-based version exists for quick testing.

How to Play

    Start the Game:
    Run the game script to start a new game. The board is initialized with an empty 4x4 matrix and one starting tile.

    Make Moves:
        Use W or the UP arrow to move tiles up.
        Use A or the LEFT arrow to move tiles left.
        Use S or the DOWN arrow to move tiles down.
        Use D or the RIGHT arrow to move tiles right.

    Merging Tiles:
    When two adjacent tiles with the same number touch during a move, they merge into one tile with double the original value.

    Game Over:
    The game ends when there are no empty spaces left and no adjacent tiles can merge. The final score is displayed on the Game Over screen.

Code Structure

    Matrix Setup & Tile Addition:
        set_value_0(matrix): Initializes the 4x4 board with zeros.
        add_tile(matrix): Adds a new tile at a random empty position with values determined by probability.

    Movement Functions:
        move_left(matrix): Shifts tiles left and merges equal adjacent values.
        move_right(matrix): Shifts tiles right and merges where possible.
        move_up(matrix) and move_down(matrix): Utilize board transposition to reuse the left/right logic.

    Game State:
        check_if_over(matrix): Checks if there are any valid moves remaining.
        calculate_score(matrix): Computes the current score as the sum of all tiles.

    Graphical Interface (Pygame):
        draw_board(matrix): Draws the current state of the board on the screen.
        game_over_screen(score): Displays a Game Over screen with the final score and a "Play Again" option.
        startgame(): Initializes the game, sets up the board, and handles the game loop including user inputs.
