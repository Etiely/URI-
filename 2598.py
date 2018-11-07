c=input()
for i in range(int(c)):
  ent=input().split()
  n=int(ent[0])
  m=int(ent[1])
  divisao=(int(n/m))
  resto= (float(n%m))
  if m>n:
    print(1)
  else:
    if resto > 0:
      print (int(divisao+1))
    else:
      print (int(divisao))
