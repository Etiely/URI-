try:
  while True:
    n=int(input())
    lista=[]
    for i in range(n):
      codigo=int(input())
      lista.append(codigo)
    for ind in range(n):
      lista.sort()
      x=str(lista[ind])
      if len(x)<4:
        while len(x)<4:
          x='0'+x
      print (x)
except EOFError:
  pass
