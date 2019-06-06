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
BLOCK_SIZE = 30
MATRIX_SPACE = 30
background = pygame.image.load('images/space.jpg')

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    width = textSurface.get_width()
    height = textSurface.get_height()
    return textSurface, textSurface.get_rect(), width, height

def draw_matrix_number(number, pos_x, pos_y):
    text = pygame.font.Font('freesansbold.ttf', 13)
    text_surface = text.render(str(number), True, white)
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (pos_x+BLOCK_SIZE/2, pos_y+BLOCK_SIZE/2)
    screen.blit(text_surface, text_surface_rect)

def draw_matrix_grid(size, matrix_id, matrix=None):
    if matrix_id == 'A':
        initial_pos_x = (screen_width/2)-((BLOCK_SIZE+1)*size)-MATRIX_SPACE
        initial_pos_y = (screen_height/2)-(BLOCK_SIZE*size)-MATRIX_SPACE
    elif matrix_id == 'B':
        initial_pos_x = (screen_width/2)+MATRIX_SPACE  
        initial_pos_y = (screen_height/2)-(BLOCK_SIZE*size)-MATRIX_SPACE
    elif matrix_id == 'C':
        initial_pos_x = (screen_width/2)-((BLOCK_SIZE+1)*size/2)  
        initial_pos_y = (screen_height/2)+MATRIX_SPACE


    for y in range(size):
        for x in range(size):
            pos_x = x*(BLOCK_SIZE+1) + initial_pos_x
            pos_y = y*(BLOCK_SIZE+1) + initial_pos_y
            rect = pygame.Rect(pos_x, pos_y , BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 0, 0), rect)
            if matrix is not None:
                draw_matrix_number(matrix[x][y], pos_x, pos_y)


class Game:
    def __init__(self):
        self.size = 10
        pass

    def run(self):
        matrix = [[1 for x in range(self.size)] for y in range(self.size)]
        while True:
            screen.blit(background, [0, 0])
            # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 0, 40, 30))
            draw_matrix_grid(self.size, 'A', matrix)
            draw_matrix_grid(self.size, 'B', matrix)
            draw_matrix_grid(self.size, 'C')
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
