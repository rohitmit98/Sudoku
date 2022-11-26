import pygame.time

from sudoku_generator import *
import sys

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
welcome_font = pygame.font.Font(None, WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)


class Buttons:
    def __init__(self, screen, x, y, color=FILL_COLOR, name='button'):
        self.color = color
        self.name = name
        self.screen = screen
        self.x = x
        self.y = y

    def create_button(self):
        surf = button_font.render(self.name, 0, LINE_COLOR)
        rect = surf.get_rect(center=(WIDTH // 2 + self.x, HEIGHT // 2 + self.y))
        pygame.draw.rect(screen, self.color, pygame.Rect(rect), 0)
        screen.blit(surf, rect)
        # shows rectangle coordinates
        # print(pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(rect), 2))


def game_difficulty_buttons():
    easy = Buttons(screen, -200, 50, FILL_COLOR, 'Easy')
    easy.create_button()
    medium = Buttons(screen, 0, 50, FILL_COLOR, 'Medium')
    medium.create_button()
    hard = Buttons(screen, 200, 50, FILL_COLOR, 'Hard')
    hard.create_button()


def game_board_buttons():
    reset = Buttons(screen, -200, 500, FILL_COLOR, 'reset')
    reset.create_button()
    restart = Buttons(screen, 0, 500, FILL_COLOR, 'restart')
    restart.create_button()
    exit = Buttons(screen, 200, 500, FILL_COLOR, 'exit')
    exit.create_button()


def game_start():
    # rohit - p;
    screen.fill(BG_COLOR)
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
1. game_start() screen doesn't "go away", and can continually click 'easy' button after I use draw() method from Board class (i.e. b.draw() )
2. need to implement 2D board from sudoku_generator.py onto GUI in Board class. Unsure, how to accomplish yet.
3. Use solution from #1 to solve for reset/restart/exit buttons when a game has started
'''

# start game by showing main menu
game_start()
game_difficulty_buttons()
running = True
while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        # print(mouse)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if select easy
            if 200 + 100 > mouse[0] > 200 and 480 + 40 > mouse[1] > 480:
                b = Board(900, 1000, screen, 'easy')
                b.draw()
                game_board_buttons()

            # if select medium
            if 370 + 160 > mouse[0] > 370 and 480 + 40 > mouse[1] > 480:
                b = Board(900, 1000, screen, 'medium')
                b.draw()
                game_board_buttons()

            # if select hard
            if 600 + 100 > mouse[0] > 370 and 480 + 40 > mouse[1] > 480:
                b = Board(900, 1000, screen, 'hard')
                b.draw()
                game_board_buttons()

    pygame.display.update()
