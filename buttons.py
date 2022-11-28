import pygame
from constants import *


class Buttons:
    def __init__(self, x, y, font, screen, color=FILL_COLOR, name='button'):
        self.x = x
        self.y = y
        self.font = font
        self.screen = screen
        self.color = color
        self.name = name
        self.surf = font.render(self.name, 0, LINE_COLOR)
        self.rect = self.surf.get_rect(center=(WIDTH // 2 + self.x, HEIGHT // 2 + self.y))
        self.clicked = False

    def create_button(self):
        # white rectangle
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.rect), 0)
        # black text
        self.screen.blit(self.surf, self.rect)
        # # shows rectangle coordinates
        # print(pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(self.rect), 2))

    def input(self):
        action = False

        # get mouse position
        mouse = pygame.mouse.get_pos()
        # print(mouse)

        # check mouseover and clicked conditions
        if self.rect.collidepoint(mouse):
            # if left mouse button clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
