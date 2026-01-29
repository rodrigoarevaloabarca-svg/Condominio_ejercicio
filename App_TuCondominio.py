from Departamento import Departamento
from Edificio import Edificio


def menu():
    print("*"*80)
    print("---APP TU CONDOMINIO---")
    print("1. Registrar Edificio")
    print("2. Registrar departamento")
    print("3. Listar departamentos")
    print("4. Buscar departamento")
    print("5. Registrar pago")
    print("6. Actualizar UF")
    print("7. Generar Cargo Mensual")
    print("8. Salir")
    print("*"*80)
    return input("Ingrese una opcion del 1 al 6: ")

def principal():
    edificio = None
    while True:
        opcion = menu()
        match opcion:
            case "1":
                #creacion de edificio
                nombre_edificio = input("Ingrese el nombre del edificio: ")
                direccion = input("Ingrese la direccion del edificio: ")
                nombre_conserje = input("Ingrese el nombre del conserje: ")
                telefono_conserje = input("Ingrese el numero de telefono del conserje: ")
                edificio = Edificio(nombre_edificio,direccion, nombre_conserje, telefono_conserje)
                print(edificio)
                print("Edificio creado exitosamente")

            case "2":
                if edificio:
                    numero_unidad = int(input("Ingrese el numero de la unidad: "))
                    propietario = input("Ingrese el nombre del propietario: ")
                    metros = int(input("Ingrese metros cuadrado de la unidad: "))
                    deuda_previa_uf = int(input("Ingrese la deuda en UF: "))
                    depto = Departamento(numero_unidad, propietario, metros, deuda_previa_uf)
                    edificio.agregar_departamento(depto)
                    print(depto)
                    print("Departamento agregado exitosamente")
                else:
                    print("[Error] Debe Registrar (Opcion 1) un edificio antes de agregar departamentos")

            case "3":
                if edificio and edificio.departamentos:
                    for depto in edificio.departamentos:
                        print(depto)
                else:
                    print("[Error] Debe Registrar (Opcion 1) un edificio antes de listar departamentos")
            case "4":
                if edificio:
                    dato = int(input("Ingrese el numero de la unidad o el nombre del propietario: "))
                    print(edificio.buscar_departamento(dato))
                else:
                    print("[Error] Debe Registrar (Opcion 1) un edificio antes de buscar departamentos")

            case "5":
                if edificio:
                    dato = input("Ingrese el numero de la unidad o el nombre del propietario: ")
                    if dato.isdigit():
                        dato = int(dato)
                    depto_objetivo = edificio.buscar_departamento(dato)
                    if depto_objetivo:
                        monto = int(input("Ingrese el monto del pago: "))
                        depto_objetivo.pagar_gastos(monto)
                    else:
                        print("[Error] Departamento no encontrado")

                else:
                    print("[Error] Debe Registrar (Opcion 1) un edificio antes de registrar pagos")


            case "6":
                if edificio:
                    nuevo_valor = int(input("Ingrese el nuevo valor de UF: "))
                    Departamento.cambiar_valor_uf(nuevo_valor)
                else:
                    print("[Error] Debe Registrar (Opcion 1) un edificio antes de actualizar el valor de UF")
            case "7":
                if edificio and edificio.departamentos:
                    edificio.generar_cobro_mensual_total()
                else:
                    print("[Error] Debe Debe Registrar (Opcion 1) un edificio antes de generar cobros")

            case "8":
                print("Gracias por usar nuestra aplicacion")
                break
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    principal()


