"""Тесты для программы Клиента"""


import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence, process_ans
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR


class TestClientFunc(unittest.TestCase):
    """
    Класс для тестирования
    """

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_def_create_presence(self):
        """Тест корректного запроса"""
        test = create_presence()
        test[TIME] = 1.1  # принудительно устанавливаем время для прохождения теста
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_process_ans_200(self):
        """Тест корректной работы(200)"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_ans_400(self):
        """Тест проверки плохого запроса(400)"""
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}),
                         '400 : Bad Request')

    def test_process_ans_no_response(self):
        """Тест проверки отсутствия ответа"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})
