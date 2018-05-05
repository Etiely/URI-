n=raw_input().split()
x=int(n[0])
y=int(n[1])
voltas = 1
y=y-x
while x>0:
     x-=y
     voltas+=1
print voltas
