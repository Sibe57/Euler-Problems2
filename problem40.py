b=''
for i in range(0,200000):
    b+=str(i)
a=str(b)

def funk(x,y):
    rez=1
    if y<=1000000:
        rez = int(x[y])*(funk(x,y*10))


    return rez


f=funk(a,1)
print(f)