k=int(input())
while k>0:
  ent=input().split()
  n=int(ent[0])
  m=int(ent[1])
  for i in range(k):
    ent1=input().split()
    x=int(ent1[0])
    y=int(ent1[1])
    if x==n or y==m:
      print ("divisa")
    elif x>n and y>m:
      print ("NE")
    elif x>n and y<m:
      print ("SE")
    elif x<n and y>m:
      print ("NO")
    elif x<n and y<m:
      print ("SO")
  k=int(input())
