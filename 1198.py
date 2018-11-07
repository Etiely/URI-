try:
  while True:
    ent=input().split()
    n=int(ent[0])
    m=int(ent[1])
    diferenca=abs(m-n)
    print (diferenca)
except EOFError:
  pass
