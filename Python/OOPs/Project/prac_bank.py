class bank:
    def __init__(self,account_holder,account_number,cust_id):
        self.aaccount_holder = account_holder
        self.account_number = account_number
        self.branch_name = cust_id
        self.initial_amount = 0
        
    def deposit(self,add_amount):
        
        if add_amount > 0:
            self.initial_amount = self.initial_amount + add_amount
            print(f"Rs.${add_amount} amount added successfully. \n After Deposit, the Total Amount = ${self.initial_amount}")
    
    def withdraw(self,withdraw_amount):
        if withdraw_amount <= self.initial_amount and withdraw_amount > 0:
            self.initial_amount -= withdraw_amount
            print(f"{self.aaccount_holder} withdraw ${withdraw_amount} from  account . \n After withdrawing, The rest amount : ${self.initial_amount} \n \t ****{self.aaccount_holder} Withdraw amount successfully.")
        else:
            print("Insufficient Amount.")   
    
    def Check_balance(self):
        print(f"Amount in your account : ${self.initial_amount}")
    
account_holder = input("Enter account holder name : ")
account_number = input("Enter account holder number : ")
cust_id = input("Enter customer ID : ")
ac1 = bank(account_holder,account_number,cust_id)

while 1:
    print("\t\t**********Welcome to our Bank Management Machine ************")
    print('''
          1) Deposit Amount 
          2) Withdraw Amount
          3) Check Balance
          4) Exist from the bank account''')
    step = int(input("Enter choice[1-4] to do some action within your account : "))
    if step == 1:
        add_amount = eval(input("Enter amount to deposit(in $) : "))
        ac1.deposit(add_amount)
    elif step == 2:
        withdraw_amount = eval(input("Enter amount to withdraw(in $) : "))
        ac1.withdraw(withdraw_amount)
    elif step == 3:
        ac1.Check_balance()
    elif step == 4:
        print("Thank You! for exist from the bank.....")
        break
    else:
        print("Invalid CHOICE: Please enter no. from 1-4....")