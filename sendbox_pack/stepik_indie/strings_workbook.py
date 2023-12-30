"""
МЕТОДЫ СТРОК:

.lower() - делает все буквы маленоькими
.upper() - делает все буквы большими
.title() - каждое слово в строке - с заглавной буквы
.capitalize() - делает первую букву строки заглавной
.swapcase() - инвертирует регистр букв

.count(sub, 2, 7) - считает сколько сабов в 2-7 символах стринги
.find(sub, 5) - вернет индекс вхождения, где найден саб после 5 символа в строке и -1, если не найдено
.rfind(sub, 5) - как find но справа-налево
.index('w', 5)) - как find, возвращает индекс первого совпадения, но вернет ошибку если не найдено

.replace('l', '?', 2)) - заменяет старый саб на новый  н-раз
.split(', ', maxsplit=2)) # разбивает строку в массив по разделителю - по умолчанию " ", maxsplit - макс кол-во зразбиений
    len(string.split()) - длина списка после разбиения - сколько слов в строке
symbol.join(words) - объединяет масситв в строку по разделителю symbol

.startswith(sub, 0, 5) - возвращает true если строка начинается с саба - по индексам начала и конца проверки
.endswith(sub) - возвращает true если строка кончается на саб - по индексам начала и конца проверки

.islower() - true если строка непустая и все символы строчные (знаки и цифры - игнор)
.isupper() - ...все символы заглавные (знаки и цифры - игнор)
.isdigit() - ...все символы цифры (знаки - НЕ игнор)
.isalpha() - ...все символы буквы (знаки и цифры - НЕ игнор)
.isalnum() - ...все символы буквы и цифры (знаки - НЕ игнор)
.istitle() - ...первые символы слов - заглавные (знаки и цифры - НЕ игнор)

.ljust(10, '-') - доводит строку до длины с указанным символом после строки
.rjust(10, '-') - как ljust тока с другой стороны
.center(13, '?') - как ljust тока добавляет символы с двух сторон
.zfill(3)) - как ljust тока с дополняет нулями

.strip(sub) - удаляет саб в начале и конце строки
.rstrip(sub) - удаляет саб только с правого края
.lstrip(sub) - ...c левого края

.partition(sep) - разбивает строку по разделителю, дает массив до, разделитель и после
.rpartition(sep) - ...такой же, но по последнему разделителю
"""

string = "Hello, world!"
sym = "_"
arr = ["Hello", "arrays"]

print(string.count("ll", 2, 7))
print(string.find('o', 5))
print(string.rfind('hell'))
print(string.index('w', 5))
print(string.replace('l', '?', 2))
print(string.split())
print(sym.join(arr))
print(string.startswith("Hello"))
print(string.endswith("Hello"))

print(string.ljust(15, sym))
print(string.rjust(15, sym))
print(string.center(16, sym))

print(string.strip("Hell"))
print('321232321Hello31121312'.strip('123'))
print(string.partition(" "))


name = "Максим"
mid_name = "Геннадьевич"
balance = 100

text = "Дорогой {0} {1}, баланс Вашего лицевого счёта составляет {2} руб.".format(name, mid_name, balance)
print(text)

a = "Выхухоль"

text = "Что Вы сказали? {word}? Какое интересное слово".format(word = a)
print(text)

# a = "A"
# b = "B"
# c = 1/2
# e = 123456
# number_pi = 3.141592653589793
#
#
# print(f"{a} и {b} cидели на трубе")
# print(f"{a  = }, {b = }")
#
#
# print(f'{c = :.3f}') # вывести ровно три знака после запятой для любого числа.
# print(f'{number_pi:.6f}')
# print(f'{e:8d}')
# print(f'{e:,d}') # вставка символов как разделитель (можно _ и ,)
# print(f'{e:08d}') # нули перед числом до 8 символов
#
# print(f'Число\tКвадрат\tКуб')
# for x in range(1, 5):
#    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')
#
#
# number = 12345.6789
# print(f"Число {number = }")
# print(f"|{number:25}|")
# print(f"|{number:<25}|")
# print(f"|{number:>25}|")
# print(f"|{number:^25}|")
# print('-'*25)
# text = "Python 3.10"
# print(f"Строка {text = }")
# print(f"|{text:25}|")
# print(f"|{text:<25}|")
# print(f"|{text:>25}|")
# print(f"|{text:^25}|")
#
# number = 12345.6789
# print(f"Число {number = }")
# print(f"|{number:=<25}|")
# print(f"|{number:=>25}|")
# print(f"|{number:=^25}|")
# print('-'*25)
# text = "Python 3.10"
# print(f"Строка {text = }")
# print(f"|{text:-<25}|")
# print(f"|{text:!>25}|")
# print(f"|{text:?^25}|")
