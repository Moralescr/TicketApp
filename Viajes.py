import Vehiculos as vehiculos

# Clase Ventas


class Viajes:

    # Método constructor de la clase
    def __init__(self,):
        self.idViaje = 0
        self.numeroPlaca = ""
        self.destino = ""
        self.capacidadPasajeros = 0
        self.tiquetesDisponibles = 0
        self.tiquetesVendidos = 0
        self.precioViaje = 0
        self.viajesTmp = {}
        self.listaViajes = []

    # Registrar un viaje
    def registrarViaje(self,):
        # Instanciamos la clase vehiculo para usar sus métodos
        vehiculo = vehiculos.Vehiculos()  # Módulo (Archivo) / Clase

        idViaje = int(input("Ingrese el id del viaje: "))
        numeroPlaca = input("Ingrese el número de placa: ")
        destino = input("Ingrese el destino: ")
        precioViaje = float(input("Ingrese el precio del tiquete: "))
        capacidadVehiculo = vehiculo.consultarVehiculo(numeroPlaca)
        capacidadPasajeros = capacidadVehiculo

        if idViaje == 0 or numeroPlaca == "" or destino == "" or precioViaje == 0 or capacidadPasajeros == None:
            print("Error: Campos obligatorios vacíos. Viaje no agregado")
        else:
            self.viajesTemp = {
                "idViaje": idViaje,
                "numeroPlaca": numeroPlaca,
                "destino": destino,
                "capacidadPasajeros": capacidadPasajeros,
                "tiquetesDisponibles": capacidadPasajeros,
                "tiquetesVendidos": 0,
                "precioTiquete": precioViaje,
            }
            self.listaViajes.append(self.viajesTemp)
            print("Viaje registrado exitosamente")

    # Consultar un viaje
    def consultarViaje(self):
        viajeExiste = False
        idViaje = int(input("Ingrese el ID del viaje a buscar: "))
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                print(
                    f"Datos del viaje, ID: {viaje ['idViaje']}, Placa: {viaje ['numeroPlaca']}, Destino: {viaje['destino']}, Capacidad Total: {viaje['capacidadPasajeros']}, Precio: {viaje['precioTiquete']}")
                print(
                    f"Tiquetes disponibles: {viaje ['tiquetesDisponibles']}, Tiquetes vendidos: {viaje ['tiquetesVendidos']}")
                viajeExiste = True
        if viajeExiste == False:
            print(f"No existe un viaje con el ID: { idViaje } ")
        return viajeExiste

    # Actualizar un viaje
    def editarViaje(self,):
        idViaje = int(input("Ingrese el ID del viaje a editar: "))
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                nuevoNumeroPlaca = input("Ingrese el nuevo número de placa: ")
                nuevoDestino = input("Ingrese el nuevo destino: ")
                nuevaCapacidadPasajeros = int(input(
                    "Ingrese la nueva capacidad de pasajeros: "))
                nuevoPrecioViaje = int(
                    input("Ingrese el nuevo precio del viaje: "))
                viaje['numeroPlaca'] = nuevoNumeroPlaca
                viaje['destino'] = nuevoDestino
                viaje['capacidadPasajeros'] = nuevaCapacidadPasajeros
                viaje['precioTiquete'] = nuevoPrecioViaje
                return
        print(f"No existe un viaje con el ID: { idViaje } ")

    # Eliminar un viaje
    def eliminarViaje(self,):
        idViaje = int(input("Ingrese el ID de viaje a eliminar: "))
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                self.listaViajes.remove(viaje)
                return
        print(f"No existe un viaje con el ID: { idViaje } ")

    # Consultar viaje para mostrarlo en la factura

    def mostrarDatosViaje(self, idViaje):
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                print(
                    f"ID Viaje: {viaje ['idViaje']}, Placa: {viaje ['numeroPlaca']}, Destino: {viaje ['destino']}, Precio: {viaje ['precioTiquete']}")

    # Validar disponibilidad de un viaje

    def validaDisponibilidad(self, idViaje):
        cantidadDisponibles = 0
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                cantidadDisponibles = viaje['tiquetesDisponibles']
        return cantidadDisponibles

    # Validar precio venta de un viaje
    def validaPrecioVenta(self, idViaje):
        precioVenta = 0
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                precioVenta = viaje['precioTiquete']
        return precioVenta

    # Control de tiquetes vendidos o anulados
    def sumaORestaTotalBoletos(self, idViaje, cantidad, opcToExec):
        for viaje in self.listaViajes:
            if viaje['idViaje'] == idViaje:
                # Si es 1, significa que se ha comprado un boleto por lo tanto se resta del disponible y se suma a los vendidos
                if opcToExec == 1:
                    viaje['tiquetesDisponibles'] -= cantidad
                    viaje['tiquetesVendidos'] += cantidad
                # Si es otro valor, significa que se ha anulado un boleto por lo tanto se suma al disponible y se resta a los vendidos
                else:
                    viaje['tiquetesDisponibles'] += cantidad
                    viaje['tiquetesVendidos'] -= cantidad
                return

    # Informe resumen
    def informeViajes(self,):
        print("********* INFORME RESUMEN DE VIAJES **********")
        print("Cantidad de viajes: ", len(self.listaViajes))
        for viaje in self.listaViajes:
            print(
                f"ID Viaje: {viaje ['idViaje']}, Placa: {viaje ['numeroPlaca']}, Destino: {viaje ['destino']}, Precio: {viaje ['precioTiquete']}")
            print("----------------------------")
        print("------------- UL ----------------")
