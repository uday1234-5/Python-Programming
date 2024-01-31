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
    print()
    print("\t\tAvailable Items")
    print("--------------------------------------------------------")
    print(f"{'S.No.':<15}{'Items':<15}{'Quantity':<15}{'Cost/Item':15}")
    print("--------------------------------------------------------")
    for i,j in dct.items():
        print(f"{i:<15}{j['Item']:<15}{j['Quantity']:<15}{j['Cost/Item']:<15}")
    print("--------------------------------------------------------")
    


dct = {
        1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
        2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
        3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
        4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
        5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
      }
display_available_items(dct)
