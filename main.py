import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "true"
import pygame
import random

import player
import parallax
import vec
import enemy
import text

WINDOW_SIZE = vec.Vec2(854, 480)

class Game():
    def __init__(self, win_size):
        pygame.init()
        pygame.display.set_caption("Drunk Space Crew")
        self.screen = pygame.display.set_mode(win_size.round())
        self.clock = pygame.time.Clock()
        self.getTicksLastFrame = 0.0
        self.dt = 0.0
        self.running = True
        self.background = parallax.ParallaxBackground("stuff/Purple_Nebula_03-1024x1024.png", (win_size.x, win_size.x), 100)
        self.player = player.Player("stuff/tiny_ship1.png")
        self.enemies = [enemy.Enemy(random.choice(["stuff/spr_meteor_small.png", "stuff/spr_big_meteor.png"])) for x in range(10)]
        self.spawn_timer = 0
        self.spawn_speed = 100
        self.level = 1
        self.menu_health = pygame.transform.scale(pygame.image.load("stuff/tile000.png"), (25, 25))
        self.dead_text = text.Text("You Are Dead!")
        

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.exit()
                case pygame.K_ESCAPE:
                    self.exit()

    def run(self):
        while self.running:
            self.handle_events()

            self.screen.fill(pygame.Color(25, 25, 25))
            
            t = pygame.time.get_ticks()
            self.dt = (t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = t
            
            self.update(self.dt)
            self.draw()
            
            pygame.display.flip()

        pygame.quit()
    
    
    def update(self, dt):
        self.background.update(dt)
        
        # death screen
        if self.player.health <= 0:
            
            return
        
        # main game
        self.player.update(dt)
        for e in self.enemies:
            e.update(dt, self.player.position)
            
            if self.player.rect.colliderect(e.rect):
                e.reset()
                self.player.health -= 1
            elif (e.position.y >= WINDOW_SIZE.y) or (e.position.x <= -e.size.x) or (e.position.x >= WINDOW_SIZE.x):
                e.reset()
                
        
        self.spawn_timer += self.spawn_speed * dt
        if self.spawn_timer >= 10:
            self.spawn_timer = 0
            self.level += 1
            enemy.Enemy.upgrade()
    
    
    def draw(self):
        self.background.draw(self.screen)
        
        # death screen
        if self.player.health <= 0:
            self.dead_text.draw(self.screen)
            return
        
        self.player.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
            
        for x in range(self.player.health):
            rect = self.menu_health.get_rect()
            self.screen.blit(self.menu_health, (rect.width * x, 0))
            
        

    def exit(self):
        self.running = False
        
        

def main():
    game = Game(WINDOW_SIZE)

    game.run()

if __name__ == "__main__":
    main()

