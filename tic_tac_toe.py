from function import *
a=['1','2','3'] # this list a will make row 1
b=['4','5','6'] # this list b will make row 2
c=['7','8','9'] # this list c will make row 3
print a,'\n',b,'\n',c

##for i in range(9):
##    if i%2 == 0:
i=0
if i == 0:
    computer(a,b,c)
if a[0] == '0':
    computer5(a,b,c)
elif a[1] == '0':
    computer1(a,b,c)
elif a[2] == '0':
    computer6(a,b,c)
elif b[0] == '0':
    computer4(a,b,c)
elif b[2] == '0':
    computer3(a,b,c)
elif c[0] == '0':
    computer7(a,b,c)
elif c[1] == '0':
    computer2(a,b,c)
elif c[2] == '0':
    computer8(a,b,c)
