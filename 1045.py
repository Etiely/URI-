n=raw_input().split()
n = [float(x)for x in n]
n.sort()
n.reverse()
a=float(n[0])
b=float(n[1])
c=float(n[2])
if a >= b + c:
    print "NAO FORMA TRIANGULO"
else:
    if a**2 == b**2 + c**2:
        print "TRIANGULO RETANGULO"
    if a**2 > b**2 + c**2:
        print "TRIANGULO OBTUSANGULO"
    if a**2 < b**2 + c**2:
        print "TRIANGULO ACUTANGULO"
    if a == b == c:
        print "TRIANGULO EQUILATERO"
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print "TRIANGULO ISOSCELES"
