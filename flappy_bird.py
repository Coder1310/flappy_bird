import pygame
pygame.init()
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя программа")
direct_x1 = 1
direct_y1 = 1
direct_x = 1
direct_y = 1
font = pygame.font.SysFont('comicsansms', 80)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
like = font.render("Гооооооол!!!", 1, GREEN, BLUE)
follow = font.render("Гол?", 1, RED, GREEN)
x, y = 130, 100
x1, y1 = 310, 200
w, h = follow.get_size()
width, height = like.get_size()
FPS = 180
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(follow, (x1, y1))
    screen.blit(like, (x, y))

    x1 += direct_x1
    if x1 + w >= 800 or x < 0:
        direct_x1 = -direct_x1

    y1 += direct_y1
    if y1 + h >= 500 or y1 < 0:
        direct_y1 = -direct_y1

    x += direct_x
    if x + width >= 800 or x < 0:
        direct_x = -direct_x

    y += direct_y
    if y + height >= 500 or y < 0:
        direct_y = -direct_y
    pygame.display.update()
