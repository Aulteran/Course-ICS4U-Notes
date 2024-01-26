#OOP Crypto

class Bank_acc:

    customer_info = {'Julie100@gmail.com':123}
    
    def __init__(self,name,email,password,balance):
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance
        self.customer_info[email] = password  

    def deposit(self,deposit):
        return (self.balance + deposit)

    def withdraw(self,nb1,withdraw):
        if nb1 < withdraw:
            return  "You have withdrawn more than your total balance"
        self.balance = nb1 - withdraw
        return self.balance 

    def new_member_added(self,nb1):
        return nb1 + 200
        

    def account_type(self):
        return ("WizCoin Basic")
        
    def __repr__(self):
        return '( user information{},{},{})'.format(self.name,
                                                            self.email,
                                                            self.password,
                                                            self = self)

class Bank_acc_plus(Bank_acc):
    def __init__(self,name,email,password,balance,):
        super().__init__(name,email,password,balance)
    def start_up(self):
        self.balance + 20
    def deposit(self,nb1,deposit):
        return self.balance + (deposit * 1.2)
    def account_type(self):
        return ("WizCoin plus")
    


bob = Bank_acc("Bob","Bobanator@gmail.com",134,200)
nb1 = bob.deposit(500)
nb2 = bob.new_member_added(nb1)
print(bob. account_type(),bob.name, "new balance is: ", nb2  )

julie = Bank_acc("Julie","Julie100@gmail.com",123,100)
nb = julie.withdraw(100,150)
print(julie.account_type(),julie.name, "new balance is: ", nb )

stan = Bank_acc('Stan','Stantheman@gmail.com',321,250)
nb1 = stan.deposit(500)
nb2 = stan.withdraw(nb1,400)
print(stan.account_type(),stan.name, "new balance is: ", nb2)

print(stan)

beth = Bank_acc_plus('Beth','bethlovesmethjustkidding@gmail.com',135,300)
nb1 = beth.start_up()
nb2 = beth.deposit(nb1,100)
print(beth.account_type(),beth.name, "new balance is: ", nb2)

        
