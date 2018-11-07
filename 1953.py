try:
  while True:
    n=int(input())
    contepr=0
    contehd=0
    conti=0
    for i in range(n):
      ent=input().split()
      a=int(ent[0])
      b=(ent[1]).upper()
      if b == 'EPR':
        contepr+=1
      elif b == 'EHD':
        contehd+=1
      else:
        conti+=1
    print ("EPR: " +str(contepr))
    print ("EHD: " +str(contehd))
    print ("INTRUSOS: "+str(conti))
except EOFError:
  pass
