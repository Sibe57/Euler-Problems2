def t(n):
    return int(n*(n+1)/2)
def p(n):
    return int(n*(3*n-1)/2)
def h(n):
    return int(n*(2*n-1))
def ansp(x):
    D=(0.5**2)-(4*1.5*-x)
    if D<0:
        return False
    x1=(0.5+D**0.5)/3
    x2=(0.5-D**0.5)/3
    if (x1>0 and x1%1==0) or (x2%1==0 and x2>0):
        return 'p={},{}'.format(x1,x2)
    return False

def ansh(x):
    D=1-(4*2*-x)
    if D<0:
        return False
    x1=(1+D**0.5)/4
    x2=(1-D**0.5)/4
    if (x1>0 and x1%1==0) or (x2%1==0 and x2>0):
        return 'p={},{}'.format(x1,x2)
    return False
n=286
while True:
    n=n+1
    x=t(n)
    if type(ansp(x))==str:
        a=[n,ansp(x),ansh(x)]
        print(a)
        print(x)

    else:
        continue
