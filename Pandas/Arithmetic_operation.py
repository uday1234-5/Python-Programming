"""Addition of column"""
# import pandas as pd
# var = pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
# print(var)
# var["A+B"] = var["A"] + var["B"]
# print(var)


"""Subtraction of column"""
# import pandas as pd
# var = pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
# print(var)
# var["A-B"] = var["A"] - var["B"]
# print(var)


"""Multiplication of column"""
# import pandas as pd
# var = pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
# print(var)
# var["A*B"] = var["A"] * var["B"]
# print(var)


"""Division of column"""
# import pandas as pd
# var = pd.DataFrame({"A":[1,24,3,4],"B":[2,3,4,5]})
# print(var)
# var["A/B"] = var["A"] / var["B"]
# var["A//B"] = var["A"] // var["B"]
# var["A%B"] = var["A"] % var["B"]
# var["A**B"] = var["A"] ** var["B"]
# print(var)


"""To check condition"""
import pandas as pd
var = pd.DataFrame({"A":[10,20,30,40],"B":[14,15,12,13]})
var["A>20"] = var["A"] > 20
var["B<=13"] = var["B"] <= 13
var["A==B"] = var["A"] == var["B"]
var["A>B"] = var["A"] > var["B"]

print(var)