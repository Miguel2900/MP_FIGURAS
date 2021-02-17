import pygame
sheet0 = pygame.image.load('animals.png')
sheet0 = pygame.transform.scale(sheet0, (960, 1280))
sheet1 = pygame.image.load('New Piskel (1).png')
sheet1 = pygame.transform.scale(sheet1, (600, 900))
size_y_s0 = 1280/4
div_x_s0 = 320
size_y_s1 = 300
div_x_s1 = 300


order = { 'tiger' : 0, 'panda' : 1, 'sloth' : 2, 'frog' : 3, 'medal' : 4}
class Img(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.tiger_sprites = []
        self.panda_sprites = []
        self.sloth_sprites = []
        self.frog_sprites = []
        self.medal_sprites = []
        self.figure_sprites = []
        self.tiger_sprites.append(sheet0.subsurface(0, 0, div_x_s0, size_y_s0 - 1))
        self.tiger_sprites.append(sheet0.subsurface(div_x_s0, 0, div_x_s0, size_y_s0 - 1))
        self.figure_sprites.append(sheet1.subsurface(0, 0, div_x_s1, size_y_s1 - 1))
        self.figure_sprites.append(sheet1.subsurface(div_x_s1, 0, div_x_s1, size_y_s1 - 1))
        self.figure_sprites.append(sheet1.subsurface(0, size_y_s1, div_x_s1, size_y_s1 - 1))
        self.figure_sprites.append(sheet1.subsurface(div_x_s1, size_y_s1, div_x_s1, size_y_s1 - 1))
        self.current_sprite = [0,0,0,0,0]
        self.animal_image = self.tiger_sprites[self.current_sprite[0]]
        self.figure_image = None
        self.rect = self.animal_image.get_rect()
        self.rect.topleft = [x, y]

    def figures(self, id):
        self.figure_image = self.figure_sprites[id]

    def victory(self, errors):
        if errors == 0:
            self.animal_image = self.medal_sprites[2]
        if errors == 1:
            self.animal_image = self.medal_sprites[1]
        if errors == 2:
            self.animal_image = self.medal_sprites[0]

    def update(self, name):
        if name == 'tigre':
            self.current_sprite[0] += 0.2
            if self.current_sprite[0] >= len(self.tiger_sprites):
                self.current_sprite[0] = 0
                self.animal_image = self.tiger_sprites[self.current_sprite[0]]
            self.animal_image = self.tiger_sprites[int(self.current_sprite[0])]