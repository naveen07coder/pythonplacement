class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amnt):
        self.balance = self.balance+amnt
        return(self.balance)

    def withdrawl(self, amnt):
        self.balance = self.balance-amnt
        return self.balance

Naveen = Bank()
Naveen.deposit(100)
Naveen.deposit(100)
print(Naveen.deposit(300))
print("Withdrawl = ",Naveen.withdrawl(200))