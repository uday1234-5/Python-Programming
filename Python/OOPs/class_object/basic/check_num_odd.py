class number:
    def __init__(self,num):
        self.num  = num
    def odd_even(self):
        if self.num % 2 == 0:
            print(f"{self.num} is an even number. ")
        else:
            print(f"{self.num} is an odd number. ")
    def prime(self):
        for i in range(1,self.num+1):
            count = 0
            if self.num%i == 0:
                count += 1 
        if count == 2:
            print(f"{self.num} is a prime number.")    
        else:
           print(f"{self.num} is  non-prime number.")  
x  = eval(input("Enter number : "))  
num1 = number(x)
num1.odd_even()
num1.prime()
