while True:
    n=input()
    conta = 0
    contb = 0
    if n == 0:
        break
    for i in xrange(n):
        entrada = raw_input().split()
        a = int(entrada[0])
        b = int(entrada[1])
        if a > b:
            conta+=1
        elif b > a:
            contb+=1
    print conta,
    print contb
