class Student:
    def __init__(self):
        self.name = "NA"
        self.age = "NA"
        self.grade = "NA"
    def setdetail(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def getdetail(self):
        print(f"Name : {self.name}\nAge  : {self.age}\nGrade:{self.grade}")
    
class Grade(Student):
    def calculate_grade(self,percent):
        if percent >= 0 and percent <=100 :    
            if percent>=90 and percent <100:
                print("\"O\"Grade")
            elif percent>=80 and percent <90:
                print("\"A+\" Grade")
            elif percent>=70 and percent <80:
                print("\"A\" Grade")
            elif percent>=60 and percent <70:
                print("\"B\" Grade")
            elif percent>=50 and percent <60:
                print("\"c\" Grade")  
            else:
                print("-*|| FAIL ||*-")
        else:
            print("Enetr Percentage from (0 - 100): ")
std = Grade()
percent = float(input("Enter Your percentage : "))
std.calculate_grade(percent)
