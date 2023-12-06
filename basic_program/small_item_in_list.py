# # small element in a list
# list_1 = [1,2,3,4,5,56,-7]
# small = list_1[0]
# for i in range(7):
#     if list_1[i]<small:
#         small = list_1[i]
# print(small)        


# count odd and even numbers in a list

list = [1,2,3,4,5,6,7,8,3,4,5,5,5,0,672,927,6]
count_even = 0
count_odd = 0
for i in list:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd +=1
print("count of odd number ",count_odd) 
print("count of even number ",count_even)       