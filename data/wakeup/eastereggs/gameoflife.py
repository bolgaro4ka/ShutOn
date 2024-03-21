import pygame
import sys
import os
import config

pygame.init()

FPS=config.fps
clock = pygame.time.Clock()

dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Game of Life")

WINW, WINH = dis.get_size()

BOXW = config.x
BOXH = config.y

# assert WINW % BOXW == 0 and WINH % BOXH == 0

BOARDW = WINW//BOXW
BOARDH = WINH//BOXH

fill_color = config.fill_color
empty_color = config.empty_color



def make_new_board(w, h):
    return list([0]*w for i in range(h))

def check(board, x, y):
    m = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(i == j == 0) and (0 <= i+y < BOARDH) and (0 <= j+x < BOARDW):
                m += board[i+y][j+x]
    if board[y][x]:
        if eval(config.life):
            return True
    if not board[y][x]:
        if eval(config.regen):
            return True
    return False
    

def update(board):
    nb = make_new_board(BOARDW, BOARDH)
    for i in range(BOARDH):
        for j in range(BOARDW):
            nb[i][j] = check(board, j, i)
    return nb


def draw(win, board):
    
    for i in range(BOARDH):
        for j in range(BOARDW):
            if board[i][j]:
                pygame.draw.rect(win, fill_color, (j*BOXW, i*BOXH, BOXW, BOXH))
            else:
                pygame.draw.rect(win, empty_color,
                                 (j*BOXW, i*BOXH, BOXW, BOXH))


def recommend_name():
    n = 0
    a = os.listdir()
    l = []
    for f in a:
        if f.startswith("gol") and f.endswith(".png"):
            l.append(f)
    t = True
    while t:
        n += 1
        t = False
        if "gol"+str(n)+".png" in l:
            t = True
    return "gol"+str(n)+".png"


def load(name):
    nb = make_new_board(BOARDW, BOARDH)
    s = pygame.image.load(name)
    for i in range(BOARDH):
        for j in range(BOARDW):
            nb[i][j] = (s.get_at((j*BOXW+BOXW//2, i*BOXH+BOXH//2))
                        == fill_color)
    global loading
    loading=False
    return nb


board = make_new_board(BOARDW, BOARDH)
updating = False
drag = False
down = False
dragval = False
loading=False
while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            x, y = x//BOXW, y//BOXH
            down = True
            dragval = not board[y][x]
            if drag == False:
                board[y][x] = not board[y][x]
        elif e.type == pygame.MOUSEBUTTONUP:
            down = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                updating = not updating
            elif e.key == pygame.K_RIGHT:
                board = update(board)
            elif e.key == pygame.K_c:
                board = make_new_board(BOARDW, BOARDH)
            elif e.key == pygame.K_s:
                pygame.image.save(dis, recommend_name())
            elif e.key == pygame.K_l:
                board = load(input())
                loading=True
            elif e.key == pygame.K_d:
                drag = not drag
                
    
    
    if drag and down:
        x, y = pygame.mouse.get_pos()
        x, y = x//BOXW, y//BOXH
        board[y][x] = dragval
    if updating:
        board = update(board)

    draw(dis, board)
    if config.show_text == 'not_show':
        pass
    if config.show_text == 'show_fps':
        f1 = pygame.font.Font(None, 16)
        text1 = f1.render(str(str('FPS: ')+str(int(clock.get_fps())) + ' / ' + str(FPS)), True,
                      (0, 180, 0))
        dis.blit(text1, (2, 2))
    if config.show_text == 'show_all':
        f1 = pygame.font.Font(None, 16)
        text1 = f1.render(str(str('FPS: ')+str(int(clock.get_fps())) + ' / ' + str(FPS)+' | '
            +'Правила: клетка выживает при: ' + str(config.life) + ', клетка оживает при: ' + str(config.regen)
            +' | Клеточный автомат запущен: '+str(updating) + ' | Режим рисования: '+str(drag) +' | Размеры клетки: ' + str(str(config.x)+ ' x '+ str(config.y))
            +' | Размер поля: ' + str(str(WINW)+' x '+str(WINH))+' | Автор: bolgaro4ka (https://github.com/bolgaro4ka) | Выход: Alt+F4' ), True,
                      (0, 180, 0))
        dis.blit(text1, (2, 2))
    clock.tick(FPS)
    pygame.display.update()
