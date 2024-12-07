import pytest
from flappy_parrot import generate_pipe

def test_generate_pipe_easy():
    difficulty = {
        'pipe_vel': 3,
        'pipe_gap': 200,
        'pipe_width': 80,
        'pipe_interval': 1500
    }
    new_pipe = generate_pipe(difficulty)
    assert len(new_pipe) == 1
    assert 'x' in new_pipe[0]
    assert 'width' in new_pipe[0]
    assert 'top_height' in new_pipe[0]
    assert 'bottom_y' in new_pipe[0]
    assert 'height' in new_pipe[0]
    assert 'passed' in new_pipe[0]

def test_generate_pipe_medium():
    difficulty = {
        'pipe_vel': 4,
        'pipe_gap': 170,
        'pipe_width': 80,
        'pipe_interval': 1200
    }
    new_pipe = generate_pipe(difficulty)
    assert len(new_pipe) == 1
    assert new_pipe[0]['pipe_gap'] == 170  # Проверяем настройки сложности
