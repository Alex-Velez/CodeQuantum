import pygame

class Vec2():
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        pass
    
    def round(self) -> (int, int):
        return (int(self.x), int(self.y))


def dt(getTicksLastFrame: float) -> float:
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    
