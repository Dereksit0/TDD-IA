# Objetivo:

La computadora elige un número del 1 al 100 y el jugador intenta adivinarlo con pistas de “mayor” o “menor”. 

# Main:

Al iniciar se genera un número secreto entre 1 y 100.

El jugador tiene máximo 7 intentos.

Tras cada intento se muestra la pista de si es mayor o menor.

Cuando el jugador adivina se le notifica, así como el puntaje y el número de intentos usados.

Si se agotan los 7 intentos se notifica al jugador que perdió y se le da el número secreto.

 

# Restricciones:

Solo admite números enteros entre 1 y 100.

 

# Funciones a implementar:

generate_number: Genera un número aleatorio entre 1 y 100.

check_try: Compara el intento con el número secreto.

calculate_score: Verifica los intentos para calulcar el puntaje.

    - 0 Si pierde.

    - 100 puntos al primer intento, menos 15 puntos por cada intento extra.