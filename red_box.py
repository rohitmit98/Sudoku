import pygame
from constants import *


class RedBox:
    def __init__(self, board, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.board = board
        self.rect = pygame.Rect(self.y * SQUARE_SIZE, self.x * SQUARE_SIZE, 50, 50)

    def create_red_box(self):
        pygame.draw.rect(self.screen, RED, self.rect, 4)

    def check_red_box(self):
        if pygame.draw.rect(self.screen, RED, self.rect, 4):
            return True
        return False

    def move_box(self):
        if self.board.empty_solution[self.x][self.y] == 0:
            red_box.create_red_box()
            print(red_box.check_red_box())
