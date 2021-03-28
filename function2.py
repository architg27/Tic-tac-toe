l=[]
def one(a,b,c):
    if a[0] == '0':
        g=1
        l.append(g)
    if a[1] == '0':
        h=2
        l.append(h)
    if a[2] == '0':
        i=3
        l.append(i)
    if b[0] == '0':
        j=4
        l.append(j)
    if b[2] == '0':
        k=6
        l.append(k)
    if c[0] == '0':
        o=7
        l.append(o)
    if c[1] == '0':
        m=8
        l.append(m)
    if c[2] == '0':
        n=9
        l.append(n)
    return l
