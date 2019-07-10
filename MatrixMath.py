import random

class Matrix:
    def __init__(self,number_rows=0,number_cols=0):
        self.number_rows = number_rows
        self.number_cols = number_cols
        self.data = []
        if isinstance(number_rows,list)==True: #manually initializing a Matrix
            self.number_rows=0
            self.number_cols=0
            self.data=number_rows
            for row in self.data:
                self.number_rows+=1
            for element in self.data[0]:
                self.number_cols += 1
        else:
            for i in range(self.number_rows): #initializing every element in a Matrix as 0
                row=[]
                for j in range(self.number_cols):
                    row.append(0)
                self.data.append(row)


    def print(self):
        for row in self.data:
            print(row)

    def randomize(self):
        for i in range(self.number_rows):  # initializing every element in a Matrix as random
            for j in range(self.number_cols):
                self.data[i][j]=random.randint(0,9)

    #transpose (non-static) --> actually changing the matrix to the tzransposed Matrix
    def transpose(self):
        transpose_Matrix=Matrix(self.number_cols,self.number_rows)
        for i in range(self.number_rows):
            for j in range(self.number_cols):
                transpose_Matrix.data[j][i]=self.data[i][j]
        self.data=transpose_Matrix.data
    #transpose (static) --> Matrix which gets transposed does not get changed
    @staticmethod
    def static_transpose(matrix):
        transpose_Matrix=Matrix(matrix.number_cols,matrix.number_rows)
        for i in range(matrix.number_rows):
            for j in range(matrix.number_cols):
                transpose_Matrix.data[j][i]=matrix.data[i][j]
        return transpose_Matrix

    #add
    def add(self,matrix):
        if isinstance(matrix,Matrix)==True: #if its a matrix add every element to every element of the self matrix
            if (self.number_rows,self.number_cols)==(matrix.number_rows,matrix.number_cols): #valid addition
                for i in range(self.number_rows):
                    for j in range(self.number_cols):
                        self.data[i][j]+=matrix.data[i][j]
            else:
                print('Addition is forbidden, because the number of rows and columns does not match!')
        else: #else (if its only a number) add the number to every element of the self matrix
            for i in range(self.number_rows):  # initializing every element in a Matrix as random
                for j in range(self.number_cols):
                    self.data[i][j]+=matrix

    #multiply by scalar
    def multiply(self, matrix):
        if isinstance(matrix,Matrix) == True:  # if its a matrix add every element to every element of the self matrix
            if (self.number_rows, self.number_cols) == (matrix.number_rows, matrix.number_cols):  # valid addition
                for i in range(self.number_rows):
                    for j in range(self.number_cols):
                        self.data[i][j] *= matrix.data[i][j]
            else:
                print('Multiplication is forbidden, because the number of rows and columns does not match!')
        else:  # else (if its only a number) add the number to every element of the self matrix
            for i in range(self.number_rows):  # initializing every element in a Matrix as random
                for j in range(self.number_cols):
                    self.data[i][j] *= matrix

    #static crossproduct
    @staticmethod
    def static_crossproduct(matrix1,matrix2):
        if isinstance(matrix1, Matrix) and isinstance(matrix2,Matrix):
            if matrix1.number_cols == matrix2.number_rows:
                result = Matrix(matrix1.number_rows, matrix2.number_cols)
                for i in range(matrix2.number_cols):
                    for j in range(matrix1.number_rows):
                        sum = 0
                        for k in range(matrix1.number_cols):
                            product = matrix1.data[j][k] * matrix2.data[k][i]
                            sum += product
                        result.data[j][i] = sum
                return result
            else:
                print('The operation crossproduct is impossible, because the number of columns (m1) does not match the number of rows (m2)!')

    #map f.i. m3.map(lambda x: 3*x)
    def map(self,function):
        for i in range(self.number_rows):  # computing for every element x in a Matrix f(x)
            for j in range(self.number_cols):
                value=self.data[i][j]
                self.data[i][j]=function(value)


m1=Matrix(4,2)
m1.randomize()
m1.print()
print()
m2=Matrix(2,7)
m2.randomize()
m2.print()
print()
m3=Matrix.static_crossproduct(m1,m2)
m3.print()
print()
m3.map(lambda x: 3*x)
m3.print()



