# find out the common element from the list


list_1 = [1,2,3,4,3,5,4,3]
list_2 = [2,3,4,5,1,3,5,6]
list_3 = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(list_1[i])
print(list_3)    


# list_1 = [1,2,3,8,7,56,4,3,5,4,3]
# list_2 = [2,56,3,4,5,1,3,5,6]
# list_3 = []
# for num in list_1:
#     if num in list_2 and num not in list_3:
#         list_3.append(num)
# print(list_3)        
