try:
    while True:
        ent=input().split()
        a=int(ent[0])
        b=int(ent[1])
        c=int(ent[2])
        if a != b and a != c:
          print ("A")
        elif b != a and b != c:
          print ("B")
        elif c != a and c != b:
          print ("C")
        else:
          print ("*")
except EOFError:
    pass
