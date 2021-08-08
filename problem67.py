t=open('/home/sibe57/PycharmProjects/Euler-Problems2/triangle.txt')
text=[]
for i in t:
    i=i[:-1]
    liner=i.replace(' ',',')
    liner=liner.split(',')
    for g in range(len(liner)):
        liner[g]=int(liner[g])

    text.append(liner)
print(text)
text.reverse()
perfect_triangle=text
for i in range(1,len(perfect_triangle)):
    for g in range(0,len(perfect_triangle[i])):
        left = perfect_triangle[i][g]+perfect_triangle[i-1][g]
        right = perfect_triangle[i][g] + perfect_triangle[i-1][g+1]
        if left>right:
            perfect_triangle[i][g]=left
        else:
            perfect_triangle[i][g]=right
    print(perfect_triangle[-1][-1])