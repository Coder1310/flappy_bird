import unittest
from flappy_parrot.py import generate_pipe

class TestFlappyParrot(unittest.TestCase):
    
    def test_generate_pipe(self):
        # Установим параметры сложности
        difficulty = {
            'pipe_vel': 3,
            'pipe_gap': 200,
            'pipe_width': 80,
            'pipe_interval': 1500
        }
        
        # Генерируем трубу
        pipe = generate_pipe(difficulty)
        
        # Проверяем, что труба имеет начальное положение по оси X (600)
        self.assertEqual(pipe['x'], 600)  # Труба должна быть в правом краю экрана
        
        # Проверяем, что высота верхней трубы не меньше 50
        self.assertGreaterEqual(pipe['top_height'], 50)
        
        # Проверяем, что расстояние между верхней и нижней трубой (pipe_gap) больше или равно 200
        self.assertGreaterEqual(pipe['bottom_y'] - pipe['top_height'], difficulty['pipe_gap'])
        
        # Проверяем, что труба не выходит за пределы экрана
        self.assertLessEqual(pipe['bottom_y'] + pipe['height'], 800)  # 800 - высота экрана

if __name__ == '__main__':
    unittest.main()
