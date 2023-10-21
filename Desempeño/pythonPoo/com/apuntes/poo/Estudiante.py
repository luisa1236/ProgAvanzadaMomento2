from com.apuntes.poo.Persona import Persona

class Estudiante(Persona):

    def __init__(self,id, nombre,correo,contrasena,programa,semestre):
        super().__init__(id,nombre,correo,contrasena)
        self.programa = programa
        self.semestre = semestre


    def verPersona(self):
        print(f"Id :{self.id} \n",
              f"Nombre: {self.nombre}\n",
              f"Correo: {self.correo}\n",
              f"Compañia:{self.compania}\n",
              f"Programa:{self.programa}\n",
              f"Semestre:{self.semestre}")



estudiante1 = Estudiante(1,"Maria","mt@gmial.com","12324","desarrollo",3)
print(estudiante1.programa)
