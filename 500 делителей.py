def t(n):
    return int(n*(n+1)/2)
n=1
while True:
    if t(n)%500!=0:
        n+=1
        continue
    counter=0
    i=1
    a=t(n)
    while i<a:
        if a%i==0:
            counter+=1
            i+=1

        else:
            i+=1

        if counter>500:
            print(t(n))
            break

    n+=1

