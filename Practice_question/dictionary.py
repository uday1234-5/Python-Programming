# # DICTIONARY========================================================================================================================
# mydict = {
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":2010
# }
# print(mydict)
# print(len(mydict))
# print(type(mydict))
# print(mydict["Year"])



# # create DICTIONARY================================================================================================================
# thisdict = dict(Name="Uday",Age=20,Program="B-Tech CSE")
# print(thisdict)


# =================================================================================================
# mydict = {
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":2010
# }
# x = mydict.get("Year")
# print(x)

# x1 = mydict.keys()
# print(x1)

# x2 = mydict.values()
# print(x2)

# print(mydict.items())
# print(mydict["Year"])
# for i in mydict.itemss():
#       print(i)
# ===============================================================================================================================
# Car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "Year": "1942"
# }
# x = Car.keys()
# print(x)

# Car["color"] = "White"
# print(Car)
# print(x)


# ==============================================================================================================================


# mydict = {
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":2010}
# print(mydict)

# mydict["Year"] = 2008

# print(mydict)


# ===========================================================================================================================
# mydict = {
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":2010}
# x  = mydict.items()
# print(x)




# ==============================================================================================================================
# mydict = {
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":2010}
# if "Year" in mydict:
#     print("Yes, 'Year' is one of the keys in the  <mydict> dictionary.....")
# if "Mathura " in mydict.values():
#     print("Yes, 'Mathura' is one of the value in the  <mydict> dictionary.....")
        
    
# =======================================================================================================================
# mydict = {
#      "University":"GLA",
#      "Location":"Mathura",
#      "Year":2010}
# mydict.update({"Year":2020,"University":"Amity"})
# print(mydict)


# ==========================================================================================================================
# mydict = {
#       "University":"GLA",
#       "Location":"Mathura",
#       "Year":2010}
# mydict.pop("Year")
# print(mydict)

# mydict.popitem()
# print(mydict)


# ===========================================================================================================================
# mydict = {
#       "University":"GLA",
#       "Location":"Mathura",
#       "Year":2010}
# del mydict
# print(mydict)


# ===========================================================================================================================
# mydict = {
#       "University":"GLA",
#       "Location":"Mathura",
#       "Year":2010}
# mydict.clear()
# print(mydict)

# ===========================================================================================================================


# nested dictionary
# mystudents = {
#       "student1" : {
#             "name": "Sachin",
#             "Year":2000 
#       },
#       "student2": {
#             "name":"Lakshman",
#             "Year" :2007
#       },
#       "student3":{
#             "name":"Ram",
#             "Year": 2003
#       }
      
# }
# print(mystudents)

# for i in mystudents:
#       print(i)
      
# print(mystudents["student2"]["name"])

# for x,y in mystudents.items():
#       print(x,y["name"])
      
      
# ===========================================================================================================================





"""You are required to create a python program that allows a user to input key_value pairs to construct
a dictionary . 
===> prompt the user to enter the number of key valye pairs they want to add
===> construct dictionary......."""
# n = eval(input("Enter the keys to create dictionary"))
# empty = {}
# for i in range(1,n+1):
#       x = input("Enter the key :")
#       y = input("Enter the values :")
#       empty.update({x:y})
# print(empty)



# user_dict = {}
# num_pairs = int(input("Enter the number of key-value pairs "))
# for x in range(num_pairs):
#        x = input("Enter the key :")
#        y = input("Enter the values :")
#        user_dict[x] = y
# print(user_dict)



# # ========================================================================================================
# mydict = {"John":85,
#           "Jane":90,
#           "Bob":75,
#           "Alice":95}
# mydict["Sam"] = 80
# mydict["Bob"] = 80
# del mydict["Jane"]
# for i,j in mydict.items():
      # print(f"{i}:{j}")
      

mydict = {"John":85,
          "Jane":90,
          "Bob":75,
          "Alice":95}
x = -1
for i in mydict.values():
      if i > x:
            x = i
top_student = [student for student,i in mydict.items( ) if i == x]
print(top_student)
      
      
      