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

    # Registra venta de tiquetes
    def registrarVentaTiquete(self):
        # Instanciamos la clase viajes para usar sus métodos
        viaje = self.instanciaClaseViajes()
        # Variables a usar en la función
        asientos = 0

        idFactura = random.randint(1, 9999)
        idViaje = int(input("Ingrese el ID del viaje: "))
        precioVenta = viaje.validaPrecioVenta(idViaje)
        tiquetesDisponibles = viaje.validaDisponibilidad(idViaje)
        if tiquetesDisponibles > 0:
            asientos = int(input("Ingrese la cantidad de asientos: "))
        if asientos <= tiquetesDisponibles:
            totalVentaBruta = float(asientos * precioVenta)
            totalIVA = float(totalVentaBruta * 0.13)
            totalVentaBrutaIVA = float(totalVentaBruta + totalIVA)
            self.ventasTemp = {
                "idViaje": idViaje,
                "idFactura": idFactura,
                "asientos": asientos,
                "totalVentaBruta": totalVentaBruta,
                "totalIVA": totalIVA,
                "totalVentaBrutaIVA": totalVentaBrutaIVA
            }
            if idViaje == "" or asientos == 0 or totalVentaBruta == 0 or totalIVA == 0 or totalVentaBrutaIVA == 0 or idFactura == 0:
                print(
                    "Error al procesar la venta, validar que todos los campos tengan información")
            else:
                self.listaTiquetesVendidos.append(self.ventasTemp)
                viaje.sumaORestaTotalBoletos(idViaje, asientos, 1)
                print("Tiquete(s) vendido(s) exitosamente")
                print("----------------------------")
                print("-     Datos Factura        -")
                print("----------------------------")
                viaje.mostrarDatosViaje(idViaje)
                print("ID Factura: ", idFactura)
                print("Cantidad asientos: ", asientos)
                print("Monto sin impuestos: ", totalVentaBruta)
                print("Monto de impuestos: ", totalIVA)
                print("Monto total a pagar: ", totalVentaBrutaIVA)
                print("Muchas gracias por su compra!")
        else:
            print("Lo sentimos, NO hay suficientes tiquetes disponibles para su compra")

    # Anular venta de tiquete
    def anularVentaTiquete(self, idTiqueteAnular=0):
        # Instanciamos la clase viajes para usar sus métodos
        viaje = self.instanciaClaseViajes()

        if idTiqueteAnular == 0:
            idTiqueteAnular = input("Digite el ID del tiquete a anular: ")
        for tiquete in self.listaTiquetesVendidos:
            if tiquete['idViaje'] == idTiqueteAnular:
                self.listaTiquetesVendidos.remove(tiquete)
                cantAsientos = tiquete['asientos']
                viaje.sumaORestaTotalBoletos(idTiqueteAnular, cantAsientos, 0)
                print("Tiquete anulado exitosamente")
                return
        print("No se pudo anular el tiquete")

    # Consulta venta de tiquetes
    def consultarVentaTiquete(self,):
        # Instanciamos la clase viajes para usar sus métodos
        viaje = self.instanciaClaseViajes()

        idViaje = int(input("Ingrese el ID del viaje a consultar: "))
        idFactura = int(
            input("Ingrese el número de factura del viaje a consultar: "))
        for tiquete in self.listaTiquetesVendidos:
            if tiquete['idViaje'] == idViaje and tiquete['idFactura'] == idFactura:
                viaje.mostrarDatosViaje(idViaje)
                print(
                    f"Total tiquetes: {tiquete['asientos']}, Precio sin impuestos: {tiquete['totalVentaBruta']}, Total a pagar: {tiquete['totalVentaBrutaIVA']}")
                print("Impuestos:", tiquete['totalIVA'])
                print('\n')
                anular = input("Quisieras anular esta venta? (S/N): ")
                if anular == "S":
                    self.anularVentaTiquete(idViaje)
                return
        print("Tiquete no encontrado")

    # Informe resumen
    def informeResumen(self,):
        # Instanciamos la clase viajes para usar sus métodos
        viaje = self.instanciaClaseViajes()

        idViaje = int(input("Ingrese el ID del viaje: "))
        print("********* INFORME RESUMEN DE VENTAS **********")
        viajeExiste = viaje.consultarViaje()
        if viajeExiste:
            print(self.listaTiquetesVendidos)
        print("------------- UL ----------------")

    # Instanciamos la clase viajes para usar sus métodos
    def instanciaClaseViajes(self,):
        viaje = viajes.Viajes()  # Módulo (Archivo) / Clase
        return viaje
