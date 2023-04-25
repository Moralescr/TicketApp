# Clase usuarios
class Usuarios:

    # Método constructor de la clase
    def __init__(self,):
        self.codigo = ""
        self.isAdmin = ""
        self.clave = ""
        self.usuarioTmp = {}
        self.listaUsuarios = [{"codigo": "Admin",
                               "isAdmin": "S", "clave": "123"}]

    # Método que permite registrar un usuario.
    def registrarUsuario(self,):
        self.codigo = input("Ingrese el nombre de usuario: ")
        usuarioIsAdmin = input("Rol de usuario es Administrador (N/S): ")
        self.clave = input("Ingrese la contraseña: ")
        usuarioExiste = self.validarUsuario(self.codigo)
        if usuarioExiste == False:
            self.usuarioTmp = {
                'codigo': self.codigo,
                "isAdmin": usuarioIsAdmin,
                'clave': self.clave
            }
            self.listaUsuarios.append(self.usuarioTmp)
            print("El usuario se ha registrado exitosamente.")
        else:
            print("No puedes registrar un usuario que ya existe")

    # Método que permite buscar un usuario.
    def buscarUsuario(self,):
        self.codigo = input("Ingrese el nombre de usuario a buscar: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                print(
                    f"Usuario: { usuario['codigo'] }, Clave: { usuario['clave'] } , Rol administrador?: {usuario['isAdmin']}")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")

    # Validar si usuario existe.
    def validarUsuario(self, codUsuario):
        existe = False
        for user in self.listaUsuarios:
            if user['codigo'] == codUsuario:
                existe = True
        return existe

    # Validar rol de usuario
    def validarRolUsuario(self, codUsuario, password):
        isAdmin = False
        for user in self.listaUsuarios:
            if user['codigo'] == codUsuario and user['clave'] == password:
                if user['isAdmin'] == "S":
                    isAdmin = True
        return isAdmin

    # Método que permite editar un usuario.
    def editarInfoUsuario(self):
        self.codigo = input("Ingrese el código de usuario a editar: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                nuevaClave = input("Ingrese la nueva clave de acceso: ")
                usuarioIsAdmin = input(
                    "Rol de usuario es Administrador (N/S): ")
                usuario['clave'] = nuevaClave
                usuario['isAdmin'] = usuarioIsAdmin
                print("La clave se ha cambiado exitosamente.")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")

    # Método que permite eliminar un usuario.
    def eliminarUsuario(self,):
        self.codigo = input("Ingrese el código de usuario: ")
        for usuario in self.listaUsuarios:
            if usuario['codigo'] == self.codigo:
                self.listaUsuarios.remove(usuario)
                print("El usuario se ha eliminado exitosamente.")
                return
        print("Error: El usuario no existe en nuestras bases de datos.")

    # Informe de usuarios
    def informeUsuarios(self,):
        print("*** INFORME RESUMEN DE LOS USUARIOS ****")
        print("Cantidad de usuarios: ", len(self.listaUsuarios))
        for usuario in self.listaUsuarios:
            print("Usuario: ", usuario['codigo'],
                  ", Contraseña: *******", ", Rol Admin:", usuario['isAdmin'])
        print("------------- UL ----------------")
