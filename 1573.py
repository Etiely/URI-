para = [int(j) for j in raw_input().split()]
a=int(para[0])
b=int(para[1])
c=int(para[2])
while a>0 and b>0 and c>0:
    cubo=int((a*b*c)**(1./3))
    print cubo
    para = [int(j) for j in raw_input().split()]
    a=int(para[0])
    b=int(para[1])
    c=int(para[2])
