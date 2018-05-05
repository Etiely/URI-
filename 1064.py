cont = 0
media = 0
for i in xrange(6):
    x = input()
    if x > 0:
        cont += 1
        media += x
media = media/cont
print "%d valores positivos\n%1.1f"%(cont,media)
