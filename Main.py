import Usuarios

# Login


def login(listaUsuarios):
    print("Iniciar sesión")
    usuarioValido = False
    while usuarioValido == False:
        userName = input("Ingrese el usuario: ")
        password = input("Ingrese la clave: ")
        for user in listaUsuarios:
            if user['codigoUsuario'] == userName and user['claveAcceso'] == password:
                usuarioValido = True
                mainMenu()
                return
        print("Error, usuario no existe. Intente de nuevo")
        print('\n')

# Submenú


def submenu(opciones):
    eleccion = 0
    while eleccion != len(opciones):
        print('\n')
        print('SubMenú')
        for opt in opciones:
            print(opt['opc'])
        eleccion = int(input("Elija una opción: "))
        if eleccion <= len(opciones):
            # posicion en la lista. data={"opc":"opcion elegida","fnc":"la opcion a ejecutar)}
            data = opciones[eleccion - 1]
            exec(data['fnc'])
        else:
            print('Opción no válida, intente de nuevo')

# Menú principal


def mainMenu():
    run = True
    while run == True:
        print('\n')
        print("Bienvenido Auto Transportes el Roble")
        print('\n')
        print("1.Usuarios")
        print("2.Autobuses")
        print("3.Viajes")
        print("4.Facturación")
        print("5.Salir")
        opcion = int(input("Seleccione la opción deseada: "))
        if opcion == 1:
            opciones = [{"opc": "1. Registrar usuario", "fnc": "usuarios.registrarUsuario()"},
                        {"opc": "2. Consultar usuario",
                            "fnc": "usuarios.consultarUsuario()"},
                        {"opc": "3. Editar usuario",
                            "fnc": "usuarios.editarInfoUsuario()"},
                        {"opc": "4. Eliminar usuario",
                            "fnc": "usuarios.eliminarUsuario()"},
                        {"opc": "5. Informe usuarios",
                            "fnc": "usuarios.informeUsuarios()"},
                        {"opc": "6. Salir", "fnc": ""}]
            submenu(opciones)
        elif opcion == 2:
            opciones = [{"opc": "1. Registrar vehiculo", "fnc": "vehiculos.registrarVehiculo()"},
                        {"opc": "2. Consultar vehiculo",
                            "fnc": "vehiculos.consultarVehiculo()"},
                        {"opc": "3. Editar vehiculo",
                            "fnc": "vehiculos.editarVehiculo()"},
                        {"opc": "4. Eliminar vehiculo",
                            "fnc": "vehiculos.eliminarVehiculo()"},
                        {"opc": "5. Informe vehiculos",
                            "fnc": "vehiculos.informeVehiculos()"},
                        {"opc": "6. Salir", "fnc": ""}]
            submenu(opciones)
        elif opcion == 3:
            opciones = [{"opc": "1. Registrar viaje", "fnc": "viajes.registrarViaje()"},
                        {"opc": "2. Consultar viaje",
                            "fnc": "viajes.consultarViaje()"},
                        {"opc": "3. Editar viaje", "fnc": "viajes.editarViaje()"},
                        {"opc": "4. Eliminar viaje",
                            "fnc": "viajes.eliminarViaje()"},
                        {"opc": "5. Informe viajes",
                            "fnc": "viajes.informeViajes()"},
                        {"opc": "6. Salir", "fnc": ""}]
            submenu(opciones)
        elif opcion == 4:
            opciones = [{"opc": "1. Venta tiquetes", "fnc": "ventas.registrarVentaTiquete()"},
                        {"opc": "2. Consultar venta",
                            "fnc": "ventas.consultarVentaTiquete()"},
                        {"opc": "3. Informe", "fnc": "ventas.informeViajes()"},
                        {"opc": "4. Salir", "fnc": ""}]
            submenu(opciones)
        elif opcion == 5:
            run = False
        else:
            print("Opción inválida, intente de nuevo")


# Instancia de la clase. Módulo: Usuarios, Clase: Usuarios
User = Usuarios.Usuarios()

# Llamado de los métodos de la clase Usuarios
User.registrarUsuario()
