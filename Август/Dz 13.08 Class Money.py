class MyMoney:
    def __init__(self, lastname,
                 firstname,
                 balance):
        self.lastname = lastname
        self.firstname = firstname
        self.balance = balance if balance >=0 else 0

    def balance_up(self, summa):
        print("Вы пополнили баланс на:", summa)
        self.balance += summa

    def balance_down(self, summa):
        print("Вы убавили баланс на:", summa)
        if summa <= self.balance:
            self.balance -= summa
        return None

    def get_balance(self):
        print("Баланс на кошельке:", self.balance)

money = MyMoney("Муркин", "Вася", 400)

print(money.balance_up(50), money.get_balance())
print(money.balance_down(100), money.get_balance())
print(money.balance_down(450), money.get_balance())




