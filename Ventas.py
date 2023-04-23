import random
import Viajes as viajes

# Clase Ventas


class Ventas:

    # Método constructor de la clase
    def __init__(self,):
        self.idViaje = 0
        self.idFactura = 0
        self.asientos = 0
        self.totalVentaBruta = 0
        self.totalIVA = 0
        self.totalVentaBrutaIVA = 0
        self.ventasTmp = {}
        self.listaTiquetesVendidos = []

    # Validar disponibilidad de un viaje
    def validaDisponibilidad(self, idViaje):
        disponibles = 0
        for viaje in viajes.Viajes().listaViajes:
            if viaje['idViaje'] == idViaje:
                disponibles = viaje['tiquetesDisponibles']
        return disponibles

    # Registra venta de tiquetes
    def registrarVentaTiquete(self):
        # Instanciamos la clase vehiculo para usar sus métodos
        viaje = viajes.Viajes()  # Módulo (Archivo) / Clase

        idFactura = random.randint(1, 9999)
        idViaje = int(input("Ingrese el ID del viaje: "))
        precioVenta = viaje.consultarViaje()
        tiquetesDisponibles = viaje.validaDisponibilidad(idViaje)
        asientos = int(input("Ingrese la cantidad de asientos: "))
        if asientos <= tiquetesDisponibles:
            totalVentaBruta = float(asientos * precioVenta)
            totalIVA = float(totalVentaBruta * 0.13)
            totalVentaBrutaIVA = float(totalVentaBruta + totalIVA)
            ventasTemp = {
                "idViaje": idViaje,
                "idFactura": idFactura,
                "asientos": asientos,
                "totalVentaBruta": totalVentaBruta,
                "totalIva": totalIVA,
                "totalVentaBrutaIVA": totalVentaBrutaIVA
            }
            if idViaje == "" or asientos == 0 or totalVentaBruta == 0 or totalIVA == 0 or totalVentaBrutaIVA == 0 or idFactura == 0:
                print(
                    "Error al procesar la venta, validar que todos los campos tengan información")
            else:
                self.listaTiquetesVendidos.append(ventasTemp)
                sumaORestaTotalBoletos(idViaje, asientos, 1)
                print("Tiquete(s) vendido(s) exitosamente")
                print("****** Datos Factura *******")
                viajes.mostrarDatosViaje(idViaje)
                print(ventasTemp)
        else:
            print("Lo sentimos, NO hay suficientes tiquetes disponibles para su compra")
