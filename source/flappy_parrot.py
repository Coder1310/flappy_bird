#Flappy parrot
import pygame
import random
import sys
import os

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

GAME_WIDTH, GAME_HEIGHT = 600, 800

game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

# Установка полноэкранного режима
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Flappy Parrot Clone with Difficulty and Parrot Selection")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BLUE = (70, 130, 180)
YELLOW = (255, 215, 0)
GOLD = (255, 215, 0)
RED = (255, 69, 0)
ORANGE = (255, 140, 0)
GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)
LIGHT_GRAY = (211, 211, 211)

# Настройки птицы
BIRD_X = 100
BIRD_Y = GAME_HEIGHT // 2
bird_vel = 0
gravity = 0.5  # Гравитация, определена глобально
jump_strength = -10

# Настройки труб (будут изменяться в зависимости от сложности)
PIPE_WIDTH = 80
PIPE_GAP = 200  # Прорезь между трубами
pipe_vel = 3
pipes = []

# Таймер для генерации труб
PIPE_INTERVAL = 1500  # миллисекунды

# Шрифты
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

# Путь к файлу с рекордом
HIGH_SCORE_FILE = "highscore.txt"


# Функция для загрузки рекорда
def load_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write("0")
        return 0
    with open(HIGH_SCORE_FILE, 'r') as file:
        try:
            return int(file.read())
        except:
            return 0


# Функция для сохранения рекорда
def save_high_score(new_high_score):
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(new_high_score))


# Функция для отрисовки попугая
def draw_parrot(x, y, parrot_type):
    if parrot_type == "Какаду":
        body_color = WHITE
        head_color = WHITE
        wing_color = LIGHT_GRAY
        beak_color = ORANGE
        tail_color1 = GOLD
        tail_color2 = RED
        crest_color = YELLOW
        eye_color = BLACK
    elif parrot_type == "Ара":
        body_color = BLUE
        head_color = GREEN
        wing_color = PURPLE
        beak_color = YELLOW
        tail_color1 = GREEN
        tail_color2 = BLUE
        crest_color = WHITE
        eye_color = BLACK
    elif parrot_type == "Серый африканский попугай":
        body_color = GRAY
        head_color = DARK_GREEN
        wing_color = BLACK
        beak_color = ORANGE
        tail_color1 = DARK_GREEN
        tail_color2 = BLACK
        crest_color = GRAY
        eye_color = BLACK
    else:
# Default цвета, если тип не определен
        body_color = GREEN
        head_color = BLUE
        wing_color = DARK_GREEN
        beak_color = ORANGE
        tail_color1 = GOLD
        tail_color2 = RED
        crest_color = YELLOW
        eye_color = BLACK

# Основное тело попугая (эллипс)
    body_width, body_height = 40, 30
    pygame.draw.ellipse(game_surface, body_color, (x, y, body_width, body_height))

# Голова попугая (круг)
    head_radius = 10
    head_x = x + body_width - head_radius
    head_y = y + head_radius - 5
    pygame.draw.circle(game_surface, head_color, (head_x, head_y), head_radius)

# Гребень на голове (маленькие треугольники)
    pygame.draw.polygon(game_surface, crest_color, [
        (head_x, head_y - head_radius),
        (head_x - 3, head_y - head_radius - 5),
        (head_x + 3, head_y - head_radius - 5)
    ])

# Глаз попугая (маленький круг)
    eye_radius = 3
    eye_x = head_x + 4
    eye_y = head_y - 3
    pygame.draw.circle(game_surface, eye_color, (eye_x, eye_y), eye_radius)

# Клюв попугая (треугольник)
    beak_points = [
        (head_x + head_radius, head_y),  # Верхняя точка
        (head_x + head_radius + 10, head_y - 5),  # Левая нижняя точка
        (head_x + head_radius + 10, head_y + 5)  # Правая нижняя точка
    ]
    pygame.draw.polygon(game_surface, beak_color, beak_points)

# Крыло попугая (полигон)
    wing_points = [
        (x + 15, y + 10),
        (x + 30, y - 5),
        (x + 35, y + 15)
    ]
    pygame.draw.polygon(game_surface, wing_color, wing_points)

# Хвостовые перья (треугольники разных цветов)
    tail_points = [
        (x, y + 10),
        (x - 10, y + 5),
        (x - 10, y + 15)
    ]
    pygame.draw.polygon(game_surface, tail_color1, tail_points)

    tail_points2 = [
        (x, y + 10),
        (x - 10, y + 15),
        (x - 10, y + 25)
    ]
    pygame.draw.polygon(game_surface, tail_color2, tail_points2)


