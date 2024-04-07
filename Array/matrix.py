class Matrix:
    def __init__(self,arr):
        self.arr = arr
        m = []
    def validity(self,m,n):
        return len(self.arr) == m*n
    def create_matrix(self,m,n):
        self.x = []
        self.y = []
        # for _ in range(len(self.arr)):
        for j in self.arr:
            self.y.append(j)
            for i in range(0,n):
                if len(self.y) == n:
                    self.x.append(self.y)
                    
            self.x.append(self.y)   
        self.arr = self.x
    def display_matrix(self):
        for k in self.arr:
            print(*k)
arr = list(map(int,input().split()))
row,column = list(map(int,input().split()))
matrix = Matrix(arr)
matrix.validity(row,column)

if matrix.validity(row,column):
    matrix.create_matrix(row,column)
    matrix.display_matrix()
else:
    print("Invalid Dimension")
 
