"""Battleship using defined functions and while loops."""

__author__ = "730648114"

# Importing random function
import random

# Named constants
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Defining input_guess
def input_guess(grid: int, rowcol: str) -> int:
    assert rowcol == "row" or rowcol == "column"
    guess = int(input(f"Guess a {rowcol}: "))
    i = 0
    while i == 0:
        if guess > grid or guess <= 0:
            guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
        else:
            i += 1

# Defining print_grid
def print_grid(grid: int, g_row: int, g_col: int, win: bool) -> None:
    row_count = 1
    col_count = 1
    result = ""
    if win == True:
        result = RED_BOX
    else:
        result = WHITE_BOX

    while row_count <= grid:
        emoji = ""
        col_count = 1
        if g_row == row_count:
            while col_count <= grid:
                if g_col == col_count:
                    emoji += result
                else:
                    emoji += BLUE_BOX
                col_count += 1
        else:
            while col_count <= grid:
                emoji += BLUE_BOX
                col_count += 1
        print(emoji)
        row_count += 1

# Defining correct_guess
def correct_guess(s_row: int, s_col: int, g_row: int, g_col: int) -> bool:
    if s_row == g_row and s_col == g_col:
        return True
    else:
        return False
    
# Defining main
def main(grid: int, s_row: int, s_col: int) -> None:
    turn = 1
    while turn <= 5:
        print(f"=== Turn {turn}/5 ===")
        gr = input_guess(grid, "row")
        gc = input_guess(grid, "column")
        success = correct_guess(s_row, s_col, gr, gc)
        print_grid(grid, gr, gc, success)
        if success == True:
            print(f"Hit!\nYou won in {turn}/5 turns!")
            turn =+ 8
            quit()
        else:
            print("Miss!")
            turn += 1
    print("X/5 - Better luck next time!")
    quit()

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))