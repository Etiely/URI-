n=int(input())
conts=0
contn=0
ent=input().split()
for i in range(n):
  q=int(ent[i])
  if q == 0:
    conts+=1
  else:
    contn+=1
if conts>contn:
  print ("Y")
else:
  print ("N")
