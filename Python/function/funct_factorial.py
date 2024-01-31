"""function with return value."""
# def factorial(x):
#     f = 1
#     for x in range(1,x+1):
#         f *= x
#     return f
# print(f" factorial of 5 is {factorial(5)}")



def factorial(x):
    f = 1
    for x in range(1,x+1):
        f *= x
    print(f)
x = int(input("Enter number ==> "))
factorial(x)
