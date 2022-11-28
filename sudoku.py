import pygame.time
import board
import buttons
import sudoku_generator
from board import *
import sys
from red_box import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, 1000 / 2))

# define fonts
welcome_font = pygame.font.SysFont('Times New Roman', WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

# button instances
easy = buttons.Buttons(-200 / 2, 50 / 2, button_font, screen, FILL_COLOR, 'Easy')
medium = buttons.Buttons(0, 50 / 2, button_font, screen, FILL_COLOR, 'Medium')
hard = buttons.Buttons(200 / 2, 50 / 2, button_font, screen, FILL_COLOR, 'Hard')

# make this work!
reset = buttons.Buttons(-200 / 2, 500 / 2, button_font, screen, FILL_COLOR, 'reset')

restart = buttons.Buttons(0, 500 / 2, button_font, screen, FILL_COLOR, 'restart')
exit_ = buttons.Buttons(200 / 2, 500 / 2, button_font, screen, FILL_COLOR, 'exit')


# start menu text
def game_start_text():
    # rohit - p;
    welcome_message = f'Welcome to Sudoku'
    welcome_surf = welcome_font.render(welcome_message, 0, LINE_COLOR)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200 / 2))
    screen.blit(welcome_surf, welcome_rect)

    game_mode_message = f'------ Select Game Mode ------'
    game_mode_surf = screen_font.render(game_mode_message, 0, LINE_COLOR)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 / 2))
    screen.blit(game_mode_surf, game_mode_rect)


def game_over(result):
    game_over = True
    while game_over is True:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 450, 500))

        # vacha- P rohit - a
        if result is False:
            losing_message = f'YOU HAVE LOST!'
            welcome_surf = welcome_font.render(losing_message, 0, LINE_COLOR)
            welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200 / 2))
            screen.blit(welcome_surf, welcome_rect)
            restart.create_button()
            if restart.input():
                menu()
                game_over = False
        else:
            game_mode_message = f'YOU WON!'
            game_mode_surf = screen_font.render(game_mode_message, 0, LINE_COLOR)
            game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 / 2))
            screen.blit(game_mode_surf, game_mode_rect)
            exit_.create_button()
            if exit_.input():
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


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


# start game by showing main menu
def menu():
    game_menu = True
    while game_menu is True:
        screen.fill(BG_COLOR)
        game_start_text()
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
    easy_board = Board(screen, 'easy')
    easy_board.draw()
    easy_board.draw_numbers(screen)
    key_user = 48
    x, y = easy_board.first_value()

    made = 0
    x_old = 0
    y_old = 0
    winner = None

    easy_mode = True
    while easy_mode is True:

        reset.create_button()
        if reset.input():
            easy_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

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

            # create red box and move red box with each click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = easy_board.click(event.pos[0], event.pos[1])

                x, y = int(x), int(y)
                key_user = 48
                Board.sketch_cover(easy_board)

                red_box = RedBox(easy_board, screen, x, y)
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if easy_board.empty_solution[x][y] == 0 and made == 0:
                        red_box.draw_red_box()
                        made += 1

                    elif easy_board.empty_solution[x][y] == 0 and (x_old != x or y_old != y):
                        red_box.delete_red_box()
                        red_box.draw_red_box()

                x_old = x
                y_old = y
            # create sketch number and cover

            if event.type == pygame.KEYDOWN:
                if 48 < event.key < 58:
                    if easy_board.empty_solution[x][y] == 0:
                        key_user = event.key
                        Board.sketch_cover(easy_board)
                        Board.sketch(easy_board, x, y, chr(key_user))

                # insert sketch number into board
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if event.key == pygame.K_RETURN and easy_board.empty_solution[x][y] == 0 and key_user != 48:
                        Board.clear(easy_board, x, y)
                        Board.place_number(easy_board, x, y, chr(key_user))

                        # update board with keystroke
                        num = (int(chr(key_user)))
                        easy_board.update_board(num, x, y)
                        key_user = 48

                        winner = easy_board.check_board()
                        if winner is not None:
                            pygame.time.wait(2500)
                            easy_mode = False

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over(winner)

