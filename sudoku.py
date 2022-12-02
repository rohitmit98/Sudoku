import pygame.time
import sys
import buttons
from board import Board
from red_box import RedBox
from constants import *

# initialize pygame screen
pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, 1000 / 2))

# define fonts
welcome_font = pygame.font.SysFont('Times New Roman', WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

# button instances
easy = buttons.Buttons(-200 / 2, 50 / 2, button_font, screen, WHITE, 'Easy')
medium = buttons.Buttons(0, 50 / 2, button_font, screen, WHITE, 'Medium')
hard = buttons.Buttons(200 / 2, 50 / 2, button_font, screen, WHITE, 'Hard')
reset = buttons.Buttons(-200 / 2, 500 / 2, button_font, screen, WHITE, 'reset')
restart = buttons.Buttons(0, 500 / 2, button_font, screen, WHITE, 'restart')
exit_ = buttons.Buttons(200 / 2, 500 / 2, button_font, screen, WHITE, 'exit')
exit_centered = buttons.Buttons(0, 500 / 2, button_font, screen, WHITE, 'exit')


def game_start_text():
    '''
    Initializes start menu text (not screen)
    '''
    welcome_message = f'Welcome to Sudoku'
    welcome_surf = welcome_font.render(welcome_message, 0, BLACK)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200 / 2))
    screen.blit(welcome_surf, welcome_rect)

    game_mode_message = f'------ Select Game Mode ------'
    game_mode_surf = screen_font.render(game_mode_message, 0, BLACK)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 / 2))
    screen.blit(game_mode_surf, game_mode_rect)


