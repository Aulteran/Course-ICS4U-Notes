'''
Author: Aadil Hussain
Built on: Python 3.11.7
'''

# Final Exam ICS4U Instructions
# There is a new cryptocurrency called wizCoin that wishes for
# you to build the basic back-end to their online program
#
# Full Assignment Instructions are included in README.md file

# PLACE CODE HERE - MAKE SURE TO CHECK ASSERTIONS AND NAME ATTRIBUTES AND BEHAVIOURS EXACTLY AS NAMED IN THE TEST_ONE FILE. 

class BankAccount():
    '''WizCoin Basic Bank Account'''
    def __init__(self, name, email, pwd, bal):
        self.account_type = "WizCoin Basic"
        self.name = name
        self.email = email
        self.user_id = (self.name, self.email)
        self.password = pwd
        self.balance = bal
        self.denied = 0 # amount of times client has been denied

        print(f"Account created with ${self.balance}")

    def withdraw(self, amt, pwd):
        '''Allows client to withdraw money'''
        if pwd != self.password:
            print("Wrong Password! Access Denied.")
            self.denied += 1
            return
        if self.balance >= amt:
            self.balance -= amt
            print("Withdrawal Success")
            return
        print("Insufficient Funds")
        self.denied += 1

    def deposit(self, amt, pwd):
        '''Allows client to deposit money'''
        if pwd != self.password:
            print("Wrong Password! Access Denied.")
            self.denied += 1
            return
        if amt < 1:
            print('Deposit must be greater than 1 WizCoin')
            self.denied += 1
            return
        self.balance += amt
        print(f"Deposit Successful of {amt}\nNew Bal: {self.balance}")

    def new_member(self):
        '''Adds 100 WizCoin if client is new'''
        self.balance += 100
        print(f"New client deposit of 100 made\n Total Bal:{self.balance}")

class BankAcountPlus(BankAccount):
    '''WizCoin Plus Bank Account'''
    def __init__(self, name, email, pwd, bal):
        super().__init__(name, email, pwd, bal)
        self.account_type = "WizCoin Plus"
        startup_fee = 20
        self.balance -= startup_fee
        print("WizCoin Plus Startup fee of 20 charged")
        print(f"New Bal: {self.balance}")
    
    def deposit(self, amt, pwd):
        '''Allows client to deposit money'''
        super().deposit(amt, pwd)
        bank_contribution_amt = amt * 0.2 # Bank Contributes +20% to all deposits
        self.balance += bank_contribution_amt
        print(f"Bank has deposited {bank_contribution_amt}")
