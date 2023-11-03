num1=eval(input("enter first number"))
num2=eval(input("enter second number"))
if num1>=0 and num2<=0 and num1<0 and num2<0 and num1<0 or num2>0:
    print("invalid")  
elif num1>0 or num2<0:
    print("invalid")  
elif 0<num1<1 and 0<num2<1:
    print("invalid")
elif num1>num2:
    print("valid")
    print(f"{num1} is the largest and {num2} is the smallest")    
    
elif num2>num1:
    print("valid")
    print(f"{num1} is the largest and {num2} is the smallest")    
