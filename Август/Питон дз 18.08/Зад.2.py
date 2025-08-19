def revers_number(N):
    for i in range(N, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

revers_number(N = int(input("Введите число: ")))

# в обратном порядке только те числа из диапазона от 0 до N, которые одновременно делятся на 3 и 5.