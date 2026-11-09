import juego

MAX_INTENTOS = 7


def main():
    secreto = juego.generate_number()
    print("Adivina el número secreto entre 1 y 100.")
    print(f"Tienes {MAX_INTENTOS} intentos.")

    intentos = 0
    while intentos < MAX_INTENTOS:
        texto = input(f"Intento {intentos + 1}/{MAX_INTENTOS}: ")
        try:
            intento = int(texto)
            resultado = juego.check_try(secreto, intento)
        except ValueError:
            print("Entrada inválida: ingresa un entero entre 1 y 100.")
            continue

        intentos += 1
        if resultado == "correcto":
            puntaje = juego.calculate_score(intentos, True)
            print(f"¡Ganaste! Puntaje: {puntaje} puntos. Intentos usados: {intentos}.")
            return
        print(f"Pista: el número secreto es {resultado}.")

    juego.calculate_score(intentos, False)
    print(f"¡Perdiste! El número secreto era {secreto}.")


if __name__ == "__main__":
    main()
