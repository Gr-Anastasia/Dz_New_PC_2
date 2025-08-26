stroka = 'Хмурый вечер середины лета'
stroka2 = 'In the hole in the ground lived a hobbit'
a = 73
b = 95
stroka3 = 'В Ереване'
stroka4 = '456'
stroka5 = '6 - (12 * (2+3)/(5+6)))'


# def cut_1():
#     print(stroka[2])
#     print(stroka[-2])
#     print(stroka[:5])
#     print(stroka[:-2])
#     print(stroka[1::2])
#     print(stroka[0::2])
#     print(stroka[::-1])
#     print(stroka[::-2])
#     print(len(stroka))

# def ex_2():
#     space = stroka.split()
#     distant = len(space)
#     print(distant)

# def ex_3():
#     y = len(stroka)
#     o = 0
#     o += y // 2
#     part_1 = stroka[:o]
#     part_2 = stroka[o:]
#     stroka_2 = part_2 + part_1
#     print(stroka_2)

# def ex_6():
#     fin1 = stroka2.find('h')
#     fin2 = stroka2.rfind('h')
#     fin_str = stroka2[:fin1] + stroka2[fin2+1:]
#     print(fin_str)

# def ex_16():
#     summa = a + b
#     stars = a * b
#
#     s = f'{a} + {b} = {summa}'
#     s2 = f'{a} * {b} = {stars}'
#
#     print("Это сумма: ", s)
#     print("Это произведение: ", s2)
#
# def ex_18():
#     low = stroka3.lower()
#     print(low.count('е'))
#
# def ex_7(str):
#     a = []
#     for i in range(len(str)):
#         x = str[i::-1]
#         a.append(x)
#     a.reverse()
#     print(a)

def ex_8():
    cont_bracket = 0
    for i in stroka5:
        if i == '(' or i == ')':
            cont_bracket += 1
    if cont_bracket % 2 == 0:
        couple = cont_bracket // 2
        print(f"Скобки расставлены правильно. Количество пар: {couple}")
    else:
        missed_bracket = 1
        print(f"Скобки расставлены неправильно. Количество скобок без пары: {missed_bracket}")

# cut_1()
# ex_2()
# ex_3()
# ex_6()
# ex_16()
# ex_18()
# ex_7(stroka4)
ex_8()