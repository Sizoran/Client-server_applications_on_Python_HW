"""Тесты для программы Сервера"""

import unittest
from server import process_client_message
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE


class TestServerFunc(unittest.TestCase):
    """
    Класс для тестирования
    """

    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }  # Очень удобный приём, обозначение переменных
    # для дальнейшего применения в тестах
    ok_dict = {RESPONSE: 200}

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_def_process_client_message(self):
        """Тест корректного запроса"""
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1,
                                                 USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_action(self):
        """Тест ошибки отсутствия действия"""
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Тест неверного действия"""
        self.assertEqual(process_client_message(
            {ACTION: 'AbraCadabra', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Тест отсутствия времени"""
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Тест отсутствия юзера"""
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Тест неизвестного юзера(не Guest)"""
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'David Blaine'}}),
                         self.err_dict)
