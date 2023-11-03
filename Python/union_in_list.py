# list_1 = [12,3,4,5,6,7]
# list_2 = [1,2,3,4,5]
# list_3 = []
# for i in list_1 + list_2:
#     if i not in list_3:
#         list_3.append(i)
# print(list_3)            
        
list_1 = [12,3,4,5,6,7]
list_2 = [1,2,3,4,5]
x = set(list_1)
y = set(list_2)
x.intersection(y)
print(list(x))