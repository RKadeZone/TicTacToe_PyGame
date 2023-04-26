# -*- coding: utf-8 -*-
#! /usr/bin/python3
# (c) RKADE GAMES, LLC. Freedom to distribute.
"""
This Python script begins the implemention of the game 'Tic-Tac-Toe' using 
PyGame.

Author: Roland Kunkel
Date: 04/26/2023

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
pygame.display.set_caption("Tic-Tac-Toe")

# Set up game loop
running = True
clock = pygame.time.Clock()
FPS = 60

# Create game board and cells
BOARD_SIZE = 3
CELL_SIZE = 200  # 600 / 3
BOARD = [[' ' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Draw game board 
def draw_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            cell_rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, cell_rect, 2)

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Draw to the screen
    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit pygame and exit the program
pygame.quit()
sys.exit()