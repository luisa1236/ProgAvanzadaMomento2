usuarios={"user1", "user2","user3","user4"}

#usuario[1] = "usern"

usuarios.add("user5")   
print(usuarios)     

#Se puede valiadar si un elemento existe o no en el set
print("user2" in usuarios)
print("user6" in usuarios)

#se pueden remover elmentos
usuarios.remove("user3")
print(usuarios)

for i in usuarios:
    print(i)


usuariosNuevos={"user6","user7"}
##Uniendo dos conjutnoa
usuarios.union(usuariosNuevos)

for i in usuarios:
    print(i)
print("--------------------------------------------")


otrosUsuarios={"user1","user3","user9","user8","user7"}
usuarios.update(otrosUsuarios)

for i in usuarios:
    print(i)

usuarios= frozenset(["user1","user2","user10"])
usuarios2={usuarios,"user11","user22"}
print(usuarios2)
print("--------------------------------------------")
print(usuarios.intersection(otrosUsuarios))
print("--------------------------------------------")
print(usuarios.symmetric_difference(otrosUsuarios))
print("--------------------------------------------")