# Date - 28-03-2024     Lab Work

# shallow copy : duplicate the item of nested list
# deep copy : 

import numpy as np

# lst = [[2,4] , [5,3]]
# arr = lst
# print(f"{arr=}")
# print(f"{lst=}")

# lst = [[2,4] , [5,3]]
# arr = lst.copy()
# arr[0][0] = 100
# print(f"{arr=}")
# print(f"{lst=}")



# lst = [[2,4] , [5,3]]
# arr = lst.copy()
# del arr[0][0]
# print(f"{arr=}")
# print(f"{lst=}")



# lst = [[2,4] , [5,3]]
# arr = eval(str(lst))
# del arr[0][0]
# print(f"{arr = }")
# print(f"{lst = }")




import numpy as np
lst = [[2,4] , [5,3]]
arr = np.array(lst)
out = np.ravel(arr)
arr[0][0] = 100
print(out)
# arr = np.zeros((1,2,3,4))
# print(arr)