import random
import datetime
def main():
    print("1. Señor\n2. Señora")
    while True:
        Titulo = int(input("Ingrese el NúMERO de su título: "))
        if Titulo == 1:
            print("Ha seleccionado Sr.")
            TitNombre = "Sr."
            break
        elif Titulo == 2:
            print("Ha seleccionado Sra.")
            TitNombre = "Sra."
            break
        else:
            print("Opción invalida, ingreselo de nuevo")
    
    nombre = input("Ingrese su primer nombre: ")
    apellido = input("Ingrese su primer apellido: ")
    print(f"{TitNombre} {nombre} {apellido}, bienvenido a AsadosThiago Airlines. Nos complace saber que nos eligió para su vuelo.")

    distancias = {
        ("Medellín", "Bogotá"): 240,  # Medellín a Bogotá
        ("Bogotá", "Medellín"): 240,  # Bogotá a Medellín
        ("Medellín", "Cartagena"): 461,  # Medellín a Cartagena
        ("Cartagena", "Medellín"): 461,  # Cartagena a Medellín
        ("Bogotá", "Cartagena"): 657,  # Bogotá a Cartagena
        ("Cartagena", "Bogotá"): 657,  # Cartagena a Bogotá
    }
    
    # profe si llega a leer esto, la verdad buscamos mucho como solucionar el problema de las tildes y no encontramos nada, le pregunte a un parcero de pereira y tampoco fue capáz. Si de pronto lo explicó en clase la verdad no lo pude encontrar.
    # hola, soy Thiago, estudiante de Ing. Sistemas, y tampoco fuí capáz de resolverlo, porque casi pierdo estructura de datos, pero aprendi c++, se como invertir una lista, no como quitar tildes.
    
    while True:
        print("Medellín\nBogotá\nCartagena")
        origen = input("Ingrese el origen, por favor tenga en cuenta las tíldes: ").capitalize()
        print("Medellín\nBogotá\nCartagena")
        destino = input("ingrese destinopor, favor tenga en cuenta las tíldes: ").capitalize()
        if (origen, destino) not in distancias:
            print("Los datos seleccionados no son válidos")
            continue
        if origen == destino:
            print("Los datos seleccionados no son válidos")
        else:
            break

    while True:
        try:
            fecha_viaje = input("ingrese la fecha de su viaje (formato: DD/MM/YYYY): ")
            fecha_viaje = datetime.datetime.strptime(fecha_viaje, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha no valida")

    distancia = distancias.get((origen, destino))

    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miercoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo",
    }
    dia_semana = dias.get(fecha_viaje.weekday())

    if distancia <= 400:
        if dia_semana in['lunes', 'martes', 'miercoles', 'jueves']:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ['lunes', 'martes', 'miercoles', 'jueves']:
            precio = 156900
        else:
            precio = 213000
    
    print("Seleccione su preferencia de asiento:\nPasillo.\nVentana.\nSin preferencia.")

    while True:
        preferencia_asiento = input().lower()
        if preferencia_asiento == "pasillo":
            tipo_asiento = "A"
            break
        elif preferencia_asiento == "ventana":
            tipo_asiento = "B"
            break
        elif preferencia_asiento == "sin preferencia":
            tipo_asiento = "C"
            break
        else:
            print("Selección no válida, por favor revise la esctritura.")

    numero_asiento = random.randint(1,29)

    mes = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }
    
    nombre_mes = mes.get(fecha_viaje.month)

    print(f"Su vuelo de {origen} a {destino} de fecha {dia_semana} {fecha_viaje.day} de {nombre_mes} de {fecha_viaje.year} está reservado.")
    print(f"Precio boleto: {precio}")
    print(f"Su silla asignada es: {numero_asiento}{tipo_asiento}")
if __name__ == "__main__":
    main()
