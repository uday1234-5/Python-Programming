class bank:
    def __init__(self,account_holder,account_num,initial_balance = 0):
        self.account_holder = account_holder 
        self.account_number = account_num
        self.initial_balance = initial_balance
        
        
    def deposit(self,add_money):
        self.initial_balance += add_money
        return f"Rs.{add_money} amount added successfully, and total amount = {self.initial_balance}"
    
    def withdraw(self,widrw_amnt):
        self.initial_balance -= widrw_amnt
        return f"After withdrawing , rest amount : {self.initial_balance}"
        
    def check_balance(self):
        print(f"Net balance : {self.initial_balance}") 

account_holder = input("Enter Account holder Name : ")   
account_number = eval(input("Enter account number : "))
amount = 0
c1 = bank(account_holder,account_number,amount)

while 1:
    print("""
    1. Deposit Amount 
    2. Withdraw Amount 
    3. Check Balance 
    4. Exist"""  )
    
    choice = input("Enter choice from [1-4] : ")   
    if choice == '1':
        add_amount = int(input("Enter amount to deposit : "))
        print(c1.deposit(add_amount))
    
    elif choice == '2':
        
        with_draw = int(input("Enter amount to withdraw : "))
        print(c1.withdraw(with_draw))
    elif choice == '3':
        c1.check_balance()
    elif choice == '4':
        print("Thank You! Exit the program")
        break
    else:
        print("Invalid choice! Please Enter the choice from 1-4")


