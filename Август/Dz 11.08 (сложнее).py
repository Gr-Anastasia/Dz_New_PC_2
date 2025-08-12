class Human:
    def __init__(self, l, h, hd, g, c, s, e):
        self.leg = l
        self.hand = h
        self.head = hd
        self.gender = g
        self.hair_color = c
        self.height = s
        self.eyes = e

    def facts(self):
        print("Самый популярный цвет глаз в России - это серый")

# Средний человек в России
    leg = 2
    hand = 2
    head = 1
    gender = "girl"
    hair_color = "Dark brown"
    height = 165
    eyes = "gray"

Nastya = Human(2, 2, 1, 'girl', 'dark-red', 170, 'green')

def girl_Nast():
    print("Это девочка Настя:")
    print(Nastya.leg)
    print(Nastya.hand)
    print(Nastya.head)
    print(Nastya.gender)
    print(Nastya.hair_color)
    print(Nastya.height)
    print(Nastya.eyes)

girl_Nast()
Nastya.facts()

