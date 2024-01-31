def odd_even(x):
    for i in range(1,x+1):
        if x%2 == 0:
            return " even "
        else:
            return "odd"
x = int(input("Enter number  :  "))
print(odd_even(x))