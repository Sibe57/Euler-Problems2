def small():
    n=1000
    while True:
        if (n%f==0 for f in range(11, 21)):
            return n
        else:n+=1
print(small())
g=232792560
for i in range(1,21):
    h=g/i
    print(h)

