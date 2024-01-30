[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/DIN6dZyp)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13565339)
# ICS_4U_hands_on

There is a new cryptocurrency called wizCoin that wishes for you to build the basic back-end to their online program. In this example, build class Bank_Account, in which you instantiate name, email, password, and balance. Store the email and password in an appropriate container when a new customer has been added using the class. Have separate methods within the Bank_Acount class for Deposit and Withdraw that allow the balance to change accordingly, and then prints out the new balance. NOTE: Withdraws cannot exceed the amount listed in the bank account, and Deposits cannot be less than 1 WizCoin.  Because it is a new company, the administration has decided to add 100 wizCoin to all new members. Also have a method called account_type that will output string ‘WizCoin Basic’ when run - make it a class variable. Also have a class variable called user_id that stores the customer name and email in a tuple

Class **Bank Account** 

**Attributes**	
-	Name 
-	Email 
-	Password 
-	Balance
-   Denied

**Behaviours**
-	Withdraw
-	Deposit
-	new_member_add


With your program, instantiate three different users:
1)	Bob – NEW MEMBER, Starting Balance is 200 wizCoin, deposits 500 wizCoin
2)	Julie – EXISTING MEMBER, Starting Balance is 100 wizCoin, tries to withdraw 150 wizCoin (deny her), withdraws 50 wizCoin
3)	Stan – NEW MEMBER, starting balance 250 wizCoin, deposits 500 wizCoin, withdraws 400 wizCoin

Make sure your program shows the user the updated balance total whenever a method is run.


4U ONLY – create a new class called Bank_Account_Plus - which inherits all the attributes and methods of the old class, but has a start up fee of 20 wizCoin. Your deposit method will add an additional 20% wizCoin to each deposit made. Change the account_type method to output WizCoin Plus

4U ONLY – instantiate one member with the Bank_Account_Plus class.
1)	Beth – NEW MEMBER, Starting Balance is 300 wizCoin, deposits 100 wizCoin.
