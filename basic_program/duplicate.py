# Remove the duplicate item from the list

my_list = [2,3,3,4,5,5,5,6,6,4,3,3,3]
empty_list = []
for i in my_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)