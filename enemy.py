import pygame
import main
import vec
import random

class Enemy():
    min_size = 25
    max_size = 100
    min_speed = 25
    max_speed = 100
    max_drift = 10
    max_rot_speed = 100
    
    def __init__(self, path: str):
        self.image = pygame.image.load(path)
        r_size = random.randint(Enemy.min_size, Enemy.max_size)
        self.size = vec.Vec2(r_size, r_size)
        self.image = pygame.transform.scale(self.image, self.size.round())
        self.rect = self.image.get_rect()
        self.position = vec.Vec2(random.randint(0, main.WINDOW_SIZE.x), 0)
        self.health = 100
        self.speed = random.randint(Enemy.min_speed, Enemy.max_speed)
        self.drift = random.randint(-Enemy.max_drift, Enemy.max_drift)
        self.rotation = 0
        self.rot_speed = random.randint(-Enemy.max_rot_speed, Enemy.max_rot_speed)
        pass
    
    def update(self, dt, to_pos):
        self.position.y += self.speed * dt
        self.position.x += self.drift * dt
        self.rotation += self.rot_speed * dt 
        
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        pass
    
    def draw(self, screen):
        loc = self.image.get_rect().center  #rot_image is not defined 
        rot_sprite = pygame.transform.rotate(self.image, self.rotation)
        rot_sprite.get_rect().center = loc
        screen.blit(rot_sprite, self.position.round())
        pass
    
    def reset(self):
        self.position.y = -self.size.y
        self.position.x = random.randint(0, main.WINDOW_SIZE.x)
        r_size = random.randint(Enemy.min_size, Enemy.max_size)
        self.size = vec.Vec2(r_size, r_size)
        self.drift = random.randint(-Enemy.max_drift, Enemy.max_drift)
        
    def upgrade():
        Enemy.min_size += 1
        Enemy.max_size += 1
        Enemy.min_speed += 1
        Enemy.max_speed += 1
        Enemy.max_drift += 1
        Enemy.max_rot_speed += 1