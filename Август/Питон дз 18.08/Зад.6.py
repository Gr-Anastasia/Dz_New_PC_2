spisok = [1, 2, 3, 4, 5, 6]

def count_sp_1(num):
    sp_cont = 0
    for i in spisok:
        if i is not None:
            sp_cont += 1
    return i

print("Всего элементов в списке: ", count_sp_1(spisok))

# Посчитайте, сколько в нем различных элементов, не изменяя самого списка.
