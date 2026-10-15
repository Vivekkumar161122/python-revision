class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Champa", 100_000)

print(acc1.name, acc1.get_balance())
