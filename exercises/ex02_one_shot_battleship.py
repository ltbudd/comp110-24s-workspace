"""EX02 - One Shot Battleship - Adding while loops and more to Battleship."""
# If I had a penny for every time I had to resubmit because of punctuation at the end of the docstring, I'd have two pennies :(
__author__ = "730649114"

BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

grid = 5
s_row = 3
s_col = 2

result = ""
row_count = 1

# While loop for guessing the row
i = 0
g_row = int(input("Guess a row: "))
while i < 1:
    if g_row > grid or g_row < 0:
        g_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))
    else:
        i = i + 1

# While loop for guessing the column
i = 0
g_col = int(input("Guess a column: "))
while i < 1:
    if g_col > grid or g_col < 0:
        g_col = int(input(f"The grid is only {grid} by {grid}. Try again: "))
    else:
        i = i + 1

# While loop for printing grid, setting result value
if s_row == g_row and s_col == g_col:
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

# Comparison of guesses and secrets, hints
if s_row == g_row and s_col == g_col:
    print("Hit!")
elif s_row == g_row and s_col != g_col:
    print("Close! Correct row, wrong column.")
elif s_row != g_row and s_col == g_col:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")