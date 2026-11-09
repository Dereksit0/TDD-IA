def generate_number() -> int:
    """Genera un número aleatorio entre 1 y 100."""
    raise NotImplementedError


def check_try(secret: int, guess: int) -> str:
    """Compara el intento con el número secreto.

    Devuelve 'mayor' si el secreto es mayor que el intento,
    'menor' si es menor y 'correcto' si es igual.
    Lanza ValueError si guess no es un entero entre 1 y 100.
    """
    raise NotImplementedError


def calculate_score(attempts: int, won: bool) -> int:
    """Calcula el puntaje.

    0 si pierde. Si gana: 100 puntos al primer intento,
    menos 15 puntos por cada intento extra.
    """
    raise NotImplementedError
