class array:
    def __init__(self,lst,r=0,c=0):
        self.lst = lst
        self.r = r
        self.c = c
        M=[]
        tmp=[]
        if r!=0 and c!=0:
            for i in self.lst:
                tmp.append(i)
                if len(tmp)==c:
                    M.append(tmp)
                    tmp=[]
            
            self.lst = M

    def disp_mat(self):
        for i in self.lst:
            print(*i)



    def __add__(self,other):
        self.lst
        other.lst
        if (self.r,self.c)==(other.r,other.c):
            M  = eval(str([[0]*self.c ]*self.r ))     # Deep Copy[0,0,0],[0,0,0]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j]=self.lst[i][j]+other.lst[i][j]
            return array(M)
        else:
            print("Not Compatible for Addition")
    def __sub__(self,other):
        self.lst
        other.lst
        if (self.r,self.c)==(other.r,other.c):
            M  = eval(str([[0]*self.c ]*self.r ))     # Deep Copy[0,0,0],[0,0,0]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j]=self.lst[i][j]-other.lst[i][j]
            return array(M)
        else:
            print("Not Compatible for Subtraction")
    
    def __mul__(self,other):
        self.lst
        other.lst
        if (self.r,self.c)==(other.r,other.c):
            M  = eval(str([[0]*self.c ]*self.r ))     # Deep Copy[0,0,0],[0,0,0]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j]=self.lst[i][j]*other.lst[i][j]
            return array(M)
        else:
            print("Not Compatible for Multiplication")    
    
    def __dot__():
        pass

        
        
        

lst1  = list(map(eval,input().
                 split()))
r1,c1 = list(map(int,input().split()))
arr1 = array(lst1,r1,c1)

lst2 = list(map(eval,input().split()))
r2,c2 = list(map(int,input().split()))
arr2 = array(lst2,r2,c2)

out = arr1+arr2


print("\nMatrix1")
arr1.disp_mat()

print("\nMatrix2")
arr2.disp_mat()

print("Addition")
out.disp_mat()

ot = arr1 - arr2
print("Subtraction")
ot.disp_mat()







# print(range(19))


# ls = [1,2,3,4,5,66,6]
# print(*ls)