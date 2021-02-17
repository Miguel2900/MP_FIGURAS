import pygame
import img

#screen parameters
SIZE = (900, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('MIS PRIMERAS FIGURAS')
pygame.display.set_icon(pygame.image.load('logo.png'))
pygame.init()

#variables
clock = pygame.time.Clock()
img = img.Img(0, 0)

#images
jugar = pygame.image.load('Jugar.png')
creditos = pygame.image.load('Creditos.png')
salir = pygame.image.load('Salir.png')
fondo_menu = pygame.image.load('MenuPrincipal.jpg')
scrol = pygame.image.load('scroll.jpg')

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

def main():
    run = True
    while run:
        img_display(fondo_menu, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 231+80 and mouse_pos[1] >= 231:
                        print(pygame.mouse.get_pos())
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 301+80 and mouse_pos[1] >= 301:
                        credito()
                    if mouse_pos [0]>= 450-75 and mouse_pos[0] <= 450-75+150 and mouse_pos[1] <= 371+80 and mouse_pos[1] >= 371:
                        run = False
        img.update('tigre')
        img_display(img.image, 0, 200)
        img_display(jugar,450-75,231)
        img_display(creditos, 450-75, 301)
        img_display(salir, 450-75, 371)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()




if __name__ == '__main__':
    main()