n=int(input())
while n!=0:
  ent=input().split()
  contm=0
  contj=0
  lista = []
  for index in range(int(n)):
    a=int(ent[index])
    lista.append(a)
    if a == 1:
      contj +=1
    else:
      contm +=1
  print ("Mary won "+str(contm)+ " times and John won "+str(contj)+" times")
  n=int(input())
