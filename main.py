import pygame
from Player import Player
from Wall import Wall
from Ghost import Ghost
from Dot import Dot
import random
pygame.init()

screen_w = 1200
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

clock = pygame.time.Clock()

red_D = pygame.image.load('Images/red_D.jpg')
red_L = pygame.image.load('Images/red_L.jpg')
red_R = pygame.image.load('Images/red_R.jpg')
red_U = pygame.image.load('Images/red_U.jpg')

pink_D = pygame.image.load('Images/pink_D.png')
pink_L = pygame.image.load('Images/pink_L.png')
pink_R = pygame.image.load('Images/pink_R.png')
pink_U = pygame.image.load('Images/pink_U.png')

'''
^^^Initializing important variables with global scope^^^
'''

def check_wall_collisions(direction, walls, player):
    for wall in walls:
        if pygame.sprite.collide_rect(wall, player):
            collide_rect = wall.rect.clip(player.rect)
            if collide_rect.width>=collide_rect.height:
                if collide_rect.y<=player.rect.y and direction=='U':
                    return True
                elif collide_rect.y>player.rect.y and direction=='D':
                    return True
            else:
                if collide_rect.x<=player.rect.x and direction=='L':
                    return True
                if collide_rect.x>player.rect.x and direction=='R':
                    return True
    return False

def at_ends(direction, walls, ghost):
    for wall in walls:
        scenarios = [
            wall.x + wall.width < ghost.rect.x < wall.x + wall.width + 7,
            wall.x - 7 < ghost.rect.x + ghost.width < wall.x,
            wall.y + wall.height < ghost.rect.y < wall.y + wall.height + 7,
            wall.y - 7 < ghost.rect.y + ghost.height < wall.y
        ]
        if (scenarios[0] or scenarios[1]) and (direction=='L' or direction=='R'):
            return True
        elif (scenarios[2] or scenarios[3]) and (direction=='U' or direction=='D'):
            return True
    return False

def change_ghost_direction(walls, ghost):
    index = ghost.possible_orientations.index(ghost.orientation)
    possible_directions = []
    for n in range(index+1, index+5):
        i = n%4
        new_direction = ghost.possible_orientations[i]
        if new_direction == 'U':
            ghost_copy = Ghost(screen, ghost.x, ghost.y, ghost.down_image, ghost.left_image, ghost.right_image, ghost.up_image)
            ghost_copy.rect.y -= 7
            ghost_copy.y -= 7
            if not check_wall_collisions('U', walls, ghost_copy):
                possible_directions.append('U')
        elif new_direction == 'D':
            ghost_copy = Ghost(screen, ghost.x, ghost.y, ghost.down_image, ghost.left_image, ghost.right_image, ghost.up_image)
            ghost_copy.rect.y += 7
            ghost_copy.y += 7
            if not check_wall_collisions('D', walls, ghost_copy):
                possible_directions.append('D')
        elif new_direction == 'L':
            ghost_copy = Ghost(screen, ghost.x, ghost.y, ghost.down_image, ghost.left_image, ghost.right_image, ghost.up_image)
            ghost_copy.rect.x -= 7
            ghost_copy.x -= 7
            if not check_wall_collisions('L', walls, ghost_copy):
                possible_directions.append('L')
        elif new_direction == 'R':
            ghost_copy = Ghost(screen, ghost.x, ghost.y, ghost.down_image, ghost.left_image, ghost.right_image, ghost.up_image)
            ghost_copy.rect.x += 7
            ghost_copy.x += 7
            if not check_wall_collisions('R', walls, ghost_copy):
                possible_directions.append('R')
    if len(possible_directions)==0:
        return None
    else:
        return random.choice(possible_directions)

def game_complete_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        font = pygame.font.SysFont(None, 175)
        img = font.render("GAME COMPLETE!", True, (0,255,0))
        rect = img.get_rect()
        rect.center = (screen_w/2, screen_h/3)

        small_font = pygame.font.SysFont(None, 75)
        small_img = small_font.render("Press space button to play again", True, (0, 0, 255))
        small_rect = small_img.get_rect()
        small_rect.center = (screen_w / 2, screen_h*.75)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            game()

        screen.fill((0, 0, 0))
        screen.blit(img, rect)
        screen.blit(small_img, small_rect)
        pygame.display.update()
        clock.tick(100)


