def palindrome(str):
    if str == str[::-1]:
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is a not palindrome.")
str = input("Enter string:")        
palindrome(str)