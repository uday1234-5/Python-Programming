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
    