import pygame
import img
import bingo
import random
#dictionary
figuras = { 0 : 'cuadrado', 1 : 'triangulo', 2 : 'rectangulo', 3 : 'circulo', 4 : 'rombo'}

#screen parameters
SIZE = (900, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('MIS PRIMERAS FIGURAS')
pygame.display.set_icon(pygame.image.load('logo.png'))
pygame.init()

#variables
clock = pygame.time.Clock()
img = img.Img(0, 0)
card = bingo.Card()

#images
jugar = pygame.image.load('Jugar.png')
creditos = pygame.image.load('Creditos.png')
salir = pygame.image.load('Salir.png')
menu_bg = pygame.image.load('Fondo-2.png')
menu_bg = pygame.transform.scale(menu_bg, (900, 500))
level1_bg = pygame.image.load('Fondo-1.png')
level1_bg = pygame.transform.scale(level1_bg, (900,500))
scrol = pygame.image.load('scroll.jpg')
board = pygame.image.load('Tablero.png')
board = pygame.transform.scale(board, (board.get_width()+300, board.get_height()+350))

def img_display(img, x, y):
    screen.blit(img, (x, y))

def menu():
    img_display()

def credito():
    mov = -.5
    y=0
    rune = True
    while rune:
        img_display(scrol, 0, y)
        pygame.display.flip()
        if y == -2480:
            rune = False
        y += mov
def draw_cfigures():
    j = 0
    while j < 9:
        img.figures(1)
        fig = img.figure_image
        img_display(pygame.transform.scale(fig, (100,100)), 450, 0)
        j += 1

def level_e():
    card.fill_boxes('easy')
    used = []
    next_figure = True
    id_used = 0
    errors = 0
    run = True
    while run:
        img_display(level1_bg, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    if mouse_pos [0]>= 480 and mouse_pos[0] <= 592 and mouse_pos[1] <= 240 and mouse_pos[1] >= 141:
                        errors += card.check_figure(used[id_used], card.boxes[0])
                        print(f'errores {errors}')
                    if mouse_pos [0]>= 0 and mouse_pos[0] <= 200 and mouse_pos[1] <= 200 and mouse_pos[1] >= 0:
                        next_figure = True
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 371+80 and mouse_pos[1] >= 371:
                        pass
        if errors == 3:
            run = False
        if len(used) == 11:
            run = False
        if next_figure:
            ran = random.randint(0, 10)
            if not ran in used:
                used.append(ran)
                print(card.boxes)
                print(ran)
                next_figure = False
        if not next_figure:
            #img.figures(ran)
            pass
            #img_display(img.figure_image, 0, 0)
        img.update('tigre')
        img_display(img.animal_image, 0, 200)
        img_display(board, (450/2 - board.get_width()/2) + 450, 250 - board.get_height() / 2)
        draw_cfigures()

        clock.tick(30)
        pygame.display.flip()

def main():
    run = True
    while run:
        img_display(menu_bg, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 231+80 and mouse_pos[1] >= 231:
                        level_e()
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 301+80 and mouse_pos[1] >= 301:
                        credito()
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 371+80 and mouse_pos[1] >= 371:
                        run = False
        img_display(jugar,450-75,231)
        img_display(creditos, 450-75, 301)
        img_display(salir, 450-75, 371)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()




if __name__ == '__main__':
    main()