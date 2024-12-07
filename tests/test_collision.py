import pytest
from flappy_parrot import check_collision

def test_check_collision_with_pipe():
    # Структура данных для тестирования
    bird_y = 400
    pipes = [
        {'x': 200, 'width': 80, 'top_height': 300, 'bottom_y': 500, 'height': 300, 'passed': False},
        {'x': 400, 'width': 80, 'top_height': 200, 'bottom_y': 400, 'height': 400, 'passed': False}
    ]
    # Проверяем столкновение с первой трубой
    assert check_collision(bird_y, pipes) == True

def test_check_collision_no_collision():
    bird_y = 600
    pipes = [
        {'x': 200, 'width': 80, 'top_height': 300, 'bottom_y': 500, 'height': 300, 'passed': False}
    ]
    # Проверяем, что столкновения нет
    assert check_collision(bird_y, pipes) == False

def test_check_collision_with_top():
    bird_y = 0  # Летит вверх и может столкнуться с верхней частью
    pipes = [
        {'x': 200, 'width': 80, 'top_height': 300, 'bottom_y': 500, 'height': 300, 'passed': False}
    ]
    assert check_collision(bird_y, pipes) == True
