# ch=input("enter any alphabet to find vowel and consonant from a to z ")
# if  ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
#     print(f"{ch} is vowel")
# else:
#     print(f"{ch} is consonant")    

ch = input("Enter the number or character====>")
n = ch

if ch == ch.isalpha():
    if  ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        print(f"{ch} is vowel")
    else:
        print(f"{ch} is consonant")  
else:
    print("it is a number.")