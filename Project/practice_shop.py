"""availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)
		Available Items:
S.No.          Item           Quanity        Cost/Item      
1              Biscuits       5              20.5           
2              Chocolates     10             35             
3              Coffee         25             55             
4              Chips          10             50             
5              Cream          5              30 
"""

def display_available_items(dct):
    print('-'*55)
    print("\t\tAvailable Items")
    print('-'*55)
    print(f"{'Sr.no.':<10}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")
    print('-'*55)
    
    for i,j in dct.items():
        print(f"{i:<10}{j['Item']:<15}{j['Quantity']:<15}{j['Cost/Item']:<15}")
    print('-'*55)
    
availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)

def display_user_cart(dct):
    pass

user_demand = {'Biscuits': 5, 'Chocolates': 100, 'Coffee': 25, 'Chips': 10, 'Cream': 5}
Name = "Uday Kushwah"
Address = 'AGRA'
delivery_charge = 30
bill = 0
user_cart = availableItems.copy()
for x in user_demand:
    for y in user_cart:
        if x == availableItems[y]['Item']:
            if user_demand[x] <= availableItems[y]['Quantity']:
                Cost = user_demand[x]*availableItems[y]['Cost/Item']
                bill += Cost

display_user_cart(user_demand)