a=range(100, 999)
b=range(100, 999)
pal=[]
res=0
for i in a:
    for y in b:
        res=y*i
        res=str(res)
        if res==res[::-1]:
            pal.append(int(res))
print(max(pal))

