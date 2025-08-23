spisok = [1, 2, 3, 4, 5]

def cycle_number(num):
    end_num = num[-1]
    for i in range(len(num)-1, 0, -1):
        num[i] = num[i-1]
    num[0] = end_num

cycle_number(spisok)
print(spisok)





