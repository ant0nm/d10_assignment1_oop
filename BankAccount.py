class BankAccount:
    """ A class representing a simple bank account """

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "Your Current Balance: {}\nYour Interest Rate: {}".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def gain_interest(self):
        self.balance *= (1 + self.interest_rate)

# test 1 <creating an instance of BankAccount>
ba1 = BankAccount(500, 0.1)
print("Printing out attributes of your object:")
print(ba1.balance)
print(ba1.interest_rate, end='\n\n')

# test 2 <printing our object>
print("Printing your bank account info:")
print(ba1, end='\n\n')

# test 3 <adding money to your account>
print("Depositing 100 to your account:")
ba1.deposit(100)
print(ba1, end='\n\n')

# test 4 <withdrawing money from your account>
print("Withdrawing 50 from your account:")
ba1.withdraw(50)
print(ba1, end='\n\n')

# test 5 <adding interest to account>
print("Adding {:.0f}% interest to your account:".format(ba1.interest_rate*100))
ba1.gain_interest()
print(ba1)
