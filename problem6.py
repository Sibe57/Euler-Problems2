sqre=0
summ=0
for i in range(1, 101):
    summ=summ+(i**2)
for f in range(1, 101):
    sqre=sqre+f
ss=sqre**2
res=ss-summ
print(res)