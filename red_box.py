import pygame
from constants import *


class RedBox:

    def __init__(self, board, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.board = board

        if (x == 0 or x == 3 or x == 6) and (y == 0 or y == 3 or y == 6):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 2, self.x * SQUARE_SIZE + 2, 48, 48)
        elif (x == 0 or x == 3 or x == 6) and (y == 1 or y == 4 or y == 7):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 2, 49, 48)
        elif (x == 0 or x == 3 or x == 6) and (y == 2 or y == 5 or y == 8):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 2, 49, 48)

        elif (x == 1 or x == 4 or x == 7) and (y == 0 or y == 3 or y == 6):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 2, self.x * SQUARE_SIZE + 1, 48, 49)
        elif (x == 1 or x == 4 or x == 7) and (y == 1 or y == 4 or y == 7):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 1, 49, 49)
        elif (x == 1 or x == 4 or x == 7) and (y == 2 or y == 5 or y == 8):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 1, 49, 49)

        elif (x == 2 or x == 5 or x == 8) and (y == 0 or y == 3 or y == 6):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 2, self.x * SQUARE_SIZE + 1, 48, 49)
        elif (x == 2 or x == 5 or x == 8) and (y == 1 or y == 4 or y == 7):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 1, 49, 49)
        elif (x == 2 or x == 5 or x == 8) and (y == 2 or y == 5 or y == 8):
            self.rect = pygame.Rect(self.y * SQUARE_SIZE + 1, self.x * SQUARE_SIZE + 1, 49, 49)

    def draw_red_box(self):
        pygame.draw.rect(self.screen, RED, self.rect, 4)
        x_old = self.x
        y_old = self.y
        global rect_old

        if (self.x == 0 or self.x == 3 or self.x == 6) and (self.y == 0 or self.y == 3 or self.y == 6):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 2, x_old * SQUARE_SIZE + 2, 48, 48)
        elif (self.x == 0 or self.x == 3 or self.x == 6) and (self.y == 1 or self.y == 4 or self.y == 7):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 2, 49, 48)
        elif (self.x == 0 or self.x == 3 or self.x == 6) and (self.y == 2 or self.y == 5 or self.y == 8):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 2, 49, 48)

        elif (self.x == 1 or self.x == 4 or self.x == 7) and (self.y == 0 or self.y == 3 or self.y == 6):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 2, x_old * SQUARE_SIZE + 1, 48, 49)
        elif (self.x == 1 or self.x == 4 or self.x == 7) and (self.y == 1 or self.y == 4 or self.y == 7):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 1, 49, 49)
        elif (self.x == 1 or self.x == 4 or self.x == 7) and (self.y == 2 or self.y == 5 or self.y == 8):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 1, 49, 49)

        elif (self.x == 2 or self.x == 5 or self.x == 8) and (self.y == 0 or self.y == 3 or self.y == 6):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 2, x_old * SQUARE_SIZE + 1, 48, 49)
        elif (self.x == 2 or self.x == 5 or self.x == 8) and (self.y == 1 or self.y == 4 or self.y == 7):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 1, 49, 49)
        elif (self.x == 2 or self.x == 5 or self.x == 8) and (self.y == 2 or self.y == 5 or self.y == 8):
            rect_old = pygame.Rect(y_old * SQUARE_SIZE + 1, x_old * SQUARE_SIZE + 1, 49, 49)

    def delete_red_box(self):
        pygame.draw.rect(self.screen, BG_COLOR, rect_old, 4)

    def check_red_box(self):
        if pygame.draw.rect(self.screen, RED, self.rect, 4):
            return True
        return False

    def move_box(self):
        if self.board.empty_solution[self.x][self.y] == 0:
            self.rect.move_ip(self.x, self.y)
            pygame.draw.rect(self.screen, RED, rect_old, 4)
