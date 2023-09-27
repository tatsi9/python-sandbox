def is_palindrome(string: str) -> bool:
    """
    the function check
    if the string is a palindrome
    """
    i = 0
    while i < (int(len(string) / 2)):
        if string[i] != string[-(i+1)]:
            return False
        i += 1
    return True

# print(len("An3astasioa") / 2)
# print(is_palindrome("радар"))


def filter_string(string: str, sym: str) -> str:
    """
    the function earases the symbol everywhere from the string
    and whitespaces before and after the string
    """
    result_str = ""
    for i in string:
        if i.lower() == sym.lower():
            result_str = result_str
        else:
            result_str += i
    return result_str.strip()

# print(filter_string("A     N aS ta sia   ", "a"))


def has_char(string: str, sym: str) -> bool:
    """
    the function checks
    if the string contains the symbol
    """
    i = 0
    while i < len(string):
        if string.lower()[i] == sym.lower():
            return True
        i += 1
    return False

#print(has_char("Anastasia", "n"))


def my_substr_1(string: str, length: int) -> str:
    """
    the function takes string and lenght
    returns a substring n-length
    """
    result = string[0:length]
    return result


def my_substr_2(string: str, length: int) -> str:
    """
    the function takes string and lenght
    returns a substring n-length
    """
    result = ''
    i = 0
    while i < length:
        result = result + string[i]
        i += 1
    return result

# print(my_substr_1("string", 3))
# print(my_substr_2("string", 3))


def join_numbers_from_range(num1: int, num2: int) -> str:
    """
    the function converts and concats
    all digits from range to the string
    """
    string = ''
    i = num1
    while i <= num2:
        string = string + str(i)
        i += 1
    return string

# print(join_numbers_from_range(0, 4))


def print_numbers(num):
    """
    the function prints
    all digits from num to 0
    """
    i = num
    while i > 0:
        print(i)
        i -= 1
    print("finished!")

# print(print_numbers(3))


# def get_number_explanation(num) -> str:
#     """
#     the function explains a number as a numerologist
#     """
#     num = int(num)
#     match num:
#         case (7):
#             numerology = "prime number"
#         case (42):
#             numerology = "answer for everything"
#         case (666):
#             numerology = "devil number"
#         case _:
#             numerology = "just a number"
#     return numerology


def normalize_url(text) -> str:
    """
    the function does normalization
    of https-address string
    """
    if text[0:8] == "https://":
        normalized_str = text
    elif text[0:7] == "http://":
        normalized_str = f"https://{text[7:]}"
    else:
        normalized_str = f"https://{text}"
    return normalized_str

# print(normalize_url("АДРЕС"))


def string_or_not(smth) -> str:
    """
    The function checks if the parameter is str
    returns "yes" or "no"
    """
    if isinstance(smth, str):
        return "yes"
    return "no"

# print(string_or_not(""))


def is_leap_year(year: int) -> bool:
    """
    The function checks
    if the year is leap
    """
    answer = ((year % 400) == 0) or \
             ((year % 4) == 0) and \
             (not (year % 100) == 0)
    return answer

# print(is_leap_year(2001))


def has_upper_case(text: str) -> bool:
    """
    The function checks if the string
    contains Uppercase letters
    """
    answer = (text.lower() != text)
    return answer

# print(has_upper_case("вап4567гоШГНЕП"))


def get_age_difference(birthyear_1: int, birthyear_2: int) -> str:
    """
    The function takes 2 years
    returns an age difference
    """
    age_difference = abs(birthyear_1 - birthyear_2)
    get_age_difference_result = f"The age difference is {age_difference}"
    return get_age_difference_result

# print(get_age_difference(2018, 2001))


def letter_multiply(text: str, symbol: str, times: int) -> str:
    """
    The function takes string, symbol, repetitions
    returns the string with repeated sym * n-times
    """
    letter_multiply_result = text.replace(symbol, symbol * times)
    return letter_multiply_result

# print(letter_multiply("python", "py", 3))


def trim_and_repeat(text, offset=0, times=1):
    """
    The function takes 3 params:
    str, offset (default 0), repetitions (default 1)
    returns the left-erased string and repeated n-times
    """
    trimmed_repeated_text = (text[offset:]) * times
    return trimmed_repeated_text

# print(trim_and_repeat("python", 1, 1))


def get_hidden_card(card_number_str, index=4):
    """
    The function takes a credit card number (16 digits) as a string
    returns a hidden number displaying on the site:  ****5589
    amount of * is 3rg parameter (default 4)
    """
    hidden_card_str = f'{"*" * index}{card_number_str[12:16]}'
    return hidden_card_str

# print(get_hidden_card('1234567812345678', 3))


def truncate(str, index):
    """
    The function returns substring
    from 0 to index with "..."
    """
    result_str = f'{str[0:index]}...'
    return result_str

# print(truncate('hexlet', 2))


def sum_module(nu1, nu2):
    """
    The function to show sum of modules
    of 2 values
    """
    result = abs(nu1 + nu2)
    return result

num1 = -1
num2 = 2
# print(sum_module(num1, num2))


def print_few_times(string, num):
    """
    The function prints the string n-times
    with concatination
    """
    result_string = str(num) + " " + str(string)
    return result_string

# print(print_few_times("times", 3))


def print_greetings(str1, str2, str3):
    """
    The function prints
    the сoncatinated f-string
    """
    result_string = f'{str1} {str2}?\n{str3}'
    return result_string


name = 'Arya'
line1 = "Do you want to eat,"
line2 = "Yes, I'm hungry, mom."
# print(print_greetings(line1, name, line2))


# tab - intent region
# shift+tab - detent region
# (len(string) // 2) - делит с округлением вниз

# value = 'Hexlet'
# value[::] = 'Hexlet'
# Вся строка
# value[:] = 'Hexlet'
# Вся строка
# value[::2] = 'Hxe'
# Нечетные по порядку символы
# value[1::2] = 'elt'
# Четные по порядку символы
# value[::-1] = 'telxeH'
# Вся строка в обратном порядке
# value[5:] = 't'
# Строка, начиная с шестого символа
# value[:5] = 'Hexle'
# Строка до шестого символа
# value[-2:1:-1] = 'elx'
# Все символы с предпоследнего до третьего в обратном порядке.
# От большего индекса к меньшему всегда нужно указывать шаг
