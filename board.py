import pygame
from constants import *
from sudoku_generator import *


# adam v - a
class Board:
    """This class represents an entire Sudoku board. A Board object has 81 Cell objects.   """

    def __init__(self, width, height, screen, difficulty):
        # nolan - a # adam v - a(dbug)
        """Constructor for the Board class.
      screen is a window from PyGame.
      difficulty is a variable to indicate if the user chose easy, medium, or hard."""

        self.width = width
        self.height = height
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


    def draw(self):
        # nolan - a; adam v - debug
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board."""

        # draw horizontal lines
        for i in range(0, BOARD_ROWS + 1):
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE),
                                 2 * LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

            # draw vertical lines
        for j in range(0, BOARD_COLS + 1):
            if j % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT),
                                 2 * LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_numbers(self, screen):
        num_font = pygame.font.SysFont('Times New Roman', VAL_FONT)
        self.board.remove_cells()
        offset_x = 39
        offset_y = 20
        for row in range(0, 9):
            for col in range(0, 9):
                if self.board.board[row][col] == 0:
                    continue
                output = self.board.board[row][col]
                numbers = num_font.render(str(output), 0, LINE_COLOR)
                self.screen.blit(numbers, ((col * 100) + offset_x, (row * 100) + offset_y))

    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""

        # USE CLICK
        pass

    def click(self, x, y):
        # adam v - p; rohit - a
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None."""
        if x <= 900 and y <= 1000:
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE + 1
            return row, col
        return None

    def clear(self):
        '''Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell      values  and  sketched  value  that  are filled by themselves.  '''
        # row, col = self.select
        # if get_board

        pass

    def sketch(self, value):
        '''Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.'''

        pass

    def place_number(self, value):
        '''Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.'''
        pass

    def reset_to_original(self):
        '''Reset all cells in the board to their original values (0 if cleared, otherwise      the corresponding digit).'''
        pass

    def is_full(self):
        '''Returns a Boolean value indicating whether the board is full or not.'''
        # Adam V- p
        # need debug
        for i in range(len(self)):
            for j in range(len(self[0])):
                # not sure what the underlying "blank" space is to check for
                if self[i][j] == '0':
                    return False
        return True

        pass

    def update_board(self):
        '''Updates the underlying 2D board with the values in all cells.'''
        pass

    def find_empty(self):
        '''Finds an empty cell and returns its row and col as a tuple (x, y).'''
        pass

    def check_board(self):
        '''Check whether the Sudoku board is solved correctly.'''
        if self.solution != self.board.board:
            print(self.solution)
            print(self.board.board)
            print("true")


        # # adam v - p
        # for i in range(WIDTH):
        #     # check that each digit is not equal to the digit before it
        #     for j in range(HEIGHT):
        #         return False
        #         # not sure what to loop thru and find in order to prove correct
        # return True
        # pass

'''
   solution =       [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   empty_solution = [[0, 2, 0], [4, 0, 6], [7, 8, 0]]
   # enumerate empty_solution list to save all 0 indexes

   user_solution =  [[8, 2, 0], [4, 0, 6], [7, 8, 0]]


   '''


