x = eval(input("Enter total no. of student : "))
empty={}
for i in range(1,x+1):
    list_1 = list(map(str,input("Enter Student Name : ").split()))
    list_2 = list(map(int,input("Enter score of each student :")))
    len_2 = len(list_2)
    for a in list_1:
        rishi = True
    for b in range(len_2):
        empty.update({a:list_2[b]})
print(empty)
z = 0
for k in empty.values():
    z += k
print(z)
print("Average Score is  ",z/len(empty))
    
    
    