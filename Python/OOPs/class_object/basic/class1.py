# class student:
#     pass
# uday = student()
# uday.college = "GLA UNIVERSITY"
# uday.course = "B-Tech CSE"
# uday.age = 18

# kamal = student()
# kamal.college = "Dr. BPS College"
# kamal.course = "B.Sc."
# kamal.age = 19

# print(uday)
# print(kamal)

# print(uday.course)
# print(kamal.course)

"""==================================================="""

class student:
    def __init__(self,college,course,age):
        self.college = college
        self.course = course        
        self.age = age
uday = student("GLA UNIVERSITY","B-Tech",18)
kamal = student("Dr. BPS College","B.Sc.","19")
print(uday.college , kamal.college)
print(kamal.age)

