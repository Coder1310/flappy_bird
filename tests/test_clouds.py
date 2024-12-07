import pytest
from flappy_parrot import initialize_clouds, update_and_draw_clouds

def test_initialize_clouds():
    far_clouds, near_clouds = initialize_clouds()
    assert len(far_clouds) == 5
    assert len(near_clouds) == 5
    assert 'x' in far_clouds[0]
    assert 'y' in near_clouds[0]
    assert 'speed' in far_clouds[0]

def test_update_and_draw_clouds():
    far_clouds, _ = initialize_clouds()
    # Тестируем обновление облаков
    cloud_before = far_clouds[0]['x']
    update_and_draw_clouds(far_clouds, 'far')
    cloud_after = far_clouds[0]['x']
    assert cloud_before > cloud_after  # Позиция облака должна уменьшиться (облачка движутся влево)
