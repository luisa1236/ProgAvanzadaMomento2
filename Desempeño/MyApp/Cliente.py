from Usuario import Usuario

class Cliente(Usuario):

    def __int__(self,id,nombre,apellido,correo,contraseña,direccion,tel):
        super.__init__(id,nombre,apellido,correo,contraseña)
        self._tel=tel
        self._direccion=direccion

        #Get
    @property
    def tel(self):
        return self._tel

        #Set
    @tel.setter
    def tel(self):
        self.tel = tel

    @property
    def direccion(self):
        return self._direccion

        #Set
    @tel.setter
    def tel(self):
        self._direccion = direccion

    def registrar_usuario(self):
        super().registrar_usuario()
        self._tel = input("ingrese el telefono del cliente: ")
        self._direccion = input("ingrese la dirección el cliente: ")

    def ver_usuario(self):
        print(f"Telefono")


