# Pseudocodigo problema 1:
Inicio

    leer título
    leer Nombre
    leer Apellido
    leer origen
    leer destino
    leer preferencia
    leer dia_mes
    leer mes
    Definir dia_viaje = [lunes, martes, miércoles, jueves, viernes, sábado, domingo]

    solicitar al usuario (título) (señor y señora)
    solicitar al usuario (Nombre)
    solicitar al usuario (Apellido)
    Imprimir título Nombre Apellido, ¡sea usted bienvenido a AsadosThiago Airlines!

    solicitar al usuario que ingrese (origen)
    solicitar al usuario que ingrese (destino)
    Definir distancias =
            [("Medellín", "Bogotá"): 240,          
            ("Bogotá", "Medellín"): 240,  
            ("Medellín", "Cartagena"): 461,  
            ("Cartagena", "Medellín"): 461,  
            ("Bogotá", "Cartagena"): 657,  
            ("Cartagena", "Bogotá"): 657]

    solicitar al usuario que ingrese (dia_mes)
    solicitar al usuario que ingrese (mes) ##esto yo lo haría con una matriz para que sea más preciso, sin embargo no se como sería.

    si distancia (origen, destino) está en distancias
        distancia = distancias[(origen, destino)]
            si distancia <= 400
                si dia_viaje es [lunes, martes, miércoles, jueves]
                    precio = 79900
                si no
                    precio = 119900
                fin si
            si no
                si dia_viaje es [lunes, martes, miércoles, jueves]
                    precio = 156900
                si no
                    precio = 213000
                fin si
            fin si
    si no
        distancia = no definido
    fin si

    solicitar al usuario que ingrese (preferencia)
    si preferencia == ventana
        tipo_asiento = A
    si no 
        si preferencia == pasillo
            tipo_asiento = B
        si no preferencia == sin preferencia
        tipo_asiento = C
        fin si
    fin si

    numero_asiento = generar.numero.aleatorio(1,29)

    imprimir tu vuelo de (origen) a (destino) del (dia_viaje) (dia_mes) de (mes) está reservado
    imprimir precio total del boleto (precio)
    imprimir su asiento asignado es (numero_asiento)(tipo_asiento)
Fin
