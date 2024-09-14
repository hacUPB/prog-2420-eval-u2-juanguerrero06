def main():
    altitud_incial = float(input("Ingrese la altitud inicial: "))
    arrastre = float(input("Ingrese el coeficiente de arrastre (0.00XX): "))
    altitud_minima= float(input("Ingrese la altitud mínima de seguridad: "))
    altitud_estabilizacion = float(input("Ingrese la perdida de altitud a la que considera se estabilizará el satelite: "))

    altitud_actual = altitud_incial
    orbita_completas = 0

    while altitud_actual > altitud_minima:
        orbita_completas +=1
        altitud_perdida = arrastre * altitud_actual
        altitud_actual -=altitud_perdida
    
        print(f"orbita: {orbita_completas}, altitud actual: {altitud_actual}km, arrastre: {arrastre}")

        arrastre +=0.001

        if altitud_perdida <= altitud_estabilizacion:
            print(f"El satelite se estabilizó a las {orbita_completas} orbitas.")
            break

    print(f"El satelite ingresó a la atmosfera después de {orbita_completas} orbitas.")
if __name__ == "__main__":
    main()
