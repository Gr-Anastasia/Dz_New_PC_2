def summa(N, M):
    num = 0
    x = 0
    for i in range (0, N):
        num = num * 10 + M
        x += num
        # print(num)
    print("Сумма разрядов: ", x)

summa(N = int(input("Введите количество: ")), M = int(input("Введите разряд: ")))


# y = int(input('Число:  '))
# x = 0
# for i in range(0, y):
#     x = x*10+y
#     print(i, y, x)

# Используя только цикл for, найдите сумму N разрядов, состоящих только из цифр, равных M.