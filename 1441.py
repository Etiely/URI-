h=input()
while (h!=0):
    maior = h
    while (h!=1):
        if h%2==0:
            h = h * 0.5
            if h > maior:
                maior = int(h)
        else:
            h = (3*h) +1
            if h > maior:
                maior = int(h)
    print maior
    h=input()
