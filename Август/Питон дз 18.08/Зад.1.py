def age (x,y):
    age_sister = x+y
    if x==y:
        print("Сестра не может быть ровесницей брата")
        return None
    return age_sister

print(age(6, 6))
print(age(7, 2))
print(age(-7, 2.0))

# ДОБАВИТЬ  СИСТЕМУ УРАВНЕНИЙ