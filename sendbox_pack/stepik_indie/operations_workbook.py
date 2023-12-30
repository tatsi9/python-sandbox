from math import trunc, floor, ceil

"""
ФУНКЦИИ ОКРУГЛЕНИЯ

trunc - отсекает дробную часть от числа
Так же работает int(), только не надо подключать модуль
floor - округляет числа в сторону минус бесконечности (вниз)
ceil - округляет числа в сторону плюс бесконечности (вверх)
round - встроенная функцией для "школьного округления", НО:
    Числа от 0 до 0.5 (не включая 0.5) - round округляет вниз.(алгоритм ниже)
    Числа 0.5 - round округляет до ближайшего целого чётного числа.
"""

print(trunc(2.5))  # 2

print(floor(2.5))  # 2
print(floor(-2.5))  # -3

print(ceil(2.5))  # 3
print(ceil(-2.5))  # -2

print(round(5.3))  # 5
print(round(6.7))  # 7
print(round(12.5))  # 12
print(round(13.5))  # 14

N = float(input())
if N - int(N) < 0.5:
    print(floor(N))
else:
    print(ceil(N))


def show_all_numbers(num: int):
    number_3 = num % 10
    number_2 = num // 10 % 10
    number_1 = num // 100 % 10
    return number_1, number_2, number_3


print(show_all_numbers(123))


"""
Варианты использования функции input()
"""
# a = input() - если необходимо ввести строку и сохранить ее в переменную а
# a = int(input()) - если необходимо ввести целое число и сохранить его в переменную а
# a = float(input()) - если необходимо ввести вещественное число и сохранить его в переменную а
# a,b = map(int,input().split()) - если необходимо ввести два целых числа в одну строку через пробел
# a,b,c = map(float,input().split()) - если необходимо ввести три вещественных числа в одну строку через пробел
# a = list(map(int, input().split())) - сразу запись в лист
# a = list(map(int, input().split(,)))

"""
Дополнительные функции print()
"\n" - (newline) перевод каретки
"\t" - (tab) отступ
"""
    # print(1, 2, 3, 4, sep=',')
    # print('hello', end='\n') print(1, 2, 3, end='!') #не будет переноса в конце


print(see_walrus := 'Look at my walrus, my walrus is amazing')  # присвоение внутри принта

print(see_walrus[:11] + 'horse')

# (count := len(words)) > 3:
