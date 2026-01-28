
class Departamento:
    uf = 30000

    def __init__(self, numero_unidad, propietario, metros_cuadrados, deuda_uf=0):
        self.numero_unidad = numero_unidad #Publico
        self.propietario = propietario #Publico
        self.__metros_cuadrados = metros_cuadrados #Privado
        self._saldo_gastos_comunes_uf = deuda_uf #Protegido

    @classmethod
    def cambiar_valor_uf(cls, nuevo_valor):
        cls.uf = nuevo_valor
        print(f"---Valor de UF actualizado a ${cls.uf}---")

    #Getter uso interno calcular
    def obtener_deuda_pesos(self):
        return self._saldo_gastos_comunes_uf * self.uf

    #Setter
    # agregar verificacion q el monto de la deuda no sea menor a lo pagado
    def pagar_gastos(self, monto_pesos):
        if monto_pesos > 0:
            abono_uf = monto_pesos / self.uf
            self._saldo_gastos_comunes_uf -= abono_uf
            print(f"Pago de ${monto_pesos:,} abonado ({abono_uf}UF) a la unidad {self.numero_unidad}.")
        else:
            print(f"Error: El monto a pagar debe ser mayor a 0. Monto abonado ${monto_pesos}")
    #Reporte Legible
    def __str__(self):
        deuda_pesos = self.obtener_deuda_pesos()
        return (f"/ Depto N°: {self.numero_unidad} / Propietario: {self.propietario} / "  
                f"Deuda: {self._saldo_gastos_comunes_uf:}UF (${deuda_pesos:} CLP)")

class Administracion:
    def __init__(self, nombre_conserje, telefono):
        self.nombre_conserje = nombre_conserje
        self.telefono = telefono

class Edificio:
    def __init__(self, nombre, nombre_conserje, telefono_conserje):
        self.nombre = nombre
        self.departamentos = [] #Agregacion
        self.administracion = Administracion(nombre_conserje, telefono_conserje) #Composicion dependencia administracion y edificio

    def agregar_departamento(self, depto):
        if isinstance(depto, Departamento):#isinstance veifica q sea del tipo departamento
            self.departamentos.append(depto)
        else:
            print("Error: Solo se pueden agregar objetos de tipo Departamento.")

    def buscar_departamento(self, dato):
        for depto in self.departamentos:
            if isinstance(dato, int) and depto.numero_unidad == dato:#isinstance veifica q sea del tipo numero y busca por numero
                return depto
            # isinstance verifica q sea del tipo cadena texto y este en minuscula y busca por nombre
            elif isinstance(dato, str) and depto.propietario.lower() == dato.lower():
                return depto
        return None
# agregamos datos de acuerdo a estructura
#creacion de edificio
edificio = Edificio("BootCamp", "Sam", "+5696532365")
#creacion departamentos
depto1 = Departamento(1, "Roberto", 60, 4)
depto2 = Departamento(2, "Juan", 75, 5)
depto3 = Departamento(3,"marina",75,5)
# agregar departamentos al edificio
edificio.agregar_departamento(depto1)
edificio.agregar_departamento(depto2)
edificio.agregar_departamento(depto3)
#Prueba
ancho = 80
print("*"* ancho)
print("Busqueda Propietarios".center(ancho))
print("*"* ancho)
print(edificio.buscar_departamento(1))
print(edificio.buscar_departamento("juan"))
print(edificio.buscar_departamento(3))
print("*"* ancho)
print("Pagos".center(ancho))
print("*"* ancho)
print("Pago 1")
depto1.pagar_gastos(60000)
print(depto1)
print("*"* ancho)
print("Pago 2")
depto2.pagar_gastos(-50000)#prueba negativo
print(depto2)
print("*"* ancho)
print("Pago 3")
depto3.pagar_gastos(90000)
print(depto3)
print("*"* ancho)
print("Actualizacion UF".center(ancho))
print("*"* ancho)
print(f"---Valor de UF actual: ${Departamento.uf}---")
Departamento.cambiar_valor_uf(40000)
print("*"* ancho)
print("Deuda Actualizada".center(ancho))
print("*"* ancho)
print(depto1)
print(depto2)
print(depto3)
