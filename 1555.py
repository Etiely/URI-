n=input()
for i in xrange(n):
    ent=raw_input().split()
    a=int(ent[0])
    b=int(ent[1])
    rafa=((3*a)**2+b**2)
    beto=(2*(a**2)+(5*b)**2)
    carlos=(-100*a+b**3)
    if rafa > beto and rafa > carlos:
        print "Rafael ganhou"
    elif beto > rafa and beto > carlos:
        print "Beto ganhou"
    else:
        print "Carlos ganhou"
