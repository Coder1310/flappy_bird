import pygame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Моя первая игра')

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    pygame.display.flip()

pygame.quit()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка экрана черным цветом
    screen.fill((0, 0, 0))
    
    # Рисование квадрата и круга
    pygame.draw.rect(screen, (0, 128, 255), (50, 50, 100, 100))
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    
    # Обновление экрана
    pygame.display.flip()

pygame.quit()

# Загрузка изображения
player_image = pygame.image.load('player.png')
player_x = 300
player_y = 300

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение изображения
    player_x += 1
    
    # Обновление экрана
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    pygame.display.flip()

pygame.quit()

player_speed = 5

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Обновление экрана
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    pygame.display.flip()

pygame.quit()
