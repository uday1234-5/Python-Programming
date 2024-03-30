"""Read CSV File Data"""
# import pandas as pd
# csv_1 = pd.read_csv("D:\\Python\\First.csv")
# print(csv_1)

# import pandas as pd
# var = pd.read_csv("first5.csv")
# print(var)


"""To fetch particular row from csv files"""
# import pandas as pd
# var1 = pd.read_csv("first5.csv",nrows = 2)
# print(var1)


"""To fetch particular column  by column name from csv files"""
# import pandas as pd
# var = pd.read_csv("first5.csv",usecols = ["1"])
# print(var)

"""To fetch particular column  by index from csv files"""
# import pandas as pd
# var = pd.read_csv("first5.csv",usecols = [0])
# print(var)


"""To skip particular rows from csv files"""
# import pandas as pd 

# var0 = pd.read_csv("First.csv")
# var1 = pd.read_csv("First.csv",skiprows=[1])
# print(var0)
# print(var1)


""" To make particular column as a index column """
# import pandas as pd
# var = pd.read_csv("First.csv",index_col = ["D"])
# print(var)


""" To make particular row as a header """
# import pandas as pd
# var = pd.read_csv("First.csv",header = 2)
# print(var)

"""To Change Heading """
import pandas as pd
var = pd.read_csv("First.csv",names = ["column1","column2","column3","column4"])
print(var)