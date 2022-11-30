import pygame
from constants import *


class RedBox:

    def __init__(self, board, screen, x, y):
        '''
        Initializes Red Box outline on a given cell. 
        self.screen    - The screen initialized on.
        self.board     - The board initialized on.
        self.x         - The column of the cell. 
        self.y         - The row of the cell. 
        '''
        self.screen = screen
        self.x = x
        self.y = y
        self.board = board
        
        # setting location and size for red-box depending on which box on board is selected boxes 1-3.
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
        '''
        Draws red-box using size and position data from initial method.
        '''
        pygame.draw.rect(self.screen, RED, self.rect, 4)

        # saving current box-data for use later.
        x_old = self.x
        y_old = self.y
        
        # creating global variable for use in delete_red_box method.
        global rect_old

        # Adding the data of the previously drawn rectangle boxes 1-3.
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
        '''
        Replaces old red-box with one of the background color
        '''
        pygame.draw.rect(self.screen, BG_COLOR, rect_old, 4)
        