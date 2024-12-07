import unittest
from unittest.mock import patch
from flappy_parrot.py import draw_parrot

class TestFlappyParrot(unittest.TestCase):
    
    @patch('flappy_parrot.py.pygame.draw.ellipse')
    @patch('flappy_parrot.py.pygame.draw.circle')
    @patch('flappy_parrot.py.pygame.draw.polygon')
    def test_draw_parrot(self, mock_polygon, mock_circle, mock_ellipse):
        # Вызываем функцию draw_parrot
        draw_parrot(100, 200, "Ара")
        
        # Проверяем, что методы отрисовки были вызваны
        mock_ellipse.assert_called()
        mock_circle.assert_called()
        mock_polygon.assert_called()

if __name__ == '__main__':
    unittest.main()
