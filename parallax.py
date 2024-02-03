import main
import pygame
import vec

class ParallaxBackground():
    def __init__(self, path: str, size: (int, int), speed: int):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        self.position = (0.0, 0.0)
        self.position = vec.Vec2(0.0, 0.0)
        self.size = vec.Vec2(size[0], size[1])
        self.speed = speed
    
    def update(self, dt):
        self.position.y += self.speed * dt
        
    
    def draw(self, screen):    
        copy_pos = (int(self.position.x), int(self.position.y - self.size.y))
        screen.blit(self.image, copy_pos)
        screen.blit(self.image, self.position.round())
        if self.position.y > main.WINDOW_SIZE.y:
            self.position.y = 0
            
    
