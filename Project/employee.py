"""Problem: Employee Management System
Description: Design an Employee class with attributes like name, employee ID, and methods for calculating salary based on hours worked."""
class Employee:
    def __init__(self,emp_name,emp_Id):
        self.emp_name = emp_name
        self.emp_Id = emp_Id
        self.per_hour_salary = 50
        
    def calculate_salary_per_hour(self):
        hour = float(input("Enter hour to calculate salary : "))
        if hour > 0:
            print(f"You worked \"{hour}hrs\"\nNow your salary is Rs{self.per_hour_salary*hour} ")

emp1 = Employee(input("Enter employee name : "),input("Enter employee Id : "))
emp1.calculate_salary_per_hour()