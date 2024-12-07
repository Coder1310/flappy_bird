import unittest
from flappy_parrot.py import check_collision

class TestFlappyParrot(unittest.TestCase):
    
    def test_check_collision(self):
        # Параметры игры
        bird_y = 400
        pipes = [
            {'x': 500, 'width': 80, 'top_height': 200, 'bottom_y': 400, 'height': 400, 'passed': False}
        ]
        
        # Проверяем, что коллизия произойдёт
        self.assertTrue(check_collision(bird_y, pipes))
        
        # Если изменим координаты птицы, то коллизии не будет
        bird_y = 1000
        self.assertFalse(check_collision(bird_y, pipes))

if __name__ == '__main__':
    unittest.main()
