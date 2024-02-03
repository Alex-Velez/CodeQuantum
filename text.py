import pygame
import main

class Text():
    def __init__(self, message):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(message, True, (0, 255, 0), (0, 0, 128))
        self.textRect = self.text.get_rect()
        self.textRect.x = (main.WINDOW_SIZE.x / 2) - (self.textRect.width / 2)
        self.textRect.y = (main.WINDOW_SIZE.y / 2) - (self.textRect.height / 2)
        pass
    
    def draw(self, screen):
        screen.blit(self.text, self.textRect)