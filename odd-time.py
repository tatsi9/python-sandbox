from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
        23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
        43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(3):
    right_this_minute = datetime.today().minute
    randomTime: int = random.randint(1,60)
    if right_this_minute in odds:
        print ("This minute seems a little odd.")
    else:
        print ("That's not an odd minute.")
    print ("Time to the next review:", randomTime)
    time.sleep(randomTime)

# Помимо обычных операторов сравнения,
# в Python имеется несколько собственных «супероператоров»,
# один из которых in - проверяет, находится ли что-то одно внутри другого.


if datetime.today().weekday() == 5:
    print("Party!!!")
elif datetime.today().weekday() == 6:
    print("Recover.")
else:
    print("Work, work, work :(")

#for i in "hi":
#    print (i)

# tab - intent region
# shift+tab - detent region


