list = [1,2,3,4,5,6,6,5,54,3,4,5,6,6,4,5,6,6,5]
del_element = int(input("Enter the number to remove ==>"))
for i in list:
    if i == del_element:
        list.remove(del_element)
print(list)        