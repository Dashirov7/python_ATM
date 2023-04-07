class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Операция выполнена успешно. Ваш баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Ошибка: недостаточно средств на балансе")
        else:
            self.balance -= amount
            print(f"Операция выполнена успешно. Ваш баланс: {self.balance}")

    def check_balance(self):
        print(f"Ваш баланс: {self.balance}")
