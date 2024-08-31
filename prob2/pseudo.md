# Pseudocodigo problema 2:
    Inicio
    leer altitud_inicial
    leer arrastre
    leer altitud_mínima
    leer altitud_estabilización

    altitud_actual = altitud_inicial
    orbitas_completas = 0

    mientras altitud_actual > altitud_mínima

        orbitas_completas = orbitas_completas + 1
        altitud_perdida = arrastre*altitud_actual
        altitud_actual = altitud_actual - altitud_perdida

        imprimir orbita: (orbitas_completas), la altitud actual es (altitud_actual)km, arrastre (arrastre), 	la altitud perdida es (altitud_perdida)

        arrastre = arrastre + 0.001
        
        si altitud_actual <= altitud_mínima
            romper miientras
            imprimir El satelite ingreso a la tierra despues de (orbita_completas) orbitas
        si no
            si altitud_perdida <= altitud_estabilización
                romper mientras
                imprimir El satelite se estabilizó después de (orbita_completas) orbitas
            fin si
        fin si
    fin mientras
    Fin
