import pygame, sys
from pygame.locals import *
from collections import deque
from collections import defaultdict
from os.path import abspath, dirname
from random import choice, randint
import heapq



pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# gameDisplay = pygame.display.set_mode((1277, 689))
screen_height = 689
screen_width = 1277
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

# pygame.mouse.set_visible(0)

background = pygame.image.load('images/space.jpg')

def draw_matrix_a(size, matrix):
    block_size = 20
    matrix_space = 30
    if matrix == 'A':
        initial_pos_x = (screen_width/2)-((block_size+1)*size)-matrix_space
        initial_pos_y = (screen_height/2)-(block_size*size)-matrix_space
    elif matrix == 'B':
        initial_pos_x = (screen_width/2)+matrix_space  
        initial_pos_y = (screen_height/2)-(block_size*size)-matrix_space
    elif matrix == 'C':
        initial_pos_x = (screen_width/2)-((block_size+1)*size/2)  
        initial_pos_y = (screen_height/2)+matrix_space
  
    for y in range(size):
        for x in range(size):
            pos_x = x*(block_size+1) + initial_pos_x
            pos_y = y*(block_size+1) + initial_pos_y
            rect = pygame.Rect(pos_x, pos_y , block_size, block_size)
            pygame.draw.rect(screen, (255, 0, 0), rect)

class Game:
    def __init__(self):
        pass

    def run(self):
        size = 10
        while True:
            screen.blit(background, [0, 0])
            # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 0, 40, 30))
            draw_matrix_a(size, 'A')
            draw_matrix_a(size, 'B')
            draw_matrix_a(size, 'C')
            # draw_matrix_b(size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == 32: # espace
                    print('keydown')
                elif event.type == KEYDOWN and event.key == 115: # key s
                    print('keydown')

            key = pygame.key.get_pressed()
            self.keyboard_manager(key)

            pygame.display.update()
    
    def keyboard_manager(self, key):
        # print(self.pos_x, self.pos_y)
        if key[pygame.K_ESCAPE]:
            sys.exit()
            

if __name__ == '__main__':
    game = Game()
    game.run()
