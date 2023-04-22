# Clase Vehiculos
class Vehiculos:

    # Método constructor de la clase
    def __init__(self,):
        self.numeroPlaca = ""
        self.marca = ""
        self.estilo = ""
        self.modelo = ""
        self.capacidad = ""
        self.vehiculoTmp = {}
        self.listaVehiculos = []

    # Registrar un vehiculo
    def registrarVehiculo(self):
        self.numeroPlaca = input("Ingrese el numero de placa: ")
        self.marca = input("Ingrese la marca: ")
        self.estilo = input("Ingrese el estilo: ")
        self.modelo = input("Ingrese el modelo(año): ")
        self.capacidad = int(input("Ingrese la capacidad de pasajeros: "))

        if self.numeroPlaca == "" or self.marca == "" or self.estilo == "" or self.modelo == "" or self.capacidad == 0:
            print("Error: Campos obligatorios vacíos. Vehículo no agregado")
        else:
            vehiculoTmp = {
                "numeroPlaca": self.numeroPlaca,
                "marca": self.marca,
                "estilo": self.estilo,
                "modelo": self.modelo,
                "capacidad": self.capacidad,
            }
            self.listaVehiculos.append(vehiculoTmp)
            print("Vehiculo registrado exitosamente")

    # Consultar un vehiculo
    def consultarVehiculo(self, numeroPlaca=""):
        if numeroPlaca == "":
            numeroPlaca = input("Ingrese el número de placa a buscar: ")
        for vehiculo in self.listaVehiculos:
            if vehiculo['numeroPlaca'] == numeroPlaca:
                print(
                    f"El vehiculo es: Placa: {vehiculo['numeroPlaca']}, Marca: {vehiculo['marca']}, Estilo: {vehiculo['estilo']}, Modelo: {vehiculo['modelo']}, Capacidad: {vehiculo['capacidad']}")
                return int(vehiculo['capacidad'])
        print("Vehículo no encontrado")

    # Actualizar un vehículo
    def editarVehiculo(self,):
        numeroPlaca = input("Ingrese el número de placa a editar: ")
        for vehiculo in self.listaVehiculos:
            if vehiculo['numeroPlaca'] == numeroPlaca:
                nuevaMarca = input("Ingrese la nueva marca: ")
                nuevoEstilo = input("Ingrese el nuevo estilo: ")
                nuevoModelo = input("Ingrese nuevo modelo: ")
                nuevaCapacidad = int(input(
                    "Ingrese la nueva capacidad de pasajeros: "))
                vehiculo['marca'] = nuevaMarca
                vehiculo['estilo'] = nuevoEstilo
                vehiculo['modelo'] = nuevoModelo
                vehiculo['capacidad'] = nuevaCapacidad
                print("Vehículo agregado exitosamente")
                return
        print("Vehículo no encontrado")

    # Eliminar un vehiculo
    def eliminarVehiculo(self,):
        numeroPlaca = input("Ingrese el número de placa a eliminar: ")
        for vehiculo in self.listaVehiculos:
            if vehiculo['numeroPlaca'] == numeroPlaca:
                self.listaVehiculos.remove(vehiculo)
                print("Vehículo eliminado exitosamente")
                return
        print("Vehículo no encontrado")

    # Informe de los vehículos almacenados en el sistema
    def informeVehiculos(self,):
        print("*** INFORME RESUMEN DE LOS VEHÍCULOS ****")
        print("Cantidad de vehículos: ", len(self.listaVehiculos))
        for vehiculo in self.listaVehiculos:
            print("Número de placa: ", vehiculo['numeroPlaca'])
            print("Marca: ", vehiculo['marca'])
            print("Estilo: ", vehiculo['estilo'])
            print("Modelo: ", vehiculo['numeroPlaca'])
            print("Capacidad: ", vehiculo['capacidad'])
            print("--------------------------------")
        print("------------- UL ----------------")
