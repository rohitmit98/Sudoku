import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        # nolan - a
        '''Constructor for the Cell class'''
        self.value = value
        self.row = row
        self.col = col
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # font size? - Adam V
        self.val_font = pygame.font.Font(None, VAL_FONT)

    def set_cell_value(self, value):
        # nolan - a
        '''Setter for this cell’s value'''
        self.value_rect = self.value_surf.get_rect(center=(450, 450))

    def set_sketched_value(self, value):
        # nolan - a
        '''Setter for this cell’s sketched value'''
        self.value_surf = VAL_FONT.render(str(value), 0, COLOR)

    def draw(self):
        # nolan - a
        '''Draws this cell, along with the value inside it.
      If this cell has a nonzero value, that value is displayed.       Otherwise, no value is displayed in the cell.
      The cell is outlined red if it is currently selected.'''

        self.screen.blit(self.value_surf, self.value_rect)