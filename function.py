from function2 import *
d=0
e=0
f=0

def computer(a,b,c):
    print "\nComputer's Turn\n"
    i=1
    if i == 1:
        x=5
        i=0
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
        elif x<=6:
            if b[x-4] == 'X' or b[x-4] != '0':
                b[x-4]='X'
        elif x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
    print a,'\n',b,'\n',c
    player2(a,b,c)
    check_col(a,b,c)
    check_row(a,b,c)
    check_diag(a,b,c)

def computer1(a,b,c):
    if  a[1] == '0':     
        x=1
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 2 and p[1] == 9:
        if c[2] == '0':
            x=7
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
        if a[2] == '0':
            x=4
            if x<=6:
                if b[x-4] == 'X' or b[x-4] != '0':
                    b[x-4]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        if b[0] == '0':
            x=3
            if x<=3:   
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        else:
            x=4
            if x<=6:
                if b[x-4] == 'X' or b[x-4] != '0':
                    b[x-4]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[1] == 3 or p[1] == 7 or p[1] == 4 or p[1] == 6 or p[1] == 8:
        x=9
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)

def computer2(a,b,c):
    if  c[1] == '0':     
        x=3
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 7 and p[1] == 8:
        if c[0] == '0':
            x=9
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
        if a[0] == '0':
            x=6
            if x<=6:
                if b[x-4] == 'X' or b[x-4] != '0':
                    b[x-4]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        if b[2] == '0':
            x=1
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        else:
            x=1
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 1 or p[0] == 2 or p[0] == 4 or p[0] == 6 or p[1] == 9:
        x=7
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)    

def computer3(a,b,c):
    if  b[2] == '0':     
        x=1
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 6 and p[1] == 9:
        if c[2] == '0':
            x=3
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
        if a[1] == '0':
            x=7
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        if c[0] == '0':
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        else:
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 2 or p[0] == 3 or p[0] == 4 or p[1] == 7 or p[1] == 8:
        x=9
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)


def computer4(a,b,c):
    if  b[0] == '0':     
        x=3
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 4 and p[1] == 7:
        if c[0] == '0':
            x=1
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
        if a[1] == '0':
            x=9
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        if c[2] == '0':
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        else:
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 2 or p[1] == 9 or p[0] == 1 or p[1] == 6 or p[1] == 8:
        x=7
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)

def computer5(a,b,c):
    if  a[0] == '0':     
        x=3
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 1 and p[1] == 7:
        if c[0] == '0':
            x=4
            if x<=6:
                if b[x-4] == 'X' or b[x-4] != '0':
                    b[x-4]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
                    p=one(a,b,c)
        if p[3] == 6:
            if b[2] == '0':
                x=8
                if x<=9:
                    if c[x-7] == 'X' or c[x-7] != '0':
                        c[x-7]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        player2(a,b,c)
            if a[1] == '0':
                x=9
                if x<=9:
                    if c[x-7] == 'X' or c[x-7] != '0':
                        c[x-7]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                d=check_col(a,b,c)
                e=check_row(a,b,c)
                f=check_diag(a,b,c)
                if d!=1 and e!=1 and f!=1:
                    print "Sorry! The game has been tied"
            if a[1] != '0':
                x=2
                if x<=3:
                    if a[x-1] == 'X' or a[x-1] != '0':
                        a[x-1]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
        else:
            x=6
            if x<=6:
                if b[x-4] == 'X' or b[x-4] != '0':
                    b[x-4]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[1] == 2 or p[1] == 9 or p[1] == 4 or p[1] == 6 or p[1] == 8:
        x=7
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)    
                  
def computer6(a,b,c):
    if  a[2] == '0':     
        x=9
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 1 and p[1] == 3:
        if a[0] == '0':
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
                    p=one(a,b,c)
        if p[4] == 8:
            if c[1] == '0':
                x=6
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        player2(a,b,c)
            if b[0] == '0':
                x=7
                if x<=9:
                    if c[x-7] == 'X' or c[x-7] != '0':
                        c[x-7]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                d=check_col(a,b,c)
                e=check_row(a,b,c)
                f=check_diag(a,b,c)
                if d!=1 and e!=1 and f!=1:
                    print "Sorry! The game has been tied"
            if b[0] != '0':
                x=4
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        check_col(a,b,c)
                        check_row(a,b,c)
                        check_diag(a,b,c)
        else:
            x=8
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 2 or p[1] == 7 or p[1] == 4 or p[1] == 6 or p[1] == 8:
        x=1
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)


