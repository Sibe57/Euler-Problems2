one=1
two=2
five=5
ten=10
twen=20
fifty=50
funt=100
funts=200
goal=200
counter=0
# x=(a in range(0,201))*one+(b in range(0,101))*two+(c in range(0,41))*five+(d in range(0,21))*ten+(e in range(0,11))*twen+(f in range (0,5))*fifty+(g in range(0,3))*funt+(j in range (0,2))*funts
def func(a,b,c,d,e,f,g,j):
    x=a*one+b*two+c*five+d*ten+e*twen+f*fifty+g*funt+j*funts
    return x
for j in range(2):
    for g in range(3):
        if goal-j<g:
            g=0
            continue
        for f in range(5):
            if goal-j-g<f:
                f=0
                continue
            for e in range(11):
                if goal-j-g-f<e:
                    e=0
                    continue
                for d in range(21):
                    if goal-j-g-f-e<d:
                        d=0
                        continue
                    for c in range(41):
                        if goal-j-g-f-e<c:
                            c=0
                            continue
                        for b in range(101):
                            if goal-j-g-f-e-c<b:
                                b=0
                                continue
                            for a in range(201):
                                ed=func(a, b, c, d, e, f, g, j)
                                if ed > goal:
                                    break
                                if ed ==goal:
                                    counter += 1
                                    print(counter)
                                    print(j,g,f,e,d,c,b,a)
print(counter)