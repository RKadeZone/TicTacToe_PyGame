# -*- coding: utf-8 -*-
#! /usr/bin/python3
# (c) RKADE GAMES, LLC. Freedom to distribute.
"""
This Python script begins the implemention of the game 'Tic-Tac-Toe' using 
PyGame.

Author: Roland Kunkel
Date: 04/27/2023

Usage:
Run the script from the command line using the following command:
python tic_tac_toe.py

Functions:
- draw_board: Draws the Tic-Tac-Toe board on the game window.

Note:
This script requires PyGame to be installed. You can install it using pip:
$ pip install pygame
"""

# Built-in libraries
import sys 
# 3rd-party libraries 
import pygame

# Initialize PyGame
pygame.init()

# Define dimensions of window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Create window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of window
pygame.display.set_caption('Tic Tac Toe - Current Turn: "X"')

# Set up game loop
running = True
clock = pygame.time.Clock()
FPS = 60

# Create game board and cells
BOARD_SIZE = 3
CELL_SIZE = 200 
EMPTY_CELL = ' '
board = [[EMPTY_CELL for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (200, 200, 200)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Define a consistent line thickness
LINE_THICKNESS = 10

# Create a function to draw an X at a given position on the game board
def draw_X(i, j):
    # calculate the coordinates of the four corners of the cell
    x1 = i * CELL_SIZE + LINE_THICKNESS
    y1 = j * CELL_SIZE + LINE_THICKNESS
    x2 = (i + 1) * CELL_SIZE - LINE_THICKNESS
    y2 = (j + 1) * CELL_SIZE - LINE_THICKNESS
    # draw the two diagonal lines of the X
    pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), LINE_THICKNESS)
    pygame.draw.line(screen, X_COLOR, (x2, y1), (x1, y2), LINE_THICKNESS)

# Create a function to draw an O at a given position on the game board
def draw_O(i, j):
    # calculate the center coordinates and radius of the circle
    center_x = i * CELL_SIZE + CELL_SIZE // 2
    center_y = j * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 2 - LINE_THICKNESS
    # draw the circle with the given color and thickness
    pygame.draw.circle(screen, O_COLOR, (center_x, center_y), radius, LINE_THICKNESS)

# Draw game board and its cells
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            cell_rect = pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, cell_rect, 2)
            if board[row][col] == ' ' and cell_rect.collidepoint(pygame.mouse.get_pos()):
                # draw a highlighted rectangle if the mouse is over the cell
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, cell_rect, 2)
            elif board[row][col] == 'X':
                draw_X(row, col)
            elif board[row][col] == 'O':
                draw_O(row, col)

# Variable to hold current player's mark
current_player = 'X'

# Update game state when player makes move
def make_move(row, col):
    # we're modifying globals within a function's scope
    # so we declare them here
    global board
    global current_player
    
    if board[row][col] == ' ':
        board[row][col] = current_player # modify a global 
        current_player = 'O' if current_player == 'X' else 'X' # modify a global 
        pygame.display.set_caption(f'Tic Tac Toe - Current Turn: "{current_player}"')

# Handle player input
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse cursor
            mouse_pos = pygame.mouse.get_pos()

            # Determine which cell the player has clicked on
            row = mouse_pos[0] // CELL_SIZE
            col = mouse_pos[1] // CELL_SIZE  
               
            
            # Make the move on the board
            make_move(row, col)



# create a function to check for a winner or a tie
def check_winner():
    # we're using the global board, not modifying it
    # check for a horizontal win
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY_CELL:
            return board[i][0]

    # check for a vertical win
    for j in range(BOARD_SIZE):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY_CELL:
            return board[0][j]

    # check for a diagonal win (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] != EMPTY_CELL:
        return board[0][0]

    # check for a diagonal win (bottom-left to top-right)
    if board[0][2] == board[1][1] == board[2][0] != EMPTY_CELL:
        return board[0][2]

    # check for a tie
    if all([cell != EMPTY_CELL for row in board for cell in row]):
        return 'tie'

    # if there is no winner or tie, return None
    return None

# Game loop
game_over = False
while running:
    # Handle events
    handle_input()

    # Update game logic
    if not game_over:
        is_winner = check_winner()
        if is_winner is not None:
            # Check for winning player or tie
            if is_winner in ['X', 'O']:
                print(f"Player: '{is_winner}' has won!")
            else:
                print("The game has ended in a tie!")
            game_over = True

    # Draw to the screen
    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit pygame and exit the program
pygame.quit()
sys.exit()