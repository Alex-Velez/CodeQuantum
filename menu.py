import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "true"
import pygame


WINDOW_SIZE = (856, 480)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True


b1 = pygame.image.load("resources/buttons/tile001.png")
b1 = pygame.transform.scale(b1, (200, 200))


while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
                break
            case _:
                pass
            
    screen.fill(pygame.Color(100, 100, 100))
    
    mp = pygame.mouse.get_pos()
    
    screen.blit(b1, (WINDOW_SIZE[0] / 3, WINDOW_SIZE[1] / 2))
    
    
    
    pygame.display.flip()
    
    pass

pygame.quit()
