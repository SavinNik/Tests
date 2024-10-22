import pytest

from main import fio, reverse, check_email


@pytest.mark.parametrize(
    'names, expected',
    (
            (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
            (['Жан', 'Клот', 'Вандамович'], 'ЖКВ'),
            (['Павлов', 'Иван', 'Уралович'], 'ПИУ'),
    )
)
def test_fio(names, expected):
    result = fio(names)
    assert result == expected


@pytest.mark.parametrize(
    'string, expected',
    (
            ('!dlroW olleH', 'hello world!'),
            ('AvadaKedavraaaaA!', '!aaaaarvadekadava'),
            ('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я', 'я наконец-то разобрался в этих ваших срезах'),
    )
)
def test_reverse(string, expected):
    result = reverse(string)
    assert result == expected


@pytest.mark.parametrize(
    'email, expected',
    (
            ('Helloworld@.ru', True),
            ('<мояпочта@нетология.ру>', True),
            ('<python@email@net>', False),
    )
)
def test_check_email(email, expected):
    result = check_email(email)
    assert result == expected

