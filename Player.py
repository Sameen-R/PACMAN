import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed=3
        '''
                All images of the pacman are initialized here.
                The L,R,D,U represent orientation of the pacman.
                The 1,2,3,4 represent each represent a different pacman pose (how wide the mouth opens)
                
                So L1 means mouth slightly opening in the leftward direction
                L2 means mouth closed in the leftward direction
                L3 means mouth opening slightly in the leftward direction
                L4 means mouth opening widely in the leftward direction
                '''
        self.L1 = pygame.image.load('Images/L1.png')
        self.L2 = pygame.image.load('Images/L2.png')
        self.L3 = pygame.image.load('Images/L3.png')
        self.L4 = pygame.image.load('Images/L4.png')

        self.R1 = pygame.image.load('Images/R1.png')
        self.R2 = pygame.image.load('Images/R2.png')
        self.R3 = pygame.image.load('Images/R3.png')
        self.R4 = pygame.image.load('Images/R4.png')

        self.D1 = pygame.image.load('Images/D1.png')
        self.D2 = pygame.image.load('Images/D2.png')
        self.D3 = pygame.image.load('Images/D3.png')
        self.D4 = pygame.image.load('Images/D4.png')

        self.U1 = pygame.image.load('Images/U1.png')
        self.U2 = pygame.image.load('Images/U2.png')
        self.U3 = pygame.image.load('Images/U3.png')
        self.U4 = pygame.image.load('Images/U4.png')
        '''
                Orientations:
                'U' --> Up
                'D' --> Down
                'L' --> Left
                'R' --> Right
                '''
        self.orientation = 'R'
        self.possible_orientations = ('U', 'D', 'L', 'R')

        self.image = self.R1
        self.width = 53
        self.height = 53
        self.rect = pygame.Rect(self.x-3, self.y-3, self.width+6, self.height+6)  
        self.counter = 0

    def draw(self):
        if self.counter<=6:
            if self.orientation == 'U':
                self.image = self.U1
            elif self.orientation == 'D':
                self.image = self.D1
            elif self.orientation == 'L':
                self.image = self.L1
            elif self.orientation == 'R':
                self.image = self.R1
        elif self.counter<=12:
            if self.orientation == 'U':
                self.image = self.U2
            elif self.orientation == 'D':
                self.image = self.D2
            elif self.orientation == 'L':
                self.image = self.L2
            elif self.orientation == 'R':
                self.image = self.R2
        elif self.counter<=18:
            if self.orientation == 'U':
                self.image = self.U3
            elif self.orientation == 'D':
                self.image = self.D3
            elif self.orientation == 'L':
                self.image = self.L3
            elif self.orientation == 'R':
                self.image = self.R3
        elif self.counter<=24:
            if self.orientation == 'U':
                self.image = self.U4
            elif self.orientation == 'D':
                self.image = self.D4
            elif self.orientation == 'L':
                self.image = self.L4
            elif self.orientation == 'R':
                self.image = self.R4
                
        self.screen.blit(self.image, (self.x, self.y))

        self.counter+=1
        if self.counter==36:
            self.counter=0



