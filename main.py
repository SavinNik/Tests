from tests.test_YD import get_token_yd


def fio(initials: list[str]) -> str:
    # Напишите ваш код здесь
    list_1 = [initials[0][0], initials[1][0], initials[2][0]]
    result = ''.join(list_1)
    return result


def reverse(string: str) -> str:
    # Напишите ваш код здесь
    revers_string = string[::-1].lower()
    return revers_string


def check_email(email: str) -> bool:
    # Напишите ваш код здесь
    if ' ' not in email and '@' in email and '.' in email:
        result = True
    else:
        result = False
    return result

# if __name__ == '__main__':
