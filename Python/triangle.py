s1=int(input("enter first side 0f triangle"))
s2=int(input("enter second side 0f triangle"))
s3=int(input("enter third side 0f triangle"))
if s1==s2 and s2==s3 and s3==s1:
    print("Equilateral triangle")
elif s1==s2 or s2==s3 or s3==s1: 
    print("Isosceles triangle")
else:
    print("scalene triangle")       