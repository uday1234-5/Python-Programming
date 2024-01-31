# """Question 2:
# Create a class Student with attributes name, age, and grade. Implement a method to display the student details. Create instances of the Student class and display their details."""
# class Student:
#     # def __init__(self,detail):
        
#     #     self.detail = detail
#     print('*'*60)
#     print(f"{'Roll.no.':<15}{'Name':<15}{'Age':<15}{'Grade':<15}")
#     def show_detail(self,detail):
        
#         print(f"{detail[0]:<15}{detail[1]:<15}{detail[2]:<15}{detail[3]:<15}")
#     print('-'*60)    
       
        

# Detail = Student() 
# std1 = [1,'Saket',20,'D']
# std2 = [2,'Shivam',18,'A+']
# std3 = [3,'Ravi',23,'F']
# std4 = [4,'Kamal',24,'B']
# Detail.show_detail(std1)
# Detail.show_detail(std2)
# Detail.show_detail(std3)
# Detail.show_detail(std4)
# print('*'*60)

"""SIR"""
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
    
std = Student()
std.setdetail('uday',20,'A+')
std.getdetail()
std.setdetail('saket',24,'B+')
std.getdetail()
std.setdetail('ravi',18,'C')
std.getdetail()