import pygame.time

import buttons
from buttons import Buttons
from sudoku_generator import *
import sys

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# game variables
game_menu = True

# define fonts
welcome_font = pygame.font.SysFont('Times New Roman', WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

# button instances
easy = buttons.Buttons(-200, 50, button_font, screen, FILL_COLOR, 'Easy')
medium = buttons.Buttons(0, 50, button_font, screen, FILL_COLOR, 'Medium')
hard = buttons.Buttons(200, 50, button_font, screen, FILL_COLOR, 'Hard')
reset = buttons.Buttons(-200, 500, button_font, screen, FILL_COLOR, 'reset')
restart = buttons.Buttons(0, 500, button_font, screen, FILL_COLOR, 'restart')
exit_ = buttons.Buttons(200, 500, button_font, screen, FILL_COLOR, 'exit')


def game_start():
    # rohit - p;
    welcome_message = f'Welcome to Sudoku'
    welcome_surf = welcome_font.render(welcome_message, 0, LINE_COLOR)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(welcome_surf, welcome_rect)

    game_mode_message = f'------ Select Game Mode ------'
    game_mode_surf = screen_font.render(game_mode_message, 0, LINE_COLOR)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_mode_surf, game_mode_rect)


# READ BEFORE CONTINUING
# CURRENT PROBLEMS I AM HAVING:
# THINGS I HAVEN'T DONE:
# ROHIT
'''
1. restart/resume/exit buttons are not registering 
2. need to implement 2D board from sudoku_generator.py onto GUI in Board class. Unsure, how to accomplish yet.
'''

# start game by showing main menu


running = True
while running:

    if game_menu:
        screen.fill(BG_COLOR)
        game_start()

        if easy.create_button():
            game_menu = False
            b = Board(900, 1000, screen, 'easy')
            b.draw()

        elif medium.create_button():
            game_menu = False
            b = Board(900, 1000, screen, 'medium')
            b.draw()

        elif hard.create_button():
            game_menu = False
            b = Board(900, 1000, screen, 'hard')
            b.draw()

    # event handler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
