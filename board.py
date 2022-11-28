import pygame
from sudoku_generator import SudokuGenerator
from constants import *


class Board:
    '''
    This class represents an entire Sudoku board. A Board object has 81 Cell objects.
    '''

    def __init__(self, screen, difficulty):
        '''
        Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy, medium, or hard.
        '''
        self.screen = screen
        pygame.display.set_caption("Sudoku")

        if difficulty == 'easy':
            self.difficulty = 30
        elif difficulty == 'medium':
            self.difficulty = 40
        elif difficulty == 'hard':
            self.difficulty = 50
        self.board = SudokuGenerator(9, self.difficulty)
        self.board.fill_values()
        self.solution = [row[:] for row in self.board.board]
        self.board.remove_cells()
        self.empty_solution = [row[:] for row in self.board.board]

    def draw(self):
        '''
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. 
        Draws every cell on this board.
        '''
        # draw horizontal lines
        for i in range(0, BOARD_ROWS + 1):
            if i % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE),
                                 2 * LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

            # draw vertical lines
        for j in range(0, BOARD_COLS + 1):
            if j % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT),
                                 2 * LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, BLACK, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_numbers(self, screen):
        num_font = pygame.font.SysFont('Times New Roman', VAL_FONT)
        offset_x = 40 / 2
        offset_y = 20 / 2
        for row in range(0, 9):
            for col in range(0, 9):
                if self.board.board[row][col] == 0:
                    continue
                output = self.board.board[row][col]
                numbers = num_font.render(str(output), 0, BLACK)
                self.screen.blit(numbers, ((col * SQUARE_SIZE) + offset_x, (row * SQUARE_SIZE) + offset_y))

    def draw_box(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.empty_solution[i][j] == 0:
                    pygame.draw.rect(self.screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, 50, 50), 4)
                else:
                    pass

    def click(self, x, y):
        '''
        If a tuple of (x, y) coordinates is within the displayed board, 
        this function returns a tuple of the (row, col) of the cell which was clicked.
        '''
        
        if x <= 450 and y <= 450:
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            return row, col
        return self.first_value()

        # returns 
    def first_value(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.empty_solution[row][col] > 0:
                    return row, col

    def first_empty(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.empty_solution[row][col] == 0:
                    return row, col

    def clear(self, x, y):
        '''
        Clears the value cell. Note that the user can only remove 
        the cell values and sketched value that arefilled by themselves.
        '''
        pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(y * SQUARE_SIZE + 6, x * SQUARE_SIZE + 6, 40, 40))

    def sketch(self, row, col, value):
        '''
        Sets the sketched value of the current selected cell equal to user entered value. 
        It will be displayed at the top left corner of the cell using the draw() function.
        '''
        num_font = pygame.font.SysFont('Times New Roman', VAL_FONT_SMALL)
        offset_x = 7
        offset_y = 4
        output = value
        numbers = num_font.render(str(output), 0, GRAY)
        self.screen.blit(numbers, ((col * SQUARE_SIZE) + offset_x, (row * SQUARE_SIZE) + offset_y))

    def sketch_cover(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                offset_x = 8
                offset_y = 6
                pygame.draw.rect(self.screen, (140, 33, 21), ((j * SQUARE_SIZE) + offset_y,
                                                              (i * SQUARE_SIZE) + offset_x, 11, 11))

    def place_number(self, row, col, value):
        '''
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.
        '''
        num_font = pygame.font.SysFont('Times New Roman', VAL_FONT)
        offset_x = 40 / 2
        offset_y = 20 / 2
        output = value
        # changed inputted 'enter' key number to white
        numbers = num_font.render(str(output), 0, WHITE)
        self.screen.blit(numbers, ((col * SQUARE_SIZE) + offset_x, (row * SQUARE_SIZE) + offset_y))

    def is_full(self):
        '''
        Returns a Boolean value indicating whether the board is full or not.
        '''
        for row in range(0, 9):
            for col in range(0, 9):
                if self[i][j] == '0':
                    return False
        return True

    def reset_board(self):
        # resets user 2D-array to empty_solution array
        self.board.board = [row[:] for row in self.empty_solution]
        for row in range(0, 9):
            for col in range(0, 9):
                if self.board.board[row][col] == 0:
                    pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(col * SQUARE_SIZE + 6, row * SQUARE_SIZE + 6, 40, 40))

    def update_board(self, num, x, y):
        '''
        Updates the underlying 2D board with the values in all cells.
        '''
        self.board.board[x][y] = num
        # click = update board with new number that gets appended to list from keydown event
        return None

    def check_board(self):
        '''
        Check whether the Sudoku board is solved correctly.
        '''
        # only occurs if all numbers are filled in sudoku board
        if sum(x.count(0) for x in self.board.board) == 0:
            if self.board.board == self.solution:
                return True
            else:
                return False