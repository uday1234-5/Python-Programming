# import pandas as pd
# x = [1,2,3,45,6,"Uday"]
# a = pd.Series(x,index = ['a','b','c','d','e','f'])
# print(a)
# print(type(a))
# print(a[3])


# import pandas as pd
# x = [1,2,3,45,6,"Uday"]
# a = pd.Series(x)
# print(a)
# print(type(a))
# print(a[3])


"""To Change Data Type"""
# import pandas as pd
# x = [1,2,3,45,6]
# a = pd.Series(x,index = ['a','b','c','d','e'],dtype = 'float',name = "python")
# print(a)
# print(type(a))
# print(a[3])


"""To pass dictionary in pandas"""
# import pandas as pd
# dict = {"Name":["Python","C","PHP","Java"],"Course Duration":[4,5,9,6]}
# var = pd.Series(dict)
# print(var)
# print(type(var))


# import pandas as pd
# print(pd.Series(8,index=[1,2,3,4,5,6]))



# import pandas as pd
# s1 = pd.Series(8,index=[1,2,3,4,5,6])
# s2 = pd.Series(8,index=[1,2,3,4,5,6])
# print(s1+s2)


import pandas as pd
s1 = pd.Series(48,index=[1,2,3,4,5,6])
s2 = pd.Series(8,index=[1,2,3])
print(s1+s2)