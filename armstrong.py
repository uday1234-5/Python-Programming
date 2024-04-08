"""armstrong number is 371(3**3+3**7+1**3)...370..1634...123...153"""
num=int(input("Enter a number to check armstrong"))
num_digit=len(str(num))
sum_of_cubes=0
temp=num
while temp>0:
    digit=temp%10
    sum_of_cubes+=digit**num_digit
    temp//=10     #temp=temp//10
if num== sum_of_cubes :
    print(f"{num} is an Armstrong number.")
else:
    print(f"({num} is not an armstrong number)")    
    
    
    
    
"""=================================================="""
def is_armstrong(num):
    # Convert the number to a string to find its length
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    
    # Initialize the sum of powered digits
    sum_of_digits = 0
    
    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits
    
    # Check if the number is Armstrong or not
    if sum_of_digits == num:
        return True
    else:
        return False

# Example usage:
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
