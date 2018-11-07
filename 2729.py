n=input()
for i in range (int(n)):
  a = input().split()
  unicos=list(sorted((set(a))))
  unicos = " ".join(unicos)
  print (unicos)
