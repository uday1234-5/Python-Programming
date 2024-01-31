class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return f"Addition : {self.num1 + self.num2}"
    
    def subtract(self):
        return f"Subtraction : {self.num1 - self.num2}"
    
    def multiply(self):
        return f"{self.num1 * self.num2}"
    
    def divide(self):
        if self.num1 == 0 or self.num2 == 0 :
            return "Division by zero"
        else:
            return f"{self.num1 / self.num2}"
x = int(input("Enter Ist number : "))   
y = int(input("Enter 2nd number : "))   
calc = calculator(x,y)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())



"""Sir code"""

# class calculator:
#     # def __init__(self):
#     #     pass
    
#     def add(self,num1,num2):
#         return f"Addition : {num1 + num2}"
    
#     def subtract(self,num1,num2):
#         return f"Subtraction : {num1 - num2}"
    
#     def multiply(self,num1,num2):
#         return f"Multiplication : {num1 * num2}"
    
#     def divide(self,num1,num2):
#         if num1 == 0 or num2 == 0 :
#             return "Division by zero"
#         else:
#             return f"Division : {num1 / num2}"
# calc = calculator()
# print(calc.add(2,3))
# print(calc.subtract(4,4))
# print(calc.multiply(3,6))
# print(calc.divide(8,2))