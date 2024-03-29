

print("  /~~~\\", " //^ ^\\\\", "(/(_*_)\\)", "_/''*''\\_", "(/_)^(_\\)", sep="\n")

"""
Электронные часы показывают время в формате h:mm:ss,
то есть сначала записывается количество часов в диапазоне от 0 до 23,
потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
Программа получает на вход число n - количество секунд, которое прошло с начала суток.
Выведите показания часов, соблюдая формат.
"""

# n = int(input())
# h = (n % (24*60*60)) // 3600
# m = ((n % (24*60*60)) - h * 3600) // 60
# s = ((n % (24*60*60)) - (h * 3600) - (m * 60))
# print(f"{h}:{m // 10}{m % 10}:{s // 10}{s % 10}")

"""
У Олега в банке есть n евро. Он хочет снять всю сумму наличными.
Номиналы еврокупюр равны 1, 5, 10, 20, 100.
Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
"""

# n = int(input())
# sotki = n // 100
# n = n - (sotki * 100)
# dvadtsatki = n // 20
# n = n - (dvadtsatki * 20)
# desiatki = n // 10
# n = n - (desiatki * 10)
# piatiorki = n // 5
# n = n - (piatiorki * 5)
# cash_items = sotki + dvadtsatki + desiatki + piatiorki + n


"""
Напишите программу, которая на вход получает координаты двух клеток 
шахматной доски и выводит сообщение, являются ли эти клетки одного цвета. 
Столбцы на шахматной доске обозначаются буквами (abcdefgh) для колонок, цифрами (1-8) для сток.
Программа должна выводить YES, когда клетки одного цвета, NO - разного. 
"""

x = "a1"
y = "b2"

xx = int(x[1])
yy = int(y[1])
evens = ["b", "d", "f", "h"]

if x[0] in evens:
   xx += 2
else:
    xx += 1

if y[0] in evens:
   yy += 2
else:
    yy += 1

if (xx % 2) == (yy % 2):
    print("YES")
else:
    print("NO")


# price_ticket = 20 if age >= 18 else 8  # тернарная запись
