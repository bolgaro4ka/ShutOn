from random import randint
import pygame
import config

exit = False

SIZE = width, height = config.width, config.height
BG_COLOR = config.background_color
fullscreen = config.fullscreen
counter=0

def percente():
    size=config.size*0.01
    return size
    
logo = pygame.image.load('wakeup/eastereggs/img/logo.png')
logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))

clock = pygame.time.Clock()

img_size = logo.get_rect().size
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('DVD Screensaver')

if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

x = randint(50, width-60)
y = randint(50, height-60)

x_speed = config.x_speed
y_speed = config.y_speed


def move(x, y):
    screen.blit(logo, (x, y))
    
def color_logo():
    global counter, logo
    if counter == 0:
        logo = pygame.image.load('wakeup/eastereggs/img/logo_red.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    elif counter == 1:
        logo = pygame.image.load('wakeup/eastereggs/img/logo_orange.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    elif counter == 2:
        logo = pygame.image.load('wakeup/eastereggs/img/logo_green.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    elif counter == 3:
        logo = pygame.image.load('wakeup/eastereggs/img/logo_blue.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    elif counter == 4:
        logo = pygame.image.load('wakeup/eastereggs/img/logo_fiolet.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    elif counter == 5:
        logo = pygame.image.load('wakeup/eastereggs/img/logo.png')
        logo = pygame.transform.scale(logo, (100*percente(), 50*percente()))
        counter+=1
    if counter > 5:
        counter=0



while not exit:
    screen.fill(BG_COLOR)
    if (x + img_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
        color_logo()
    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
        color_logo()
    x += x_speed
    y += y_speed
    move(x, y)
    pygame.display.update()
    clock.tick(config.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()