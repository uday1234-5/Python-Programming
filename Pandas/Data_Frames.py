# import pandas as pd
# lst = [12,3,3,4,5,56,6,655,5]
# x = pd.DataFrame(lst)
# print(x,type(x))


"""To pass Dictionary in pandas"""
# import pandas as pd
# dic = dict = {"Name":["Python","C","PHP","Java"],"Course Duration":[4,5,9,6]}
# x = pd.DataFrame(dic)
# print(x,type(x))


"""To change index"""
# import pandas as pd
# dic = dict = {"Name":["Python","C","PHP","Java"],"Course Duration":[4,5,9,6],"Rank":[1,5,4,3]}
# x = pd.DataFrame(dic,index = ["a","b","c","d"])
# print(x,type(x))


"""To access column"""
# import pandas as pd
# dic = dict = {"Name":["Python","C","PHP","Java"],"Course Duration":[4,5,9,6],"Rank":[1,5,4,3]}
# x = pd.DataFrame(dic,index = ["a","b","c","d"],columns = ["Name","Rank"])
# print(x,type(x))


"""To access custom element"""
# import pandas as pd
# dic = dict = {"Name":["Python","C","PHP","Java"],"Course Duration":[4,5,9,6],"Rank":[1,5,4,3]}
# x = pd.DataFrame(dic)
# print(x)
# print(x["Name"][2])


"""Data Frame using nested list"""
# import pandas as pd
# lst = [[12,3,3,4,5],[56,6,655,5]]
# x = pd.DataFrame(lst)
# print(x)


"""Data Frame using Series"""
# import pandas as pd
# sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
# print(pd.DataFrame(sr))