def hcf(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            hcf = i
    return f"The hcf of {a} and {b} is {hcf}"
def lcm(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            hcf = i
            lcm = int((a*b)/hcf)
            
    return f"The lcm of {a} and {b} is {lcm} "                                                

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(lcm(a,b))
print(hcf(a,b))
    