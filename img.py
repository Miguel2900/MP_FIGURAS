import pygame
sheet = pygame.image.load('animals.png')
sheet = pygame.transform.scale(sheet, (960, 1280))
tamy = 1280/4
divx = 320

order = { 'tiger' : 0, 'panda' : 1, 'sloth' : 2, 'frog' : 3, 'medal' : 4}
class Img(pygame.sprite.Sprite):
    def __init__(self, x, y):
        print(order['panda'])
        self.tiger_sprites = []
        self.panda_sprites = []
        self.sloth_sprites = []
        self.frog_sprites = []
        self.medal_sprites = []
        self.tiger_sprites.append(sheet.subsurface(0, 0, divx, tamy - 1))
        self.tiger_sprites.append(sheet.subsurface(divx * 1, 0, divx, tamy - 1))
        self.current_sprite = [0,0,0,0,0]
        self.image = self.tiger_sprites[self.current_sprite[0]]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def victory(self, errors):
        if errors == 0:
            self.image = self.medal_sprites[2]
        if errors == 1:
            self.image = self.medal_sprites[1]
        if errors == 2:
            self.image = self.medal_sprites[0]

    def update(self, name):
        if name == 'tigre':
            self.current_sprite[0] += 0.2
            if self.current_sprite[0] >= len(self.tiger_sprites):
                self.current_sprite[0] = 0
                self.image = self.tiger_sprites[self.current_sprite[0]]
            self.image = self.tiger_sprites[int(self.current_sprite[0])]