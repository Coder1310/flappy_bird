import unittest
import os
from flappy_parrot.py import load_high_score

class TestFlappyParrot(unittest.TestCase):
    
    def test_load_high_score(self):
        # Перед тестом удалим файл, если он существует
        if os.path.exists("highscore.txt"):
            os.remove("highscore.txt")
        
        # Проверяем, что функция возвращает 0, если файла нет
        self.assertEqual(load_high_score(), 0)

        # Создадим файл с рекордом
        with open("highscore.txt", "w") as f:
            f.write("100")
        
        # Проверяем, что рекорд загружается правильно
        self.assertEqual(load_high_score(), 100)

        # Удалим файл после теста
        os.remove("highscore.txt")

if __name__ == '__main__':
    unittest.main()
