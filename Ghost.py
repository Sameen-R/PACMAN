import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, down_image, left_image, right_image, up_image):
        self.screen = screen

        self.x = x
        self.y = y

        '''
        When the pacman eats the ghost, we want to use the first coordinates
        the ghost was assigned. The ghost will respawn at that location.
        '''
        self.startX = self.x
        self.startY = self.y

        self.speed = 3

        self.down_image = down_image 
        self.left_image = left_image 
        self.right_image = right_image
        self.up_image = up_image 
        self.edible_image = pygame.image.load('Images/Edible_Ghost.png')

        self.edible=False
        self.edible_counter=0
        '''
                Orientations:
                'U' --> Up
                'D' --> Down
                'L' --> Left
                'R' --> Right
                '''
        self.orientation = 'R'
        self.possible_orientations = ('U', 'D', 'L', 'R')

        self.image = self.right_image
        self.width = 53
        self.height = 53
        self.rect = pygame.Rect(self.x-3, self.y-3, self.width+6, self.height+6) 

    def make_edible(self):
        self.edible=True
        self.edible_counter=700

    def reset(self):
        self.edible=False
        self.edible_counter=0

        self.x=self.startX
        self.y=self.startY

        self.rect.x=self.startX
        self.rect.y=self.startY

    def draw(self):
        if self.edible:
            self.image = self.edible_image
            self.edible_counter -= 1
            if self.edible_counter == 0:
                self.edible = False
        else:
            if self.orientation == 'U':
                self.image = self.up_image
            elif self.orientation == 'D':
                self.image = self.down_image
            elif self.orientation == 'L':
                self.image = self.left_image
            elif self.orientation == 'R':
                self.image = self.right_image

        self.screen.blit(self.image, (self.x, self.y))