def game_over_screen(result):
    '''
    Uses bool (result) to determine whether to show loser or winner text and respective buttons.
    If result = False: Create loser screen.
    If result = True: Create winner screen. 
    '''
    game_over = True
    while game_over is True:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 450, 500))

        if result is False:
            losing_message = f'YOU HAVE LOST!'
            welcome_surf = welcome_font.render(losing_message, 0, BLACK)
            welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200 / 2))
            screen.blit(welcome_surf, welcome_rect)
            restart.create_button()
            if restart.input():
                menu_screen()
                game_over = False
        else:
            game_mode_message = f'YOU WON!'
            game_mode_surf = screen_font.render(game_mode_message, 0, BLACK)
            game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 / 2))
            screen.blit(game_mode_surf, game_mode_rect)
            exit_centered.create_button()
            if exit_centered.input():
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def menu_screen():
    '''
    Creates a menu screen. 
    '''
    menu = True
    while menu is True:
        screen.fill(BG_COLOR)
        game_start_text()

        # create buttons and input conditions 
        easy.create_button()
        medium.create_button()
        hard.create_button()

        if easy.input():
            easy_mode_screen()
            menu = False

        if medium.input():
            medium_mode_screen()
            menu = False

        if hard.input():
            hard_mode_screen()
            menu = False

        # event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def easy_mode_screen():
    '''
    Create initialized sudoku board screen for 'easy' difficulty.
    '''
    screen.fill(BG_COLOR)
    easy_board = Board(screen, 'easy')
    easy_board.draw()
    easy_board.draw_numbers(screen)
    x, y = easy_board.first_value()

    # define variables
    made = 0
    x_old = 0
    y_old = 0
    key_user = 48
    winner = None

    easy_mode = True
    while easy_mode is True:

        # create buttons and input conditions
        reset.create_button()
        if reset.input():
            easy_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

        restart.create_button()
        if restart.input():
            menu_screen()
            easy_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        # check winner condition
        winner = easy_board.check_board()
        if winner is not None:
            pygame.time.wait(2000)
            easy_mode = False

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

                if 0 <= x <= 8 and 0 <= y <= 8:
                    # insert sketch number into board dimensions on RETURN (Enter)
                    if event.key == pygame.K_RETURN:
                        if easy_board.empty_solution[x][y] == 0 and key_user != 48:
                            Board.clear(easy_board, x, y)
                            Board.place_number(easy_board, x, y, chr(key_user))

                            # update internal 2D array with keystroke
                            num = (int(chr(key_user)))
                            easy_board.update_board(num, x, y)
                            key_user = 48

                    # clear sketch number and update 2D array with 0 on BACKSPACE (Delete)
                    if event.key == pygame.K_BACKSPACE:
                        if easy_board.board.board[x][y] > 0 and easy_board.empty_solution[x][y] == 0:
                            easy_board.update_board(0, x, y)
                            Board.clear(easy_board, x, y)
                    
                    # allow user to navigate fillable cells using arrow keys
                    if event.key == pygame.K_UP and easy_board.empty_solution[x-1][y] == 0:
                        red_box = RedBox(easy_board, screen, x - 1, y)
                    if x < 8:
                        if event.key == pygame.K_DOWN and easy_board.empty_solution[x+1][y] == 0:
                            red_box = RedBox(easy_board, screen, x + 1, y)
                    if event.key == pygame.K_LEFT and easy_board.empty_solution[x][y-1] == 0:
                        red_box = RedBox(easy_board, screen, x, y - 1)
                    if y < 8:
                        if event.key == pygame.K_RIGHT and easy_board.empty_solution[x][y+1] == 0:
                            red_box = RedBox(easy_board, screen, x, y + 1)

                    x_copy = x
                    
                    if made > 0:

                        if event.key == pygame.K_UP:
                            key_user = 48
                            Board.sketch_cover(easy_board)
                            column = []
                            for i in range(x_copy):
                                column.append(easy_board.empty_solution[x_copy-1][y])
                                x_copy -= 1
                            while 0 < x <= 8:
                                if easy_board.empty_solution[x-1][y] == 0:
                                    red_box = RedBox(easy_board, screen, x - 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x -= 1
                                    break
                                elif 0 not in column:
                                    break
                                elif easy_board.empty_solution[x-1][y] != 0:
                                    x -= 1

                        if event.key == pygame.K_DOWN:
                            key_user = 48
                            Board.sketch_cover(easy_board)
                            column = []
                            for i in reversed(range(x_copy, 8)):
                                column.append(easy_board.empty_solution[x_copy+1][y])
                                x_copy += 1
                            while 0 <= x < 8:
                                if easy_board.empty_solution[x+1][y] == 0:
                                    red_box = RedBox(easy_board, screen, x + 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x += 1
                                    break
                                elif 0 not in column:
                                    break
                                elif easy_board.empty_solution[x+1][y] != 0:
                                    x += 1

                        if event.key == pygame.K_LEFT:
                            key_user = 48
                            Board.sketch_cover(easy_board)
                            while 0 < y <= 8:
                                if easy_board.empty_solution[x][y-1] == 0:
                                    red_box = RedBox(easy_board, screen, x, y - 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y -= 1
                                    break
                                elif 0 not in easy_board.empty_solution[x][:y]:
                                    break
                                elif easy_board.empty_solution[x][y-1] != 0:
                                    y -= 1

                        if event.key == pygame.K_RIGHT:
                            key_user = 48
                            Board.sketch_cover(easy_board)
                            while 0 <= y < 8:
                                if easy_board.empty_solution[x][y+1] == 0:
                                    red_box = RedBox(easy_board, screen, x, y + 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y += 1
                                    break
                                elif 0 not in easy_board.empty_solution[x][y+1:]:
                                    break
                                elif easy_board.empty_solution[x][y+1] != 0:
                                    y += 1

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over_screen(winner)


def medium_mode_screen():
    '''
    Create initialized sudoku board screen for 'medium' difficulty.
    '''
    screen.fill(BG_COLOR)
    medium_board = Board(screen, 'medium')
    medium_board.draw()
    medium_board.draw_numbers(screen)
    x, y = medium_board.first_value()

    # define variables 
    made = 0
    x_old = 0
    y_old = 0
    key_user = 48
    winner = None

    medium_mode = True
    while medium_mode is True:

        # create buttons and input conditions
        reset.create_button()
        if reset.input():
            medium_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

        restart.create_button()
        if restart.input():
            menu_screen()
            medium_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        # check winner condition
        winner = medium_board.check_board()
        if winner is not None:
            pygame.time.wait(2000)
            medium_mode = False

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

                if 0 <= x <= 8 and 0 <= y <= 8:
                    # insert sketch number into board dimensions on RETURN (Enter)
                    if event.key == pygame.K_RETURN:
                        if medium_board.empty_solution[x][y] == 0 and key_user != 48:
                            Board.clear(medium_board, x, y)
                            Board.place_number(medium_board, x, y, chr(key_user))

                            # update internal 2D array with keystroke
                            num = (int(chr(key_user)))
                            medium_board.update_board(num, x, y)
                            key_user = 48

                    # clear sketch number and update 2D array with 0 on BACKSPACE (Delete)
                    if event.key == pygame.K_BACKSPACE:
                        if medium_board.board.board[x][y] > 0 and medium_board.empty_solution[x][y] == 0:
                            medium_board.update_board(0, x, y)
                            Board.clear(medium_board, x, y)

                    # allow user to navigate fillable cells using arrow keys
                    if event.key == pygame.K_UP and medium_board.empty_solution[x-1][y] == 0:
                        red_box = RedBox(medium_board, screen, x - 1, y)
                    if x < 8:
                        if event.key == pygame.K_DOWN and medium_board.empty_solution[x+1][y] == 0:
                            red_box = RedBox(medium_board, screen, x + 1, y)
                    if event.key == pygame.K_LEFT and medium_board.empty_solution[x][y-1] == 0:
                        red_box = RedBox(medium_board, screen, x, y - 1)
                    if y < 8:
                        if event.key == pygame.K_RIGHT and medium_board.empty_solution[x][y+1] == 0:
                            red_box = RedBox(medium_board, screen, x, y + 1)

                    x_copy = x
                    
                    if made > 0:

                        if event.key == pygame.K_UP:
                            key_user = 48
                            Board.sketch_cover(medium_board)
                            column = []
                            for i in range(x_copy):
                                column.append(medium_board.empty_solution[x_copy-1][y])
                                x_copy -= 1
                            while 0 < x <= 8:
                                if medium_board.empty_solution[x-1][y] == 0:
                                    red_box = RedBox(medium_board, screen, x - 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x -= 1
                                    break
                                elif 0 not in column:
                                    break
                                elif medium_board.empty_solution[x-1][y] != 0:
                                    x -= 1

                        if event.key == pygame.K_DOWN:
                            key_user = 48
                            Board.sketch_cover(medium_board)
                            column = []
                            for i in reversed(range(x_copy, 8)):
                                column.append(medium_board.empty_solution[x_copy+1][y])
                                x_copy += 1
                            while 0 <= x < 8:
                                if medium_board.empty_solution[x+1][y] == 0:
                                    red_box = RedBox(medium_board, screen, x + 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x += 1
                                    break
                                elif 0 not in column:
                                    break
                                elif medium_board.empty_solution[x+1][y] != 0:
                                    x += 1

                        if event.key == pygame.K_LEFT:
                            key_user = 48
                            Board.sketch_cover(medium_board)
                            while 0 < y <= 8:
                                if medium_board.empty_solution[x][y-1] == 0:
                                    red_box = RedBox(medium_board, screen, x, y - 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y -= 1
                                    break
                                elif 0 not in medium_board.empty_solution[x][:y]:
                                    break
                                elif medium_board.empty_solution[x][y-1] != 0:
                                    y -= 1

                        if event.key == pygame.K_RIGHT:
                            key_user = 48
                            Board.sketch_cover(medium_board)
                            while 0 <= y < 8:
                                if medium_board.empty_solution[x][y+1] == 0:
                                    red_box = RedBox(medium_board, screen, x, y + 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y += 1
                                    break
                                elif 0 not in medium_board.empty_solution[x][y+1:]:
                                    break
                                elif medium_board.empty_solution[x][y+1] != 0:
                                    y += 1

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over_screen(winner)


def hard_mode_screen():
    '''
    Create initialized sudoku board screen for 'hard' difficulty.
    '''
    screen.fill(BG_COLOR)
    hard_board = Board(screen, 'hard')
    hard_board.draw()
    hard_board.draw_numbers(screen)
    x, y = hard_board.first_value()

    # define variables
    made = 0
    x_old = 0
    y_old = 0
    key_user = 48
    winner = None

    hard_mode = True
    while hard_mode is True:

        # create buttons and input conditions
        reset.create_button()
        if reset.input():
            hard_board.reset_board()
            if made > 0:
                red_box.delete_red_box()
                made = 0

        restart.create_button()
        if restart.input():
            menu_screen()
            hard_mode = False

        exit_.create_button()
        if exit_.input():
            sys.exit()

        # check winner condition
        winner = hard_board.check_board()
        if winner is not None:
            pygame.time.wait(2000)
            hard_mode = False

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

                    elif hard_board.empty_solution[x][y] == 0 and (
                            x_old != x or y_old != y):
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

                if 0 <= x <= 8 and 0 <= y <= 8:
                    # insert sketch number into board dimensions on RETURN (Enter)
                    if event.key == pygame.K_RETURN:
                        if hard_board.empty_solution[x][y] == 0 and key_user != 48:
                            Board.clear(hard_board, x, y)
                            Board.place_number(hard_board, x, y, chr(key_user))

                            # update internal 2D array with keystroke
                            num = (int(chr(key_user)))
                            hard_board.update_board(num, x, y)
                            key_user = 48
                    
                    # clear sketch number and update 2D array with 0 on BACKSPACE (Delete)
                    if event.key == pygame.K_BACKSPACE:
                        if hard_board.board.board[x][y] > 0 and hard_board.empty_solution[x][y] == 0:
                            hard_board.update_board(0, x, y)
                            Board.clear(hard_board, x, y)

                    # allow user to navigate fillable cells using arrow keys
                    if event.key == pygame.K_UP and hard_board.empty_solution[x-1][y] == 0:
                        red_box = RedBox(hard_board, screen, x - 1, y)
                    if x < 8:
                        if event.key == pygame.K_DOWN and hard_board.empty_solution[x+1][y] == 0:
                            red_box = RedBox(hard_board, screen, x + 1, y)
                    if event.key == pygame.K_LEFT and hard_board.empty_solution[x][y-1] == 0:
                        red_box = RedBox(hard_board, screen, x, y - 1)
                    if y < 8:
                        if event.key == pygame.K_RIGHT and hard_board.empty_solution[x][y+1] == 0:
                            red_box = RedBox(hard_board, screen, x, y + 1)

                    x_copy = x
                    
                    if made > 0:

                        if event.key == pygame.K_UP:
                            key_user = 48
                            Board.sketch_cover(hard_board)
                            column = []
                            for i in range(x_copy):
                                column.append(hard_board.empty_solution[x_copy-1][y])
                                x_copy -= 1
                            while 0 < x <= 8:
                                if hard_board.empty_solution[x-1][y] == 0:
                                    red_box = RedBox(hard_board, screen, x - 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x -= 1
                                    break
                                elif 0 not in column:
                                    break
                                elif hard_board.empty_solution[x-1][y] != 0:
                                    x -= 1

                        if event.key == pygame.K_DOWN:
                            key_user = 48
                            Board.sketch_cover(hard_board)
                            column = []
                            for i in reversed(range(x_copy, 8)):
                                column.append(hard_board.empty_solution[x_copy+1][y])
                                x_copy += 1
                            while 0 <= x < 8:
                                if hard_board.empty_solution[x+1][y] == 0:
                                    red_box = RedBox(hard_board, screen, x + 1, y)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    x += 1
                                    break
                                elif 0 not in column:
                                    break
                                elif hard_board.empty_solution[x+1][y] != 0:
                                    x += 1

                        if event.key == pygame.K_LEFT:
                            key_user = 48
                            Board.sketch_cover(hard_board)
                            while 0 < y <= 8:
                                if hard_board.empty_solution[x][y-1] == 0:
                                    red_box = RedBox(hard_board, screen, x, y - 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y -= 1
                                    break
                                elif 0 not in hard_board.empty_solution[x][:y]:
                                    break
                                elif hard_board.empty_solution[x][y-1] != 0:
                                    y -= 1

                        if event.key == pygame.K_RIGHT:
                            key_user = 48
                            Board.sketch_cover(hard_board)
                            while 0 <= y < 8:
                                if hard_board.empty_solution[x][y+1] == 0:
                                    red_box = RedBox(hard_board, screen, x, y + 1)
                                    red_box.delete_red_box()
                                    red_box.draw_red_box()
                                    y += 1
                                    break
                                elif 0 not in hard_board.empty_solution[x][y+1:]:
                                    break
                                elif hard_board.empty_solution[x][y+1] != 0:
                                    y += 1

            elif key_user == 48:
                continue

        pygame.display.update()
    game_over_screen(winner)


menu_screen()
