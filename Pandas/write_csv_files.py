"""Write csv files"""
import pandas as pd
x = {"A":[1,2,"hello",4,5],"B":[5,6,6,7,8],"C":[2,3,45,5,6]}
var = pd.DataFrame(x)
print(var)
print(var.to_csv("first2.csv",index = False))



"""To change the head data"""
# import pandas as pd
# x = {"A":[1,2,"hello",4,5],"B":[5,6,6,7,8],"C":[2,3,45,5,6]}
# var = pd.DataFrame(x)
# print(var)
# print(var.to_csv("first5.csv",index = False,header = [1,2,3]))