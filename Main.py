import Usuarios
import Vehiculos
import Viajes
import Ventas


# Login
def login(listaUsuarios, userName, password):
    credencialesCorrectas = False
    for user in listaUsuarios:
        if user['codigo'] == userName and user['clave'] == password:
            credencialesCorrectas = True
    return credencialesCorrectas


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


# ----------------------------------------------------------------
# Menu del sistema
# ----------------------------------------------------------------

# Instancia de la clases
usuario = Usuarios.Usuarios()
vehiculo = Vehiculos.Vehiculos()
viaje = Viajes.Viajes()
venta = Ventas.Ventas()


userValid = True
while userValid == True:
    print('\n')
    print('--------------------------------')
    print("Iniciar sesión                 -")
    print('--------------------------------')
    userName = input("Digite el usuario: ")
    password = input("Digite la contraseña: ")
    isTrue = login(usuario.listaUsuarios, userName, password)
    if isTrue == True:
        isAdmin = usuario.validarRolUsuario(userName, password)
        run = True
        while run == True:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('>                                               >')
            print('>     Bienvenido Auto Transportes el Roble      >')
            print('>                                               >')
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            if isAdmin == True:
                print("1.Usuarios")
                print("2.Autobuses")
                print("3.Viajes")
                print("4.Facturación")
                print("5.Cerrar sesión")
                print("6.Salir")
            else:
                print("1.Facturación")
                print("2.Cerrar sesión")
                print("3.Salir")
            opcion = int(input("Seleccione la opción deseada: "))
            if opcion == 1 and isAdmin == True:
                opciones = [{"opc": "1. Registrar usuario", "fnc": "usuario.registrarUsuario()"},
                            {"opc": "2. Consultar usuario",
                                "fnc": "usuario.buscarUsuario()"},
                            {"opc": "3. Editar usuario",
                                "fnc": "usuario.editarInfoUsuario()"},
                            {"opc": "4. Eliminar usuario",
                                "fnc": "usuario.eliminarUsuario()"},
                            {"opc": "5. Informe usuarios",
                                "fnc": "usuario.informeUsuarios()"},
                            {"opc": "6. Salir", "fnc": ""}]
                submenu(opciones)
            elif opcion == 2 and isAdmin == True:
                opciones = [{"opc": "1. Registrar vehiculo", "fnc": "vehiculo.registrarVehiculo()"},
                            {"opc": "2. Consultar vehiculo",
                                "fnc": "vehiculo.consultarVehiculo()"},
                            {"opc": "3. Editar vehiculo",
                                "fnc": "vehiculo.editarVehiculo()"},
                            {"opc": "4. Eliminar vehiculo",
                                "fnc": "vehiculo.eliminarVehiculo()"},
                            {"opc": "5. Informe vehiculos",
                                "fnc": "vehiculo.informeVehiculos()"},
                            {"opc": "6. Salir", "fnc": ""}]
                submenu(opciones)
            elif opcion == 3 and isAdmin == True:
                opciones = [{"opc": "1. Registrar viaje", "fnc": "viaje.registrarViaje()"},
                            {"opc": "2. Consultar viaje",
                                "fnc": "viaje.consultarViaje()"},
                            {"opc": "3. Editar viaje",
                                "fnc": "viaje.editarViaje()"},
                            {"opc": "4. Eliminar viaje",
                                "fnc": "viaje.eliminarViaje()"},
                            {"opc": "5. Informe viajes",
                                "fnc": "viaje.informeViajes()"},
                            {"opc": "6. Salir", "fnc": ""}]
                submenu(opciones)
            elif (opcion == 1) or (opcion == 4 and isAdmin == True):
                opciones = [{"opc": "1. Venta tiquetes", "fnc": "venta.registrarVentaTiquete()"},
                            {"opc": "2. Consultar venta",
                                "fnc": "venta.consultarVentaTiquete()"},
                            {"opc": "3. Informe", "fnc": "venta.informeResumen()"},
                            {"opc": "4. Salir", "fnc": ""}]
                submenu(opciones)
            elif (opcion == 5 and isAdmin == True) or (opcion == 2):
                run = False
            elif (opcion == 6 and isAdmin == True) or (opcion == 3):
                run = False
                userValid = False
            else:
                print("Opción inválida, intente de nuevo")
    else:
        print("Error, usuario o clave incorrectas, intente de nuevo")
