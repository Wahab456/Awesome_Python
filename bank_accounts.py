class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount    
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")    
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")    

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")    
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')   

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)         
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ☑️ \n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        # Add 5% interest to the deposit
        interest = amount * 0.05
        super().deposit(amount + interest)  # Call the base class's deposit method

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)        
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)    
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print (f'\nWithdraw interrupted: {error}')


# Create instances of the classes
Dave = BankAccount(1000, "Dave")
Sara = InterestRewardsAcct(2000, "Sara")
Blaze = SavingAcct(1500, "Blaze")

# Perform operations on the accounts
Dave.deposit(500)
Sara.deposit(100)
Blaze.withdraw(200)

Dave.transfer(300, Sara)
Sara.transfer(200, Blaze)
