
print("-------------------PRIMER EJERCICIO DE COMPERTENCIA-----------------------")

print("_____________________________________________________________________________")

print("Este programa esta diseñado para saber si su sueldo puede cubrir dor articulos que quiera comprar,si su sueldo es apto aparecerapproducto mayor y sino suma")

print("_____________________________________________________________________________")

sueldo=float(input("Ingrese su sueldo: "))

print("_____________________________________________________________________________")

producto_1=float(input("Ingrese el precio del primer producto: "))

producto_2=float(input("Ingrese el precio del segundo producto: "))

print("_____________________________________________________________________________")

datos={ "sueldo": sueldo,
    "producto_1": producto_1,
    "producto_2": producto_2}

print(datos)

print("_____________________________________________________________________________")

productos=[producto_1,producto_2]

print(productos)

print("_____________________________________________________________________________")

print("suma de los dos productos que usted qeu usted compro")

oper=productos[0]+productos[1]

print(oper)

print("_____________________________________________________________________________")

if oper > sueldo :
    print("PRODUCTO MAYOR")

elif oper < sueldo :
    print("SUMA MAYOR")

else:
    print("RESULTADOS IGUALES")

print("_____________________________________________________________________________")





