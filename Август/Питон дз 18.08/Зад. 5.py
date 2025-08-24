spisok = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

def cycle_numbers(num):
    num = None
    for i in spisok:
        x = spisok.count(i)
        if x > 1:
            num = i
    return num

print(cycle_numbers(spisok))

# какое число в этом списке встречается чаще всего. Если таких чисел несколько, выведите любое из них.
