import board
from sudoku_generator import *
import sys

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
welcome_font = pygame.font.Font(None, WELCOME_FONT)
screen_font = pygame.font.Font(None, SCREEN_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)


# draw horizontal and vertical lines
# def draw_line():
#     for i in range(1, BOARD_ROWS):
#         pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE*i), (900, SQUARE_SIZE*i))
#     for i in range(1, BOARD_COLS):
#         pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*i, 0), (SQUARE_SIZE*i, 900))


def game_start():
    # rohit - p;
    screen.fill(BG_COLOR)
    welcome_message = f'Welcome to Sudoku'
    welcome_surf = welcome_font.render(welcome_message, 0, LINE_COLOR)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(welcome_surf, welcome_rect)

    game_mode_message = f'Select Game Mode:'
    game_mode_surf = screen_font.render(game_mode_message, 0, LINE_COLOR)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_mode_surf, game_mode_rect)

    easy_button = f'Easy'
    easy_surf = button_font.render(easy_button, 0, LINE_COLOR)
    easy_rect = easy_surf.get_rect(center=(WIDTH // 2 - 350, HEIGHT // 2 + 120))
    screen.blit(easy_surf, easy_rect)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(easy_rect), 2)

    medium_button = f'Medium'
    medium_surf = button_font.render(medium_button, 0, LINE_COLOR)
    medium_rect = medium_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    screen.blit(medium_surf, medium_rect)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(medium_rect), 2)


    hard_button = f'Hard'
    hard_surf = button_font.render(hard_button, 0, LINE_COLOR)
    hard_rect = hard_surf.get_rect(center=(WIDTH // 2 + 350, HEIGHT // 2 + 120))
    screen.blit(hard_surf, hard_rect)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(hard_rect), 2)



game_start()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
