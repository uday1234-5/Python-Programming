"""Problem Statement : """

def squares(x):
    sum = 0
    for i in x:
        sum += i**2
    return f"sum of the squares of the item of list",sum
    
    
numbers = [2,3,4]
print(squares(numbers))
    