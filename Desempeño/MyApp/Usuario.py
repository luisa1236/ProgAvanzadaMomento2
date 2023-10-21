

class Usuario:

    def __int__(self,id, nombre, apellido, correo, contrasena):

        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena


             #ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
         self._apellido = apellido
       #CORREO
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo


    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
         self._contrasena = contrasena


    def registrar_usuario(self):
        self.id = input("ingrese el id del usuario: ")
        self.nombre = input("Ingrese el nombre del usuario: ")
        self.apellido = input("ingrese el apellido del usuario: ")
        self.correo = input("Ingrese el correo del usuario: ")
        self.contrasena = input("cree una contraseña")

    def ver_usuario(self):
        print(f"Id:{self._id} Nombre:{self._nombre} Apellido:{self._apellido} Correo:{self._correo}")
