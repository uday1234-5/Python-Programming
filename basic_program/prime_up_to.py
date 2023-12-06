# x = int(input("Enter the lower limit: "))
# y = int(input("Enter the upper limit: "))

# for i in range(x,y+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)



lower = int(input("Enter the lower limit :  "))
upper = int(input("Enter upper limit :  "))
if lower>upper:
    print("Please enter the upper limit greater than lower limit.")
elif lower==upper:
    print("please enter different number")
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
