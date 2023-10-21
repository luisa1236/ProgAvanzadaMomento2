#las tuplas se encierran en parentesis
#Son inmutables
#Sise requiere que tenga añgun cambio debe casquear a lista

colores=("amarillo","azul","rojo")
print(type(colores))
print(len(colores))
print(colores[0])
print(colores[1])
print(colores[2])

#casquear
coloresList= list(colores)

print(type(coloresList))

coloresList.append("verde")

print(coloresList[0:])

colores=tuple(coloresList)
print(type(colores))    

#recorrer una tupla
for i in range(len(colores)):
    print(colores[i])

#Slicing 

print(colores[1:4])
print(colores[:-1])