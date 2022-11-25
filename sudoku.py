from sudoku_generator import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((width, height))
screen.fill(bg_color)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

#     if event.type == pygame.quit():
#         pygame.quit()
#
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#         if is_full:
#             game_over = True
#

    pygame.display.update()
