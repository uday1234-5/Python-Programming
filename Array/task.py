""" np.array(object,dtype = None,ndim = 0)

object : Any object exposing the array interface method
    """
import numpy as np
# print(np.array(2),type(np.array(2)))
# x = [[1,2],[2],[]]
# # print(ndim(x))


# x = [2,3,4,56,6]
# arr = np.array(x,dtype='int8')
# print(arr)

# Task 1
ls = list(map(int,input().split()))
arr = np.array(ls)
out = np.flip(arr)
print(np.array(out,dtype = 'float'))


#Task 2
# print(np.array(list(map(int,input().split()))).reshape(3, 3))


# Task 3
# n = int(input("Enter The dim : "))
# print((np.array(np.eye(n),dtype = int)))

# print(np.__version__)