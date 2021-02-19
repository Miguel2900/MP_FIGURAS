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
        self.image = pygame.image.load(f_name) #sprite sheet
        self.sprites = [] #list of sprites
        self.current_sprite = 0

    #obtains sprites from the sheet
    def get_sprite(self, width, height, x, y):
        self.sprites.append(self.image.subsurface(x, y, width, height))
    #updates sprites and changes the image
    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]



class Card():

    def __init__(self):
        self.boxes = []
        self.ready = True
    #fill with random numbers the boxes in the card
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
#all stages of the game
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
        self.figures_ready = True
        self.figures = []
        self.errors = 0
        self.actual_figure = 0
        self.get_sprites()

    #Fills the list figures with random values
    def fill_figures(self, min_value, max_value):
        i = 0
        while i < max_value:
            rn = random.randint(min_value, max_value)
            if not rn in self.figures:
                self.figures.append(rn)
                i += 1
        self.figures_ready = False
    # checks if the figure choosen is the same as the one asked
    def check_figure(self, i):
        if self.card.boxes[i] == self.figures[self.actual_figure]:
            self.actual_figure += 1
            return True
        else:
            self.errors += 1
            return False
    # reset values in order to proceed
    def reset(self, stage):
        self.stage = stage
        self.errors = 0
        self.actual_figure = 0
        self.figures_ready = True
        self.figures = []
        self.card.ready = True
        self.card.boxes = []
    #obtains sprites for each object
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
    #shows the medal earned
    def victory(self):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.reset(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 231 + 80 and mouse_pos[1] >= 231:
                        self.reset(0)
        if self.errors == 0:
            draw_img(self.medal.sprites[2])
        if self.errors == 1:
            draw_img(self.medal.sprites[1])
        if self.errors == 2:
            draw_img(self.medal.sprites[0])
        pygame.display.flip()

    #show credits
    def credits(self, y):
        screen.fill((0, 0, 0))
        draw_img(scroll, 0, y)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stage = 0#returns to menu
                return 0
        if y == -2480:
            y = 0
            self.stage = 0
        else:
            y += -.5
        clock.tick(30)
        return y
    #main menu
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
                        self.stage = 1#takes to level 1
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 301 + 80 and \
                            mouse_pos[1] >= 301:
                        self.stage = -1# takes to credits
                    if mouse_pos[0] >= 450 - 75 and mouse_pos[0] <= 450 - 75 + 150 and mouse_pos[1] <= 371 + 80 and \
                            mouse_pos[1] >= 371:
                        return False
        pygame.display.flip()
        clock.tick(30)
        return True
    #level 1
    def level_1(self):
        draw_img(level1_bg)
        self.card.fill_boxes(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.reset(0)
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= 476  and mouse_pos[0] <= 574 and mouse_pos[1] <= 200 and mouse_pos[1] >= 102:
                        if self.check_figure(0):
                            print('same figure')
                        else:
                            print('Error')
                    if mouse_pos[0] >= 591 and mouse_pos[0] <= 689 and mouse_pos[1] <= 200 and mouse_pos[1] >= 102:
                        if self.check_figure(1):
                            print('same figure')
                        else:
                            print('Error')
                    if mouse_pos[0] >= 707 and mouse_pos[0] <= 805 and mouse_pos[1] <= 200 and mouse_pos[1] >= 102:
                        if self.check_figure(2):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 476  and mouse_pos[0] <= 574 and mouse_pos[1] <= 320 and mouse_pos[1] >= 222:
                        if self.check_figure(3):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 591 and mouse_pos[0] <= 689 and mouse_pos[1] <= 320 and mouse_pos[1] >= 222:
                        if self.check_figure(4):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 707 and mouse_pos[0] <= 805 and mouse_pos[1] <= 320 and mouse_pos[1] >= 222:
                        if self.check_figure(5):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 476  and mouse_pos[0] <= 574 and mouse_pos[1] <= 440 and mouse_pos[1] >= 342:
                        if self.check_figure(6):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 591 and mouse_pos[0] <= 689 and mouse_pos[1] <= 440 and mouse_pos[1] >= 342:
                        if self.check_figure(7):
                            print('same figure')
                        else:
                            print('Error')
                        pass
                    if mouse_pos[0] >= 707 and mouse_pos[0] <= 805 and mouse_pos[1] <= 440 and mouse_pos[1] >= 342:
                        if self.check_figure(8):
                            print('same figure')
                        else:
                            print('Error')
                        pass
        self.panda.update(0.08)
        draw_img(self.panda.image)
        if self.actual_figure == 8:
            self.stage = 4#takes to victory
            self.victory()
            self.actual_figure += -1
        draw_img(self.easy_figures.sprites[self.figures[self.actual_figure]], 0, 250)
        draw_img(self.easy_figures.sprites[self.card.boxes[0]], int(476 - 81 /2) , int(102 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[1]], int(591 - 81 / 2), int(102 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[2]], int(707 - 81 / 2), int(102 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[3]], int(476 - 81 / 2), int(222 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[4]], int(591 - 81 / 2), int(222 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[5]], int(707 - 81 / 2), int(222 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[6]], int(476 - 81 / 2), int(342 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[7]], int(591 - 81 / 2), int(342 - 81 / 2))
        draw_img(self.easy_figures.sprites[self.card.boxes[8]], int(707 - 81 / 2), int(342 - 81 / 2))
        if self.errors == 3:
            self.reset(0)
        clock.tick(30)
        pygame.display.flip()



#functions
def draw_img(img, x=0, y=0):
    screen.blit(img, (x, y))



#variables
clock = pygame.time.Clock()
stage = Game_stage()


def main():
    y = 0
    run = True
    while run:
        if stage.stage == 0:#if its menu
            run = stage.menu()
        elif stage.stage == 1:#if its level 1
            if stage.figures_ready:
                stage.fill_figures(0, 8)
            stage.level_1()
        elif stage.stage == -1:#if its credits
            y = stage.credits(y)
        elif stage.stage == 4:#if its victory
            stage.victory()
    pygame.quit()

if __name__ == '__main__':
    main()


