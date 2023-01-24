class BankAccount:
    
    def __init__(self, int_rate , balance  ): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -=5
            print("insufficient funds, charging a 5$ fee")
            return self
        else: 
            self.balance = self.balance - amount
            return self
    
    def display_account_info(self):
        print (f"balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance * (1+ self.int_rate)
        return self
    
    # @classmethod
    # def bank_account_info(self):
    #     print(BankAccount.in)

adrian_checking = BankAccount (.05,500)
xiomara_checking = BankAccount (.1, 100)
# checkingAccount = BankAccount()
# checkingAccount.deposit(10)
# checkingAccount.display_account_info()
# checkingAccount.withdraw(511)
# checkingAccount.display_account_info()
# checkingAccount.yield_interest()
# checkingAccount.display_account_info()


adrian_checking.deposit(10).deposit(5).deposit(5).withdraw(100).yield_interest().display_account_info()
xiomara_checking.deposit(20).deposit(10).withdraw(10).withdraw(10).withdraw(10).withdraw(10.).yield_interest().display_account_info()