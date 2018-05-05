N = input()
for i in xrange(N):
    C = input()
    dias = 0
    while (C > 1):
        C -= (C/2)
        dias += 1	
    print dias,"dias"