def computer7(a,b,c):
    if  c[0] == '0':     
        x=1
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 7 and p[1] == 9:
        if c[2] == '0':
            x=8
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
                    p=one(a,b,c)
                    print p
        if p[2] == 2:
            if a[1] == '0':
                x=6
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        player2(a,b,c)
            if b[0] == '0':
                x=3
                if x<=3:
                    if a[x-1] == 'X' or a[x-1] != '0':
                        a[x-1]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                d=check_col(a,b,c)
                e=check_row(a,b,c)
                f=check_diag(a,b,c)
                if d!=1 and e!=1 and f!=1:
                    print "Sorry! The game has been tied"
            if b[0] != '0':
                x=4
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        check_col(a,b,c)
                        check_row(a,b,c)
                        check_diag(a,b,c)
        else:
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 2 or p[0] == 3 or p[0] == 4 or p[0] == 6 or p[1] == 8:
        x=9
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)

def computer8(a,b,c):
    if  c[2] == '0':     
        x=3
        if x<=3:
            if a[x-1] == 'X' or a[x-1] != '0':
                a[x-1]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                player2(a,b,c)
                p=one(a,b,c)
    if p[0] == 7 and p[1] == 9:
        if c[0] == '0':
            x=8
            if x<=9:
                if c[x-7] == 'X' or c[x-7] != '0':
                    c[x-7]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    player2(a,b,c)
                    p=one(a,b,c)
        if p[2] == 2:
            if a[1] == '0':
                x=4
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        player2(a,b,c)
            if b[2] == '0':
                x=1
                if x<=3:
                    if a[x-1] == 'X' or a[x-1] != '0':
                        a[x-1]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                d=check_col(a,b,c)
                e=check_row(a,b,c)
                f=check_diag(a,b,c)
                if d!=1 and e!=1 and f!=1:
                    print "Sorry! The game has been tied"
            if b[2] != '0':
                x=6
                if x<=6:
                    if b[x-4] == 'X' or b[x-4] != '0':
                        b[x-4]='X'
                        print "\nComputer's Turn\n"
                        print a,'\n',b,'\n',c
                        check_col(a,b,c)
                        check_row(a,b,c)
                        check_diag(a,b,c)
        else:
            x=2
            if x<=3:
                if a[x-1] == 'X' or a[x-1] != '0':
                    a[x-1]='X'
                    print "\nComputer's Turn\n"
                    print a,'\n',b,'\n',c
                    check_col(a,b,c)
                    check_row(a,b,c)
                    check_diag(a,b,c)
    if p[0] == 2 or p[0] == 3 or p[0] == 1 or p[0] == 6 or p[0] == 8:
        x=7
        if x<=9:
            if c[x-7] == 'X' or c[x-7] != '0':
                c[x-7]='X'
                print "\nComputer's Turn\n"
                print a,'\n',b,'\n',c
                check_col(a,b,c)
                check_row(a,b,c)
                check_diag(a,b,c)

def player2(a,b,c):
    x=int(input("\nPlayer2 enter the location="))
    if x<=3:
        if a[x-1] != 'X' or a[x-1] == '0':
            a[x-1]='0'
    elif x<=6:
        if b[x-4] != 'X' or b[x-4] == '0':
            b[x-4]='0'
    elif x<=9:
        if c[x-7] != 'X' or c[x-7] == '0':
            c[x-7]='0'
    print '\n',a,'\n',b,'\n',c
    

def check_col(a,b,c):
    for i in range(3):
        if a[i] == b[i] == c[i]:
            print a[i],'winner'
            return 1
            break

def check_row(a,b,c):
    for i in range(1):
        if a[i] == a[i+1] == a[i+2]:
            print a[i],'winner'
            return 1
            break
        elif b[i] == b[i+1] == b[i+2]:
            print b[i],'winner'
            return 1
            break
        elif c[i] == c[i+1] == c[i+2]:
            print c[i],'winner'
            return 1
            break

def check_diag(a,b,c):
    for i in range(1):
        if a[i] == b[i+1] == c[i+2]:
            print a[i],'winner'
            return 1
            break
        elif c[i] == b[i+1] == a[i+2]:
            print c[i],'winner'
            return 1
            break 
