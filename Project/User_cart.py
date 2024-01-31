# dct = {}
# total_items = int(input("Enter total no.items "))

# user_dct = {}
# for i in range(1,total_items+1):
#     item1 = input("Enter item name :")
#     quantity = input("Enter item quantity")
    
#     dct[item1] = quantity
    
# print(dct)

# def display_items(available_item):
    

# available_item = {'cofee':2,'Tea':3,'Toffee':5}
# display_items(ava)
# for x in available_item:
#     if x in dct:
#         user_dct.update(x)
# print(user_dct) 



"""
def display_available_items(dict):
    print("\t\tAvailable Items:")
    print(f"{'S.No.':<15}{'Item':<15}{'Quanity':<15}{'Cost/Item':<15}")
    for i,j in dict.items():
        print(f"{i:<15}{j['Item']:<15}{j['Quantity']:<15}{j['Cost/Item']:<15}")
    


availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}
display_available_items(availableItems)
CustomerName = input("Enter Customer Name ")
CustomerAddress = input("Enter Customer Address City/State ")
userdemand = {}
no_items = eval(input("Enter Number of Items"))
for i in range(no_items):
    item = input("Enter Item Purchased")
    quantity = eval(input("Enter Quantity"))
    userdemand[item] = quantity
print(userdemand)
usercart={}
print("\t\t Items Purchased:")
print(f"{'Item':<15}{'Quantity':<15}{'Total Cost':<15}")
for i in userdemand:
    for m,n in availableItems.items():
        if(i!= n['Item'] and userdemand[i]!=n['Quantity']):
            break
        else :
            print("Item not Exist or Quantity is not available")

    print(f"{i:<15}{userdemand[i]:<15}{userdemand[i]*0:<15}")
       """
       
       
       ##sir
       

def display_available_items(dct):
    '''
    Display all available items in the store
    '''
    print("\t\tAvailable Items:")
    print(f"{'S.No.':<15}{'Item':<15}{'Quanity':<15}{'Cost/Item':<15}")
    for index, row in dct.items():
        print(f"{index:<15}{row['Item']:<15}{row['Quantity']:<15}{row['Cost/Item']:<15}")
def display_user_cart(dct):
    '''
    Display all items in the cart
    '''
    print("\t\tItems in Cart:")
    print(f"{'S.No.':<15}{'Item':<15}{'Quanity':<15}{'Total Cost':<15}")
    for index, row in dct.items():
        print(f"{index:<15}{row['Item']:<15}{row['Quantity']:<15}{row['TotalCost']:<15}")
availableItems = {
1: {'Item': 'Biscuits'  , 'Quantity': 5 , 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35.0}, 
3: {'Item': 'Coffee'    , 'Quantity': 25, 'Cost/Item': 55.0},
4: {'Item': 'Chips'     , 'Quantity': 10, 'Cost/Item': 50.0},
5: {'Item': 'Cream'     , 'Quantity': 5 , 'Cost/Item': 30.0}}
display_available_items(availableItems)

# user demand for items
userDemand = {'Biscuits': 5, 'Chocolates': 100, 'Coffee': 25, 'Chips': 10, 'Cream': 5}
name = 'Amir'
address = 'Meerut'
distance =  15
deliveryCharge = 30
bill = 0
bill = 0
user_cart = availableItems.copy()
for it in userDemand:
    for i in availableItems.copy():
        if it ==  availableItems[i]['Item']:
            if userDemand[it] <= availableItems[i]['Quantity']:
                tt = userDemand[it] * availableItems[i]['Cost/Item']
                bill += tt
                availableItems[i]['Quantity'] -= userDemand[it]
                user_cart[i]['Quantity'] = userDemand[it]
                user_cart[i]['TotalCost'] = tt
            else:  
                print(f"Sorry, we don't have enough {it} in stock")
                user_cart.pop(i)
                break   
totalBill = bill + deliveryCharge
display_user_cart(user_cart)
print('Total Item Cost:', bill)
print('Total Bill Amount = Total Amount + delivery charge:', totalBill)
customer_details = {'Name': name, 'Address': address, 'Distance': distance, 'Delivery Charge': deliveryCharge, 'Bill': totalBill}
print(customer_details)
