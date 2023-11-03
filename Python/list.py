# mydata=["student 1","student 2","student 3"]
# print(mydata)
# print(len(mydata))
# print(type(mydata))


# thislist=list(("abc","xyz","ert"))
# print(thislist)


# list=["python","uday","kushwah","shiv","are","studying" ,"and"]
# print(list[3],end=" ")
# print(list[-1],end=" ")
# print(list[1],end=" ")
# print(list[2],end=" ")
# print(list[-3],end=" ")
# print(list[-2],end=" ")
# print(list[0],end=" ")


# mylist=["GLA","Sharda","LPU","Amity","Delhi University","CU"]
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:4])
# print(mylist[2:])
# print(mylist[-4:-1])

# mylist=[9,10,11]
# mylist.append(12)
# print(mylist)


# list1=["a","b","c"]
# list2=["p","q","r"]
# list1.extend(list2)
# print(list1)

# # add items in list by using list
# mydata=["milk","Tea","Coffee","Sugar","Bread"]
# print(mydata)

# mydata[1]="Black Tea"
# print(mydata)

# mydata[1:3]=["Black Tea","Cold Coffee"]
# print(mydata)

# mydata[1:7]=["D1","D2"]
# print(mydata)


# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# list1=["a","b","c"]
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)  


# newlist=["apple","banana","cherry"]
# finallist=newlist.copy()
# print(finallist) 

 
# newlist=["apple","banana","cherry"]
# finallist=list(newlist)
# print(finallist)  
    

# mydata=["a","b","c"]
# for x in mydata:
#     print(x)


# mydata=["a","b","c"]
# for i in range(len(mydata)):
#     print(mydata[i], end = " ")
    
   
# mydata=["a","b","c"]   
# i=0
# while i<len(mydata):
#     print(mydata[i])
#     i+=1


# vegetable=["cabbage","potato","chilli","cauli flower","carrot"]
# mylist=[]
# for x in vegetable:
#     if "o" in x:
#         mylist.append(x)
# print(mylist)        


# mylist2 =  ["a","b","c","a"]
# mylist2.pop(2)
# print(mylist2)

# mylist3 = ["a","b","c","d","e"]
# del mylist3[1]
# print(mylist3)

mylist3 = ["a","b","c","d","e"]
del mylist3    #shows error as already deleted
print(mylist3)

# mylist3 = ["a","b","c","d","e"]
# mylist3.clear()
# print(mylist3)      #gives empty list

# mylist3 = ["a","b","c","d","e"]
# mylist3.remove("c")
# print(mylist3)
 
 
# mydata2 = [-32,-42,100, 13, 23, 62, 82,64] 
# mydata2.sort()
# print(mydata2)

# mydata2 = [-32,-42,100, 13, 23, 62, 82,64] 
# mydata2.sort( reverse = True)
# print(mydata2)

# mydata2 = ["a","g","r","r","d","y","t"] 
# mydata2.sort( reverse = True)
# print(mydata2)

# mydata2 = ["a","g","r","r","d","y","t"] 
# mydata2.sort( )
# print(mydata2)

# list2 = []
# list1 = [2,3,4,5,6,7]      #Squre of item in list    square = [x**2 for x in range(8)]
# for i in list1:
#     #print(i**2,end=",")
#     list2.append(i**2)
# print(list2)
 
# even_numbers = [x for x in range(10) if x % 2 ==0 ]
# print(even_numbers)

# result = ['pass' if score >= 60 else "fail" for score in [75, 30, 85,50]]
# print(result)

# name1 = ["john","jane","jim"]
# name_length = [len(name) for name in name1]
# print(name_length)


"""you are given a list of numbers containing integers.
your task is to perform the following operations....
*acces and print the element at index 3
*acces and print the last element of the list
*acces and print a sublist containing elements from index 1 to 4(inclusive)
*change the value at index 2 to 10
*append the value 20 at the end of the list
*remove the element at index 0
*insert the value 5 at index 1
*print the final list"""

# list1 = [23,3,14,12,32,7,8,34]
# # print(f"element at index 3 : {list1[3]}")
# # print(f"last element :{list1[7]}")    #print(list1[-1])
# # sublist = list1[1:5]
# # print(f"sublist from index 1 to 4 : {sublist}")

# list1[2] = 10
# # print(f"modified list after changing element at index 2 :{list1}")

# list1.append(20)
# # print(f"list after appending 20 :{list1}")

# del list1[0]
# # print(f"list after removing element at index 0:{list1} ")

# list1.insert(1,5)
# # print(f"element at index 1:{list1}")
# print(list1)

"""take number from user and make a list"""
# mylist = []
# for i in range(1,10):
#     j = int(input("Enter the number to add in list "))
#     mylist.append(j)
# print(mylist)

# my_list = []
# for i in range(1,11):
#     j = int(input("Enter the number to add in list ")) 
#     my_list.insert(i,j)
# print(my_list)

