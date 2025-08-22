spisok = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

def cycle_numbers():
    num = None
    for i in spisok:
        x = spisok.count(i)
        if x > 1:
            num = i
    print(num)

cycle_numbers()
