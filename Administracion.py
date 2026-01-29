class Administracion:
    def __init__(self, nombre_conserje, telefono):
        self.nombre_conserje = nombre_conserje
        self.telefono = telefono
    def __str__(self):
        return f"Administracion :{self.nombre_conserje} / Telefono: {self.telefono}"