def medium_mode():
    screen.fill(BG_COLOR)
    medium_board = Board(screen, 'easy')
    medium_board.draw()
    medium_board.draw_numbers(screen)
    key_user = 48
    x, y = medium_board.first_value()

    made = 0
    x_old = 0
    y_old = 0
    winner = None

    medium_mode = True
    while medium_mode is True:

        reset.create_button()
        if reset.input():
            medium_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

        restart.create_button()
        if restart.input():
            menu()
            medium_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # create red box and move red box with each click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = medium_board.click(event.pos[0], event.pos[1])

                x, y = int(x), int(y)
                key_user = 48
                Board.sketch_cover(medium_board)

                red_box = RedBox(medium_board, screen, x, y)
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if medium_board.empty_solution[x][y] == 0 and made == 0:
                        red_box.draw_red_box()
                        made += 1

                    elif medium_board.empty_solution[x][y] == 0 and (x_old != x or y_old != y):
                        red_box.delete_red_box()
                        red_box.draw_red_box()

                x_old = x
                y_old = y
            # create sketch number and cover

            if event.type == pygame.KEYDOWN:
                if 48 < event.key < 58:
                    if medium_board.empty_solution[x][y] == 0:
                        key_user = event.key
                        Board.sketch_cover(medium_board)
                        Board.sketch(medium_board, x, y, chr(key_user))

                # insert sketch number into board
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if event.key == pygame.K_RETURN and medium_board.empty_solution[x][y] == 0 and key_user != 48:
                        Board.clear(medium_board, x, y)
                        Board.place_number(medium_board, x, y, chr(key_user))

                        # update board with keystroke
                        num = (int(chr(key_user)))
                        medium_board.update_board(num, x, y)
                        key_user = 48

                        winner = medium_board.check_board()
                        if winner is not None:
                            pygame.time.wait(2500)
                            medium_mode = False

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over(winner)

def hard_mode():
    screen.fill(BG_COLOR)
    hard_board = Board(screen, 'easy')
    hard_board.draw()
    hard_board.draw_numbers(screen)
    key_user = 48
    x, y = hard_board.first_value()

    made = 0
    x_old = 0
    y_old = 0
    winner = None

    hard_mode = True
    while hard_mode is True:

        reset.create_button()
        if reset.input():
            hard_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

        restart.create_button()
        if restart.input():
            menu()
            hard_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # create red box and move red box with each click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = hard_board.click(event.pos[0], event.pos[1])

                x, y = int(x), int(y)
                key_user = 48
                Board.sketch_cover(hard_board)

                red_box = RedBox(hard_board, screen, x, y)
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if hard_board.empty_solution[x][y] == 0 and made == 0:
                        red_box.draw_red_box()
                        made += 1

                    elif hard_board.empty_solution[x][y] == 0 and (x_old != x or y_old != y):
                        red_box.delete_red_box()
                        red_box.draw_red_box()

                x_old = x
                y_old = y
            # create sketch number and cover

            if event.type == pygame.KEYDOWN:
                if 48 < event.key < 58:
                    if hard_board.empty_solution[x][y] == 0:
                        key_user = event.key
                        Board.sketch_cover(hard_board)
                        Board.sketch(hard_board, x, y, chr(key_user))

                # insert sketch number into board
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if event.key == pygame.K_RETURN and hard_board.empty_solution[x][y] == 0 and key_user != 48:
                        Board.clear(hard_board, x, y)
                        Board.place_number(hard_board, x, y, chr(key_user))

                        # update board with keystroke
                        num = (int(chr(key_user)))
                        hard_board.update_board(num, x, y)
                        key_user = 48

                        winner = hard_board.check_board()
                        if winner is not None:
                            pygame.time.wait(2500)
                            hard_mode = False

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over(winner)

menu()
