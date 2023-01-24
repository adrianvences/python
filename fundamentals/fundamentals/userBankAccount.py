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
    
class User:
    def __init__(self, name , email  ): 
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate = 0.02, balance = 100)]

    def make_deposit(self,amount,acc_num):
        self.account[acc_num-1].deposit(amount)
        return self
    def make_withdraw(self,amount,acc_num):
        self.account[acc_num-1].withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.name,self.email)
        for i in range (len(self.account)):
            self.account[i].display_account_info()
        return self
    def add_bank_account(self,int_rate , balance):
        self.account.append (BankAccount(int_rate , balance ))
        return self

        



    # def example_method(self):
    #     self.account.deposit(100)		# we can call the BankAccount instance's methods
    # print(self.account.balance)		# or access its attributes


user1 = User ("adrian","adrian@gmail.com")

user1.make_deposit(20,1).make_withdraw(30,1).add_bank_account(.05,100).make_deposit(50,2).display_user_balance()
# adrian_checking = BankAccount (.05,500)
# xiomara_checking = BankAccount (.1, 100)


# adrian_checking.deposit(10).deposit(5).deposit(5).withdraw(100).yield_interest().display_account_info()
# xiomara_checking.deposit(20).deposit(10).withdraw(10).withdraw(10).withdraw(10).withdraw(10.).yield_interest().display_account_info()