def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        font = pygame.font.SysFont(None, 200)
        img = font.render("Game Over", True, (255,0,0))
        rect = img.get_rect()
        rect.center = (screen_w/2, screen_h/3)

        small_font = pygame.font.SysFont(None, 75)
        small_img = small_font.render("Press space button to play again", True, (0, 0, 255))
        small_rect = small_img.get_rect()
        small_rect.center = (screen_w / 2, screen_h*.75)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            game()

        screen.fill((0, 0, 0))
        screen.blit(img, rect)
        screen.blit(small_img, small_rect)
        pygame.display.update()
        clock.tick(100)

def game():
    '''
    Initilizing all the game sprites
        -player: pacman
        -ghosts: a list of ghost (one red, one pink)
        -walls: a list of walls that make up the maze
    '''
    player = Player(screen, 575, 563.5)
    ghosts = [
        Ghost(screen, 23, 123, red_D, red_L, red_R, red_U),
        Ghost(screen, 1124, 123, pink_D, pink_L, pink_R, pink_U)
    ]
    walls = [
        Wall(screen, 0, 100, 1200, 20),
        Wall(screen, 0, 780, 1200, 20),
        Wall(screen, -10, 100, 30, 265),
        Wall(screen, -10, 435, 30, 365),
        Wall(screen, 1180, 100, 30, 265),
        Wall(screen, 1180, 435, 30, 365),

        Wall(screen, 80, 180, 310, 540),
        Wall(screen, 810, 180, 310, 540),
        Wall(screen, 452, 180, 288, 200),
        Wall(screen, 452, 440, 288, 120),
        Wall(screen, 452, 620, 288, 100)
    ]

    dots = [Dot(screen, False, x, 150) for x in range(100, 1101, 50)]
    dots.extend([Dot(screen, False, x, 750) for x in range(100, 1101, 50)])
    dots.extend([Dot(screen, False, 50, y) for y in range(200, 701, 50)])
    dots.extend([Dot(screen, False, 1150, y) for y in range(200, 701, 50)])
    dots.extend([Dot(screen, False, 420, y) for y in range(200, 701, 50)])
    dots.extend([Dot(screen, False, 770, y) for y in range(200, 701, 50)])
    dots.extend([Dot(screen, True, 50, 150), Dot(screen, True, 1150, 150), Dot(screen, True, 50, 750), Dot(screen, True, 1150, 750),])

    latest_keys = None
    while True:
        '''
        Check if the user wants to quit (press the red x button that closes the game window)
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        '''
        Getting the key stokes from the user:
            -pressed variable: a list of booleans that indiciate which keys were pressed
            -latest_keys: stores the value of pressed that last time the user actually pressed a key
            -pressing the keys will only change the player's orientation
        '''
        pressed = pygame.key.get_pressed()
        no_keys_pressed = True
        for key in pressed:
            if key:
                no_keys_pressed = False
        if not no_keys_pressed or latest_keys==None:
            latest_keys=pressed

        if latest_keys[pygame.K_UP]:
            if not check_wall_collisions('U', walls, player):
                player.orientation = 'U'
        elif latest_keys[pygame.K_DOWN]:
            if not check_wall_collisions('D', walls, player):
                player.orientation = 'D'
        elif latest_keys[pygame.K_LEFT]:
            if not check_wall_collisions('L', walls, player):
                player.orientation = 'L'
        elif latest_keys[pygame.K_RIGHT]:
            if not check_wall_collisions('R', walls, player):
                player.orientation = 'R'

        '''
        Controlling player movements:
            -The player moves based on the direction its facing (orientation) and wall collisions
            -If the player collides with a wall and faces that direction (as shown in check_wall_collisions()), 
             the player can't move.
            -Also, the player can teleport to the other side of the screen if it moves off the left or right 
             edges of the screen.
        '''
        if player.orientation=='U' and not check_wall_collisions('U', walls, player):
            player.y -= player.speed
            player.rect.y -= player.speed
        elif player.orientation=='D' and not check_wall_collisions('D', walls, player):
            player.y += player.speed
            player.rect.y += player.speed
        elif player.orientation=='L' and not check_wall_collisions('L', walls, player):
            player.x -= player.speed
            player.rect.x -= player.speed
            if player.x+player.width<=0:
                player.x=screen_w
                player.rect.x=screen_w-3
        elif player.orientation=='R' and not check_wall_collisions('R', walls, player):
            player.x += player.speed
            player.rect.x += player.speed
            if player.x>=screen_w:
                player.x=0-player.width
                player.rect.x = 0-player.width-3

        '''
        Controlling ghost movements:
            -For each ghost in ghosts, there are two options for moving:
                *The ghost actively decides to change direction whenever it approaches the end of a wall
                *The ghost only changes direction when it hits a wall
                (A chance variable and an if-statement determines which way a ghost move at a particular moment)
            -In the for loop, only one method of changing direction is needed. However, the mixture of two methods makes
             the ghost movements more interest and fun.
        '''
        for ghost in ghosts:
            chance = random.randint(0,1)
            if chance==0:
                '''
                First method of changing direction
                    -The ghost actively tries to change direction whenever possible
                '''
                orientation = change_ghost_direction(walls, ghost)
                if orientation != None and at_ends(ghost.orientation, walls, ghost):
                    ghost.orientation = orientation
                if ghost.orientation == 'R':
                    ghost.x += ghost.speed
                    ghost.rect.x += ghost.speed
                    if ghost.x >= screen_w:
                        ghost.x = 0 - ghost.width
                        ghost.rect.x = 0 - ghost.width - 3
                elif ghost.orientation == 'L':
                    ghost.x -= ghost.speed
                    ghost.rect.x -= ghost.speed
                    if ghost.x + ghost.width <= 0:
                        ghost.x = screen_w
                        ghost.rect.x = screen_w - 3
                elif ghost.orientation == 'U':
                    ghost.y -= ghost.speed
                    ghost.rect.y -= ghost.speed
                elif ghost.orientation == 'D':
                    ghost.y += ghost.speed
                    ghost.rect.y += ghost.speed
            else:
                '''
                First method of changing direction
                    -The ghost only changes direction when it collides against a wall
                '''
                if check_wall_collisions(ghost.orientation, walls, ghost):
                    ghost.orientation = change_ghost_direction(walls, ghost)
                else:
                    if ghost.orientation == 'R':
                        ghost.x += ghost.speed
                        ghost.rect.x += ghost.speed
                        if ghost.x >= screen_w:
                            ghost.x = 0 - ghost.width
                            ghost.rect.x = 0 - ghost.width - 3
                    elif ghost.orientation == 'L':
                        ghost.x -= ghost.speed
                        ghost.rect.x -= ghost.speed
                        if ghost.x + ghost.width <= 0:
                            ghost.x = screen_w
                            ghost.rect.x = screen_w - 3
                    elif ghost.orientation == 'U':
                        ghost.y -= ghost.speed
                        ghost.rect.y -= ghost.speed
                    elif ghost.orientation == 'D':
                        ghost.y += ghost.speed
                        ghost.rect.y += ghost.speed

        for dot in dots.copy():
            if pygame.sprite.collide_rect(player, dot):
                if dot.is_ghost_killer:
                    for ghost in ghosts:
                        ghost.make_edible()
                dots.remove(dot)

        for ghost in ghosts:
            if pygame.sprite.collide_rect(player, ghost):
                if ghost.edible:
                    ghost.reset()
                else:
                    game_over_screen()

        if len(dots)==0:
            game_complete_screen()

        '''
        Drawing and updating everything
        '''
        screen.fill((0,0,0))
        for wall in walls:
            wall.draw()
        for dot in dots:
            dot.draw()
        player.draw()
        for ghost in ghosts:
            ghost.draw()
        pygame.display.update()
        clock.tick(100)

game()
