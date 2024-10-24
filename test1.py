import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, 300
GRAVITY = 0.6
JUMP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
SPEED = 4

# Цвета
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Загрузка изображений
bird_image = pygame.image.load("bird.png")
background = pygame.image.load("background.png")

# Класс птицы
class Bird:
    def __init__(self):
        self.image = bird_image
        self.x = BIRD_X
        self.y = BIRD_Y
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Класс труб
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)

    def update(self):
        self.x -= SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Основная функция игры
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH + 100), Pipe(WIDTH + 300)]
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Обновление птицы
        bird.update()
        bird.draw(screen)

        # Обновление труб
        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH))
                score += 1

        # Проверка столкновений
        for pipe in pipes:
            if bird.x + bird_image.get_width() > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + bird_image.get_height() > pipe.height + PIPE_GAP:
                    running = False

        # Проверка на выход за экран
        if bird.y > HEIGHT or bird.y < 0:
            running = False

        # Обновление экрана и задержка
        pygame.display.flip()
        clock.tick(30)

    print(f"Game Over! Score: {score}")
    pygame.quit()

if __name__ == "__main__":
    main()
