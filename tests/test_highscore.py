import unittest
import os
from flappy_parrot.py import save_high_score

class TestFlappyParrot(unittest.TestCase):
    
    def test_save_high_score(self):
        # Путь к файлу
        high_score_file = "highscore.txt"
        
        # Перед тестом удалим файл, если он существует
        if os.path.exists(high_score_file):
            os.remove(high_score_file)
        
        # Сохраняем новый рекорд
        save_high_score(150)
        
        # Проверяем, что файл существует и в нём правильное значение
        self.assertTrue(os.path.exists(high_score_file))
        
        with open(high_score_file, "r") as f:
            saved_score = int(f.read().strip())
        
        self.assertEqual(saved_score, 150)
        
        # Удаляем файл после теста
        os.remove(high_score_file)

if __name__ == '__main__':
    unittest.main()
import pytest
from flappy_parrot import load_high_score, save_high_score

def test_load_high_score_new_file():
    # Тестируем создание нового файла с рекордами
    score = load_high_score()
    assert score == 0  # Ожидаем 0, так как файл только что создан

def test_save_high_score():
    # Проверяем правильность сохранения нового рекорда
    save_high_score(123)
    score = load_high_score()
    assert score == 123  # Проверяем, что рекорд сохранился
