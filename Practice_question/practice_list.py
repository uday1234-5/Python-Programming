## Question 1.
""" Create a program that will keep track of items for a shopping list. The program should keep asking for new
items until nothing is entered (no input followed by enter/return key). The program should then display
the full shopping list."""

##                   
##lst = []
##while 1:
##    item = input('Type the item name  ')
##    if len(item) == 0:
##        break
##    lst.append(item)
##print(lst)

##==========================================================or=================================
##
##n = int(input("enter total no. of item"))                            
##i = 0
##x = []
##while i < n:
##    y = input("Enter the item")
##    x.append(y)
##    i += 1
##print(x)    
    
## =======================================================================================

## question 4
"""Convert a string into characters"""
##string = input("Enter the string")
##for i in string:
##    if i==" ":
##        rishi = True
##    else:
##        print(i,end=" ")
##print(type(i))

## =======================================================================================


## Question 5
"""Sort the list by the length of string elements"""
##a = input("Enter the string")
##b = list(a)
##b.sort()
##for i in b:
##    print(i,end=" ")

## =======================================================================================


##Question 6
"""Sort the list in reverse order"""
##lst = eval(input("Enter the list ==> "))
##lst.reverse()
##print(lst)

## =======================================================================================


##question 7
"""Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers
on one side is equal to the sum of the numbers on the other side.
canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true"""

##
##lst = list(map(int, input().split()))
##new_lst = []
##for i in lst:
##    if i not in new_lst:
##        new_lst.append(lst.count(i))
##print(max(new_lst))
##



##+++++++++++++++++++++++++string+++++++++++++++++++++++++++++++++
##question 1
"""Write a program that takes an integer input from the user and counts down from that number to 1
using a while loop.
"""
##n = int(input("Enter the number"))
##count = 0
##i = 0
##while i<n:
##    count += 1
##    i += 1
##print(count)

##=========================================================
##question 2
"""Write a program that calculates the factorial of a given positive integer using a while loop.
"""

##n = int(input("Enter the number"))
##count = 1
##i = 1
##while i<=n:
##    count *= i
##    i += 1
##print(count)

##question3
"""Create a simple number guessing game where the computer selects a random number between 1
and 100, and the user has to guess it. Use a while loop to keep the game running until the user
guesses correctly."""

##Question 4
"""Write a program that calculates the sum of all even numbers from 1 to n, where n is an integer
input by the user, using a while loop."""
##n = int(input("Enter the number"))
##sum = 0
##i = 1
##while i<n+1:
##    if i % 2 == 0:
##        sum += i
##    i = i +1
##print(sum)

##Question 5
"""Implement a program that asks the user to enter a password and keeps asking until the correct
password is entered. Use a while loop for this."""
##n = input("Enter password")
##m = input("again Enter password")
##if n == m:
##    print("your password is matched")
##else:
##    print("not matched")

##Question 6
"""Write a program that generates and prints the first n terms of the Fibonacci sequence using a while
loop."""
##n = int(input("Enter The number"))
##a = 0
##b = 1
##print(a,b,end=" ")
##i = 0
##while i < n-2:
##    c = a + b
##    print(c,end=" ")
##    a = b
##    b = c
##    i += 1
    

##Question 7
"""Create a program that takes an integer as input and prints the multiplication table for that number
from 1 to 10 using a while loop"""
##n = int(input("Enter the number to find table ==>"))
##i = 1
##while i <= 10:
##    print(f"{n} X {i} = {n*i}")
##    i += 1
  
##Question 8
"""8. Palindrome Checker:
 Write a program that checks if a given string is a palindrome (reads the same forwards and
backwards) using a while loop."""
##string = input("Enter string")
##if string == string[::-1]:
##    print("palindrome")
##else:
##    print("not palindrome")



##Question 9
"""9. Sum of Digits:
 Implement a program that calculates the
 sum of the digits of a given integer using a while loop"""
##n = int(input("Enter number"))
##sum = 0
##i = 1
##while i <= n:
##    sum += i
##    i += 1
##print(sum)

##Question 10
""" Prime Number Checker:
 Write a program that checks if a given number is prime or not using a while loop"""
##n = int(input("Enter the number"))
##i = 2
##while i <n:
##    if n % i != 0:
##        print("prime")
##        break
##    else:
##        print("non prime")
##        break
##    i += 1
"""ooooooooooooooooooooooooooooooooorrrrrrrrrrrrrrrrrrrrrr"""


