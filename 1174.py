a=[]
for i in xrange(100):
    n=input()
    a.append(n)
for i in xrange(100):
    if a[i] <=10:
        print "A[%d] = %1.1f"%(i,a[i])
