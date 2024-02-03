import pygame
import vec
import main

class Player():
    def __init__(self, path: str):
        self.image = pygame.image.load(path)
        self.size = vec.Vec2(50, 50)
        self.image = pygame.transform.scale(self.image, self.size.round())
        self.rect = self.image.get_rect()
        self.position = vec.Vec2((main.WINDOW_SIZE.x / 2) - (self.size.x / 2), 7 * (main.WINDOW_SIZE.y / 8))
        self.rotation = 0
        self.rot_speed = 100
        self.health = 10
        self.fire_rate = 1
        self.speed = 300
        pass
    
    def update(self, dt):
        
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.position.x -= self.speed * dt
            self.rotation -= self.rot_speed * dt
            
        if keys[pygame.K_RIGHT]:
            self.position.x += self.speed * dt
            self.rotation += self.rot_speed * dt
        if keys[pygame.K_UP]:
            self.position.y -= self.speed * dt
            
        if keys[pygame.K_DOWN]:
            
            self.position.y += self.speed * dt
            
        
        # check bounds
        if self.position.y >=  main.WINDOW_SIZE.y - self.size.y:
            self.position.y = main.WINDOW_SIZE.y - self.size.y
        if self.position.x <= 0:
            self.position.x = 0
        elif self.position.x >= main.WINDOW_SIZE.x - self.size.x:
            self.position.x = main.WINDOW_SIZE.x - self.size.x
            
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        
                
    def draw(self, screen):
        loc = self.image.get_rect().center  #rot_image is not defined 
        rot_sprite = pygame.transform.rotate(self.image, self.rotation)
        rot_sprite.get_rect().center = loc
        screen.blit(rot_sprite, self.position.round())
        
        pass
    
    def is_collide(self, enemy) -> bool:
        return (
            ((self.position.x + self.size.x) >= enemy.position.x) and
            (self.position.x <= (enemy.position.x + enemy.size.x)) and
            ((self.position.y + self.size.y) >= enemy.position.y) and
            (self.position.y <= (enemy.position.y + enemy.size.y)))
                
        