# Функция для отрисовки кнопки "Завершить игру"
def draw_quit_button(surface, quit_button_rect):
# Рисование кнопки
    pygame.draw.rect(surface, RED, quit_button_rect)
    pygame.draw.rect(surface, BLACK, quit_button_rect, 2)  # Обводка кнопки
# Рисование текста "Quit"
    quit_text = small_font.render("Quit", True, WHITE)
    text_rect = quit_text.get_rect(center=quit_button_rect.center)
    surface.blit(quit_text, text_rect)


# Обновленная функция для отрисовки труб с дополнительными деталями
def draw_pipes(pipes):
    pipe_color = GREEN
    pipe_border_color = DARK_GREEN
    grass_color = DARK_GREEN
    grass_height = 20  # Высота травы на трубах

    for pipe in pipes:
        x = pipe['x']
        width = pipe['width']
        top_height = pipe['top_height']
        bottom_y = pipe['bottom_y']
        height = pipe['height']

# Отрисовка верхней трубы
        pygame.draw.rect(game_surface, pipe_color, (x, 0, width, top_height))
        pygame.draw.rect(game_surface, pipe_border_color, (x, 0, width, top_height), 4)  # Обводка

# Добавление травы на верхнюю трубу
        pygame.draw.rect(game_surface, grass_color, (x, top_height - grass_height, width, grass_height))

# Отрисовка нижней трубы
        pygame.draw.rect(game_surface, pipe_color, (x, bottom_y, width, height))
        pygame.draw.rect(game_surface, pipe_border_color, (x, bottom_y, width, height), 4)  # Обводка

# Добавление травы на нижнюю трубу
        pygame.draw.rect(game_surface, grass_color, (x, bottom_y, width, grass_height))


# Функция для генерации новых труб
def generate_pipe(difficulty):
    top_height = random.randint(50, GAME_HEIGHT - difficulty['pipe_gap'] - 150)
    bottom_y = top_height + difficulty['pipe_gap']
    pipe = {
        'x': GAME_WIDTH,
        'width': difficulty['pipe_width'],
        'top_height': top_height,
        'bottom_y': bottom_y,
        'height': GAME_HEIGHT - bottom_y,
        'passed': False
    }
    pipes.append(pipe)


# Функция для проверки столкновений
def check_collision(bird_y, pipes):
    bird_rect = pygame.Rect(BIRD_X, bird_y, 40, 30)  # Основное тело попугая
    head_rect = pygame.Rect(BIRD_X + 30, bird_y, 20, 20)  # Голова попугая

    for pipe in pipes:
        top_pipe_rect = pygame.Rect(pipe['x'], 0, pipe['width'], pipe['top_height'])
        bottom_pipe_rect = pygame.Rect(pipe['x'], pipe['bottom_y'], pipe['width'], pipe['height'])
        if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
            return True
        if head_rect.colliderect(top_pipe_rect) or head_rect.colliderect(bottom_pipe_rect):
            return True

# Проверка на выход за пределы экрана
    if bird_y < 0 or bird_y + 30 > GAME_HEIGHT:
        return True
    return False


# Функция экрана окончания игры
def game_over_screen(score, high_score):
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # 60 FPS

