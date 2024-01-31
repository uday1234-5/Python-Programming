dct = {}
total_items = int(input("Enter total no. of items :"))
for i in range(total_items):
    item1 = input("Enter item name :")
    quantity = input("Enter item quantity")
    cost = eval(input("Enter cost :"))
    dct[item1] = quantity
print(dct)