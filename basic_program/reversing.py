"""num=int(input("Enter the number"))
for i in range(num,0,-1):
    print("*"*i)"""
    
reversed_number=0 
number=int(input("Enter the number"))
# num = number
while number > 0:
      
    digit=number%10
    reversed_number=(reversed_number*10)+digit
    number = number//10
print(f"reversed num is {reversed_number}")
