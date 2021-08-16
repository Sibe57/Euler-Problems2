f=open('p081_matrix.txt')
matrix=[]
for i in f:
    a=[int(g) for g in i.split(',')]
    matrix.append(a)
def collapse_1part(matrix):
    for summ in range(1,80):
        for x in range(0,summ+1):
            y=summ-x
            if (x==0 and y==0):
                continue
            elif x==79 and y==79:

                return (matrix)
            elif x==0 or x==79:
                matrix[x][y]=matrix[x][y]+matrix[x][y-1]
            elif y==0 or y==79:
                 matrix[x][y]=matrix[x][y]+matrix[x-1][y]
            if matrix[x-1][y]<matrix[x][y-1]:
                matrix[x][y] = matrix[x][y] + matrix[x - 1][y]
            else:
                matrix[x][y] = matrix[x][y] + matrix[x][y-1]
    return matrix

def collapse_2part(matrix):
    for summ in range(78,-1,-1):
        for x in range(78,summ,-1):
            y=summ-x
            if (x==0 and y==0):
                continue
            elif x==79 and y==79:
                print(matrix)
                return (matrix)
            elif x==0 or x==79:
                matrix[x][y]=matrix[x][y]+matrix[x][y-1]
            elif y==0 or y==79:
                 matrix[x][y]=matrix[x][y]+matrix[x-1][y]
            if matrix[x-1][y]<matrix[x][y-1]:
                matrix[x][y] = matrix[x][y] + matrix[x - 1][y]
            else:
                matrix[x][y] = matrix[x][y] + matrix[x][y-1]

reversed_matrix=list(reversed(matrix))
for i in reversed_matrix:
    g=list(reversed(i))
    del(reversed_matrix[0])
    reversed_matrix.append(g)
print(reversed_matrix)
print(len(reversed_matrix))
a=collapse_1part(matrix)
b=collapse_1part(a)
middle_list=[]
for x in range(0,80):
    y=79-x
    c=b[x][y]
    middle_list.append(c)
print(min(middle_list))

