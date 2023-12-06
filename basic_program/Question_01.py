""" Write a Python Program that takes a starting and ending number as input from the user.
  the program should print all the numbers from the starting to the ending number, following these rules:
 If a number is divisible by 2, print "Good".
 If a number is divisible by 3, print "Student".
 If a number is divisible by both 2 and 3, print "Good Student".
 Otherwise, simply print the number itself.
 Example
 sample input:
 Enter the starting number: 1
 Enter the ending number : 10
 Sample output:
 1:
 2: Good
 3: Student
 4: Good
 5:
 6: Good Student
 7:
 8: Good
 9: Student
 10: Good
"""
x = int(input("Enter first number : "))
y = int(input("Enter last number : "))
for i in range(x,y+1):
    if i % 2 == 0 and i%3!=0:
        print(i,":"+"Good")
    elif i % 3 == 0 and i % 2!=0:
        print(i,":"+"Student!")
    elif i%2==0 and i%3==0:
        print(i,":"+"Good Student")
    else:
        print(i)



