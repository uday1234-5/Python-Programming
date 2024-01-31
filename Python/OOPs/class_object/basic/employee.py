# class Employee:
#     def setDetails(self,name,emp_ID,salary,deptt):
#         self.name = name
#         self.emp_ID = emp_ID
#         self.salary = salary
#         self.deptt = deptt
#     def getDetails(self):
#         return f'''
#         Name : {self.name}
#         ID : {self.emp_ID}
#         salary : {self.salary}
#         Department : {self.deptt}''' 
#     def update_salary(self,new_salary):
#         self.new_salary = new_salary
# emp1 = Employee()
# emp2 = Employee()

# emp1.setDetails('saket','GLA1234',12000,'civil')
# emp2.setDetails('Ravi','GLA6789',15000,'Electrical')
# print(emp1.getDetails())

# emp1.update_salary(20000)
# print("Update salary")
# print(emp1.getDetails())

# # print(emp2.getDetails())

'''Above code by using Destructor'''
class Employee:
    def __init__(self,name,emp_ID,salary,deptt):
        self.name = name
        self.emp_ID = emp_ID
        self.salary = salary
        self.deptt = deptt
    def getDetails(self):
        return f'''
        Name : {self.name}
        ID : {self.emp_ID}
        salary : {self.salary}
        Department : {self.deptt}''' 
    def update_salary(self,new_salary):
        self.new_salary = new_salary
emp1 = Employee('saket','GLA1234',12000,'civil')
emp2 = Employee('Ravi','GLA6789',15000,'Electrical')

print(emp1.getDetails())
print(emp2.getDetails())