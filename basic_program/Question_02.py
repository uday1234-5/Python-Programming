"""Create dictionary and add values"""       
item = eval(input("Enter the total items :"))        
empty = {}
for i in range(1,item+1):
    key = input("Enter purchasing item :")
    value = int(input("Enter Price : "))
    empty.update({key:value})
print(empty)

price = 0
for x in empty.values():
    price += x
print("Total Price is : ",price)
