class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    def __del__(self):
        print("Account deactivated")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance - amount >= self.min_balance):
            self.balance -= amount
        else:
            print("Sorry, you don't have enough balance for this transaction!")

    def statement(self):
        print("Account Balance: Rs.{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account: Balance Rs.{}".format(self.name, self.balance)
    
