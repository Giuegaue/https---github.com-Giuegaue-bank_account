class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance" + ' $' + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

gorilla = BankAccount(0.21, 0)
monkey = BankAccount(0.21, 0)
gorilla.deposit(20).deposit(10).deposit(140).withdraw(4000).yield_interest().display_account_info()
monkey.deposit(40000).deposit(12000).withdraw(1).withdraw(12).withdraw(4000).withdraw(4).yield_interest().display_account_info()
