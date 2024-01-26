from solution import *

print ('Bob')

Bob = BankAccount('Bob','Bob@gmail.com','password',200)
Bob.new_member()
print (Bob.balance)
print (Bob.user_id)
Bob.deposit(500,'password')
print (Bob.balance)
print (Bob.account_type)


print ('\nJulie')

Julie = BankAccount ('Julie','Julie@gmail.com','password1',100)
Julie.withdraw(200,'password1')
Julie.withdraw(50,'password1')
print (Julie.balance)
print (Julie.denied)
print (Julie.account_type)

print ('\nStan')

Stan = BankAccount ('Stan','Stan@gmail.com','password2',250)
Stan.new_member()
Stan.deposit(500,'wrongpass')
Stan.deposit(500,'wrongpass')
Stan.deposit(500,'password2')
Stan.withdraw(400,'password2')
print (Stan.balance)
print (Stan.account_type)

print ('\nBeth')
Beth = BankAcountPlus ('Beth','Beth@gmail.com','password3',300)
Beth.new_member()
Beth.deposit(100,'password3')
print (Beth.balance)
print (Beth.user_id)
print (Beth.account_type)

def one_test():
    try:
        assert Bob.balance == 800
        assert Bob.account_type == 'WizCoin Basic'
        assert Bob.denied == 0
        assert Bob.user_id == ('Bob', 'Bob@gmail.com')
        assert Julie.denied == 1
        assert Julie.balance == 50
        assert Julie.account_type == 'WizCoin Basic'
        assert Stan.balance == 450
        assert Stan.account_type == 'WizCoin Basic'
        assert Stan.denied == 2
        assert Beth.balance == 500
        assert Beth.denied == 0
        assert Beth.user_id == ('Beth', 'Beth@gmail.com')
        assert Beth.account_type == 'WizCoin Plus'
        assert issubclass(BankAcountPlus,BankAcountPlus)

        print ('success')
    except (AssertionError):
        print ('failure')

one_test()
