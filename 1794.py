n=input()
e=raw_input().split()
la=int(e[0])
lb=int(e[1])
f=raw_input().split()
sa=int(f[0])
sb=int(f[1])
if n >= la and n <= lb and n >= sa and n <= sb:
  print "possivel"
else:
  print "impossivel"
