import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.color = (30,0,100)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.interior = pygame.Rect(self.x+10, self.y+10, self.width-20, self.height-20)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, (0,0,0), self.interior)