# Определение области кнопки "Quit"
        quit_button_rect = pygame.Rect(GAME_WIDTH - 100, 20, 80, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()  # Перезапуск игры
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
# Сопоставление координат экрана с координатами game_surface
                game_x = int(mouse_x * GAME_WIDTH / SCREEN_WIDTH)
                game_y = int(mouse_y * GAME_HEIGHT / SCREEN_HEIGHT)
                if quit_button_rect.collidepoint(game_x, game_y):
                    pygame.quit()
                    sys.exit()

# Отрисовка
        game_surface.fill(SKY_BLUE)
        game_over_text = font.render("Game Over", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)
        high_score_text = small_font.render(f"High Score: {high_score}", True, WHITE)
        restart_text = small_font.render("Press SPACE to Restart", True, WHITE)

        game_surface.blit(game_over_text, (GAME_WIDTH // 2 - game_over_text.get_width() // 2, GAME_HEIGHT // 2 - 150))
        game_surface.blit(score_text, (GAME_WIDTH // 2 - score_text.get_width() // 2, GAME_HEIGHT // 2 - 50))
        game_surface.blit(high_score_text, (GAME_WIDTH // 2 - high_score_text.get_width() // 2, GAME_HEIGHT // 2))
        game_surface.blit(restart_text, (GAME_WIDTH // 2 - restart_text.get_width() // 2, GAME_HEIGHT // 2 + 50))

# Рисование кнопки "Quit"
        draw_quit_button(game_surface, quit_button_rect)

# Масштабирование и отображение
        scaled_surface = pygame.transform.smoothscale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        WIN.blit(scaled_surface, (0, 0))
        pygame.display.update()


# Функции для управления облаками
def initialize_clouds():
# Создаем несколько облаков для каждого слоя
    far_clouds = []
    near_clouds = []

    for _ in range(5):
# Дальние облака (медленнее)
        cloud = {
            'x': random.randint(0, GAME_WIDTH),
            'y': random.randint(50, GAME_HEIGHT // 2),
            'radius': random.randint(20, 40),
            'speed': 1  # Медленная скорость
        }
        far_clouds.append(cloud)

# Ближние облака (быстрее)
        cloud = {
            'x': random.randint(0, GAME_WIDTH),
            'y': random.randint(100, GAME_HEIGHT // 2 + 100),
            'radius': random.randint(30, 50),
            'speed': 2  # Быстрая скорость
        }
        near_clouds.append(cloud)

    return far_clouds, near_clouds


def update_and_draw_clouds(clouds, layer):
    for cloud in clouds:
# Обновляем позицию облака
        cloud['x'] -= cloud['speed']
# Если облако вышло за левую границу, возвращаем его справа
        if cloud['x'] + cloud['radius'] * 2 < 0:
            cloud['x'] = GAME_WIDTH
            cloud['y'] = random.randint(50, GAME_HEIGHT // 2) if layer == 'far' else random.randint(100, GAME_HEIGHT // 2 + 100)

# Отрисовка облака
        if layer == 'far':
            color = GRAY
        else:
            color = WHITE
        pygame.draw.circle(game_surface, color, (cloud['x'], cloud['y']), cloud['radius'])


# Функция экрана выбора сложности
def difficulty_selection_screen():
    clock = pygame.time.Clock()
    selected = 0
    difficulties = ["Easy", "Medium", "Hard"]

# Параметры для каждого уровня сложности
    difficulty_settings = {
        "Easy": {
            'pipe_vel': 3,
            'pipe_gap': 200,
            'pipe_width': 80,
            'pipe_interval': 1500
        },
        "Medium": {
            'pipe_vel': 4,
            'pipe_gap': 170,
            'pipe_width': 80,
            'pipe_interval': 1200
        },
        "Hard": {
            'pipe_vel': 5,
            'pipe_gap': 150,
            'pipe_width': 80,
            'pipe_interval': 1000
        }
    }

    while True:
        clock.tick(60)  # 60 FPS

# Определение области кнопки "Quit"
        quit_button_rect = pygame.Rect(GAME_WIDTH - 100, 20, 80, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected = (selected - 1) % len(difficulties)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected = (selected + 1) % len(difficulties)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    selected_difficulty = difficulties[selected]
                    return difficulty_settings[selected_difficulty]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
# Сопоставление координат экрана с координатами game_surface
                game_x = int(mouse_x * GAME_WIDTH / SCREEN_WIDTH)
                game_y = int(mouse_y * GAME_HEIGHT / SCREEN_HEIGHT)
                if quit_button_rect.collidepoint(game_x, game_y):
                    pygame.quit()
                    sys.exit()

# Отрисовка
        game_surface.fill(SKY_BLUE)
        title_text = font.render("Select Difficulty", True, WHITE)
        game_surface.blit(title_text, (GAME_WIDTH // 2 - title_text.get_width() // 2, GAME_HEIGHT // 4))

        for idx, level in enumerate(difficulties):
            if idx == selected:
                color = GOLD
                indicator = ">>"
            else:
                color = WHITE
                indicator = "  "
            level_text = small_font.render(f"{indicator} {level}", True, color)
            game_surface.blit(level_text, (GAME_WIDTH // 2 - level_text.get_width() // 2, GAME_HEIGHT // 2 + idx * 50))

# Рисование кнопки "Quit"
        draw_quit_button(game_surface, quit_button_rect)

# Масштабирование и отображение
        scaled_surface = pygame.transform.smoothscale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        WIN.blit(scaled_surface, (0, 0))
        pygame.display.update()


# Функция экрана выбора типа попугая
def parrot_selection_screen():
    clock = pygame.time.Clock()
    selected = 0
    parrots = ["Какаду", "Ара", "Серая африканская попугай"]

    while True:
        clock.tick(60)  # 60 FPS

# Определение области кнопки "Quit"
        quit_button_rect = pygame.Rect(GAME_WIDTH - 100, 20, 80, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected = (selected - 1) % len(parrots)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected = (selected + 1) % len(parrots)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    selected_parrot = parrots[selected]
                    return selected_parrot
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
# Сопоставление координат экрана с координатами game_surface
                game_x = int(mouse_x * GAME_WIDTH / SCREEN_WIDTH)
                game_y = int(mouse_y * GAME_HEIGHT / SCREEN_HEIGHT)
                if quit_button_rect.collidepoint(game_x, game_y):
                    pygame.quit()
                    sys.exit()

# Отрисовка
        game_surface.fill(SKY_BLUE)
        title_text = font.render("Выберите попугая", True, WHITE)
        game_surface.blit(title_text, (GAME_WIDTH // 2 - title_text.get_width() // 2, GAME_HEIGHT // 4))

        for idx, parrot in enumerate(parrots):
            if idx == selected:
                color = GOLD
                indicator = ">>"
            else:
                color = WHITE
                indicator = "  "
            parrot_text = small_font.render(f"{indicator} {parrot}", True, color)
            game_surface.blit(parrot_text, (GAME_WIDTH // 2 - parrot_text.get_width() // 2, GAME_HEIGHT // 2 + idx * 50))

# Рисование кнопки "Quit"
        draw_quit_button(game_surface, quit_button_rect)

# Масштабирование и отображение
        scaled_surface = pygame.transform.smoothscale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        WIN.blit(scaled_surface, (0, 0))
        pygame.display.update()


# Основной цикл игры
def main():
    global BIRD_Y, bird_vel, pipes
    BIRD_Y = GAME_HEIGHT // 2
    bird_vel = 0
    pipes = []
    score = 0

# Загрузка текущего рекорда
    high_score = load_high_score()

# Инициализация облаков
    far_clouds, near_clouds = initialize_clouds()

# Выбор уровня сложности
    difficulty = difficulty_selection_screen()

# Выбор типа попугая
    parrot_type = parrot_selection_screen()

    clock = pygame.time.Clock()
    run = True

# Таймер событий для генерации труб
    pygame.time.set_timer(pygame.USEREVENT, difficulty['pipe_interval'])

    while run:
        clock.tick(60)  # 60 FPS

# Определение области кнопки "Quit"
        quit_button_rect = pygame.Rect(GAME_WIDTH - 100, 20, 80, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_vel = jump_strength
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
# Сопоставление координат экрана с координатами game_surface
                game_x = int(mouse_x * GAME_WIDTH / SCREEN_WIDTH)
                game_y = int(mouse_y * GAME_HEIGHT / SCREEN_HEIGHT)
                if quit_button_rect.collidepoint(game_x, game_y):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.USEREVENT:
                generate_pipe(difficulty)

# Обновление позиции птицы
        bird_vel += gravity
        BIRD_Y += bird_vel

# Обновление позиций труб
        for pipe in pipes:
            pipe['x'] -= difficulty['pipe_vel']

# Удаление труб, вышедших за экран
        pipes = [pipe for pipe in pipes if pipe['x'] + pipe['width'] > 0]

# Проверка столкновений
        if check_collision(BIRD_Y, pipes):
# Обновление рекорда, если необходимо
            if score > high_score:
                high_score = score  
                save_high_score(high_score)
            game_over_screen(score, high_score)
            run = False  # Завершение текущего цикла игры

# Обновление счета
        for pipe in pipes:
            if not pipe['passed'] and pipe['x'] + pipe['width'] < BIRD_X:
                score += 1
                pipe['passed'] = True

# Отрисовка
        game_surface.fill(SKY_BLUE)  # Заливка фона

        update_and_draw_clouds(far_clouds, 'far')
        update_and_draw_clouds(near_clouds, 'near')

        draw_parrot(BIRD_X, BIRD_Y, parrot_type)

        draw_pipes(pipes)

# Отображение счета
        score_text = font.render(str(score), True, WHITE)
        game_surface.blit(score_text, (GAME_WIDTH // 2 - score_text.get_width() // 2, 50))

# Отображение рекорда в углу
        high_score_text = small_font.render(f"High Score: {high_score}", True, WHITE)
        game_surface.blit(high_score_text, (10, 10))

# Рисование кнопки "Quit"
        draw_quit_button(game_surface, quit_button_rect)

# Масштабирование и отображение на экране
        scaled_surface = pygame.transform.smoothscale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        WIN.blit(scaled_surface, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
