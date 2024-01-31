"""Immutable Data Types """

# def modify_int(x):
#     x += 10
#     print("Inside the function : ",x)
# num = 5
# modify_int(num)
# print("Outside the function : ",num)

"""string is immutable"""
# def modify_string(s):
#     s += " Kushwah"
#     print("Inside the function : ",s)
# name = "Uday"
# modify_string(name)
# print("Outside the function : ",name)

"""tuple is immutable"""
# def modify_tuple(t): 
#     """tuples are immutable, so creating a new tuple"""        
#     t += (4,)
#     print("Inside the function : ",t)
# coordinates = (1,2,3)
# modify_tuple(coordinates)
# print("Outside the function : ",coordinates)
      
      
"""list is mutable"""      
# def modify_list(lst): 
#     lst.append(4)       
#     lst[0] = 99
#     print("Inside the function : ",lst)
# numbers = [1,2,3]
# modify_list(numbers)
# print("Outside the function : ",numbers)


"""dictionary is also mutable"""
# def modify_dict(dict): 
#     dict[3] = "Python"
#     print("Inside the function : ",dict)
# my_dict = {1:"Uday Kushwah",2:"GLA UNIVERSITY"}
# modify_dict(my_dict)
# print("Outside the function : ",my_dict)

"""set is also mutable."""
# def modify_set(set): 
#     set.add(5)
#     print("Inside the function : ",set)
# my_set = {3,1,2,3}
# modify_set(my_set)
# print("Outside the function : ",my_set)