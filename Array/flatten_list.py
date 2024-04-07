"""
nested list
[2,[4,6,[8]],[[[[5]]]],[],[[]],0]

flatten list
[2,4,6,8,5,0]
"""

# class Flatten:
#     def __init__(self,lst):
#         self.lst = lst
    
#     def flatten(self):
#         data = [i for i in self.lst if i or i == 0]
#         str_data = str(data).replace('[',"").replace(']',"")
#         print(list(eval(str_data)))
    
# lst1 = Flatten([2,[4,6,[8]],[[[[5]]]],[],[[]],0])
# lst1.flatten()

def flatten(lst):
    flattened = []
    for item in lst:
        if type(item) == list:
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [2, [4, 6, [8]], [[[[5]]]], [], [[]], 0]
flattened_list = flatten(nested_list)
print(flattened_list)





"""==========================================================================="""
"""Flatten the nd-array"""
import numpy as np

lst = [[2,3,4],[3,4,5],[6,7,8]]
arr = np.array(lst)
out = arr.flatten()
print(out)


"""=============================================================================="""
print(arr.reshape(-1))