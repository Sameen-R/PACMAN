import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, screen, is_ghost_killer, x, y):
        self.screen = screen
        self.is_ghost_killer = is_ghost_killer
        self.x = x
        self.y = y
        self.width = None
        self.height = None
        self.color = (255, 200, 0)
        if self.is_ghost_killer:
            self.width = 20
            self.height = 20
        else:
            self.width = 10
            self.height = 10
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def draw(self):
        if self.is_ghost_killer:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.width/2)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)

