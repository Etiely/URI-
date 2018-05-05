salario = input()
if salario >= 0 and salario <= 400.00:
    print "Novo salario: %1.2f" %(((salario * 15) / 100) + salario)
    print "Reajuste ganho: %1.2f" %((salario * 15) / 100)
    print "Em percentual: 15 %"
elif salario >400 and salario <=800.00:
    print "Novo salario: %1.2f" %(((salario * 12) / 100) + salario)
    print "Reajuste ganho: %1.2f" %((salario * 12) / 100)
    print "Em percentual: 12 %"
elif salario >800 and salario <= 1200.00:
    print "Novo salario: %1.2f" %(((salario * 10) / 100) + salario)
    print "Reajuste ganho: %1.2f" %((salario * 10) / 100)
    print "Em percentual: 10 %"
elif salario > 1200 and salario <= 2000.00:
    print "Novo salario: %1.2f" %(((salario * 7) / 100) + salario)
    print "Reajuste ganho: %1.2f" %((salario * 7) / 100)
    print "Em percentual: 7 %"
else:
    print "Novo salario: %1.2f" %(((salario * 4) / 100) + salario)
    print "Reajuste ganho: %1.2f" %((salario * 4) / 100)
    print "Em percentual: 4 %"
