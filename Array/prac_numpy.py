import numpy as np
# m,n = list(map(int,input().split()))
# lst = []
# for i in range(m):
#     for j in range(n):
#         lst.append(list(map(int,input().split())))
        
# arr1 = np.array(lst)
# lst1 = np.min(arr1,axis = 1)
# print(np.max(lst1))

# lst = [1.22,0.44,0.56]
# arr = np.array(lst)
# a = np.around(lst,decimals = 0)
# print(np.array(a,dtype = "int"))
# print(, dtype = 'int') )

arr1 = np.array([1,2,31])
arr2 = np.array([2,3,4])
print(np.inner(arr1,arr2))
print(np.outer(arr1,arr2))
