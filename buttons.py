import pygame
from constants import *


class Buttons:
    def __init__(self, x, y, font, screen, color=WHITE, name='button'):
        '''
        Initializes button with appropriate parameters. 
        self.x and self.y  - x/y offset from the board's origin. 
        self.font          - the font used for the button name.
        self.screen        - the screen initialized on.
        self.color         - the color of the button's background.
        self.name          - the text that appears on the button. 
        '''
        self.x = x
        self.y = y
        self.font = font
        self.screen = screen
        self.color = color
        self.name = name
        self.surf = font.render(self.name, 0, BLACK)
        self.rect = self.surf.get_rect(center=(WIDTH // 2 + self.x, HEIGHT // 2 + self.y))
        self.clicked = False

    def create_button(self):
        '''
        Creates a button rectangle on the GUI.
        '''
        # white rectangle
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.rect), 0)
        # black text
        self.screen.blit(self.surf, self.rect)

    def input(self):
        '''
        Allows button to be clicked. 
        Returns bool; True if clicked, False if unclicked.
        '''
        # set variable
        action = False

        # get mouse position
        mouse = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(mouse):
            
            # if left mouse button clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
