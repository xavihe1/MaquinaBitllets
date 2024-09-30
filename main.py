MONEDES_PERMESES = [0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]

preusBaseZona1 = {
    1: 2.40,  # Bitllet senzill
    2: 11.35,  # TCasual
    3: 40.00,  # TUsual
    4: 10.00,  # TFamiliar
    5: 80.00  # TJove
}


def main():
    while True:
        seguir = False
        while not seguir:
            tipusBitllet = seleccionarBitllet()
            if tipusBitllet is None:
                continue

            numZones = seleccionarZones()
            if numZones is None:
                continue

            numBitllets = seleccionarNumeroBitllets()
            if numBitllets is None:
                continue

            preuTotal = calcularPreuTotal(tipusBitllet, numZones, numBitllets)
            if preuTotal is None:
                continue

            dinersIngresats = introduirDiners(preuTotal)
            if dinersIngresats is None:
                continue

            imprimirBitllets()
            retornarCanvi(dinersIngresats, preuTotal)
            imprimirTiquet()

            seguir = True

    print("La màquina està llesta per al següent usuari.")
    print("============================================\n")



# Menú bitllets
def seleccionarBitllet():
    while True:
        print("Benvingut a la màquina de bitllets de RodalITB!")
        print("\nSelecciona el bitllet que desitgis comprar.")
        print("1. Bitllet senzill")
        print("2. TCasual")
        print("3. TUsual")
        print("4. TFamiliar")
        print("5. TJove")
        print("6. Tornar enrere")

        try:
            tipus = int(input("Introdueix el número del tipus de bitllet: "))
            if tipus in range(1, 6):
                return tipus
            elif tipus == 6:
                return None
            else:
                print("Opció no vàlida. Torna-ho a intentar.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número entre 1 i 6.")


# Seleccionar número de zones
def seleccionarZones():
    while True:
        print(f"\nSelecciona el nombre de zones (1-6) o selecciona 7 per tornar enrere.")
        try:
            zones = int(input("Nombre de zones: "))
            if 1 <= zones <= 6:
                return zones
            elif zones == 7:
                return None
            else:
                print("Nombre de zones no vàlid. Introdueix un número entre 1 i 6.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número entre 1 i 6.")


# Seleccionar número de bitllets
def seleccionarNumeroBitllets():
    while True:
        print(f"\nSelecciona el nombre de bitllets (1-3) o selecciona 4 per tornar enrere.")
        try:
            bitllets = int(input("Nombre de bitllets: "))
            if 1 <= bitllets <= 3:
                return bitllets
            elif bitllets == 4:
                return None
            else:
                print("Número de bitllets no vàlid. Introdueix un número entre 1 i 3.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número entre 1 i 3.")


# Càlcul preu
def calcularPreuTotal(tipusBitllet, zones, bitllets):
    preuBase = preusBaseZona1.get(tipusBitllet, None)
    if preuBase is None:
        print("Error: Tipus de bitllet no vàlid.")
        return None

    preuPerZona = preuBase * (1.25 ** (zones - 1))
    preuTotal = preuPerZona * bitllets
    print(f"\nPreu total per {bitllets} bitllet(s) de zona {zones}: {preuTotal:.2f} €")
    return preuTotal


def introduirDiners(preuTotal):
    dinersIngresats = 0.0
    print(f"Introdueix els diners per un total de {preuTotal:.2f} €")
    while dinersIngresats < preuTotal:
        try:
            moneda = float(input("Introdueix una moneda o bitllet: "))
            if moneda in MONEDES_PERMESES:
                dinersIngresats += moneda
                if dinersIngresats < preuTotal:
                    print(f"Import insuficient. Falten {preuTotal - dinersIngresats:.2f} €")
            else:
                print("Moneda o bitllet no acceptat. Torna-ho a intentar.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un valor numèric.")
    return dinersIngresats


def imprimirBitllets():
    print("Bitllets comprats amb èxit!")


def retornarCanvi(dinersIngresats, preuTotal):
    canvi = dinersIngresats - preuTotal
    print(f"Canvi a tornar: {canvi:.2f} €")


def imprimirTiquet():
    resposta = input("Vols un tiquet? (S/N): ").strip().lower()
    if resposta == "si":
        print("Imprimint tiquet...")


if __name__ == "__main__":
    main()
