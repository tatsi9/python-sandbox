word = "bottles"

for beer_num in range(5, 0, -1):
    print(beer_num, word, " of beer on the wall.")
    print(beer_num, word, " of beer.")
    print("Take one down.")
    print("Pass it around.")

    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_beer_num = beer_num - 1

        if new_beer_num == 1:
            word = "bottle"
            print(new_beer_num, word, " of beer on the wall.")
    print()

