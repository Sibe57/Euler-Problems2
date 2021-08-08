f=open('triangle.txt')d
triangle=('75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')
triangle=triangle.replace(' ',',')
triangle=triangle.split(',')
triangle2=[]
for i in triangle:
    i = int(i)
    triangle2.append(i)
triangle2.reverse()
perfect_triangle=[]
print(triangle2)

for i in range(14,-1,-1):
    count=i
    nextline=[]
    while count>=0:
        nextline.append(triangle2[count])
        count-=1
        print(nextline)
    perfect_triangle.append(nextline)
    del triangle2[0:i+1]
for i in range(1,15):
    for g in range(0,len(perfect_triangle[i])):
        left = perfect_triangle[i][g]+perfect_triangle[i-1][g]
        right = perfect_triangle[i][g] + perfect_triangle[i-1][g+1]
        if left>right:
            perfect_triangle[i][g]=left
        else:
            perfect_triangle[i][g]=right
    print(perfect_triangle[-1][-1])

