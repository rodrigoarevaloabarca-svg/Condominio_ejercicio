class Departamento:
    uf = 30000
    costo_m2_uf = 0.05

    def __init__(self, numero_unidad, propietario, metros_cuadrados, deuda_previa_uf):
        self.numero_unidad = numero_unidad #Publico
        self.propietario = propietario #Publico
        self._metros_cuadrados = metros_cuadrados #Protegido
        self.__saldo_gastos_comunes_uf = deuda_previa_uf #Privado

    @classmethod
    def cambiar_valor_uf(cls, nuevo_valor):
        cls.uf = nuevo_valor
        print(f"---Valor de UF actualizado a ${cls.uf}---")

    def generar_gasto_mensual(self):
        monto_generado = self._metros_cuadrados * self.costo_m2_uf
        self.__saldo_gastos_comunes_uf += monto_generado
        print(f"Se han cargado {monto_generado:.2f} UF al Depto {self.numero_unidad}")

    #Getter uso interno calcular
    def obtener_deuda_pesos(self):
        return self.__saldo_gastos_comunes_uf * self.uf

    #Setter
    # Agregada validacion por pagos superiores a la deuda
    def pagar_gastos(self, monto_pesos):

        abono_uf = monto_pesos / self.uf

        if monto_pesos > 0 and self.__saldo_gastos_comunes_uf > abono_uf :
            self.__saldo_gastos_comunes_uf -= abono_uf
            print(f"Pago de ${monto_pesos:,} abonado ({abono_uf:.2f}UF) al Depto N° {self.numero_unidad}.")
        elif abono_uf > self.__saldo_gastos_comunes_uf:
            print(f"El monto ingresado ${monto_pesos} equivale a {abono_uf:.2f}UF, es superior a la deuda actual {self.__saldo_gastos_comunes_uf}UF")
        else:
            print(f"Error: El monto a pagar debe ser mayor a 0. Monto abonado ${monto_pesos}")

    #Reporte Legible
    def __str__(self):
        deuda_pesos = self.obtener_deuda_pesos()
        return (f"/ Depto N°: {self.numero_unidad} / Propietario: {self.propietario} / "  
                f"Deuda: {self.__saldo_gastos_comunes_uf:.2f}UF (${deuda_pesos:} CLP)")
