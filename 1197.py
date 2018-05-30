try:
    while True:
        ent=raw_input().split()
        v=int(ent[0])
        t=int(ent[1])
        aceleracao=v*(t*2)
        print aceleracao
except EOFError:
    pass
