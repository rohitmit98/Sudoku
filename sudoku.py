import pygame.time

import board
import buttons
from sudoku_generator import *
from board import *
import sys
from constants import *
from red_box import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, 1000 / 2))

# define fonts
welcome_font = pygame.font.SysFont('Times New Roman', WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

# button instances
easy = buttons.Buttons(-200 / 2, 50/2, button_font, screen, FILL_COLOR, 'Easy')
medium = buttons.Buttons(0, 50/2, button_font, screen, FILL_COLOR, 'Medium')
hard = buttons.Buttons(200/2, 50/2, button_font, screen, FILL_COLOR, 'Hard')
reset = buttons.Buttons(-200/2, 500/2, button_font, screen, FILL_COLOR, 'reset')
restart = buttons.Buttons(0, 500/2, button_font, screen, FILL_COLOR, 'restart')
exit_ = buttons.Buttons(200/2, 500/2, button_font, screen, FILL_COLOR, 'exit')


# start menu text
def game_start():
    # rohit - p;
    welcome_message = f'Welcome to Sudoku'
    welcome_surf = welcome_font.render(welcome_message, 0, LINE_COLOR)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200/2))
    screen.blit(welcome_surf, welcome_rect)

    game_mode_message = f'------ Select Game Mode ------'
    game_mode_surf = screen_font.render(game_mode_message, 0, LINE_COLOR)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50/2))
    screen.blit(game_mode_surf, game_mode_rect)


# READ BEFORE CONTINUING
# CURRENT PROBLEMS I AM HAVING:
# THINGS I HAVEN'T DONE:
# ROHIT
'''
# 3 different arrays 
1. Keeping track of final solution
2. Keep track of solution with removed cells separately
3. Keep track of user_inputs 
'''


def pygame_events_modes():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


# start game by showing main menu
def menu():
    game_menu = True
    while game_menu is True:
        screen.fill(BG_COLOR)
        game_start()
        easy.create_button()
        medium.create_button()
        hard.create_button()

        if easy.input():
            easy_mode()
            game_menu = False

        if medium.input():
            medium_mode()
            game_menu = False

        if hard.input():
            hard_mode()
            game_menu = False

        # event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def easy_mode():
    screen.fill(BG_COLOR)
    easy_board = Board(900, 1000, screen, 'easy')
    easy_board.draw()
    easy_board.draw_numbers(screen)
    # easy_board.check_board()
    # easy_board.draw_box()

    easy_mode = True
    while easy_mode is True:

        reset.create_button()
        restart.create_button()
        if restart.input():
            menu()
            easy_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # mouse = pygame.mouse.get_pos()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = easy_board.click(event.pos[0], event.pos[1])
            #     x, y = int(x), int(y)
            #     red_box = RedBox(screen, x, y)
            #     if easy_board.empty_solution[x][y] == 0:
            #         red_box.create_red_box()
        pygame.display.update()



def medium_mode():
    screen.fill(BG_COLOR)
    medium_board = Board(900, 1000, screen, 'medium')
    medium_board.draw()
    medium_board.draw_numbers(screen)
    # medium_board.check_board()

    medium_mode = True
    while medium_mode is True:
        reset.create_button()
        restart.create_button()
        if restart.input():
            menu()
            medium_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        pygame_events_modes()


def hard_mode():
    screen.fill(BG_COLOR)
    hard_board = Board(900, 1000, screen, 'hard')
    hard_board.draw()
    hard_board.draw_numbers(screen)
    # hard_board.check_board()

    hard_mode = True
    while hard_mode is True:

        reset.create_button()

        restart.create_button()
        if restart.input():
            menu()
            hard_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        pygame_events_modes()


def winner():
    pass


menu()

# b = SudokuGenerator(9, 30)
# solution = b.fill_values()
# b.print_board()
# empty_solution = b.remove_cells()
# print()
# b.print_board()
# user_input_arr = []
