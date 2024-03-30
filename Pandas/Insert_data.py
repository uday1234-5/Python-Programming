"""Data insertion"""
# import pandas as pd
# x = {"A":[1,2,3,4],"B":[3,6,7,8]}
# var = pd.DataFrame(x)
# print("****Befor  Updation****")  
# print(var)


# print("****After  Updation****")  
# var.insert(1,"C",[4,7,9,0])
# var.insert(3,"D",var["B"]+4)
# print(var)


"""To copy limited amount of data"""
import pandas as pd
x = {"A":[1,2,3,4,5,8],"B":[3,6,7,8,5,9]}
var = pd.DataFrame(x)
var["C"] = var["A"][1:3]
print(var)

"""To delete data"""
# import pandas as pd
# x = {"A":[1,2,3,4,5,6],"B":[3,6,7,8,9,5],"C":[3,4,6,7,7,8]}
# var = pd.DataFrame(x)
# var1 = var.pop("A") #del var("B")
# print(var)
# print(var1)
