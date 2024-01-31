class BankAccount:
    def __init__(self,account_num,account_holder,balance = 0):
        self.account_holder = account_holder 
        self.account_number = account_num
        self.balance = balance
    def deposit(self,add_money):
        self.balance += add_money
        print('*'*60)
        print(f"${add_money} amount added successfully, and total amount = ${self.balance}")
        print('*'*60)
    
    def withdraw(self,withdraw_amount):
        # self.balance -= widrw_amnt
        # return f"After withdrawing , rest amount : {self.balance}"
        if withdraw_amount <= self.balance and withdraw_amount > 0:
            self.balance -= withdraw_amount
            print('*'*60)
            print(f"{self.account_holder} withdraw ${withdraw_amount} from  account . \nAfter withdrawing, The rest amount : ${self.balance} \n\"{self.account_holder}\" Withdraw amount successfully.")
            print('*'*60)
        else:
            print('*'*60)
            print("Insufficient Amount.")
            print('*'*60)
        
    def check_balance(self):
        print('*'*60)
        print(f"""\tAccount Holder : {account_holder}\n\tAccount Number : {account_number}\n\tNet balance    : ${self.balance}""") 
        print('*'*60)

        
class SavingAccount(BankAccount):
    def __init__(self,account_num,account_holder,balance = 0, interest_rate = 0.02):
        self.interest_rate = interest_rate 
        super().__init__(account_num,account_holder,balance)
    def add_interest(self):
        interest_amount = self.interest_rate * self.balance
        self.balance += interest_amount
        print('*'*60)
        print(f"Interest added : {interest_amount}\nNew balance : {self.balance}")
        print('*'*60)
        
class CheckingAccount(BankAccount):
    def __init__(self,account_num,account_holder,balance = 0,overlimit_draft = 100):
        super().__init__(account_num,account_holder,balance)
        self.overlimit_draft = overlimit_draft
             
    def withdraw(self,amount):
        if amount <= self.balance + self.overlimit_draft:
            self.balance -= amount
            print('*'*60)
            print(f"{self.account_holder} withdraw ${amount} from  account . \nAfter withdrawing, The rest amount : ${self.balance} \n\"{self.account_holder}\" Withdraw amount successfully.")
            print('*'*60)
        else:
            print("Insufficient Amount ")
            
account_holder = input("Enter Account holder Name : ")   
account_number = eval(input("Enter account number : "))
amount = 0


accounts = []
count = 0
while 1:
    print('*'*60)
    print('''
      Welcome to GLA Bank
      which account you want to open 
      1. Saving Account
      2. Checking Account
      3. Current Account
      4. Exit
      ''')
    print('*'*60)
    choice = int(input("Enter choice 1/2/3/4 : "))
    if choice == 1:
        save = SavingAccount(account_number,account_holder,balance = 0, interest_rate=0.02)
        accounts.append(save)
        print('*'*60)
        print("\tYou want to do some action with Saving Account.......")
        print('*'*60)
        while 1: 
            print('\tMenu')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            print('4. Add Interest')
            print('5. Exit from saving account....')
            print('*'*60)
            choice = int(input("Enter choice from 1-5 : "))
            if choice == 1:
                add_money = eval(input("Enter amount(in $) to deposit in your account : "))
                save.deposit(add_money)
            elif choice == 2:
                withdraw_amt = eval(input("Enter amount(in $) to withdraw from your account : "))
                save.withdraw(withdraw_amt)
            elif choice == 3:
                save.check_balance()
            elif choice == 4:
                save.add_interest()
                
            elif choice == 5:
                print("Thank You! for exist from the saving account.....")
                break
            else:
                print("Invalid CHOICE: Please enter no. from 1-4....")
    elif choice == 2:
        check = CheckingAccount(account_number,account_holder,balance = 0,overlimit_draft = 100)
        accounts.append(check)
        print('*'*60)
        print("\tYou want to do some action with Checking Account.......")
        print('*'*60)
        while 1: 
            print('Menu')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            print('4. Exit from checking account....')
            choice = int(input("Enter choice from 1-4 : "))
            if choice == 1:
                add_money = eval(input("Enter amount(in $) to deposit in your account : "))
                check.deposit(add_money)
            elif choice == 2:
                withdraw_amt = eval(input("Enter amount(in $) to withdraw from your account : "))
                check.withdraw(withdraw_amt)
            elif choice == 3:
                check.check_balance()
            elif choice == 4:
                print("Thank You! for exist from the checking account.....")
                break
            else:
                print("Invalid CHOICE: Please enter no. from 1-4....")
    elif choice == 3:
        current = BankAccount(account_holder,account_number,amount)
        accounts.append(current)
        print('*'*60)
        print("\tYou want to do some action with Current Account.......")
        print('*'*60)
        while 1: 
            print('Menu')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            
            print('4. Exit from current account....')
            choice = int(input("Enter choice from 1-4 : "))
            if choice == 1:
                add_money = eval(input("Enter amount(in $) to deposit in your account : "))
                current.deposit(add_money)
            elif choice == 2:
                withdraw_amt = eval(input("Enter amount(in $) to withdraw from your account : "))
                current.withdraw(withdraw_amt)
            elif choice == 3:
                current.check_balance()
            elif choice == 4:
                print("Thank You! for exist from the saving account.....")
                break
            else:
                print("Invalid CHOICE: Please enter no. from 1-4....")
    elif choice == 4:
        print("Thank You! for exist from the current account.....")
        break
    else:
        print("Invalid CHOICE: Please enter no. from 1-4....")
