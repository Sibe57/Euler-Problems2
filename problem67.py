t=open('triangle.txt')
text=[]
for i in t:
    i=i[:-1]
    liner=i.split(' ')
    for g in range(len(liner)):
        liner[g]=int(liner[g])
    text.append(liner)
print(text)
text.reverse()
triangle=text
for i in range(1, len(triangle)):
    for g in range(0, len(triangle[i])):
        left = triangle[i][g] + triangle[i - 1][g]
        right = triangle[i][g] + triangle[i - 1][g + 1]
        if left>right:
            triangle[i][g]=left
        else:
            triangle[i][g]=right
    print(triangle[-1][-1])