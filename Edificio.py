from Administracion import Administracion
class Edificio:
    def __init__(self, nombre, direccion, nombre_conserje, telefono_conserje):
        self.nombre = nombre
        self.direccion = direccion
        self.departamentos = [] #Agregacion
        self.administracion = Administracion(nombre_conserje, telefono_conserje) #Composicion dependencia administracion y edificio

    def agregar_departamento(self, depto):
            self.departamentos.append(depto)


    def buscar_departamento(self, dato):
        for depto in self.departamentos:
            if isinstance(dato, int) and depto.numero_unidad == dato:#isinstance veifica q sea del tipo numero y busca por numero
                return depto
            # isinstance verifica q sea del tipo cadena texto y .lower q este en minuscula y busca por nombre
            elif isinstance(dato, str) and depto.propietario.lower() == dato.lower():
                return depto
        return None

    def generar_cobro_mensual_total(self):
        print(f"\n--- Generando Cargos Mensuales para Edificio: {self.nombre} ---")
        for depto in self.departamentos:
            depto.generar_gasto_mensual()
        print("--- Proceso finalizado con éxito ---\n")

    def __str__(self):
        return f"Edificio: {self.nombre} / Direccion: {self.direccion} / {self.administracion}"