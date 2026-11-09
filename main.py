import juego

MAX_INTENTOS = 7


def pedir_intento(secreto, prompt):
    """Pide un intento hasta que sea válido; devuelve (intento, resultado)."""
    while True:
        texto = input(prompt)
        try:
            intento = int(texto)
            return intento, juego.check_try(secreto, intento)
        except ValueError:
            print("Entrada inválida: ingresa un entero entre 1 y 100.")


def preguntar_continuar():
    while True:
        resp = input("¿Quieres seguir jugando hasta adivinar? (s/n): ").strip().lower()
        if resp in ("s", "n"):
            return resp == "s"


def main():
    secreto = juego.generate_number()
    print("Adivina el número secreto entre 1 y 100.")
    print(f"Tienes {MAX_INTENTOS} intentos.")

    intentos = 0
    while intentos < MAX_INTENTOS:
        _, resultado = pedir_intento(secreto, f"Intento {intentos + 1}/{MAX_INTENTOS}: ")
        intentos += 1
        if resultado == "correcto":
            puntaje = juego.calculate_score(intentos, True)
            print(f"¡Ganaste! Puntaje: {puntaje} puntos. Intentos usados: {intentos}.")
            return
        print(f"Pista: el número secreto es {resultado}.")

    juego.calculate_score(intentos, False)
    print(f"¡Perdiste! El número secreto era {secreto}.")

    if not preguntar_continuar():
        print(f"El número secreto era {secreto}.")
        return

    while True:
        _, resultado = pedir_intento(secreto, "Intento: ")
        if resultado == "correcto":
            print("¡Adivinaste el número! Puntaje: 0")
            return
        print(f"Pista: el número secreto es {resultado}.")


if __name__ == "__main__":
    main()
