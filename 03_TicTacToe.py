# -*- coding: utf-8 -*-
#! /usr/bin/python3
# (c) RKADE GAMES, LLC. Freedom to distribute.
"""
This Python script containts the final implemention of the game 'Tic-Tac-Toe' 
using PyGame.

Author: Roland Kunkel
Date: 05/01/2023

Usage:
Run the script from the command line using the following command:
python tic_tac_toe.py

Functions:
- draw_board: Draws the Tic-Tac-Toe board on the game window.
- handle_input: Handles player input for QUIT and MOUSEBUTTONDOWN.
- make_move: Checks for valid move and updates board contents on sucessful move.
- draw_X: Draws an 'X' in the center position of associated grid.
- draw_O: Draws an 'O' in the center position of associated grid.
- display_game_over: Draws the game over message to screen.
- draw_restart_buttons: Draws the "Play Again?" message and Yes/No buttons to screen.
- new_game: Handle new game state, reset board and game state flags.

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
CROSS = 'X'
CIRCLE = 'O'
board = [[EMPTY_CELL for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (200, 200, 200)
X_COLOR = NO_BUTTON_COLOR = (255, 0, 0)
YES_BUTTON_COLOR = (0, 255, 0)
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
            if board[row][col] == EMPTY_CELL and cell_rect.collidepoint(pygame.mouse.get_pos()):
                # draw a highlighted rectangle if the mouse is over the cell
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, cell_rect, 2)
            elif board[row][col] == CROSS:
                draw_X(row, col)
            elif board[row][col] == CIRCLE:
                draw_O(row, col)

# Variable to hold current player's mark
current_player = CROSS

# Update game state when player makes move
def make_move(row, col):
    # we're modifying globals within a function's scope
    # so we declare them here
    global board
    global current_player
    
    if board[row][col] == EMPTY_CELL:
        board[row][col] = current_player # modify a global 
        current_player = CIRCLE if current_player == CROSS else CROSS # modify a global 
        pygame.display.set_caption(f'Tic Tac Toe - Current Turn: "{current_player}"')

# Handle new game state
def new_game():
    global board
    global current_player
    global game_over
    global is_winner

    board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    game_over = False
    is_winner = None
    current_player = CROSS

# Handle player input
def handle_input():
    global running 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse cursor
                mouse_pos = pygame.mouse.get_pos()

                # Determine which cell the player has clicked on
                row = mouse_pos[0] // CELL_SIZE
                col = mouse_pos[1] // CELL_SIZE  
                
                # Make the move on the board
                make_move(row, col)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse cursor
                mouse_pos = pygame.mouse.get_pos()
                if yes_btn_rect.collidepoint(mouse_pos):
                    new_game()
                elif no_btn_rect.collidepoint(mouse_pos):
                    running = False

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

# set the font and font size for the game
GAME_FONT = pygame.font.Font(None, 64)

def display_game_over(message):
    # create the game over message surface with the given message
    game_over_msg = GAME_FONT .render(message, True, BLACK)
    # get the size and position of the message surface
    game_over_msg_rect = game_over_msg.get_rect()
    game_over_msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)
    # draw the game over message on the screen
    screen.blit(game_over_msg, game_over_msg_rect)

# set the font and font size for the buttons
BUTTON_FONT = pygame.font.Font(None, 32)

# create the 'play again' text
restart_msg = GAME_FONT.render("Play Again?", True, BLACK)
restart_msg_rect = restart_msg.get_rect()
restart_msg_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
# create the 'yes' button surface
yes_btn = BUTTON_FONT.render("Yes", True, BLACK)
yes_btn_rect = yes_btn.get_rect()
yes_btn_rect.center = (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 75)
# create the 'no' button surface
no_btn = BUTTON_FONT.render("No", True, BLACK)
no_btn_rect = no_btn.get_rect()
no_btn_rect.center = (WINDOW_WIDTH // 2 + 50, WINDOW_HEIGHT // 2 + 75)

# create a function to draw the restart prompt buttons
def draw_restart_buttons():
    # draw the game over message on the screen
    screen.blit(restart_msg, restart_msg_rect)
    # draw the 'yes' button on the screen
    pygame.draw.rect(screen, YES_BUTTON_COLOR, (yes_btn_rect.x - 10, yes_btn_rect.y - 10, yes_btn_rect.width + 20, yes_btn_rect.height + 20))
    screen.blit(yes_btn, yes_btn_rect)
    # draw the 'no' button on the screen
    pygame.draw.rect(screen, NO_BUTTON_COLOR, (no_btn_rect.x - 10, no_btn_rect.y - 10, no_btn_rect.width + 20, no_btn_rect.height + 20))
    screen.blit(no_btn, no_btn_rect)

# Game loop
game_over = False
is_winner = None
while running:
    # Handle events
    handle_input()

    # Update game logic
    if not game_over:
        is_winner = check_winner()
        if is_winner is not None:
            game_over = True

    # Draw to the screen
    screen.fill(WHITE)

    # if not game over, display the board
    if not game_over:
        draw_board()
    else:  # otherwise we handle win/lose/tie message and play again buttons
        if is_winner in [CROSS, CIRCLE]:
            display_game_over(f"Player: '{is_winner}' has won!")
        else:
            display_game_over("The game has ended in a tie!")
        draw_restart_buttons()

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit pygame and exit the program
pygame.quit()
sys.exit()