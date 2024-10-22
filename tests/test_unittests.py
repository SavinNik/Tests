from unittest import TestCase
from main import fio, reverse, check_email


class TestMain(TestCase):
    def test_fio(self):
        for i, (names, expected) in enumerate([
            (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
            (['Жан', 'Клот', 'Вандамович'], 'ЖКВ'),
            (['Павлов', 'Иван', 'Уралович'], 'ПИУ')
        ]):
            with self.subTest(i=i):
                result = fio(names)
                self.assertEqual(result, expected)


    def test_reverse(self):
        for i, (string, expected) in enumerate([
            ('!dlroW olleH', 'hello world!'),
            ('AvadaKedavraaaaA!', '!aaaaarvadekadava'),
            ('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я', 'я наконец-то разобрался в этих ваших срезах'),
        ]):
            with self.subTest(i=i):
                result = reverse(string)
                self.assertEqual(result, expected)


    def test_check_email(self):
        for i, (email, expected) in enumerate([
            ('Helloworld@.ru', True),
            ('<мояпочта@нетология.ру>', True),
            ('<python@email@net>', False),
        ]):
            with self.subTest(i=i):
                result = check_email(email)
                self.assertEqual(result, expected)
