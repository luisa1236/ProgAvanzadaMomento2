user1={"nombre:":"Juan","lastName:":"Castro","email:":"jcastro@gmail.com"}
print(len(user1))
print(type(user1))
#POdermos agregar elementos
user1["password"] ="xyz123"

#muestra el item
print(user1.keys())

#muestra el valor
print(user1.values())

#muestra item y valor
print(user1.items())

print(user1.get("name:"))
# pop eliminar un item
user1.pop("email:","name:")
print(user1.items())

#popitem Eliminar el ultimo element
user1.popitem()
print(user1.items())


#Podemos usar for para imprimir el diccionario ya sea solo claves,solo valores o ambos
for x,y in user1.items():
    print(x,y)

#acceder solo a claves
for x in user1.keys():
    print(x)

#acceder a lo valores
for y in user1.values():
    print(y)




user1={"nombre:":"Juan","lastName:":"Castro","email:":"jcastro@gmail.com","password:":"jk123"}
user2={"nombre:":"Santiago","lastName:":"Perez","email:":"perez@gmail.com","password:":"123pol"}
user3={"nombre:":"Mateo","lastName:":"gonzalez","email:":"gonza@gmail.com","password:":"456jum"}

users={"user1":user1,
       "user2":user2,
       "user3":user3}

users1={"user1":user1,
       "user2":user2,
       "user3":user3}

print(users)
print(type(users))

print(users["user2"]["lastName"])
#

#Ejercicio usando diccionarios y funciones en el que creemosun producto con los siguientes clasves:
#id,nombre,costo,cantidad,margendeganancia
#se deben alamcenar losprofuctos con dos campos adicionales calculados precio de venta = costo/(1-margendeg) y valor de inventarios = cantidad * costo.
#almacenar los productos creados en un diccionario de diccionario


#la aplicacion debe permitir iniciar,
# #mostrar un menu ,
# #1. agregar producto, 
# #2. listar los producto
# 

#tenemos una lista de productoy dentro de esa 