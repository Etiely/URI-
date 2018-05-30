n=input()
soma=0
while n>0:
    for i in xrange(n):
        quadrado=(n*n)
        n-=1
        soma+=quadrado
    print soma
    n=input()
    soma=0



