class Persona:
    compania = "xyz"

    def __init__(self, id, nombre, correo, contrasena):
        self.id = id
        self.nombre = nombre  # Instancias de loa atributos
        self.correo = correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"Id :{self.id} \n",
              f"Nombre: {self.nombre}\n",
              f"Correo: {self.correo}\n",
              f"Compañia:{self.compania}")

maria = Persona(1, "Maria", "mr@gmail.com", "qwer1")
maria.verPersona()


