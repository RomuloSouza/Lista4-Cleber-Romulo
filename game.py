import pygame, sys
from pygame.locals import *
from random import randint
from strassen import strassen

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

screen_height = 689
screen_width = 1277
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

# pygame.mouse.set_visible(0)
BLOCK_SIZE = 25
MATRIX_SIZE = 12
MATRIX_SPACE = 30
MATRIX_FONT_SIZE = 10
COUNTER_FONT_SIZE = 30
background = pygame.image.load('images/space.jpg')
plus_image = pygame.image.load('images/plus.png')
minus_image = pygame.image.load('images/minus.png')


def draw_matrix_number(number, pos_x, pos_y):
    text = pygame.font.Font('freesansbold.ttf', MATRIX_FONT_SIZE)
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
            pos_x = x * (BLOCK_SIZE+1) + initial_pos_x
            pos_y = y * (BLOCK_SIZE+1) + initial_pos_y
            rect = pygame.Rect(pos_x, pos_y , BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 0, 0), rect)
            if matrix is not None:
                draw_matrix_number(matrix[x][y], pos_x, pos_y)


def generate_random_matrix(size):
    matrix = [[randint(0, 10) for x in range(size)] for y in range(size)]
    return matrix


class Game:
    def __init__(self):
        self.size = MATRIX_SIZE
        self.size_number_size = 40
        self.matrix_a = None
        self.matrix_b = None
        self.matrix_c = None
        self.plus_size = plus_image.get_width()
        self.plus_x = 30
        self.plus_y = (screen_height/2) - self.plus_size - self.size_number_size/2 + MATRIX_SPACE/2
        self.minus_size = minus_image.get_width()
        self.minus_x = self.plus_x
        self.minus_y = self.plus_y + self.plus_size + self.size_number_size

    def run(self):
        self.create_new_matrices()
        while True:
            screen.blit(background, [0, 0])
            screen.blit(plus_image, (self.plus_x, self.plus_y))
            screen.blit(minus_image, (self.minus_x, self.minus_y))
            draw_matrix_grid(self.size, 'A', self.matrix_a)
            draw_matrix_grid(self.size, 'B', self.matrix_b)
            draw_matrix_grid(self.size, 'C', self.matrix_c)
            self.draw_size_number()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == 32: # espace
                    print('keydown')
                elif event.type == KEYDOWN and event.key == 115: # key s
                    print('keydown')
                elif event.type == KEYDOWN and event.key == 273: # key up
                    if self.size < MATRIX_SIZE:
                        self.size += 1
                        self.create_new_matrices()
                elif event.type == KEYDOWN and event.key == 274: # key down
                    if self.size > 1:
                        self.size -= 1
                        self.create_new_matrices()


            key = pygame.key.get_pressed()
            self.keyboard_manager(key)

            pygame.display.update()
    
    def keyboard_manager(self, key):
        if key[pygame.K_ESCAPE]:
            sys.exit()
    
    def draw_size_number(self):
        text = pygame.font.Font('freesansbold.ttf', COUNTER_FONT_SIZE)
        text_surface = text.render(str(self.size), True, white)
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (
            self.plus_x + self.plus_size/2,
            self.plus_y + self.plus_size + self.size_number_size/2
        )
        screen.blit(text_surface, text_surface_rect)

    def create_new_matrices(self):
        self.matrix_a = generate_random_matrix(self.size)
        self.matrix_b = generate_random_matrix(self.size)
        self.matrix_c = strassen(self.matrix_a, self.matrix_b)
            

if __name__ == '__main__':
    game = Game()
    game.run()
