class Usuarios:
    def __init__(self,):
        self.codigo = ""
        self.clave = ""
        self.usuarioTmp = {}
        self.listaUsuarios = []

    def registrarUsuario(self,):
        self.codigo = input("Ingrese el nombre de usuario: ")
        self.clave = input("Ingrese la contraseña: ")
        self.usuarioTmp = {
            'codigo': self.codigo,
            'clave': self.clave
        }
        self.listaUsuarios.append(self.usuarioTmp)
        print("El usuario se ha registrado exitosamente.")

    def buscarUsuario(self,):
        self.codigo = input("Ingrese el nombre de usuario a buscar: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                print(
                    f"Usuario: { usuario['codigo'] } Clave: { usuario['clave'] }")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")

    def editarUsuario(self):
        self.codigo = input("Ingrese el código de usuario a editar: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                claveNueva = input("Ingrese la nueva clave de acceso: ")
                usuario['clave'] = claveNueva
                print("La clave se ha cambiado exitosamente.")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")

    def eliminarUsuario(self,):
        self.codigo = input("Ingrese el código de usuario: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                self.listaUsuarios.remove(usuario)
                print("El usuario se ha eliminado exitosamente.")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")
