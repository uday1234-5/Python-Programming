def add(a,b):
    print(a+b)

def arearect(l,b):
    print("Area of rectangle is",l*b)

def odd(n):
    if(n%2!=0):
        print(n,"is odd")

def even(n):
    if(n%2==0):
        print(n,"is even")
        
def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count==2):
        print(n,"is prime")
    else:
        print(n,"is non prime")

def areasquare(n):
    print(n**2)
