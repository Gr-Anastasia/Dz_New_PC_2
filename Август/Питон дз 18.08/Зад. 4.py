spisok = [1, 2, 3, 4, 5]

def cycle_numbers(num):
    a = [5, 4, 3, 2, 1]
    for j in range(len(num)):
        for i in range(0, len(num)-1):
            if a.index(num[i])>a.index(num[i+1]):
                num[i], num[i+1]=num[i+1], num[i]
    return num

cycle_numbers(spisok)
print(spisok)

# СПРОСИТЬ АРТУРА МОЖНО ЛИ ТАК