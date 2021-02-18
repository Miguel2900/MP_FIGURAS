import pygame
import random

#screen parameters
SIZE = (900, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('MIS PRIMERAS FIGURAS')
pygame.display.set_icon(pygame.image.load('logo.png'))
pygame.init()


#images
menu_bg = pygame.image.load('MenuPrincipal.png')
menu_bg = pygame.transform.scale(menu_bg, (900, 500))
level1_bg = pygame.image.load('Facil.png')
level1_bg = pygame.transform.scale(level1_bg, (900,500))
scroll = pygame.image.load('TextoCreditos.png')



#Classes
class Sprite_sheet():
    def __init__(self, f_name):
        self.image = pygame.image.load(f_name)
        self.sprites = []
        self.current_sprite = 0


    def get_sprite(self, width, height, x, y):
        self.sprites.append(self.image.subsurface(x, y, width, height))

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]



class Card():

    def __init__(self):
        self.boxes = []
        self.ready = True

    def fill_boxes(self, diff):
        j = 0
        if self.ready:
            if diff == 0:
                max_range = 8
                min_range = 0
            else:
                max_range = 10
                min_range = 0
            while j < 9:
                ran = random.randint(min_range, max_range)
                if not ran in self.boxes:
                    self.boxes.append(ran)
                    j += 1
            self.ready = False

#widht & height
AX = 960 / 3
AY = 1280 / 4
FX = 650 / 4
FY = 813 / 5
class Game_stage():
    def __init__(self):
        self.stage = 0
        self.card = Card()
        self.easy_figures = Sprite_sheet('Figuras1.png')
        self.medium_figures = Sprite_sheet('Figuras1.png')
        self.hard_figures = Sprite_sheet('Figuras1.png')
        self.tiger = Sprite_sheet('animals.png')
        self.panda = Sprite_sheet('animals.png')
        self.sloth = Sprite_sheet('animals.png')
        self.frog = Sprite_sheet('animals.png')
        self.medal = Sprite_sheet('animals.png')
        self.get_sprites()

    def get_sprites(self):
        self.tiger.get_sprite(AX, AY, 0, 0)
        self.tiger.get_sprite(AX, AY, AX, 0)
        self.panda.get_sprite(AX, AY, AX * 2, 0)
        self.panda.get_sprite(AX, AY, 0, AY)
        self.sloth.get_sprite(AX, AY, AX, AY)
        self.sloth.get_sprite(AX, AY, AX * 2, AY)
        self.frog.get_sprite(AX, AY, 0, AY * 2)
        self.frog.get_sprite(AX, AY, AX, AY * 2)
        self.frog.get_sprite(AX, AY, AX * 2, AY * 2)
        self.medal.get_sprite(AX, AY, 0, AY * 3)
        self.medal.get_sprite(AX, AY, AX, AY * 3)
        self.medal.get_sprite(AX, AY, AX * 2, AY * 3)
        self.easy_figures.get_sprite(FX, FY, 0, 0)
        self.easy_figures.get_sprite(FX, FY, FX, 0)
        self.easy_figures.get_sprite(FX, FY, FX * 2, 0)
        self.easy_figures.get_sprite(FX, FY, FX * 3, 0)
        self.easy_figures.get_sprite(FX, FY, 0, FY)
        self.easy_figures.get_sprite(FX, FY, FX, FY)
        self.easy_figures.get_sprite(FX, FY, FX * 2, FY)
        self.easy_figures.get_sprite(FX, FY, FX * 3, FY)
        self.easy_figures.get_sprite(FX, FY, 0, FY * 2)
        self.easy_figures.get_sprite(FX, FY, FX, FY * 2)


    def menu(self):
        draw_img(menu_bg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 231 + 80 and \
                            mouse_pos[1] >= 231:
                        self.stage = 1
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 301 + 80 and \
                            mouse_pos[1] >= 301:
                        credito()
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 371 + 80 and \
                            mouse_pos[1] >= 371:
                        return False
        pygame.display.flip()
        clock.tick(30)
        return True

    def level_1(self):
        draw_img(level1_bg)
        self.card.fill_boxes(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stage = 0
                self.card.ready = True
                self.card.boxes = []
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 231 + 80 and \
                            mouse_pos[1] >= 231:
                        pass
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 301 + 80 and \
                            mouse_pos[1] >= 301:
                        pass
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 371 + 80 and \
                            mouse_pos[1] >= 371:
                        pass
        self.tiger.update(0.08)
        draw_img(self.tiger.image)
        draw_img(self.easy_figures.sprites[self.card.boxes[0]], 476 - 81 /2 , 102 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[1]], 591 - 81 / 2, 102 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[2]], 707 - 81 / 2, 102 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[3]], 476 - 81 / 2, 222 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[4]], 591 - 81 / 2, 222 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[5]], 707 - 81 / 2, 222 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[6]], 476 - 81 / 2, 342 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[7]], 591 - 81 / 2, 342 - 81 / 2)
        draw_img(self.easy_figures.sprites[self.card.boxes[8]], 707 - 81 / 2, 342 - 81 / 2)

        clock.tick(30)
        pygame.display.flip()



#functions
def draw_img(img, x=0, y=0):
    screen.blit(img, (x, y))

def credito():
    mov = -.5
    y=0
    rune = True
    while rune:
        draw_img(scroll, 0, y)
        pygame.display.flip()
        if y == -2480:
            rune = False
        y += mov


#variables
clock = pygame.time.Clock()
stage = Game_stage()

def main():
    run = True
    while run:
        if stage.stage == 0:
            run = stage.menu()
        elif stage.stage == 1:
            stage.level_1()
    pygame.quit()

if __name__ == '__main__':
    main()

