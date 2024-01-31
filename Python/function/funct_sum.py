def sum(x):
    y = 0
    for i in range(1,x+1):
        y += i
    return y
x = int(input("Enter number ==>   "))
print(f"sum of {x} natural number is",sum(x))