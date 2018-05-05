entradas=raw_input().split()
a=float(entradas[0])
b=float(entradas[1])
c=float(entradas[2])
triangulo= (a*c)/2
circulo = 3.14159 * (c**2)
trapezio = (a+b)*c/2
quadrado = b*b
retangulo = a*b
print "TRIANGULO: %1.3f"%triangulo
print "CIRCULO: %1.3f"%circulo
print "TRAPEZIO: %1.3f"%trapezio
print "QUADRADO: %1.3f"%quadrado
print "RETANGULO: %1.3f"%retangulo
