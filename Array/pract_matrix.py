class array:
    def __init__(self,lst,r=0,c=0):
        self.lst = lst
        self.r = r
        self.c = c
        if r != 0 and c != 0 :
            M = []
            temp = []
            for i in self.lst:
                temp.append(i)
                if len(temp) == self.c:
                    M.append(temp)
                    temp = []
            self.lst = M
                
    def __add__(self,other):
        self.lst
        other.lst
        M = eval(str([[0]*self.c]*self.r))
        if (self.r, self.c) == (other.r,other.c):
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] + other.lst[i][j]
                    
            return array(M)
        else:
            print('Not compatible for additton!!!')
            
    def __sub__(self,other):
        self.lst
        other.lst
        M = eval(str([[0]*self.c]*self.r))
        if (self.r, self.c) == (other.r,other.c):
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] - other.lst[i][j]
                    
            return array(M)
        else:
            print('Not compatible for subtracton!!!')
    def __mul__(self,other):
        self.lst
        other.lst
        M = eval(str([[0]*self.c]*self.r))
        if (self.r, self.c) == (other.r,other.c):
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] * other.lst[i][j]
                    
            return array(M)
        else:
            print('Not compatible for multiplicatition!!!')
    def __div__(self,other):
        self.lst
        other.lst
        M = eval(str([[0]*self.c]*self.r))
        if (self.r, self.c) == (other.r,other.c):
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] / other.lst[i][j]
                    
            return array(M)
        else:
            print('Not compatible for division!!!')
    def dot(self,other):
        self.lst 
        other.lst
        M = eval(str([[0]*self.c]*self.r))
        if self.c == other.r :
            M = eval(str([[0]*self.r]*self.c))
            for i in range(self.r):
                for j in range(other.c):
                    for k in range(self.c):
                        M[i][j] = self.lst[i][k] * other.lst[k][j]
            return array(M)
    def disp_mat(self):
        for i in self.lst:
            print(*i)
#Driver code
lst1 = list(map(int,input("Enter space separated elements of matrix 1 : ").split()))    
r1,c1 = list(map(int,input("Enter space separated row and column of matrix 1 : ").split()))   
arr1 = array(lst1,r1,c1)

lst2 = list(map(int,input("Enter space separated elements of matrix 2 : ").split()))    
r2,c2 = list(map(int,input("Enter space separated row and column of matrix 2 : ").split()))    
arr2 = array(lst2,r2,c2)

print("\nMatrix 1 ==> ")
arr1.disp_mat()
print("\nMatrix 2 ==> ")
arr2.disp_mat()

add = arr1 + arr2
print("\nAddition of matrix 1 and matrix 2 : ")
add.disp_mat()


sub = arr1 - arr2
print("\nDivision of matrix 1 and matrix 2 : ")
sub.disp_mat()

mul = arr1 * arr2
print("\nmultiplication of matrix 1 and matrix 2 : ")
mul.disp_mat()

mlt = arr1.dot(arr2)
print("\n Dot Product : ")
mlt.disp_mat()
